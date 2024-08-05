import time
from datetime import datetime
from win11toast import toast
import schedule

def show_toast(title, message,link):
    print(link)
    toast(title, message, audio='ms-winsoundevent:Notification.Looping.Alarm',on_click=link,button = "Dismiss")
    

def schedule_toast(title, message, target_time, link):
    def job():
        show_toast(title, message, link)
    
    schedule_time = target_time.strftime("%H:%M")
    schedule.every().day.at(schedule_time).do(job)

# Example usage
def setNotification (title, message, link, hours, minutes):
    title = title
    message = message
    link = link

    # Set the target time to 5:22 PM
    target_time = datetime.strptime(f"{hours}:{minutes}", "%H:%M")

    # Schedule the toast notification
    schedule_toast(title, message, target_time, link)

    # Keep the script running to check for scheduled tasks
    while True:
        schedule.run_pending()
        time.sleep(1)
