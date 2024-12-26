import tkinter as tk
from tkinter import Text, Menu, messagebox, filedialog
import os

# Global variables
file = None

# Function to create widgets
def createWidgets():
    global textArea

    # Text area
    textArea = Text(root, wrap='word')
    textArea.grid(sticky="nsew")

    # Scrollbar
    scrollbar = tk.Scrollbar(textArea)
    scrollbar.pack(side='right', fill='y')
    textArea.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=textArea.yview)

    # Menu Bar
    menuBar = Menu(root)
    root.config(menu=menuBar)

    # File Menu
    fileMenu = Menu(menuBar, tearoff=0)
    fileMenu.add_command(label="New", command=newFile)
    fileMenu.add_command(label="Open", command=openFile)
    fileMenu.add_command(label="Save", command=saveFile)
    fileMenu.add_command(label="Save As", command=saveFileAs)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=exitApp)
    menuBar.add_cascade(label="File", menu=fileMenu)

    # Edit Menu
    editMenu = Menu(menuBar, tearoff=0)
    editMenu.add_command(label="Cut", command=cut)
    editMenu.add_command(label="Copy", command=copy)
    editMenu.add_command(label="Paste", command=paste)
    menuBar.add_cascade(label="Edit", menu=editMenu)

    # Help Menu
    helpMenu = Menu(menuBar, tearoff=0)
    helpMenu.add_command(label="About Notepad", command=showAbout)
    menuBar.add_cascade(label="Help", menu=helpMenu)

    # Grid configuration for resizing
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)


# Function to create a new file
def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    textArea.delete(1.0, tk.END)


# Function to open an existing file
def openFile():
    global file
    file = filedialog.askopenfilename(defaultextension=".txt",
                                      filetypes=[("Text Documents", ".txt"), ("All Files", ".*")])
    if file:
        root.title(os.path.basename(file) + " - Notepad")
        textArea.delete(1.0, tk.END)
        with open(file, "r") as f:
            textArea.insert(1.0, f.read())


# Function to save the current file
def saveFile():
    global file
    if file:
        with open(file, "w") as f:
            f.write(textArea.get(1.0, tk.END))
    else:
        saveFileAs()


# Function to save the file with a new name
def saveFileAs():
    global file
    file = filedialog.asksaveasfilename(defaultextension=".txt",
                                        filetypes=[("Text Documents", ".txt"), ("All Files", ".*")])
    if file:
        with open(file, "w") as f:
            f.write(textArea.get(1.0, tk.END))
        root.title(os.path.basename(file) + " - Notepad")


# Function to exit the application
def exitApp():
    root.destroy()


# Functions for Edit Menu
def cut():
    textArea.event_generate("<<Cut>>")


def copy():
    textArea.event_generate("<<Copy>>")


def paste():
    textArea.event_generate("<<Paste>>")


# Function for Help Menu
def showAbout():
    messagebox.showinfo("About Notepad", "This Simple Notepad is developed by a Software Engineering Student!")


# Main application window
root = tk.Tk()
root.title("Untitled - Notepad")
root.geometry("800x600")

createWidgets()
root.mainloop()