import psutil #pass test
import time #pass test
from plyer import notification #pass test
import os
import pygame
from pygame import mixer
app_list = [ ]
user_time = 0
mode = "second"
#add one on top: 
#1. when they run the program, it will ask do you have any programs you want to add Y -> setting_up() N -> run program? N -> close Y -> start detector detects true -> start clock
def main():
    while True:
        start_choice = input("Do you have any games to add? (Y/N): ")
        if start_choice == 'Y':
            setting_up_programs()
        elif start_choice == 'N':
            prompt_tostart()
            break
        else:
            print("Enter a valid input.")

def setting_up_programs(): #works
    while True:
        add_programs = input("Programs to be added to watchlist (KEY 'D' when done): ")
        if add_programs.endswith(".exe"):
            if add_programs in app_list:
                print("This porgram has already been added pls add a new program.")
            else:
                app_list.append(add_programs)
            print(app_list)
        elif add_programs == "D":
            print(app_list)
            return False
        else:
            print("Error")
#--------------------------------------------------------------------------------------------------------
def is_valid_file_path(path):
    return os.path.isfile(path)

#lets the user choose the song they want to play
def choose_song():
    while True:
        #Get user input for a file path
        global user_input_path
        user_input_path = input("Enter a song file path: ")

        # Check if the input is a valid file path
        if is_valid_file_path(user_input_path):
            print(f"{user_input_path} is a valid file path.")
            return False
        else:
            print(f"{user_input_path} is not a valid file path.")

        
def prompt_tostart(): #prompts whether they want to start the program (MAIN PAGE)
    while True:
        start = input("Are you ready to run the program? (Y/N): ")
        if start == "Y":
            choose_song()
            mode = input("Do you want the timer to be Seconds, Minutes, Hours: ")
            user_time = input(f'How long before each bell rings? (give your number in {mode}): ')
            if user_time.isdigit():
                print("Valid number")
                running_pro()
                print(f"A {user_time} {mode} timer has been started")
                start_timer()
            else:
                break
            #TBD
        elif start == "N":
            print("goodbye")
            break
        else:
            print("goodbye")

#checks if process is running
def is_process_running(process_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            return True
    return False

# List of applications to check

# Check if any of the applications is running
def running_pro():
    for app_name in app_list:
        if is_process_running(app_name):
            print(f"{app_name} is running.")

        else:
            print(f"{app_name} is not running.")

def stop_timer():
    # Stop the sound and reset the timer
    mixer.music.stop()

def start_timer():
    running = True
    elasped_time = 0
    while running :
        time.sleep(1)
        elasped_time += 1
        if elasped_time >= int(user_time):  # 1 hour
            send_notification()
            print("Alarm Started")
            play_sound()
        running = False


def send_notification():
    # Send a desktop notification
    notification.notify(
        title='Game Time Reminder',
        message='You have been gaming for 1 hour. Take a break!',
    )

def play_sound():
    # Play a sound
    mixer.init()
    mixer.music.set_volume(0.2)
    mixer.music.load(user_input_path)
    mixer.music.play(-1)
    # This is loop is to give the ability to stop the timer
    m_running = True
    while m_running:
        m_running = input("Type [S] to Stop the alarm: ")
        if m_running == "S":
            print("Alarm has been stop.")
            mixer.music.pause()
            break

main()
