import os 
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

root=tk.Tk()
root.title("File Organizer")
root.geometry("500x400")


extensions={
    "jpg": "Images",
    "png": "Images",
    "jpeg": "Images",
    "gif": "Images",
    "mp4": "Videos",
    "pdf": "Documents",
    "docx": "Documents",
    "txt": "Documents",
    "mp3": "Music",
    "zip": "Archives",
    "exe": "Programs"
}

folder_path=""

def select_folder():
    global folder_path
    folder_path=filedialog.askdirectory()
    if folder_path:
        label.config(text=f"Selected Folder: {folder_path}")

def organize_files():
    if not folder_path:
        messagebox.showerror("Error", "please select a folder first!")
        return



    for filename in os.listdir(folder_path):
        file_path=os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            extension=os.path.splitext(filename)[1][1:].lower()
            
            if extension in extensions: # pyright: ignore[reportUndefinedVariable]
                folder_name=extensions[extension]
            else:
                folder_name="others"

            subfolder_path=os.path.join(folder_path, folder_name)
            os.makedirs(subfolder_path, exist_ok=True)

            destination_path=os.path.join(subfolder_path, filename)
            shutil.move(file_path, destination_path)

    messagebox.showinfo("Done", "Files organized successfully!")


btn_select=tk.Button(root, text="Select Folder", command=select_folder)
btn_select.pack(pady=20)

btn_organize=tk.Button(root, text="Organize Folder", command=organize_files)
btn_organize.pack(pady=20)

label=tk.Label(root, text="No folder selected")
label.pack(pady=20)

root.mainloop()


              


