# create the form to search movie

import tkinter as tk
from imdb import Cinemagoer
root = tk.Tk()
root.title("Movie Scraper")
root.geometry("400x400")
root.configure(bg="black")
ia = Cinemagoer()

# create a frame to hold the widgets
frame = tk.Frame(root, bg="black")
frame.pack()

# create a label
label = tk.Label(frame, text="Movie Scraper", bg="black", fg="white",font=("Times New Roman", 20, "bold"))
label.pack()



root.mainloop()
