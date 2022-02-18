from tkinter import Tk, Text, Menu, Scrollbar, BOTH, RIGHT, END, Y
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename
import os


class NotePad(Tk):
    def __init__(self):
        super().__init__()
        self.title("Untitled - Notepad")
        self.wm_iconbitmap("assets/favicon.ico")
        self.geometry("400x600")
        self.file = None
        self.__text_area__()
        self.__init_menu__()
        self.__init_scrollbar__()
        self.mainloop()

    # Add self.text_area
    def __text_area__(self):
        self.text_area = Text(self, font="lucida 13")
        self.text_area.pack(expand=True, fill=BOTH)

    # Lets create a menu_bar
    def __init_menu__(self):
        self.menu_bar = Menu(self)
        self.__init_file_menu__()
        self.__init_edit_menu__()
        self.__init_help_menu__()
        self.config(menu=self.menu_bar)

    # Lets create a file_menu_bar
    def __init_file_menu__(self):
        file_menu = Menu(self.menu_bar, tearoff=0)

        # To open new file
        file_menu.add_command(label="New", command=self.new_file)

        # To Open already existing file
        file_menu.add_command(label="Open", command=self.open_file)

        # To save the current file
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()

        # To exit the current file
        file_menu.add_command(label="Exit", command=self.quit_app)

        self.menu_bar.add_cascade(label="File", menu=file_menu)

    # Lets create an edit_menu_bar
    def __init_edit_menu__(self):
        edit_menu = Menu(self.menu_bar, tearoff=0)

        # To give a feature of cut, copy and paste
        edit_menu.add_command(label="Cut", command=self.cut)
        edit_menu.add_command(label="Copy", command=self.copy)
        edit_menu.add_command(label="Paste", command=self.paste)

        self.menu_bar.add_cascade(label="Edit", menu=edit_menu)

    # Lets create a help_menu_bar
    def __init_help_menu__(self):
        help_menu = Menu(self.menu_bar, tearoff=0)
        help_menu.add_command(label="About Notepad", command=self.about)
        self.menu_bar.add_cascade(label="Help", menu=help_menu)

    # Adding Scrollbar using rules from Tkinter lecture no 22
    def __init_scrollbar__(self):
        scroll = Scrollbar(self.text_area)
        scroll.pack(side=RIGHT, fill=Y)
        scroll.config(command=self.text_area.yview)
        self.text_area.config(yscrollcommand=scroll.set)

    def new_file(self):
        self.title("Untitled - Notepad")
        self.file = None
        self.text_area.delete(1.0, END)

    def open_file(self):
        self.file = askopenfilename(
            defaultextension=".txt",
            filetypes=[("All files", "*.*"), ("Text Documents", "*.txt")],
        )
        if not self.file:
            self.file = None
        else:
            self.title(os.path.basename(self.file) + "- Notepad")
            self.text_area.delete(1.0, END)
            with open(self.file, "r", encoding="UTF-8") as file:
                self.text_area.insert(1.0, file.read())

    def save_file(self):
        if self.file is None:
            self.file = askopenfilename(
                initialfile="Untitled.txt",
                defaultextension=".txt",
                filetypes=[("All files", "*.*"), ("Text Documents", "*.txt")],
            )

            if not self.file:
                self.file = None
            else:
                # Save as a new file
                with open(self.file, "w", encoding="UTF-8") as file:
                    file.write(self.text_area.get(1.0, END))

                self.title(os.path.basename(self.file) + "- Notepad")
                print("File Saved")
        else:
            # Save the file
            with open(self.file, "w", encoding="UTF-8") as file:
                file.write(self.text_area.get(1.0, END))

    def quit_app(self):
        self.destroy()

    def cut(self):
        self.text_area.event_generate("<<Cut>>")

    def copy(self):
        self.text_area.event_generate("<<Copy>>")

    def paste(self):
        self.text_area.event_generate("<<Paste>>")

    def about(self):
        showinfo("Notepad", "Notepad by Baelfire18")


if __name__ == "__main__":
    note_pad = NotePad()
