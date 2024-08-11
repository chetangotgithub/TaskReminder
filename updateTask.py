import customtkinter
from win11toast import toast
from setNotification import setNotification
import threading


def updateTaskScreen (obj,alltaskDetails,viewTask):
    updateScreen = customtkinter.CTk()
    updateScreen.geometry("500x500")

    print(obj)
    print(obj['task'])
    print(obj['taskdesc'])
    print(obj['link'])
    print(obj['hours'])
    print(obj['minutes'])

    updateFrame1 = customtkinter.CTkScrollableFrame(updateScreen, width= 500, height= 500)
    updateFrame1.pack(padx = 20, pady = 20)

    framTask2 = customtkinter.CTkFrame(updateFrame1)
    framTask2.pack(padx=20, pady=20)

    lableTask = customtkinter.CTkLabel(framTask2, text="Task")
    lableTask.grid(column = 0, row = 0, padx = 20, pady = 5)

    InputTask = customtkinter.CTkEntry(framTask2, width= 200, fg_color="#bde6f1" )
    InputTask.insert(0,obj['task'])
    InputTask.configure(state="disabled")
    InputTask.grid(column = 1, row = 0, padx = 20, pady = 5)
    

    lableTaskDesc = customtkinter.CTkLabel(framTask2, text="Task Description")
    lableTaskDesc.grid(column = 0, row = 1, padx = 20, pady = 5)

    InputTaskDesc = customtkinter.CTkEntry(framTask2, width= 200)
    InputTaskDesc.insert(0,obj['taskdesc'])
    InputTaskDesc.grid(column = 1, row = 1, padx = 20, pady = 5)
    

    lableLink = customtkinter.CTkLabel(framTask2, text="link")
    lableLink.grid(column = 0, row = 2, padx = 20, pady = 5)

    InputLink = customtkinter.CTkEntry(framTask2, width= 200)
    InputLink.insert(0,obj['link'])
    InputLink.grid(column = 1, row = 2, padx = 20, pady = 5)
    

    frameDateTime2 = customtkinter.CTkFrame(updateFrame1)
    frameDateTime2.pack(padx=20, pady=20)

    def validate_numeric_input(action, value_if_allowed, text, validation_type, trigger_type, widget_name):
        if action == '1':  # '1' means insert
            return text.isdigit()    
        return True

    vcmd = (updateScreen.register(validate_numeric_input), '%d', '%P', '%S', '%v', '%V', '%W')

    fontDate = customtkinter.CTkFont("Roboto", 15)
    labelDate = customtkinter.CTkLabel(frameDateTime2, text="Select Hours:", font=fontDate)
    labelDate.grid(row=0, column=0, padx=10, pady=5, sticky="e")
    EntryHours = customtkinter.CTkEntry(frameDateTime2, width=30, validate="key", validatecommand=vcmd)
    EntryHours.insert(0,obj['hours'])
    EntryHours.grid(row=0, column=1, padx=5, pady=5, sticky="w")
    
    labelDate = customtkinter.CTkLabel(frameDateTime2, text="Select Minutes:", font=fontDate)
    labelDate.grid(row=0, column=2, padx=10, pady=5, sticky="e")
    EntryMinutes = customtkinter.CTkEntry(frameDateTime2, width=30, validate="key", validatecommand=vcmd)
    EntryMinutes.insert(0,obj['minutes'])
    EntryMinutes.grid(row=0, column=3, padx=5, pady=5, sticky="w")


    frameButtons = customtkinter.CTkFrame(updateFrame1)
    frameButtons.pack(padx=20, pady=20)

    def submitTask ():
        taskDetails = {}
        taskDetails["task"] = InputTask.get()
        taskDetails["taskdesc"] = InputTaskDesc.get()
        taskDetails["hours"] = EntryHours.get()
        taskDetails["minutes"] = EntryMinutes.get()
        taskDetails["link"] = InputLink.get()
        alltaskDetails[InputTask.get()] = taskDetails
        toast("Updated Task","Updated Task: "+ taskDetails["task"], audio='ms-winsoundevent:Notification.Looping.Alarm')

        other_thread = threading.Thread(target=lambda:setNotification(taskDetails["task"],taskDetails["taskdesc"],taskDetails["link"],taskDetails["hours"] ,taskDetails["minutes"]))
        other_thread.start()

        viewTask()

    buttonSubmit = customtkinter.CTkButton(frameButtons, text = "Update", command=submitTask)
    buttonSubmit.pack(pady = 5, padx = 10)

    updateScreen.mainloop()