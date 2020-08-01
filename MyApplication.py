import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import *


# Lets create a new tab called "exif".

class MyApplication:
    def __init__(self, master):
        self.master = master
        master.title("Find My File")
        root.geometry('400x400')
        root.configure(background='#3E4149')
        
        
        self.upload = Button(master, text="Upload File", highlightbackground='#3E4149', command=self.UploadAction)
        self.upload.place(x=20, y=30)

        self.folder = Button(master, text="Select Search Folder", highlightbackground='#3E4149', command=self.FolderSelection)
        self.folder.place(x=20, y=60)

        self.save_folder = Button(master, text="Select Output Folder", highlightbackground='#3E4149', command=self.Save)
        self.save_folder.place(x=20, y=90)

        self.run_script = Button(master, text="Execute Script", highlightbackground='#3E4149', command=self.ExecuteScript)
        self.run_script.place(x=20, y=120)

        self.close_button = Button(master, text="Quit Process", highlightbackground='#3E4149', command=master.quit)
        self.close_button.place(x=20, y=150)
        

    def UploadAction(self, event=None):
        global filePath
        filePath = filedialog.askopenfilename()
        print('Selected:', filePath)

    def FolderSelection(self, event=None):
        global folderPath
        folderPath = filedialog.askdirectory()
        print('Selected:', folderPath)

    def Save(self, event=None):
        global destination
        destination = filedialog.askdirectory()
        print('Selected:', destination)

    def ExecuteScript(self, event=None):
        filesToFind = []
        with open(filePath, "r") as fh:
            for row in fh:
                filesToFind.append(row.strip())

        for filename in os.listdir(folderPath):
            if filename in filesToFind:
                filename = os.path.join(folderPath, filename)
                shutil.copy(filename, destination)


root = Tk()
my_gui = MyApplication(root)
root.mainloop()

