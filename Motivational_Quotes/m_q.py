from tkinter import *
import random
import time


def mq_win():
  window = Tk()
  window.title('TBD')
  window.geometry('600x600')
  window.config(bg='lightcyan3')
  #img = PhotoImage(file="image.png")
  label = Label(window)
  label.place(x=0, y=0)

  def number():
    global img_
    a = random.randint(1, 6)
    if a == 1:
      img_ = PhotoImage(file="Motivational_Quotes/image1.png")
    elif a == 2:
      img_ = PhotoImage(file="Motivational_Quotes/image2.png")
    elif a == 3:
      img_ = PhotoImage(file="Motivational_Quotes/image3.png")
    elif a == 4:
      img_ = PhotoImage(file="Motivational_Quotes/image4.png")
    elif a == 5:
      img_ = PhotoImage(file="Motivational_Quotes/image5.png")
    elif a == 6:
      img_ = PhotoImage(file="Motivational_Quotes/image6.png")

  def quotes():
    number()
    label1 = Label(window, image=img_)
    label1.place(x=50, y=50)

  def freq():
    entry_var = StringVar()

    def submit():
      if time_sel == 'seconds':
        time.sleep(int(entry_var.get()))
        quotes()
      if time_sel == 'minutes':
        time.sleep(int(entry_var.get()) * 60)
        quotes()
      if time_sel == 'hours':
        time.sleep(int(entry_var.get()) * 3600)
        quotes()

    def selected1(ch):
      ch1 = clicked1.get()
      global time_sel
      time_sel = ch1
      time_entry = Entry(window, textvariable=entry_var, width=5)
      time_entry.place(x=425, y=10)
      btn = Button(window, text='Submit', command=submit)
      btn.place(x=475, y=10)

    def selected(choice):
      ch = clicked.get()
      choice = ch

      def time_(ch):
        if choice == '30 minutes':
          time.sleep(1800)
          quotes()
        if choice == '1 hour':
          time.sleep(3600)
          quotes()
        if choice == '2 hour':
          time.sleep(3600 * 2)
          quotes()
        if choice == 'custom':
          label1 = Label(window, text="enter time in...")
          label.place(x=300, y=10)
          options1 = ['seconds', 'minutes', 'hours']
          global clicked1

          clicked1 = StringVar()
          drop1 = OptionMenu(window, clicked1, *options1, command=selected1)
          drop1.config(bg='dimgrey')
          drop1["menu"].config()
          drop1.place(x=325, y=10)
      print(time_(entry_var))

    clicked = StringVar()
    clicked.set("select a time")
    drop = OptionMenu(window, clicked, "30 minutes", "1 hour",
                      "2 hours", "custom", command=selected)
    drop.place(x=230, y=10)

  def h():
      window.destroy()
      import main
      main.main_window()

  button = Button(window, text="Motivate me", command=quotes).place(x=10, y=10)
  button2 = Button(window, text="Frequent reminders",
                   command=freq).place(x=100, y=10)
  button3 = Button(window, text="Home", command=h).place(x=540, y=10)

  window.mainloop()
