# Importing required module(s)
from tkinter import *
from Tasks import deltask, addtask,connect

# Task Window Function
def task_win():
    tasks_win = Tk()
    tasks_win.title('TASKS')
    tasks_win['bg'] = 'grey20'

    # Home Button Function
    def h():
        connect
        tasks_win.destroy()
        import main
        main.main_window()

    # Home Button
    home = Button(tasks_win,text = 'HOME',bg = 'seagreen1',command = lambda : h(),padx = 22).grid(row = 24, column = 1)

    # Add Task Window Button Function
    def adta():
        tasks_win.destroy()
        addtask.at()

    # Add Task Window Button
    add = Button(tasks_win,text = 'ADD TASK',bg = 'light sky blue',command = lambda : adta(),padx = 12).grid(row = 24, column = 2)

    # Delete Task Window Button Functiom
    def del_func():
        tasks_win.destroy()
        deltask.del_win()

    # Delete Task Window Button
    delete = Button(tasks_win,text = 'DELETE TASK',bg = 'red',command = lambda : del_func()).grid(row = 24, column = 3)
    
    def upd():
        # Serial Number Column
        Label(tasks_win,text = 'SrNo.',font=('Courier New',14),width = 8,relief = 'ridge').grid(row = 0, column = 0)

        # Task Name Column
        Label(tasks_win,text = 'TASKS',font=('Courier New',14),width = 30,relief = 'ridge').grid(row = 0, column = 1)

        # Task Name Column
        Label(tasks_win,text = 'NOTES',font=('Courier New',14),width = 30,relief = 'ridge').grid(row = 0, column = 2)

        # Due Date_Time Column
        Label(tasks_win,text = 'DATE_TIME',font=('Courier New',14),width = 17,relief = 'ridge').grid(row = 0, column = 3)

        connect.cursor.execute('SELECT * FROM taskstable;')
        rec = connect.cursor.fetchall()

        i = 1 #row number
        for a in rec:

            j=0     #column number
            for k in a:
                if j == 1 or j == 2:

                    dat1 = Label(tasks_win,text=a[j],fg = 'gray99',font=('Courier New',12),bg = 'grey20',width = 56,).grid(row=i, column=j)
                if j != 1 or j!= 2:

                    dat2 = Label(tasks_win,text=a[j],fg = 'gray99',font=('Courier New',12),bg = 'grey20').grid(row=i, column=j)
                j+=1

            i += 1

    
    update = Button(tasks_win, text='REFRESH', command=lambda: upd(), padx = 12).grid(row=24, column=0)

    tasks_win.mainloop()

#Calling Tasks window dunction
#task_win()
