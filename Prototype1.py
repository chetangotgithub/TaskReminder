import customtkinter 
from win11toast import toast
from tkcalendar import DateEntry
from test2 import setNotification
import threading


alltaskDetails = {}

app = customtkinter.CTk()
app.geometry("500x500")

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

fontTitle = customtkinter.CTkFont(family='Roboto', size=15)
title = customtkinter.CTkLabel(app, text = "Welcome to Task Reminder", font= fontTitle)
title.pack(padx = 50, pady = 20)

InputFrame = customtkinter.CTkScrollableFrame(app, width=500, height=500)
InputFrame.pack(padx = 20, pady = 5)

framTask = customtkinter.CTkFrame(InputFrame)
framTask.pack(padx=20, pady=20)

lableTask = customtkinter.CTkLabel(framTask, text="Task")
lableTask.grid(column = 0, row = 0, padx = 20, pady = 5)

variableTask = customtkinter.StringVar(value="")
InputTask = customtkinter.CTkEntry(framTask, width= 200 , textvariable=variableTask)
InputTask.grid(column = 1, row = 0, padx = 20, pady = 5)

lableTaskDesc = customtkinter.CTkLabel(framTask, text="Task Description")
lableTaskDesc.grid(column = 0, row = 1, padx = 20, pady = 5)

variableTaskDesc = customtkinter.StringVar(value="")
InputTaskDesc = customtkinter.CTkEntry(framTask, width= 200 , textvariable=variableTaskDesc)
InputTaskDesc.grid(column = 1, row = 1, padx = 20, pady = 5)

lableLink = customtkinter.CTkLabel(framTask, text="Link")
lableLink.grid(column = 0, row = 2, padx = 20, pady = 5)

variableLink = customtkinter.StringVar(value="")
InputLink = customtkinter.CTkEntry(framTask, width= 200 , textvariable=variableLink)
InputLink.grid(column = 1, row = 2, padx = 20, pady = 5)

frameDateTime = customtkinter.CTkFrame(InputFrame)
frameDateTime.pack(padx=20, pady=20)

def validate_numeric_input(action, value_if_allowed, text, validation_type, trigger_type, widget_name):
    if action == '1':  # '1' means insert
        return text.isdigit()    
    return True

vcmd = (app.register(validate_numeric_input), '%d', '%P', '%S', '%v', '%V', '%W')

variableHours = customtkinter.StringVar(value="")
fontDate = customtkinter.CTkFont("Roboto", 15)
labelDate = customtkinter.CTkLabel(frameDateTime, text="Select Hours:", font=fontDate)
labelDate.grid(row=0, column=0, padx=10, pady=5, sticky="e")
EntryHours = customtkinter.CTkEntry(frameDateTime, width=30, textvariable=variableHours, validate="key", validatecommand=vcmd)
EntryHours.grid(row=0, column=1, padx=5, pady=5, sticky="w")

variableMunites = customtkinter.StringVar(value="")
labelDate = customtkinter.CTkLabel(frameDateTime, text="Select Minutes:", font=fontDate)
labelDate.grid(row=0, column=2, padx=10, pady=5, sticky="e")
EntryMinutes = customtkinter.CTkEntry(frameDateTime, width=30, textvariable=variableMunites, validate="key", validatecommand=vcmd)
EntryMinutes.grid(row=0, column=3, padx=5, pady=5, sticky="w")


frameButtons = customtkinter.CTkFrame(InputFrame)
frameButtons.pack(padx=20, pady=20)

def submitTask ():
    taskDetails = {}
    taskDetails["task"] = variableTask.get()
    taskDetails["taskdesc"] = variableTaskDesc.get()
    taskDetails["hours"] = variableHours.get()
    taskDetails["minutes"] = variableMunites.get()
    taskDetails["link"] = variableLink.get()
    alltaskDetails[variableTask.get()] = taskDetails
    toast("Added Task","Added Task: "+ taskDetails["task"], audio='ms-winsoundevent:Notification.Looping.Alarm')

    other_thread = threading.Thread(target=lambda:setNotification(taskDetails["task"],taskDetails["taskdesc"],taskDetails["link"],taskDetails["hours"] ,taskDetails["minutes"]))
    other_thread.start()

buttonSubmit = customtkinter.CTkButton(frameButtons, text = "Submit", command=submitTask)
buttonSubmit.grid(row = 0, column = 0, pady = 5, padx = 10)


def viewTask ():
    print(alltaskDetails)

    app2 = customtkinter.CTk()
    app2.geometry("500x500")

    def deleteTask (task):
        del alltaskDetails[task]
        toast("Deleted Task","Successfully Deleted Task"+ task,audio='ms-winsoundevent:Notification.Looping.Alarm')
        viewTask()
    
    def updateTask (task):
        print("Updated")

    scrollFrame = customtkinter.CTkScrollableFrame(app2, width= 500, height= 500)
    scrollFrame.pack(padx = 20, pady = 20)

    

    for obj in alltaskDetails:
        frameView = customtkinter.CTkFrame(scrollFrame, fg_color=("#ADD8E6","#2c3968"))
        frameView.pack(padx = 5, pady = 5)

        lableTask = customtkinter.CTkLabel(frameView, text="Task: ")
        lableTask.grid(column = 0, row = 0, padx = 20, pady = 10)

        lableTaskid = customtkinter.CTkLabel(frameView, text=alltaskDetails[obj]["task"])
        lableTaskid.grid(column = 1, row = 0, padx = 20, pady = 10)

        lableTaskDesc = customtkinter.CTkLabel(frameView, text="Task Descrition: ")
        lableTaskDesc.grid(column = 0, row = 1, padx = 20, pady = 5)

        lableTaskDescid = customtkinter.CTkLabel(frameView, text=alltaskDetails[obj]["taskdesc"])
        lableTaskDescid.grid(column = 1, row = 1, padx = 20, pady = 5)

        lableLink = customtkinter.CTkLabel(frameView, text="Link: ")
        lableLink.grid(column = 0, row = 2, padx = 20, pady = 5)

        lableLinkid = customtkinter.CTkLabel(frameView, text=alltaskDetails[obj]["link"])
        lableLinkid.grid(column = 1, row = 2, padx = 20, pady = 5)

        lableHours = customtkinter.CTkLabel(frameView, text="Hours")
        lableHours.grid(column = 0, row = 3, padx = 20, pady = 5)

        lableHoursid = customtkinter.CTkLabel(frameView, text=alltaskDetails[obj]["hours"])
        lableHoursid.grid(column = 1, row = 3, padx = 20, pady = 5)

        lableMinutes = customtkinter.CTkLabel(frameView, text="Minutes")
        lableMinutes.grid(column = 0, row = 4, padx = 20, pady = 5)

        lableMinutesid = customtkinter.CTkLabel(frameView, text=alltaskDetails[obj]["minutes"])
        lableMinutesid.grid(column = 1, row = 4, padx = 20, pady = 5)

        frameButtons= customtkinter.CTkFrame(scrollFrame)
        frameButtons.pack(padx = 5, pady = 5)

        buttonDeleteTask = customtkinter.CTkButton(frameButtons, text = "Delete", command=lambda:deleteTask(obj))
        buttonDeleteTask.grid(row = 0, column = 0, padx = 20, pady = 5)

        buttonUpdateTask = customtkinter.CTkButton(frameButtons, text = "Update", command=lambda:updateTask(obj))
        buttonUpdateTask.grid(row = 0 , column = 1, padx = 20, pady = 5)


    app2.mainloop()

     # master argument is optional  

buttonSubmit = customtkinter.CTkButton(frameButtons, text = "View Tasks", command=viewTask)
buttonSubmit.grid(row = 0, column = 1, pady = 5, padx = 10)

flag = [True]
def changeColor ():
    if flag[0] == True :
        customtkinter.set_appearance_mode("dark")
        buttonToggel.configure(text = "light")
        flag[0] = False
    else :
        customtkinter.set_appearance_mode("light")
        buttonToggel.configure(text = "dark")
        flag[0] = True


buttonToggel = customtkinter.CTkButton(frameButtons, text= "dark", command = lambda: changeColor())
buttonToggel.grid(row = 1, column = 0, padx = 10, pady = 5 )






app.mainloop()