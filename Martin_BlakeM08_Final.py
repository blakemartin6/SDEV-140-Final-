from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox 
# Create object 
root = Tk()
root.title("Brickyard Pit Stop") 
# Adjust size 
root.geometry("700x600")


#Changing background
#assigning global variables to call on later 
global bg, count

#starting count at -1
count = -1

#list to hold multiple images 
bg = [PhotoImage(file = "fallGolf3.png"),
      PhotoImage(file = "golfresize1.png"),
      PhotoImage(file = "golfresize2.png"),
      ]

# Create Canvas
canvas1 = Canvas(root, width = 700,
                 height = 600)
  
canvas1.pack(fill = "both", expand = True)

#adding text to the canvas
label17 = Label(root, text="Brickyard Pit Stop \n Menu", font = "arial 10 bold", relief=SUNKEN)
label17.place(x=300, y=25)


# Display images 
canvas1.create_image(0, 0, image = bg[0], 
                     anchor = "nw")
 
#calculating price of everything
def calculate():
    #dictionary with menu items and prices
    dic = {"Hot Dog": [e1, 2],
           "Burger": [e2, 2],
           "Pizza Slice":[e3, 2],
           "Chips": [e4, 1],
           "Cookies": [e5, 1.50],
           "Crackers": [e6, .50],
           "Water": [e7, 2],
           "Soda": [e8, 2.50],
           "Beer": [e9, 3],
           }
    total = 0

    for key, val in dic.items():
        if val[0].get() != "":
            total += float(val[0].get())*val[1]

    label16 = Label(root, text="Your total bill is $"+str("{:.2f}".format(total)), font="times 18", relief = RAISED)
    label16.place(x=350,y=400)
    label16.after(1000,label16.destroy)
    root.after(1000,calculate)


def message():
    messagebox.showinfo("Order Confirmation", "Thank you for your order! You can pick it up in the club house.")
def message2():
    messagebox.showinfo("Instructions", "To order type the amount of each item you would like \n into the black boxes your total \n will update as you enter in your items."
                        "\n Click order when done! ")

# Create Buttons
button1 = Button( root, text = "Order", command=message)
button2 = Button( root, text = "Exit", command=root.destroy)
button3 = Button(root, text="Instructions", command=message2)
  
# Display Buttons
button1_canvas = canvas1.create_window( 350, 550, 
                                       anchor = "center",
                                       window = button1)
  
button2_canvas = canvas1.create_window( 350, 575,anchor = "center",
                                       window = button2)
button3_canvas = canvas1.create_window( 50, 25,anchor = "center",
                                       window = button3)

#Displaying the menu
label1 = Label(root, text="SPECIALS\n Hot Dog $2.00\n Burger $2.00\n Pizza Slice $2.00",font="arial 16 bold",relief=RAISED)
label1.place(x=100,y=100)

label2 = Label(root, text="SNACKS\n Chips 1.00\n Cookies $1.50\n Crackers $.50",font="arial 16 bold", relief=RAISED)
label2.place(x=287, y=100)

label3 = Label(root, text="DRINKS\n Water = $2.00\n Soda = $2.50\n Beer = $3.00", font ="arial 16 bold",relief=RAISED)
label3.place(x=450,y=100)


#Labels to know what you are picking 
#Entry boxes to pick how much of each item
label4 = Label(root, text=" Hot Dog \n Burger \n Pizza Slice ",font="arial 10 bold",relief=RAISED)
label4.place(x=100,y=220)

e1 = Entry(root, width=5, relief =RAISED, background="black",foreground="white")
e1.place(x=185,y=220)

e2 = Entry(root, width = 5, relief=RAISED, background="black",foreground="white")
e2.place(x=185,y=239)

e3 = Entry(root, width = 5, relief=RAISED,background="black",foreground="white")
e3.place(x=185,y=255)

label5 = Label(root, text=" Chips \n Cookies \n Crackers ",font="arial 10 bold",relief=RAISED)
label5.place(x=287,y=220)

e4 = Entry(root, width=5, relief =RAISED, background="black",foreground="white")
e4.place(x=356,y=220)

e5 = Entry(root, width=5, relief =RAISED, background="black",foreground="white")
e5.place(x=356,y=239)

e6 = Entry(root, width=5, relief =RAISED, background="black",foreground="white")
e6.place(x=356,y=255)

label6 = Label(root, text=" Water \n Soda \n Beer ",font="arial 10 bold",relief=RAISED)
label6.place(x=450,y=220)

e7 = Entry(root, width=5, relief =RAISED, background="black",foreground="white")
e7.place(x=500,y=220)

e8 = Entry(root, width=5, relief =RAISED, background="black",foreground="white")
e8.place(x=500,y=239)

e9 = Entry(root, width=5, relief =RAISED, background="black",foreground="white")
e9.place(x=500,y=255)

#Counter function for background images 
def next():
    global count
    if count == 2:
        canvas1.create_image(0,0, image=bg[0], anchor='nw')
        count = 0
    else:
        canvas1.create_image(0,0, image=bg[count+1], anchor='nw')
        count += 1

    root.after(10000,next)

next()
root.after(1000,calculate)
# Execute tkinter
root.mainloop()
