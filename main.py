# Importing required module(s)
from tkinter import *
from Health_Reminders import h_r
from Motivational_Quotes import m_q
from Tasks import task, connect
from Time_Table import TimeTable

# Main Window function
def main_window():
    # Characteristics of main window
    main_win = Tk()
    main_win.title("WELCOME TO YOUR PLANNING SPACE")
    main_win.geometry('375x300')
    main_win['bg'] = 'grey20'

    # Health Reminders Button CommandP
    def hr():
        main_win.destroy()
        h_r.healthreminders()

    # Health Reminders Button
    health_reminders = Button(main_win,text = 'Health Reminders',command = lambda : hr(),bg = 'orchid1',font = ('Courier New','15','bold'),padx = 18,).place(relx = 0.5, rely = 0.2, anchor = CENTER)

    # Motivational Quotes Button Command
    def mq():
        main_win.destroy()
        m_q.mq_win()

    # Motivational Quotes Button
    motivational_quotes = Button(main_win,text = 'Motivational Quotes',command = lambda : mq(),bg = 'light sky blue',font = ('Courier New','15','bold')).place(relx = 0.5, rely = 0.4, anchor = CENTER)

    # Task Button Command
    def t():
        main_win.destroy()
        task.task_win()

    # Task Button
    tasks = Button(main_win,text = 'Tasks',command = lambda : t(),bg = 'seagreen1',font = ('Courier New','15','bold'),padx = 84,).place(relx = 0.5, rely = 0.6, anchor = CENTER)
    
    # Time Table Button Command
    def tt():
        TimeTable.tt()

    # Time Table Button
    time_table = Button(main_win,text = 'Time Table',command =lambda : tt(),bg = 'light goldenrod',font = ('Courier New','15','bold'),padx = 54).place(relx = 0.5, rely = 0.8, anchor = CENTER)

    main_win.mainloop()

#Calling main window function
main_window()