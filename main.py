from tkinter import *
from tkextrafont import Font

if __name__ == "__main__":
    window = Tk()
    window.title("Noita key generator")
    window.geometry("1200x719")
    
    font = Font(file="Izuver.otf")
    image = PhotoImage(file="noita.png")

    image_lab = Label(window, image=image)
    image_lab.place(x=-3, y=-3)

    text = Label(window, text = "Generated key for noita", font=font)
    text.place(x=300, y=150)


    window.mainloop()

