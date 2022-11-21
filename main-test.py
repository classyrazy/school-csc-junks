import tkinter as tk


class Marquee(tk.Canvas):  # creating a new class
    def __init__(self, master, text, font, fill, width, height, fps, bgColor,bgFps):  # constructor function
        tk.Canvas.__init__(self, master, bg=bgColor, width=width, height=height) # configuring tkinter canvas
        # super().__init__(master, bg=bgColor, width=width, height=height) # configuring tkinter canvas
        self.text = self.create_text(0, -2000, text=text, font=font, fill=fill, tags=("marquee"), anchor='w') # creating tkinter text
        self.fps = fps # setting the rate the text will be moving
        self.shift() # actually calling the shift function
        self.animateBg("black", "#333", 2) # calling the animateBg function

    def shift(self): # defining the function to call the shift the text
        x1, y1, x2, y2 = self.bbox("marquee") # getting the coordinates of the text
        if x2 < 0 or y1 < 0:  # reset the coordinates
            x1 = self.winfo_width() # getting the width of the canvas
            y1 = self.winfo_height()//2 # getting the height of the canvas, divided by 2 because the text we want a centered text
            self.coords("marquee", x1, y1) # setting the coordinates of the text as it changes
        else:
            self.move("marquee", -2, 0) # moving the text if the coordinates are not resetting
        self.after(1000//self.fps, self.shift) # calling the shift function again after a certain amount of time so it will repeat the text moving

    def animateBg(self, color1, color2, fps=40): # defining the function to animate the background
        self.config(bg=color1)
        self.after(10000// fps, lambda: self.animateBg(color2, color1, fps)) # calling the animateBg function again after a certain amount of time so it will repeat the background changing


root = tk.Tk() # creating the tkinter window
root.title('Tkinter Animation') # setting the title of the window
text_var = "Welcome to computer science department, University of lagos" # setting the text we want to animate
font = ('Times New Roman', 50, 'bold') # setting the font of the text
fill = 'white'  # setting the color of the text
width = 800     # setting the width of the canvas
height = 600    # setting the height of the canvas
fps = 80   # setting the rate the text will be moving
bgFPS = 4 # setting the rate the background will be changing
backgroundColor = "#000"    # setting the background color of the canvas
marquee = Marquee(root, text_var, font, fill, width, height, fps, backgroundColor, bgFPS) # creating the marquee class instance
marquee.pack(fill=tk.BOTH, expand=1) # packing the canvas to the window so it will be displayed (tried it without this line and it wasn't working)
root.mainloop() # running the tkinter window
