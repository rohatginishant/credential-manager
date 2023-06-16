from classes import Credentials
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import json
from writejson import data


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
private_key = tk.StringVar()
usernamesecret = tk.BooleanVar()
description = tk.StringVar()
password = tk.StringVar()
new_id = tk.StringVar()
new_name = tk.StringVar()
new_pass = tk.StringVar()
del_id = tk.StringVar()
update_id = tk.BooleanVar()
new_description = tk.StringVar
new_private_key = tk.StringVar()
new_id_assign = tk.IntVar()
new_id_assign.set(0)
new_id.set("")


def display():
    for widget in default_kind_frame.winfo_children():
        widget.destroy()

    label = tk.Label(default_kind_frame, text=typeVar.get())
    label.pack(side="left")

def multiple_fun():
    id_update()
    manage_frame()
    display()

def create_multiple_fun():
    create_frame()
    display()

def kind_frame():

    typeVar.set("")

    for widget in default_kind_frame.winfo_children():
        widget.destroy()

    for widget in kind_update_frame.winfo_children():
        widget.destroy()

    for widget in new_id_frame.winfo_children():
        widget.destroy()

    for widget in details_frame.winfo_children():
            widget.destroy()

    mbtn = tk.Menubutton(kind_update_frame, text="Kind")
    mbtn.pack()

    mbtn.menu = Menu(mbtn, tearoff=0)
    mbtn["menu"] = mbtn.menu

    mbtn.menu.add_radiobutton(label="Username with Password", variable=typeVar, value="username_with_password",
                              command=create_multiple_fun)
    mbtn.menu.add_radiobutton(label="SSH username with key ", variable=typeVar, value="ssh", command=create_multiple_fun)


def manage_kind_frame():

    typeVar.set("")
    for widget in default_kind_frame.winfo_children():
        widget.destroy()

    for widget in kind_update_frame.winfo_children():
        widget.destroy()

    for widget in id_update_frame.winfo_children():
        widget.destroy()

    for widget in details_frame.winfo_children():
        widget.destroy()

    mbtn = tk.Menubutton(kind_update_frame, text="Kind")
    mbtn.pack()

    mbtn.menu = Menu(mbtn, tearoff=0)
    mbtn["menu"] = mbtn.menu

    mbtn.menu.add_radiobutton(label="Username with Password", variable=typeVar, value="username_with_password",
                              command=multiple_fun)
    mbtn.menu.add_radiobutton(label="SSH username with key ", variable=typeVar, value="ssh", command=multiple_fun )


def create_submit():
    if (typeVar.get() == "username_with_password"):
        for jenkins_name, item in data.items():
            if item["select"] == 1:
                jenkins_url = item["jenkins__url"]
                jenkins_auth_username = item["auth__username"]
                jenkins_auth_password = item["auth__password"]
                crumb_url = item["crumbIssuer"]
                obj = Credentials(jenkins_url, jenkins_auth_username, jenkins_auth_password)
                print(obj.create_username_with_password(id.get(), username.get(), password.get(), crumb_url))
    else:
        for jenkins_name, item in data.items():
            if item["select"] == 1:
                jenkins_url = item["jenkins__url"]
                jenkins_auth_username = item["auth__username"]
                jenkins_auth_password = item["auth__password"]
                crumb_url = item["crumbIssuer"]
                obj = Credentials(jenkins_url, jenkins_auth_username, jenkins_auth_password)
                print(obj.create_ssh_with_private_key(id.get(),"description", username.get(), "privatekey",False, crumb_url))




def manage_submit():
    if(typeVar.get()=="username_with_password"):
        for jenkins_name, item in data.items():
            if item["select"] == 1:
                jenkins_url = item["jenkins__url"]
                jenkins_auth_username = item["auth__username"]
                jenkins_auth_password = item["auth__password"]
                obj = Credentials(jenkins_url, jenkins_auth_username, jenkins_auth_password)
                print(obj.manage_username_with__password(id.get(), new_id.get(), new_name.get(), new_pass.get(),
                                                        new_id_assign.get()))
    else:
        for jenkins_name, item in data.items():
            if item["select"] == 1:
                jenkins_url = item["jenkins__url"]
                jenkins_auth_username = item["auth__username"]
                jenkins_auth_password = item["auth__password"]
                obj = Credentials(jenkins_url, jenkins_auth_username, jenkins_auth_password)
                print(obj.manage_ssh_with_private_key(id.get(), new_id.get(), new_name.get(), "",
                                                        new_private_key.get(),new_id_assign.get()))


def delete_submit():
    for jenkins_name, item in data.items():
        if item["select"] == 1:
            jenkins_url = item["jenkins__url"]
            jenkins_auth_username = item["auth__username"]
            jenkins_auth_password = item["auth__password"]
            obj = Credentials(jenkins_url, jenkins_auth_username, jenkins_auth_password)
            print(obj.delete(del_id.get()))

def print_credentials():

    for widget in new_id_frame.winfo_children():
        widget.destroy()
    for widget in default_kind_frame.winfo_children():
        widget.destroy()

    for widget in kind_update_frame.winfo_children():
        widget.destroy()

    for widget in id_update_frame.winfo_children():
        widget.destroy()

    for widget in details_frame.winfo_children():
        widget.destroy()

    int = 0
    for jenkins_name, item in data.items():
        if item["select"] == 1:
            jenkins_url = item["jenkins__url"]
            jenkins_auth_username = item["auth__username"]
            jenkins_auth_password = item["auth__password"]
            crumb_url = item["crumbIssuer"]
            obj = Credentials(jenkins_url, jenkins_auth_username, jenkins_auth_password)
            response = obj.get_credentials()
            credentials = response.json()["credentials"]
            new_label = tk.Label(details_frame,text=f" Credentials for {jenkins_name}: ")
            new_label.pack(side="top")
            for i in credentials:

                label = tk.Label(details_frame,text = f"Id : {i['id']}, Description : {i['description']}, Type : {i['typeName']}")
                label.pack(side="top",padx=(0,10))


def create_frame():

    for widget in id_update_frame.winfo_children():
        widget.destroy()

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

    if typeVar.get() == "username_with_password":

        password_label = tk.Label(details_frame, text=" Enter password: ")
        password_label.pack(side="left", padx=(0, 10))  # padx = left,right , pady = top,bottom
        password_entry = tk.Entry(details_frame, width=15, textvariable=password,show="*")
        password_entry.pack(side="left", padx=(0, 10))

    else:

        description_label = tk.Label(details_frame, text=" Enter description: ")
        description_label.pack(side="left", padx=(0, 10))  # padx = left,right , pady = top,bottom
        description_entry = tk.Entry(details_frame, width=15, textvariable=description)
        description_entry.pack(side="left", padx=(0, 10))
        description_entry.focus()  # enter on a particular component so that it apeears focused in a window.

        private_key_label = tk.Label(details_frame, text=" Enter private key : ")
        private_key_label.pack(side="left", padx=(0, 10))  # padx = left,right , pady = top,bottom
        private_key_entry = tk.Entry(details_frame, width=15, textvariable=private_key)
        private_key_entry.pack(side="left", padx=(0, 10))
        private_key_entry.focus()

        mbtn = tk.Menubutton(details_frame, text="UsernameSecret")
        mbtn.pack(side="left")

        mbtn.menu = Menu(mbtn, tearoff=0)
        mbtn["menu"] = mbtn.menu

        mbtn.menu.add_radiobutton(label="True", variable=usernamesecret, value=True)
        mbtn.menu.add_radiobutton(label="False", variable=usernamesecret, value=False)


    # button_frame = tk.Frame(details_frame)
    # button_frame.pack(side="bottom", pady=10)

    submit_button = tk.Button(details_frame, text="Submit", command=create_submit)
    submit_button.pack(side="left", padx=10)

    quit_button = tk.Button(details_frame, text="Quit", command=quit)
    quit_button.pack(side="left", padx=10)

def id_update():

    for widget in new_id_frame.winfo_children():
        widget.destroy()

    for widget in id_update_frame.winfo_children():
        widget.destroy()

    for widget in details_frame.winfo_children():
        widget.destroy()

    checkbox5 = tk.Label(new_id_frame, text="Do you wish to update the id : ")
    checkbox5.pack(side="left")
    # proceed_button = tk.Button(id_update_frame, text="Proceed", command = manage_frame)
    # proceed_button.pack(side="left", padx=10)

    R1 = Radiobutton(new_id_frame, text="Yes", variable=new_id_assign, value=1,command=manage_frame)
    R1.pack(side="left")

    R2 = Radiobutton(new_id_frame, text="No", variable=new_id_assign, value=0,command=manage_frame)
    R2.pack(side="left")



def manage_frame():

    for widget in id_update_frame.winfo_children():
        widget.destroy()

    for widget in details_frame.winfo_children():
        widget.destroy()

    id_label = tk.Label(details_frame, text=" Enter Id of cred to update : ")
    id_label.pack(side="left", padx=(0, 10))  # padx = left,right , pady = top,bottom
    id_entry = tk.Entry(details_frame, width=15, textvariable=id)
    id_entry.pack(side="left", padx=(0, 10))
    id_entry.focus()  # enter on a particular component so that it apeears focused in a window.

    if new_id_assign.get() == 1:

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

    if typeVar.get() == "username_with_password":

        password_label = tk.Label(details_frame, text=" Enter new password: ")
        password_label.pack(side="left", padx=(0, 10))  # padx = left,right , pady = top,bottom
        password_entry = tk.Entry(details_frame, width=15, textvariable=new_pass)
        password_entry.pack(side="left", padx=(0, 10))

    else:

        description_label = tk.Label(details_frame, text=" Enter new description: ")
        description_label.pack(side="left", padx=(0, 10))  # padx = left,right , pady = top,bottom
        description_entry = tk.Entry(details_frame, width=15, textvariable=new_description)
        description_entry.pack(side="left", padx=(0, 10))
        description_entry.focus()  # enter on a particular component so that it apeears focused in a window.

        private_key_label = tk.Label(details_frame, text=" Enter new private key : ")
        private_key_label.pack(side="left", padx=(0, 10))  # padx = left,right , pady = top,bottom
        private_key_entry = tk.Entry(details_frame, width=15, textvariable=new_private_key)
        private_key_entry.pack(side="left", padx=(0, 10))
        private_key_entry.focus()

        mbtn = tk.Menubutton(details_frame, text="UsernameSecret")
        mbtn.pack(side="left")

        mbtn.menu = Menu(mbtn, tearoff=0)
        mbtn["menu"] = mbtn.menu

        mbtn.menu.add_radiobutton(label="True", variable=usernamesecret, value=True)
        mbtn.menu.add_radiobutton(label="False", variable=usernamesecret, value=False)



    submit_manage_button = tk.Button(details_frame, text="Submit", command=manage_submit)
    submit_manage_button.pack(side="left", padx=10)

    quit_button = tk.Button(details_frame, text="Quit", command=quit)
    quit_button.pack(side="bottom", padx=10)


def del_frame():

    for widget in default_kind_frame.winfo_children():
        widget.destroy()

    for widget in new_id_frame.winfo_children():
        widget.destroy()

    for widget in kind_update_frame.winfo_children():
        widget.destroy()

    for widget in id_update_frame.winfo_children():
        widget.destroy()

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


def printe():
    print(typeVar.get())

typeVar = tk.StringVar()


menu_frame = tk.Frame(root, height=50, width=400, pady=10)
menu_frame.pack()

label = tk.Label(menu_frame, text=" Options : ", pady=10)
label.pack()

create_button = tk.Button(menu_frame, text="Create", command = kind_frame)
create_button.pack(side="left", padx=(0, 10))  # Pack : put in window ,  place the components where they should be

view_button = tk.Button(menu_frame, text="View", command = print_credentials)
view_button.pack(side="left", padx=(0, 10))

manage_button = tk.Button(menu_frame, text="Manage", command = manage_kind_frame)
manage_button.pack(side="left", padx=(0, 10))

del_button = tk.Button(menu_frame, text="Delete", command=del_frame)
del_button.pack(side="left", padx=(0, 10))

kind_update_frame = tk.Frame(root, height=50, width=200, pady=10)
kind_update_frame.pack()

default_kind_frame = tk.Frame(root, height=50, width=200, pady=10)
default_kind_frame.pack()

new_id_frame = tk.Frame(root, height=50, width=200, pady=10)
new_id_frame.pack()

id_update_frame = tk.Frame(root, height=50, width=200, pady=10)
id_update_frame.pack()

details_frame = tk.Frame(root, height=100, width=50)
details_frame.pack(expand=False)



# q_button = tk.Button(root, text="Quit", command=quit)
# q_button.pack(side="bottom", padx=(0, 10))

root.mainloop()
