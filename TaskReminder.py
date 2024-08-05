import customtkinter
from win11toast import toast

dist = {}

app = customtkinter.CTk()
app.geometry("400x500")

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

label  = customtkinter.CTkLabel(app, text = "Name")
label.pack(pady = "20")


flag = [True]

def changeColor ():
    if flag[0] == True :
        customtkinter.set_appearance_mode("dark")
        button.configure(text = "light")
        flag[0] = False
    else :
        customtkinter.set_appearance_mode("light")
        button.configure(text = "dark")
        flag[0] = True


button = customtkinter.CTkButton(app, text= "dark", fg_color=("green","red"), command = lambda: changeColor())
button.pack(pady = "20")

def checkbox_event():
     print("checkbox toggled, current value:", check_var.get())


check_var = customtkinter.StringVar(value="on")
checkbox = customtkinter.CTkCheckBox(app, text="CTkCheckBox", command=checkbox_event, onvalue="on", offvalue="off", variable= check_var)
checkbox.pack(pady = "20")


def combobox_callback(choice):
    print("combobox dropdown clicked:", combobox_var.get())

combobox_var = customtkinter.StringVar(value="option 2")
combobox = customtkinter.CTkComboBox(app, values=["option 1", "option 2"],command= combobox_callback, variable=combobox_var,justify="center")
combobox_var.set("option 2")
combobox.pack(pady = "20")

def entry_check ():
    print("Entered Value ", entry_var.get())
    dist["name"] = entry_var.get()
    entry_var.set("")
    print(dist)

entry_var = customtkinter.StringVar(value="")
entry = customtkinter.CTkEntry(app, placeholder_text="CTkEntry",textvariable=entry_var)
button_entry = customtkinter.CTkButton(app, text="Submit", command= entry_check)
entry.pack(pady = "20")
button_entry.pack(pady = "20")

def windowsAlert ():
    # toast('Hello', 'Hello from Python', icon='https://unsplash.it/64?image=669', audio='ms-winsoundevent:Notification.Looping.Alarm')
    #toast('Hello Python🐍', dialogue='Hello world')
    toast('Hello Python🐍', scenario='incomingCall')
    toast('Hello', 'Hello from Python', button='Dismiss')
    toast('Hello Python', 'Click to open url', on_click='https://www.python.org')

button_alert = customtkinter.CTkButton(app, text="Alarm", command=windowsAlert)
button_alert.pack(pady = "20")
app.mainloop()