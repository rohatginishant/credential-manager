from classes import Credentials
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import json


with open("cred.json", "r") as json_file:
    data = json.load(json_file)


def all():
    value1.set(1)
    data["jenkins1"]["select"] = value1.get()
    value2.set(1)
    data["jenkins2"]["select"] = value2.get()


def select1():
    data["jenkins1"]["select"] = value1.get()


def select2():
    data["jenkins2"]["select"] = value2.get()


root = tk.Tk()
root.title(" Watchguard CI Operations Center ")
root.geometry('1200x800+50+50')

value1 = tk.IntVar()
value2 = tk.IntVar()

username = tk.StringVar()  #object where to store the value received as input ,string where value = whatever is entered.
id = tk.StringVar()
password = tk.StringVar()
new_id = tk.StringVar()
new_name = tk.StringVar()
new_pass = tk.StringVar()
del_id = tk.StringVar()


def create_submit():
    for jenkins_name, item in data.items():
        if item["select"] == 1:
            jenkins_url = item["jenkins__url"]
            jenkins_auth_username = item["auth__username"]
            jenkins_auth_password = item["auth__password"]
            crumb_url = item["crumbIssuer"]
            obj = Credentials(jenkins_url, jenkins_auth_username, jenkins_auth_password)
            print(obj.create(id.get(), username.get(), password.get(), crumb_url))


def manage_submit():
    for jenkins_name, item in data.items():
        if item["select"] == 1:
            jenkins_url = item["jenkins__url"]
            jenkins_auth_username = item["auth__username"]
            jenkins_auth_password = item["auth__password"]
            obj = Credentials(jenkins_url, jenkins_auth_username, jenkins_auth_password)
            print(obj.manage(id.get(), new_id.get(), new_name.get(), new_pass.get()))


def delete_submit():
    for jenkins_name, item in data.items():
        if item["select"] == 1:
            jenkins_url = item["jenkins__url"]
            jenkins_auth_username = item["auth__username"]
            jenkins_auth_password = item["auth__password"]
            obj = Credentials(jenkins_url, jenkins_auth_username, jenkins_auth_password)
            print(obj.delete(del_id.get()))


def create_frame():
    for widget in root.winfo_children():
        print(widget)

    for widget in details_frame.winfo_children():
        widget.destroy()

    label = tk.Label(details_frame, text=" Enter credentials : ")
    label.pack()

    id_label = tk.Label(details_frame, text=" Enter id: ")
    id_label.pack(side="left", padx=(0, 10))  # padx = left,right , pady = top,bottom
    id_entry = tk.Entry(details_frame, width=15, textvariable=id)
    id_entry.pack(side="left", padx=(0, 10))
    id_entry.focus()  # enter on a particular component so that it apeears focused in a window.

    name_label = tk.Label(details_frame, text=" Enter username: ")
    name_label.pack(side="left", padx=(0, 10))  # padx = left,right , pady = top,bottom
    name_entry = tk.Entry(details_frame, width=15, textvariable=username)
    name_entry.pack(side="left", padx=(0, 10))
    name_entry.focus()  # enter on a particular component so that it apeears focused in a window.

    password_label = tk.Label(details_frame, text=" Enter password: ")
    password_label.pack(side="left", padx=(0, 10))  # padx = left,right , pady = top,bottom
    password_entry = tk.Entry(details_frame, width=15, textvariable=password)
    password_entry.pack(side="left", padx=(0, 10))

    button_frame = tk.Frame(details_frame)
    button_frame.pack(side="bottom", pady=10)

    submit_button = tk.Button(button_frame, text="Submit", command=create_submit)
    submit_button.pack(side="left", padx=10)

    quit_button = tk.Button(button_frame, text="Quit", command=quit)
    quit_button.pack(side="bottom", padx=10)


def manage_frame():
    for widget in details_frame.winfo_children():
        widget.destroy()

    id_label = tk.Label(details_frame, text=" Enter Id of cred to update : ")
    id_label.pack(side="left", padx=(0, 10))  # padx = left,right , pady = top,bottom
    id_entry = tk.Entry(details_frame, width=15, textvariable=id)
    id_entry.pack(side="left", padx=(0, 10))
    id_entry.focus()  # enter on a particular component so that it apeears focused in a window.

    newid_label = tk.Label(details_frame, text=" Enter new  id: ")
    newid_label.pack(side="left", padx=(0, 10))  # padx = left,right , pady = top,bottom
    newid_entry = tk.Entry(details_frame, width=15, textvariable=new_id)
    newid_entry.pack(side="left", padx=(0, 10))
    newid_entry.focus()  # enter on a particular component so that it apeears focused in a window.

    name_label = tk.Label(details_frame, text=" Enter new username: ")
    name_label.pack(side="left", padx=(0, 10))  # padx = left,right , pady = top,bottom
    name_entry = tk.Entry(details_frame, width=15, textvariable=new_name)
    name_entry.pack(side="left", padx=(0, 10))
    name_entry.focus()  # enter on a particular component so that it apeears focused in a window.

    password_label = tk.Label(details_frame, text=" Enter new password: ")
    password_label.pack(side="left", padx=(0, 10))  # padx = left,right , pady = top,bottom
    password_entry = tk.Entry(details_frame, width=15, textvariable=new_pass)
    password_entry.pack(side="left", padx=(0, 10))

    button_frame = tk.Frame(details_frame)
    button_frame.pack(side="bottom", pady=10)

    submit_manage_button = tk.Button(button_frame, text="Submit", command=manage_submit)
    submit_manage_button.pack(side="left", padx=10)

    quit_button = tk.Button(button_frame, text="Quit", command=quit)
    quit_button.pack(side="bottom", padx=10)


def del_frame():
    for widget in details_frame.winfo_children():
        widget.destroy()

    id_label = tk.Label(details_frame, text=" Enter Id of credentials to delete : ")
    id_label.pack(side="left", padx=(0, 10))  # padx = left,right , pady = top,bottom
    id_entry = tk.Entry(details_frame, width=15, textvariable=del_id)
    id_entry.pack(side="left", padx=(0, 10))
    id_entry.focus()

    button_frame = tk.Frame(details_frame)
    button_frame.pack(side="bottom", pady=10)

    delete_button = tk.Button(button_frame, text="Submit", command=delete_submit)
    delete_button.pack(side="left", padx=10)

    quit_button = tk.Button(button_frame, text="Quit", command=quit)
    quit_button.pack(side="bottom", padx=10)


cv = Canvas(root, width=150, height=150)
cv.pack(side=TOP)
img = ImageTk.PhotoImage(Image.open("jnk.png"))
cv.create_image(75, 75, anchor=CENTER, image=img)

jenkins_frame = tk.Frame(root, width=200,height=100,pady=20)
jenkins_frame.pack()

checkbox3 = tk.Checkbutton(jenkins_frame, text="Select all",command=all)
checkbox3.pack(side="left")
checkbox = tk.Checkbutton(jenkins_frame, text="Jenkins-1", variable=value1, command=select1)
checkbox.pack(side="left")
checkbox2 = tk.Checkbutton(jenkins_frame, text="Jenkins-2", variable=value2, command=select2)
checkbox2.pack(side="left")

label = tk.Label(root, text=" Options : ", pady=10)
label.pack()

menu_frame = tk.Frame(root, height=50, width=400, pady=10)
menu_frame.pack()

create_button = tk.Button(menu_frame, text="Create", command=create_frame)
create_button.pack(side="left", padx=(0, 10))  # Pack : put in window ,  place the components where they should be

manage_button = tk.Button(menu_frame, text="Manage", command=manage_frame)
manage_button.pack(side="left", padx=(0, 10))  # Pack : put in window ,  place the components where they should be

del_button = tk.Button(menu_frame, text="Delete", command=del_frame)
del_button.pack(side="left", padx=(0, 10))

details_frame = tk.Frame(root, height=400, width=200, pady=10)
details_frame.pack()

root.mainloop()
