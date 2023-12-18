import psutil #pass test
import time #pass test
from plyer import notification #pass test
import os
import pygame
app_list = [ ]
user_time = int("60")
user_input_path = ""
#add one on top: 
#1. when they run the program, it will ask do you have any programs you want to add Y -> setting_up() N -> run program? N -> close Y -> start detector detects true -> start clock
def main():
    while True:
        start_choice = input("Do you have any programs to add? (Y/N): ")
        if start_choice == 'Y':
            setting_up_programs()
        elif start_choice == 'N':
            prompt_tostart()
        else:
            print("Enter a valid input.")

def setting_up_programs(): #works
    while True:
        add_programs = input("Programs to be added to watchlist (KEY 'D' when done): ")
        if add_programs.endswith(".exe"):
            app_list.append(add_programs)
            print(app_list)
        elif add_programs == "D":
            print(app_list)
            choose_song()
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
        user_input_path = input("Enter a file path: ")

        # Check if the input is a valid file path
        if is_valid_file_path(user_input_path):
            print(f"{user_input_path} is a valid file path.")
            prompt_tostart()
            return False
        else:
            print(f"{user_input_path} is not a valid file path.")
            return True
        
def prompt_tostart(): #prompts whether they want to start the program (MAIN PAGE)
    while True:
        start = input("Are you ready to run the program? (Y/N): ")
        if start == "Y":
            user_time = input('How long before each bell rings? (give your number in seconds): ')
            if isinstance(user_time, int):
                print("Valid number.")
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
for app_name in app_list:
    if is_process_running(app_name):
        print(f"{app_name} is running.")

    else:
        print(f"{app_name} is not running.")

def stop_timer():
    # Stop the sound and reset the timer
    pygame.mixer.music.stop()

def start_timer():
    start_time = time.time()

    while True:
        elapsed_time = time.time() - start_time

        if elapsed_time >= user_time:  # 1 hour
            play_sound()
            send_notification()

        time.sleep(1 * 60) 

def send_notification():
    # Send a desktop notification
    notification.notify(
        title='Game Time Reminder',
        message='You have been gaming for 1 hour. Take a break!',
    )

def play_sound():
    # Play a sound
    pygame.mixer.music.load(user_input_path)
    pygame.mixer.music.play()
    
if __name__ == "__main__":
    main()
