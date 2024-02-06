# Mason Thomas
#Assignment P1
#GUI Dev

from tkinter import *
from tkinter import ttk

#Create Window
root = Tk()
root.title("French Numbers")
root.geometry("750x350")

#Display Instructions
lblInstructions = Label(text = "Do you know the french words for the numbers 1 throught 5?\nClick the butttons below to see them.")
lblInstructions.place(relx=.5, rely=.3, anchor=CENTER)

#Button Actions(I got help from the website tutorialspoint but I\ did not copy and paste anything)
def option1():
    lblFrench = Label(text = "un")
    lblFrench.place(relx=.5, rely=.5, anchor=CENTER)
def option2():
    lblFrench = Label(text = "duex")
    lblFrench.place(relx=.5, rely=.5, anchor=CENTER)
def option3():
    lblFrench = Label(text = "trois")
    lblFrench.place(relx=.5, rely=.5, anchor=CENTER)
def option4():
    lblFrench = Label(text = "quatre")
    lblFrench.place(relx=.5, rely=.5, anchor=CENTER)
def option5():
    lblFrench = Label(text = "cinq")
    lblFrench.place(relx=.5, rely=.5, anchor=CENTER)
def option6():
    root.destroy()

#Create Buttons
btnOne = ttk.Button(text = "1", command=option1)
btnOne.place(relx=.1, rely=.7, anchor=CENTER)
btnTwo = ttk.Button(text = "2", command=option2)
btnTwo.place(relx=.3, rely=.7, anchor=CENTER)
btnThree = ttk.Button(text = "3", command=option3)
btnThree.place(relx=.5, rely=.7, anchor=CENTER)
btnFour = ttk.Button(text = "4", command=option4)
btnFour.place(relx=.7, rely=.7, anchor=CENTER)
BtnFive = ttk.Button(text = "5", command=option5)
BtnFive.place(relx=.9, rely=.7, anchor=CENTER)
btnExit = ttk.Button(text = "Exit", command=option6)
btnExit.place(relx=.5, rely=.8, anchor=CENTER)



root.mainloop()

