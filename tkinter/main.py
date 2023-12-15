from tkinter import *
#
window = Tk()
window.title("My first Gui program")
window.minsize(width=500, height=300)
#
label = Label(text="I am a Label", font=("Arial", 24, "bold"))
label.pack()

def button_click():
    text = enput.get()
    label.config(text=text)


button = Button(text="Click Me", command=button_click)
button.pack()

enput = Entry(width=20)
enput.pack()


# def add(*args):
#     sum_it = 0
#     for num in args:
#         print(num)
#         sum_it += num
#     print(sum_it)

# add(3, 6, 9, 0, 5, 13, 85)
window.mainloop()

