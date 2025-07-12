import tkinter as tk
import ttkbootstrap as tb

from app.DogsApi import DogsApi
from app.WebImage import WebImage

WINDOW_WIDTH: int   = 800
WINDOW_HEIGHT: int  = 600
APP_TITLE: str      = "Random Doggos"

class App():
    def __init__(self):
        self.window = tb.Window(themename="darkly")
        self.window.title(APP_TITLE)
        self.window.resizable(0, 0)

        self.api = DogsApi()
        self.selected_category = tk.StringVar(value="random")
        
        self.__setupWidgets()

    def run(self):
        self.__updateImage__()
        self.window.mainloop()

    def __setupWidgets(self):
        top_frame = tb.Frame(self.window)
        top_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        top_frame.columnconfigure(0, weight=1)
        top_frame.columnconfigure(1, weight=1)

        dropdown = tb.Combobox(
            top_frame, 
            textvariable=self.selected_category,
            values=self.api.getBreedList(), 
            state="readonly", 
            width=20
        )
        dropdown.grid(row=0, column=0, sticky="w")

        load_button = tb.Button(
            top_frame, 
            text="Gimme Gimme Doggos!", 
            command=self.__updateImage__
        )
        load_button.grid(row=0, column=1, sticky="e")

        self.image_canvas = tb.Canvas(
            self.window, 
            width=WINDOW_WIDTH, 
            height=WINDOW_HEIGHT,
            highlightthickness=0
        )
        self.image_canvas.grid(row=1, column=0, pady=20)
    
    def __updateImage__(self):
        self.api.filterByBreed(self.selected_category.get())
        imageUrl = self.api.getRandomImageUrl()
        if imageUrl == None: return
        self.image = WebImage(imageUrl, WINDOW_WIDTH - 20, WINDOW_HEIGHT - 20).getImage()
        self.image_canvas.create_image(
            (WINDOW_WIDTH - self.image.width()) / 2,
            (WINDOW_HEIGHT - self.image.height()) / 2, 
            anchor="nw", 
            image=self.image
        )