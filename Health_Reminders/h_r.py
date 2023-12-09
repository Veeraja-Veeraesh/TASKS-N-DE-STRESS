#importing module
from tkinter import *
import threading
import time

# the name of the function


def healthreminders():
    # to create a window
    a = Tk()
    #defining a title
    a.title('water break reminder')
    # to create a frame for the buttons
    fr = Frame(a)
    fr.pack()
    #background image
    bg = PhotoImage(master=fr, file='Health_Reminders/background.png')
    label = Label(fr, image=bg)
    label.pack()

    # Home Button Function
    def h():
        a.destroy()
        import main
        main.main_window()

    # Home Button
    home = Button(a, text='HOME', bg='seagreen1',
                  command=lambda: h(), padx=22).place(x=340, y=130)

    #options for drop down menu
    options = ["1 hour", "2 hours", "3 hours", "custom"]
    # time_sel is the user's input
    global time_sel

    clicked = StringVar()

    entry_var = StringVar()
    # to set the default drop down option
    clicked.set("set time")

    # to display the image
    def image():
        b = Tk()
        b['bg'] = 'mediumspringgreen'
        b.title('Reminder')
        img = PhotoImage(master=b, file='Health_Reminders/water.png')
        labelimg = Label(b, image=img)
        labelimg.pack()
        b.mainloop()

    # submit button
    def sub_btn():
        if time_sel == 'seconds':
            # Setting the timer using threading
            timer = threading.Timer(int(entry_var.get()), image)
            timer.start()

        if time_sel == 'minutes':
            timer = threading.Timer(int(entry_var.get())*60, image)
            timer.start()

        if time_sel == 'hours':
            timer = threading.Timer(int(entry_var.get())*3600, image)
            timer.start()

    #function for the cancel button
    def cancel_btn():
        timer = threading.Timer(int(entry_var.get()), image)
        timer.cancel()
        # label to display 'timer cancelled'
        label = Label(text='Timer Cancelled', bg='navajowhite',
                      fg='midnightblue',
                      activebackground='skyblue')
        label.place(x=340, y=95)

    # function to save user's input from drop down list 2
    def display_selected2(choice):
        choice2 = clicked2.get()
        global time_sel
        time_sel = choice2
        time_entry = Entry(fr, textvariable=entry_var, width=5,
                           bg='navajowhite', fg='saddlebrown')
        time_entry.place(x=230, y=175)
        # submit button
        btn = Button(fr, text='Submit', command=sub_btn, bg='navajowhite',
                     fg='midnightblue', activebackground='skyblue')
        btn.place(x=210, y=200)
        # cancel button
    cancel_btn = Button(fr, text="Cancel Reminder", command=cancel_btn,
                        bg='navajowhite', fg='midnightblue', activebackground='skyblue')
    cancel_btn.place(x=340, y=50)

    # function to save user's input from drop down list 1
    def display_selected(choice):
        choice = clicked.get()
        global val
        val = choice

        def time1(choice):
            if choice == '1 hour':
                time.sleep(3600)
                image()
            if choice == '2 hour':
                time.sleep(3600 * 2)
                image()
            if choice == '3 hour':
                print('recorded')
                time.sleep(3600 * 3)
                image()
            if choice == 'custom':
                label2 = Label(a,
                               text='Enter time in?',
                               bg='navajowhite',
                               fg='midnightblue',
                               activebackground='skyblue')
                label2.place(x=209, y=94)
                options2 = ['seconds', 'minutes', 'hours']
                global clicked2
                clicked2 = StringVar()
                clicked2.set(options2[0])
                drop2 = OptionMenu(fr,
                                   clicked2,
                                   *options2,
                                   command=display_selected2)
                drop2.config(bg='navajowhite',
                             fg='midnightblue',
                             activebackground='skyblue')
                drop2["menu"].config(bg='navajowhite')
                drop2.place(x=210, y=130)

        print(time1(val))

    drop = OptionMenu(fr, clicked, *options,
                      command=display_selected)
    drop.config(bg='navajowhite',
                fg='midnightblue',
                activebackground='skyblue')

    drop["menu"].config(bg='navajowhite',
                        fg='midnightblue')

    drop.place(x=210, y=50)

    a.mainloop()

#healthreminders()
