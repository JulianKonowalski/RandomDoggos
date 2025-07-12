import requests

API_BREEDS_URL: str = "https://dog.ceo/api/breeds/list/all"
API_IMAGE_URL: str  = "https://dog.ceo/api/breeds/image/random"

class DogsApi:
    def __init__(self):
        self.cached_breed_list: list[str]   = None
        self.api_image_url: str             = API_IMAGE_URL
        self.api_breeds_url: str            = API_BREEDS_URL

    def getRandomImageUrl(self) -> str:
        response: requests.Response = requests.get(self.api_image_url)
        if response.status_code != 200:
            print(f"Error while fetching image url: {response.status_code}")
            return None
        return response.json()["message"]
    
    def getBreedList(self) -> dict:
        if (self.cached_breed_list != None): return self.cached_breed_list
        response: requests.Response = requests.get(self.api_breeds_url)
        if response.status_code != 200:
            print(f"Error while fetching breed list: {response.status_code}", )
            return None
        self.cached_breed_list = self.__dictToList__(response.json()["message"])
        return self.cached_breed_list

    def filterByBreed(self, filter: str) -> None:
        if filter == "random": self.api_image_url: str = API_IMAGE_URL
        else: self.api_image_url: str = f"https://dog.ceo/api/breed/{filter}/images/random"

    def __dictToList__(self, idict: dict) -> list[str]:
        olist: list[str] = ["random"]
        for outer_key in idict:
            if len(idict[outer_key]) == 0:
                olist.append(outer_key)
            else:
                for inner_key in idict[outer_key]:
                    olist.append(f"{outer_key}-{inner_key}")
        return olist

