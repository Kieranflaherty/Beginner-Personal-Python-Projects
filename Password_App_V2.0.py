from tkinter import *
import tkinter.messagebox

def onClick():
    tkinter.messagebox.showinfo("Password Manager","Data Saved Successfully")

#def clear():
#    username_str.delete(0, END)

def save_info():
    global username
    global password
    global website

    username_str = username.get()
    password_str = password.get()
    website_str = website.get()
    print(username,password,website)

    file = open("Software.txt","a")
    file.write("Username: " + username_str)
    file.write("\n")
    file.write("Password: " + password_str)
    file.write("\n")
    file.write("Website: " + website_str)
    file.write("\n")
    file.write("----------")
    file.write("\n")
    file.close()
    return

app = Tk()
app.geometry("500x500")
app.title("Password Manager")
heading = Label(text="Password Manager",fg="white",bg="blue",width="500",height="3",font="10")
heading.pack()

username_text = Label(text="Username: ")
password_text = Label(text="Password: ")
website_text = Label(text="Website: ")
username_text.place(x=15,y=70)
password_text.place(x=15,y=140)
website_text.place(x=15,y=210)

username = StringVar()
password = StringVar()
website = StringVar()

username_entry = Entry(textvariable=username,width="30")
password_entry = Entry(textvariable=password,width="30")
website_entry = Entry(textvariable=website,width="30")
username_entry.place(x=15,y=100)
password_entry.place(x=15,y=170)
website_entry.place(x=15,y=240)

button = Button(app,text="Submit Data",command=lambda:[save_info(),onClick()],width="15",height="2",bg="lightgrey")
button.place(x=15,y=290)

#button2 = Button(app,text="Clear",command=clear,width="15",height="2",bg="lightgrey")
#button2.place(x=15,y=350)

app.mainloop()
