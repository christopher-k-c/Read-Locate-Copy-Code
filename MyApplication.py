import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import *

class MyApplication:
    def __init__(self, master):
        self.master = master
        master.title("Find My File")
        root.geometry('400x400')
        root.configure(background='#323336')
        
        
        self.upload = Button(master, text="Upload File", command=self.UploadAction)
        self.upload.place(x=20, y=30)

        self.folder = Button(master, text="Select Search Folder", command=self.FolderSelection)
        self.folder.place(x=20, y=60)

        self.save_folder = Button(master, text="Select Output Folder", command=self.Save)
        self.save_folder.place(x=20, y=90)

        self.run_script = Button(master, text="Execute Script", command=self.ExecuteScript)
        self.run_script.place(x=20, y=120)

        self.close_button = Button(master, text="Quit Process", command=master.quit)
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

