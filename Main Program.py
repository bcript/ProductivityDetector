#  <Main Program>

import tkinter
import tkinter.messagebox
import customtkinter as ctk
import packaging
import subprocess
import sys

# Changing the look of the main GUI.
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Way to open the other programs.
def open_pro(file):
    subprocess.run(['python', file])

# Main GUI.
class MainMenu(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Productivity Helper")
        self.geometry(f"{1100}x{580}")
        self.columnconfigure((0,1), weight=2)
        self.rowconfigure((0,1,2,3), weight= 2)

        self.heading = ctk.CTkLabel(master=self, text_color=("gray10", "#DCE4EE"), text= "Welcome to productivity helper 1.0.", font=ctk.CTkFont(size=20, weight="bold"))
        self.heading.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

        self.add_pro = ctk.CTkButton(master=self, text= "Add Programs", fg_color='#0033cc', border_width=3, text_color='white',
                                    width=400, height=105, corner_radius=50, command=lambda: open_pro('SetUp.py'))
        self.add_music = ctk.CTkButton(master=self, text= "Change Music", fg_color='#0033cc', border_width=3, text_color='white', 
                                    width=400, height=105, corner_radius=50, command=lambda: open_pro('MusicSetUp.py'))
        self.run_pro = ctk.CTkButton(master=self, text= "Run helper", fg_color='#0033cc', border_width=3, text_color='white',
                                    width=400, height=105, corner_radius=50, command=lambda: open_pro('RunPro.py'))
        self.exit = ctk.CTkButton(master=self, text= "Exit", fg_color='#0033cc', border_width=3, text_color='white', 
                                    width=400, height=105, corner_radius=50)

        self.add_pro.grid(row= 1, column=0, columnspan=1, padx=20, pady=10)
        self.add_music.grid(row= 1, column=1, columnspan=1, padx=20, pady=10)
        self.run_pro.grid(row= 2, column=0, columnspan=1, padx=20, pady=10)
        self.exit.grid(row= 2, column=1, columnspan=1, padx=20, pady=10)








# Running the program
if __name__ == "__main__":
    app = MainMenu()
    app.mainloop()
