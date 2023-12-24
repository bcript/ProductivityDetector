#   <Runnign program and logic behind productivity helper.>

import psutil
import time
import tkinter as tk
import tkinter.messagebox
import customtkinter as ctk
import packaging
import sys
import os
import pygame
from pygame import mixer
from plyer import notification

# Varibles
music_list= []
program_list = []
T_mode = 'Seconds'
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Way to enter the list into a text file to end the program
def leave():
    with open('MusicFile.txt', 'w') as file:
    # Convert each list element to a string and write to the file
        for item in music_list:
            file.write(str(item) + '\n')
    sys.exit()


# Reading The Files
def read_pro_list():
    with open ('Program List.txt', 'r') as file:
        file = file.read().splitlines()
        for item in file:
            program_list.append(item)
    return program_list
def read_mus_list():
    with open ('MusicFile.txt', 'r') as file:
        file = file.read().splitlines()
        for item in file:
            music_list.append(item)
    return music_list


# See Whethers a program is running
def is_process_running(process_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            return True
    return False

# Send a desktop notification
def send_notification():
    notification.notify(
        title='Game Time Reminder',
        message='You have been gaming for 1 hour. Take a break!',
    )

# Play a sound.
def play_sound():
    mixer.init()
    mixer.music.set_volume(0.2)
    mixer.music.load(music_list[0])
    mixer.music.play(-1)

read_pro_list()
read_mus_list()

# Main Menu For Running Program.
class RunPro(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Set Up List Of Programs")
        self.geometry(f"{1100}x{580}")
        self.columnconfigure((1), weight=1)
        self.rowconfigure((0,1,2,3), weight= 1)
    
        self.label = ctk.CTkLabel(master=self, text_color=("gray10", "#DCE4EE"), text= "Run Program", 
                                  font=ctk.CTkFont(size=20, weight="bold"))
        self.label.grid(row=0, column=1, padx=10, pady=(10,10))

        self.Entry = ctk.CTkEntry(self, placeholder_text="How long to run for.", width= 400)
        self.Entry.grid(row=1, column=0, columnspan=2, padx=(10,10), pady=(10,10))
        
        self.Start = ctk.CTkButton(master=self, text= "Start", fg_color='transparent', border_width=3, text_color='white', command= self.Start_Timer)
        self.Start.grid(row=3, column=1, padx=(10,10), pady=(10,10))

        self.Stop = ctk.CTkButton(master=self, text= "Stop Alarm", fg_color='transparent', border_width=3, text_color='white', command= self.Stop_Timer)

        self.error = ctk.CTkLabel(master=self, fg_color='transparent', bg_color='transparent', text_color=("gray10", "#DCE4EE"), text= "The program has already been added.", font=ctk.CTkFont(size=20, weight="bold"))


        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self, values=["Seconds", "Minutes", "Hours"],
                                                                       command= self.Timermode)
        self.appearance_mode_optionemenu.grid(row=1, column=2, padx=20, pady=(10, 10))    

        self.Exit = ctk.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text= "Exit", command = leave)
        self.Exit.grid(row=4, column=3, padx=(10, 10), pady=(10, 10), sticky="nsew")             

    def Timermode(self, unit: str):
        global T_mode
        T_mode = unit

    def Start_Timer(self):
        self.error.grid_forget()
        def running_pro():
            for app_name in program_list:
                if is_process_running(app_name):
                    return True

                else:
                    return False
        if T_mode == 'Seconds':
            Mode = 1
        elif T_mode == 'Minutes':
            Mode = 60
        elif T_mode == 'Hours':
            Mode = 3600
        if running_pro() == True:
            Time = self.Entry.get()
            if Time.isdigit():
                self.Start.grid_forget()
                self.Stop.grid(row=3, column=1, padx=(10,10), pady=(10,10))
                self.Stop.configure(state="normal")
                elasped_time = 0
                running = True
                while running :
                    time.sleep(1)
                    elasped_time += 1
                    print(elasped_time)
                    if elasped_time >= (int(Time) * Mode):  # 1 hour
                        send_notification()
                        self.error.configure(text='Alarm Started.')
                        self.error.grid(row=2, column=1, padx=10, pady=(20,10))
                        self.error.configure(state="normal")
                        self.Entry.delete(0,"end") 
                        play_sound()
                        running = False
            else:
                self.error.configure(text='Please Enter A Whole Number.')
                self.error.grid(row=2, column=1, padx=10, pady=(20,10))
                self.error.configure(state="normal")
                self.Entry.delete(0,"end") 
        elif running_pro() == False:
            self.error.configure(text='Program has not been opened.')
            self.error.grid(row=2, column=1, padx=10, pady=(20,10))
            self.error.configure(state="normal")
            self.Entry.delete(0,"end")  
    def Stop_Timer(self):  
        self.error.grid_forget()
        self.Stop.grid_forget()
        self.Start.configure(state="normal")
        self.Start.grid(row=3, column=1, padx=(10,10), pady=(10,10))
        mixer.music.pause()        
            

if __name__ == "__main__":
    app = RunPro()
    app.mainloop()
