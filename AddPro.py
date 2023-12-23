#   <Set Up Program Window>

import tkinter as tk
import tkinter.messagebox
import customtkinter as ctk
import packaging
import sys

# Varibles
app_list = []

# Changing the look of the GUI
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Way to enter the list into a text file to end the program
def leave():
    with open('Program List.txt', 'w') as file:
    # Convert each list element to a string and write to the file
        for item in app_list:
            file.write(str(item) + '\n')
    sys.exit()


# Changing list of programs for the porductivity helper
class SetUpList(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Set Up List Of Programs")
        self.geometry(f"{1100}x{580}")
        self.columnconfigure(1, weight=1)
        self.rowconfigure((0,1,2,3), weight= 1)

        self.label = ctk.CTkLabel(master=self, text_color=("gray10", "#DCE4EE"), text= "List Of Programs To Add", font=ctk.CTkFont(size=20, weight="bold"))
        self.label.grid(row=0, column=1, padx=10, pady=(10,10))

        self.Entry = ctk.CTkEntry(self, placeholder_text="Type in the game file in (.exe)", width= 400)
        self.Entry.grid(row=1, column=0, columnspan=2, padx=(10,10), pady=(10,10))

        self.Enter = ctk.CTkButton(master=self, text= "Enter", fg_color='transparent', border_width=3, text_color='white', command= self.add_pro)
        self.Enter.grid(row=3, column=1, padx=(10,10), pady=(10,10))


        self.Exit = ctk.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text= "Exit", command = leave)
        self.Exit.grid(row=4, column=3, padx=(10, 10), pady=(10, 10), sticky="nsew")
        
        self.error = ctk.CTkLabel(master=self, fg_color='transparent', bg_color='transparent', text_color=("gray10", "#DCE4EE"), text= "The program has already been added.", font=ctk.CTkFont(size=20, weight="bold"))

        self.listbox = tk.Listbox(self, selectmode=tk.SINGLE, fg='white', bg= '#242424', font=24, width=30)
        self.listbox.grid(row=0, column=2, rowspan=3, columnspan=1, padx=40, pady=20)
    
    # List Adding
    def add_pro(self):
        self.error.grid_forget()
        if self.Entry.get() in app_list:
            self.error.configure(text='The program has already been added.')
            self.error.grid(row=2, column=1, padx=10, pady=(20,10))
            self.error.configure(state="normal")
            self.Entry.delete(0,"end")
        elif self.Entry.get().endswith('.exe'):
            self.error.configure(state="disabled")
            app_list.append(self.Entry.get())
            self.Entry.delete(0,"end")
            self.update_listbox()
        else:
            self.error.configure(text='Invalid Program')
            self.error.grid(row=2, column=1, padx=10, pady=(20,10))
            self.error.configure(state="normal")
            self.Entry.delete(0,"end")

    
    # Listbox Updating
    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for item in app_list:
            self.listbox.insert(tk.END, item)


# Starting the program
if __name__ == "__main__":
    app = SetUpList()
    app.mainloop()
