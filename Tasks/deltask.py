from tkinter import *
from Tasks import task,connect

# Retreiving data from taskstable
connect.cursor.execute('SELECT * FROM taskstable;')
rec1 = connect.cursor.fetchall()


# Delete Task Window Function
def del_win():
    delwin = Tk()
    delwin.title('DELETE TASK')
    delwin['bg'] = 'grey20'

    # Enter Task Name Label
    Label(delwin,text = 'Task No.',font = ('Courier New','12','bold'),fg = 'grey99',bg = 'grey20').grid(row = 0, column = 0)

    srno_var = IntVar()

    Entry(delwin,textvariable = srno_var,font = ('Courier New','12')).grid(row = 0, column = 1)

    # Delete Task Button Function
    def deltask():
        srno = srno_var.get()


        # Deleting all the data from taskstable; data of notes table gets deleted simultaneously
        sql = 'DELETE FROM taskstable WHERE ID = %s'%(srno)
        connect.cursor.execute(sql)
        connect.mycon.commit()
    
    # Delete task button
    Button(delwin,text = 'CONFIRM DELETE',command = lambda : deltask(),font = ('Courier New','12','bold'),bg = 'red').grid(row = 1, column = 1)
    
    def back():
        delwin.destroy()
        task.task_win()
    
    Button(delwin,text = 'BACK',command = lambda : back(),font = ('Courier New','12','bold'),bg = 'seagreen1').grid(row = 1, column = 0)
    
    delwin.mainloop()