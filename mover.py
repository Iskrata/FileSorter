import glob, os
import sys, getopt
import shutil
import argparse
import file_extension_list

# files_dir = str(input('Type the path to sort: \n'))
files_dir = r'D:\Downloads'
if not files_dir.endswith('\\'):
        files_dir += '\\'

extensions = file_extension_list.extensions
extensions_folder_dict = file_extension_list.extensions_folder_dict

files = os.listdir(files_dir)

def check_for_folder_and_create(path_to_the_folder):
        if not os.path.isdir(path_to_the_folder):
                os.mkdir(path_to_the_folder)

for f in files:

        # check if the current file is folder
        if os.path.isdir(os.path.join(files_dir, f)) and f not in extensions:
                path_to_destination_folder = os.path.join(files_dir, 'Folders')
                file_path_before_leave = os.path.join(files_dir, f)

                check_for_folder_and_create(path_to_destination_folder)

                shutil.move(file_path_before_leave, path_to_destination_folder)

                print('Moved', f, 'in', path_to_destination_folder)

        filename, file_extension = os.path.splitext(os.path.join(files_dir, f))
        for type_of_file in extensions:
                if file_extension in extensions[type_of_file] and f not in extensions:
                        
                        path_to_destination_folder = os.path.join(files_dir, type_of_file)
                        file_path_before_leave = os.path.join(files_dir, f)

                        check_for_folder_and_create(path_to_destination_folder)

                        shutil.move(file_path_before_leave, path_to_destination_folder)

                        print('Moved', f, 'in', path_to_destination_folder)


documents_dir = os.path.join(files_dir, 'Documents\\')
documents = os.listdir(documents_dir)


for document in documents:

        document_dir = documents_dir + document
        filename, file_extension = os.path.splitext(document_dir)
        os.path.sep

        for extension in extensions_folder_dict:

                if file_extension == extension:
                        path_to_destination_folder = os.path.join(documents_dir, extensions_folder_dict[extension])
                        print('Moved', document, 'in', path_to_destination_folder)
                        check_for_folder_and_create(path_to_destination_folder)

                        shutil.move(document_dir, path_to_destination_folder)
        

# TODO: optimizirai da ne chekva za vseki edin ekstenshun faila
# TODO: da mu davash argument
