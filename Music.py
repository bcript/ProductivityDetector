#   <Set Up Music Window>

import tkinter as tk
import tkinter.messagebox
import customtkinter as ctk
import packaging
import sys
import os
import pygame
from pygame import mixer

# Varible
music_list= []

# Changing the look of the GUI
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Way to enter the list into a text file to end the program
def leave():
    with open('MusicFile.txt', 'w') as file:
    # Convert each list element to a string and write to the file
        for item in music_list:
            file.write(str(item) + '\n')
    sys.exit()


# Check to see if file path is valid
def is_valid_file_path(path):
        return os.path.isfile(path)


# Changing Music
class SetUpList(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Set Up List Of Programs")
        self.geometry(f"{1100}x{580}")
        self.columnconfigure(1, weight=1)
        self.rowconfigure((0,1,2,3), weight= 1)
    
        self.label = ctk.CTkLabel(master=self, text_color=("gray10", "#DCE4EE"), text= "Music To Add", font=ctk.CTkFont(size=20, weight="bold"))
        self.label.grid(row=0, column=1, padx=10, pady=(10,10))

        self.Entry = ctk.CTkEntry(self, placeholder_text="Type in the music file path", width= 400)
        self.Entry.grid(row=1, column=0, columnspan=2, padx=(10,10), pady=(10,10))

        self.Enter = ctk.CTkButton(master=self, text= "Enter", fg_color='transparent', border_width=3, text_color='white', command= self.choose_song)
        self.Enter.grid(row=3, column=1, padx=(10,10), pady=(10,10))

        self.Exit = ctk.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text= "Exit", command = leave)
        self.Exit.grid(row=4, column=3, padx=(10, 10), pady=(10, 10), sticky="nsew")  
        
        self.error = ctk.CTkLabel(master=self, fg_color='transparent', bg_color='transparent', text_color=("gray10", "#DCE4EE"), text= "s", font=ctk.CTkFont(size=20, weight="bold"))
        
        self.listbox = tk.Listbox(self, selectmode=tk.SINGLE, fg='white', bg= '#242424', font=24, width=30)
        self.listbox.grid(row=0, column=2, rowspan=3, columnspan=1, padx=40, pady=20)

    # Check to see if file path is valid.
    def is_valid_file_path(path):
            return os.path.isfile(path)
    
    # Adding music file path to a list.
    def choose_song(self):
        self.error.grid_forget()
        if self.Entry.get() in music_list:
            self.error.configure(text='This music has already been added.')
            self.error.grid(row=2, column=1, padx=10, pady=(20,10))
            self.error.configure(state="normal")
            self.Entry.delete(0,"end")
            # Check if the input is a valid file path
        elif is_valid_file_path(self.Entry.get()):
            self.error.configure(state="disabled")
            music_list.append(self.Entry.get())
            self.Entry.delete(0,"end")
            self.update_listbox()
        else:
            self.error.configure(text='Invalid Music File Path')
            self.error.grid(row=2, column=1, padx=10, pady=(20,10))
            self.error.configure(state="normal")
            self.Entry.delete(0,"end")


    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for item in music_list:
            self.listbox.insert(tk.END, item)


# Starting the program
if __name__ == "__main__":
    app = SetUpList()
    app.mainloop()
