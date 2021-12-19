""""
User interface (UI) design concepts before coding are subdivided into 3 categories:-
1) Low fidelity== sketching and wireframe
2) Medium fidelity== mockup
3) High-fidelity== Prototype

visit for UI for use; Zeplin seems fair
https://medium.com/@denisz.design/the-best-ui-sketching-tools-a600758be692

Task is to create a program that stores this book information:

-Title, Author
Year, ISBN

User can perform the following tasks:-
-view all records
-search an entry
-update entry
-Delete
-Close

"""
# importing whole ** tkinter library with *
from tkinter import *

window=Tk()     # for the UI inputs

l1= Label(window, text= "Title")  # input the labels
l1.grid(row=0, column=0)           # sketch the grid for the


# create inputs for data entry
title_text=StringVar()
e1= Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)                   # locate the placement of data entry



# for the functions within the
window.mainloop()