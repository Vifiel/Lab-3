from tkinter import Tk, font, Label, Button, PhotoImage
from random import randint, shuffle
from pygame import mixer, init
from time import sleep

alphabet = [chr(x) for x in range(ord("A"), ord("Z")+1)]
nums = list(map(str, range(9)))
key = ""
l = [alphabet, alphabet, nums, nums, nums]
window = Tk()
fn_b = font.Font(family="Izuver", size=50)
fn_s = font.Font(family="Izuver", size=30)
fn_ss = font.Font(family="Izuver", size=10)


def display():
    k_text.place(x=325, y=300)
def anim(k):
    k += 1
    if k == 15:
        k = 0
    fr = cow[k]
    cow_lab.configure(image=fr)
    window.after(100, anim, k)
        
if __name__ == "__main__":
    
    init()
    mixer.music.load("10 - Lava Lake.mp3")
    mixer.music.set_volume(1)
    mixer.music.play(-1)


    window.title("Noita key generator")
    window.geometry("1200x719")
    window.configure(bg="gray")

    image = PhotoImage(file="noita.png")
    image_lab = Label(window, image=image)
    image_lab.place(x=-3, y=-3)
    
    cow = [PhotoImage(file="dancing-polish-cow-at4am.gif", format = f"gif -index {k}") for k in range(21)]
    cow_lab = Label(window, image=cow[0])
    cow_lab.place(x=900, y=500)


    for i in range(3):
        shuffle(l)
        for j in l:
            key += j[randint(0, len(j)-1)]
        key += "-"
    key = key[0:17]
    k_text = Label(window, text=key, bg="black", fg="orange", font=fn_s)


    btn = Button(window, text="Generate", bg="black", fg="orange", font=fn_s, command=display)
    btn.place(x=100, y=300)


    text = Label(window, text = "Generated key for Noita", font=fn_b, bg="black", fg="orange")
    text.place(x=100, y=150)

    window.after(0, anim, 0)
    window.mainloop()

