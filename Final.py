import time
import datetime
import pygame

''' This program allows you set up an alarm in military time. First you put in your name, 
Then it will let you enter the hour, minute, and second you want the alarm to go off.
When the program gets to the time you entered it will sound an alarm, and a notification will pop up.
'''


#Funcation that will to print name
def say_name(name):
    print("Your name is:", name)

user_name = input("Enter your name: ")


# Displays the time the user set for the alarm
def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    #The audio file that will play when the alarm goes off
    sound_file = "alarm.mp3"
    #A flag to keep the alarm loop running
    is_running = True

#Loop that constantly checks the current time
    while is_running:
        #Gets the current time and formats it as HH:MM:SS
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        #Prints the current time every second
        print(current_time)

 #Checks if the current time matches the alarm time
        if current_time == alarm_time:
            print("WAKE UP! 😴")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
#Loop while the sound is still playing
            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False

        time.sleep(1)


#This block only runs if the script is executed directly (not imported)
if __name__ == "__main__":
    say_name(user_name)
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)