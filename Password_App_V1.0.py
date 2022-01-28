#-------------------------------------------------------
# THIS PROGRAM READS PASSWORD INPUT FROM USER
# AND OUPUTS IT TO THE FILE software.txt
#----------------------------------------------------

#Create window and set size
import tkinter as tk
window = tk.Tk()
window.geometry("620x780")
window.title("Password Database")

#Create 3 labels for username, password and website
username = tk.Label(text = "Username")
username.grid(column=0,row=1)
password = tk.Label(text = "Password")
password.grid(column=0,row=2)
website = tk.Label(text = "Website")
website.grid(column=0,row=3)

#Create 3 entry fields for username, password and website
username_entry = tk.Entry()
username_entry.grid(column=1,row=1)
password_entry = tk.Entry()
password_entry.grid(column=1,row=2)
website_entry = tk.Entry()
website_entry.grid(column=1,row=3)

#Create function to take entries and create a results bar
def getInput():
    result = Web(str(username_entry.get()),str(password_entry.get()),str(website_entry.get()))
    textArea = tk.Text(master=window,height=10,width=25)
    textArea.grid(column=1,row=6)
    answer = "Password Entry Complete!"
    textArea.insert(tk.END,answer)

class Web:
    def _init_(name,word,site):
        name.username = username
        word.password = password

#Create a button to submit results
button=tk.Button(window,text="Save",command=getInput,bg="lightblue")
button.grid(column=1,row=5)

# FIRST WE TAKE INPUT FOR THE SOFTWARE TITLE
file = open("Software.txt", "a")
file.write(website + "\n")
file.write(username + "\n")
file.write(password + "\n")
file.write("---" + "\n")
file.close()
window.mainloop()
