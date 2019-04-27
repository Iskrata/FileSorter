import glob, os
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
import sys, getopt
import shutil
import argparse
import file_extension_list

####################### START OF TKINTER GUI #########################

def browse_button():
        global folder_path
        filename = filedialog.askdirectory()
        folder_path.set(filename)
        print(filename)


root = Tk()
root.title("Choose path to clean")
folder_path = StringVar()

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Path:").grid(column=2, row=1)
ttk.Label(mainframe, textvariable=folder_path).grid(column=3, row=1)
button2 = Button(text="Browse", command=browse_button)
button2.grid(column=0, row=1)

quit_button = Button(text="CLEAN", fg="red", command=root.destroy)
quit_button.grid(column=2, row=3)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()

####################### END OF TKINTER GUI #########################

files_dir = str(folder_path.get())

if files_dir == '':
        exit
        # NAPRAVI DA SPIRA KODA

extensions = file_extension_list.extensions
extensions_folder_dict = file_extension_list.extensions_folder_dict

files = os.listdir(files_dir)

def check_for_folder_and_create(path_to_the_folder):
        if not os.path.isdir(path_to_the_folder):
                os.mkdir(path_to_the_folder) 

def move_file_and_alert(file_path_before_leave, path_to_existing_folder, f, path_to_destination_folder):
        shutil.move(file_path_before_leave, path_to_existing_folder)
        print('Moved', f, 'in', path_to_destination_folder)        

for file in files:

        # check if the current file is folder
        if os.path.isdir(os.path.join(files_dir, file)) and file not in extensions:
                path_to_destination_folder = os.path.join(files_dir, 'Folders')
                folder_path_before_leave = os.path.join(files_dir, file)

                check_for_folder_and_create(path_to_destination_folder)

                try:
                        move_file_and_alert(folder_path_before_leave, path_to_destination_folder, file, path_to_destination_folder)

                except:
                        
                        for file_in_folder in os.listdir(folder_path_before_leave):

                                path_to_existing_folder = os.path.join(path_to_destination_folder, file)
                                file_path_before_leave = os.path.join(folder_path_before_leave, file_in_folder)

                                try:
                                        move_file_and_alert(file_path_before_leave, path_to_existing_folder, file, path_to_destination_folder)
                                
                                except:
                                        print('Failed to move files from', file_path_before_leave, 'to', path_to_existing_folder, 'beacause already exists')

                                        path_to_duplicated_folder = os.path.join(files_dir, 'Duplicated')
                                        check_for_folder_and_create(path_to_duplicated_folder)

                                        move_file_and_alert(folder_path_before_leave, path_to_duplicated_folder, file, '"Duplicated"')

                                        break
                        

        # check if the current file extension is in the list and sort it
        elif not os.path.isdir(os.path.join(files_dir, file)) and file not in extensions:
                filename, file_extension = os.path.splitext(os.path.join(files_dir, file))
                for type_of_file in extensions:
                        if file_extension in extensions[type_of_file] and file not in extensions:
                                
                                path_to_destination_folder = os.path.join(files_dir, type_of_file)
                                file_path_before_leave = os.path.join(files_dir, file)

                                check_for_folder_and_create(path_to_destination_folder)
                                
                                try:
                                        move_file_and_alert(file_path_before_leave, path_to_destination_folder, file, path_to_destination_folder)

                                except:

                                        path_to_duplicated_folder = os.path.join(files_dir, 'Duplicated')

                                        check_for_folder_and_create(path_to_duplicated_folder)
                                        move_file_and_alert(file_path_before_leave, path_to_duplicated_folder, file, "Duplicated")


# Sort different type of documents
documents_dir = os.path.join(files_dir, 'Documents\\')
documents = os.listdir(documents_dir)

for document in documents:

        document_dir = os.path.join(documents_dir, document)
        filename, file_extension = os.path.splitext(document_dir)
        os.path.sep

        for extension in extensions_folder_dict:

                if file_extension == extension:
                        path_to_destination_folder = os.path.join(documents_dir, extensions_folder_dict[extension])
                        
                        check_for_folder_and_create(path_to_destination_folder)
                        move_file_and_alert(document_dir, path_to_destination_folder, document, path_to_destination_folder)
        
