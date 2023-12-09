# MySQL Connect Module
import mysql.connector as sqlcon

# #Connecting to remote SQL database
# mycon = sqlcon.connect(host='db4free.net', port=3306, user='planner202122',
#                        passwd='YBv2VEPTM3', database='planner202122')

# #Checking if connection is established
# if mycon.is_connected():
#     print('Connected Successfully!')
# else:
#     print('Error in Connecting')


mycon = sqlcon.connect(host='127.0.0.1', port=3306, user='root',
                       passwd='Root@123', database='planner202122')

#Checking if connection is established
if mycon.is_connected():
    print('Connected Successfully!')
else:
    print('Error in Connecting')

#Creating a cursor
cursor = mycon.cursor()
