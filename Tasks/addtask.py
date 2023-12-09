from tkinter import *
import Tasks.task
import Tasks.instructions

from Tasks import connect

# Add Task Window Function
def at():
    at_win = Tk()
    at_win.title('ADD TASK')
    at_win['bg'] = 'grey20'
    
    Label(at_win,text = 'READ INSTRUCTIONS FIRST',font = ('Courier New','12'),fg = 'grey99',bg = 'grey20').grid(row = 0, column = 1)

    Label(at_win,text = 'SrNo.',font = ('Courier New','12'),fg = 'grey99',bg = 'grey20').grid(row=1,column=0)
    
    srno_var = IntVar()

    Entry(at_win,textvariable = srno_var,font = ('Courier New','12')).grid(row = 1, column = 1)

    # Task Name label + entry box
    Label(at_win,text = 'Task Name',font = ('Courier New','12'),fg = 'grey99',bg = 'grey20').grid(row = 2, column = 0)
    
    name_var = StringVar()

    Entry(at_win,textvariable = name_var,font = ('Courier New','12')).grid(row = 3, column = 0)

    # Task Notes label + entry box
    Label(at_win,text = 'Task Notes',font = ('Courier New','12'),fg = 'grey99',bg = 'grey20').grid(row = 2, column = 2)

    notes_var = StringVar()

    Entry(at_win,textvariable = notes_var,font = ('Courier New','12'),).grid(row = 3, column = 2)

    # Due Date Section Label + Entry Box
    Label(at_win,text = 'DUE DATE SECTION',font = ('Courier New','12','bold'),fg = 'grey99',bg = 'grey20').grid(row = 4, column = 0)
    
    date_var = StringVar()

    Entry(at_win,textvariable = date_var,font = ('Courier New','12')).grid(row = 5, column = 0)

    # Due Time Section label + Entry Box
    Label(at_win,text = 'DUE TIME SECTION',font = ('Courier New','12','bold'),fg = 'grey99',bg = 'grey20').grid(row = 4, column = 2)

    time_var = StringVar()

    Entry(at_win,textvariable = time_var,font = ('Courier New','12')).grid(row = 5, column = 2)

    def b():
        at_win.destroy()
        Tasks.task.task_win()

    # Back Button
    Button(at_win,text = 'BACK',command = lambda : b(),font = ('Courier New','12','bold')).grid(row = 14, column = 0)

    # Saving entered values
    def save_val():
        srno = srno_var.get()
        name = name_var.get()
        notes = notes_var.get()
        date = date_var.get()
        time = time_var.get()
        date_time = date + ' ' + time

        # Inserting data into taskstable
        sql1 = "INSERT INTO taskstable VALUES (%s,%s,%s,%s);"
        val1 = (srno,name,notes,date_time)
        connect.cursor.execute(sql1,val1)
        connect.mycon.commit()
    # Save Task Button
    Button(at_win,text = 'SAVE',command = lambda : save_val(),font = ('Courier New','12','bold')).grid(row = 14, column = 1)

    # Instructions Button
    Button(at_win,text = 'INSTRUCTIONS',command = lambda : Tasks.instructions.inst(),font = ('Courier New','12','bold')).grid(row = 14, column = 2)


    at_win.mainloop()
#at()