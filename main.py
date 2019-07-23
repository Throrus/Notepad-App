import tkinter
from tkinter import messagebox, filedialog
import tkinter.font
import sys

# primary function
def main():

    #window setup
    window = tkinter.Tk()
    window.title("Notebook")
    window.geometry("600x600")
    window.resizable(True, True)

    # default font
    current_font = tkinter.font.Font(family='Helvetica', size=12)

    # text box class
    class Textbox:
        def __init__(self):
            self.window = window
            self.height = 800
            self.width = 600
            self.font = current_font
            self.text = tkinter.Text(window, font=current_font)
            self.save_state = False
            self.filename = ''
            self._filetypes = [
            ('Text', '*.txt'),
                ('All files', '*'),
                ]

        # saving a named file
        def save_file(self):
            if (self.filename == ''):
                self.save_file_as()
            else:
                f = open(self.filename, 'w')
                f.write(self.text.get('1.0', 'end'))
                f.close()

        # saving an unnamed file
        def save_file_as(self):
            self.filename = tkinter.filedialog.asksaveasfilename(defaultextension='.txt',
                                                                 filetypes = self._filetypes)
            f = open(self.filename, 'w')
            f.write(self.text.get('1.0', 'end'))
            f.close()

        # opening a previously saved file
        def open_file(self):
            if self.text.get("1.0",'end-1c') == '': #if current page is empty
                pass
            else:
                question = messagebox.askquestion("Alert", "Save your work?")
                if question == 'yes':
                    if main_text.filename == '':
                        main_text.save_file_as()
                    else:
                        main_text.save_file()
                else:
                    pass
            self.filename = tkinter.filedialog.askopenfilename(filetypes = self._filetypes)
            f = open(self.filename, 'r')
            f2 = f.read()
            self.text.delete('1.0', 'end')
            self.text.insert('1.0', f2)
            f.close()

        # creating a new file
        def new_file(self):
            if self.text.get("1.0",'end-1c') == '': #if current page is empty
                pass
            else:
                question = messagebox.askquestion("Alert", "Save your work?")
                if question == 'yes':
                    if main_text.filename == '':
                        main_text.save_file_as()
                    else:
                        main_text.save_file()
                else:
                    pass
            self.filename = ''
            self.text.delete('1.0', 'end')

    # text body
    main_text = Textbox()
    main_text.text.pack(expand=True, fill='both')

    # menu bar
    root_menu = tkinter.Menu(window)
    window.config(menu = root_menu)

    # function that runs when the window is closed
    def exit_program():
        if main_text.text.get("1.0",'end-1c') == '': #if current page is empty
            pass
        else:
            question = messagebox.askquestion("Alert", "Save before exiting?")
            if question == 'yes':
                if main_text.filename == '':
                    main_text.save_file_as()
                else:
                    main_text.save_file()
            else:
                pass
        window.destroy()

    # file tab
    file_menu = tkinter.Menu(root_menu)
    root_menu.add_cascade(label = "File", menu = file_menu)
    file_menu.add_command(label = "New File", command = main_text.new_file)
    file_menu.add_command(label = "Open File", command = main_text.open_file)
    file_menu.add_command(label = "Save File", command = main_text.save_file)
    file_menu.add_command(label = "Save File As", command = main_text.save_file_as)
    file_menu.add_separator()
    file_menu.add_command(label = "Exit", command = exit_program)

    # more window setup :)
    window.protocol( "WM_DELETE_WINDOW", exit_program)
    window.mainloop()

if __name__=='__main__':
    main()
