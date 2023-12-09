from tkinter import *

# Instructions Window Function
def inst():
    in_win = Tk()
    in_win.title('INSTRUCTIONS')
    in_win.geometry('400x210')

    Label(in_win,text = 'All the values are compulsory',font = ('Courier New','12','bold'),pady = 5).pack()

    # Labels for the instructions
    Label(in_win,text = 'Enter Due Date in YYYY-MM-DD format.',font = ('Courier New','12','bold'),pady = 5).pack()

    Label(in_win,text = 'Enter Due Time in HH:MM:SS',font = ('Courier New','12','bold'),pady = 5).pack()

    Label(in_win,text = 'Only one task can be saved at a time.',font = ('Courier New','12','bold'),pady = 5).pack()
    
    Label(in_win,text = 'In order to save another task, reopen',font = ('Courier New','12','bold'),pady = 5).pack()
    
    Label(in_win,text = 'the add task window, enter the details',font = ('Courier New','12','bold'),pady = 5).pack()

    Label(in_win,text = 'and click save again.',font = ('Courier New','12','bold'),pady = 5).pack()

    in_win.mainloop()

#inst()