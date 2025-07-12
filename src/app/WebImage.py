import io
import urllib.request

from PIL import ImageTk, Image, ImageFile

class WebImage:
    def __init__(
        self, 
        image_url: str, 
        max_width: int, 
        max_height: int
    ) -> None:
        with urllib.request.urlopen(image_url) as data:
            raw_data = data.read()
        self.image = ImageTk.PhotoImage(
            image = self.__resize__(
                Image.open(io.BytesIO(raw_data)), 
                max_width, 
                max_height 
            )
        )

    def __resize__(
        self, 
        image: ImageFile.ImageFile, 
        max_width: int, 
        max_height: int
    ) -> ImageFile.ImageFile:
        width: int  = image.width
        height: int = image.height
        width_coeff: float   = max_width / width
        height_coeff: float  = max_height / height

        if(height_coeff> width_coeff):
            return image.resize((
                (int)(width_coeff * width), 
                (int)(width_coeff * height)
            ))
        return image.resize((
            (int)(height_coeff * width), 
            (int)(height_coeff * height)
        ))

    def getImage(self) -> ImageTk.PhotoImage:
        return self.image