import tkinter as tk

root = tk.Tk()
root.geometry('300x300')
items=['Food a','Food b','food c','food d','food e','food f']         #food items

#a tkinter label object shouldn't be stored as a string, as it loses it's value
#if you print tkinter label object, it looks like this: .!label1 or .!label2   same for button objects: .!button1 then .!button2 etc

#stores the food name as key and tkinter label object(here the label shows the food name) as value like {'food a':<tkinter label object>,'food b':<tkinter label object>}
itemslbl_dict={} 
itemlblnum=0

#stores the quantity of each food that the user has added to cart
quantityval_dict={}
for i in items:
    quantityval_dict[i]=0   #initially it is 0

#stores the food name as key and tkinter label object as value. Here the label shows the quantity of each food and is placed between the + and - buttons
quantitylbl_dict={}
quantlblnum=0

#stores food name as key and tkinter button object associated with the food name as value. 
#i.e. one plus button is associated with increasing the quantity of one food item and not any other food item
plusbtn_dict={}
plusbtnnum=0

#same with the minus button dict
minusbtn_dict={}
minusbtnnum=0

#loop to generate the labels for the items/food names
for i in items:
    lbl=tk.Label(root, text=i)    
    lbl.grid(row=itemlblnum,column=0)
    itemlblnum+=1
    itemslbl_dict[i] = [lbl]   


#this function increase the label showing qauntity by 1 & update the dictionary containing the quantity of each food
#executes whenever a plus button is clicked
def plusbtnclick(item_name):
    global quantitylbl_dict, quantityval_dict

    lbl = quantitylbl_dict[item_name]
    val = int(lbl[0].cget("text"))
    lbl[0].config(text=str(val+1))  # increases the value of the variable by 1
    quantityval_dict[item_name]=val+1 #updating the dictionary so that it stores the right quantity of each food item

#same fucntion as the above one except that it decreses quantity by 1 and
#executes whenever a minus button is clicked 
def minusbtnclick(item_name):
    global quantitylbl_dict, quantityval_dict

    lbl=quantitylbl_dict[item_name]
    val = int(lbl[0].cget("text"))
    lbl[0].config(text=str(val-1))  # decreaseses the value of the variable by 1
    quantityval_dict[item_name]=val-1

for i in items:

    #creating the quantity label, placing it between the + and - buttons and adding the label's object id to the lbldictionary
    lbl=tk.Label(root,text=0)
    lbl.grid(row=quantlblnum,column=2)
    quantitylbl_dict[i]=[lbl]
    
    #creating the + button , placing it before the quantity label and adding the button's object id to the plusbtndictionary
    plusbtn = tk.Button(root, text="+")
    plusbtn.grid(row=plusbtnnum, column=1)
    plusbtn_dict[i]=[plusbtn]

    #creating the - button , placing it after the quantity label and adding the button's object id to the minusbtndictionary
    minusbtn = tk.Button(root, text="-")
    minusbtn.grid(row=minusbtnnum, column=3)
    minusbtn_dict[i]=[minusbtn]

    #updating the value by one so that the buttons and labels can be placed at the next row
    quantlblnum+=1
    plusbtnnum+=1
    minusbtnnum+=1

#assigning the plusbtnclick fucntion to each of the + buttons that we created
for plusbtnobj in plusbtn_dict:
    plusbtn_dict[plusbtnobj][0].configure(command= lambda x=plusbtnobj: plusbtnclick(x))

#assigning the minusbtnclick fucntion to each of the - buttons that we created
for minusbtnobj in minusbtn_dict:
    minusbtn_dict[minusbtnobj][0].configure(command=lambda x=minusbtnobj: minusbtnclick(x))

tk.mainloop()

#this loop shows the final quantities of the food that was oredered once the tkinter window is closed
for i in quantityval_dict:
    print(i,'  :  ',quantityval_dict[i])
