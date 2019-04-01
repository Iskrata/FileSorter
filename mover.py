import glob, os
import shutil
import argparse
import file_extension_list

# files_dir = str(input('Type the path to sort: \n'))
files_dir = r'C:\Users\iskre\Downloads'
if not files_dir.endswith('\\'):
        files_dir += '\\'

extensions = file_extension_list.extensions

files = os.listdir(files_dir)

def check_for_folder_and_create(path_to_the_folder):
        if not os.path.isdir(path_to_the_folder):
                os.mkdir(path_to_the_folder)

for f in files:
        # print(f)

        filename, file_extension = os.path.splitext(os.path.join(files_dir, f))
        for type_of_file in extensions:
                if file_extension in extensions[type_of_file]:
                        
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

        # EXCEL
        if file_extension == '.xlsx' or file_extension == '.xls':
                path_to_destination_folder = os.path.join(documents_dir, 'Excel')
                print('Moved', document, 'in', path_to_destination_folder)
                check_for_folder_and_create(path_to_destination_folder)

                shutil.move(document_dir, path_to_destination_folder)
        
        # WORD
        elif file_extension == '.docx' or file_extension == '.doc':
                path_to_destination_folder = os.path.join(documents_dir, 'Word')
                print('Moved', document, 'in', path_to_destination_folder)
                check_for_folder_and_create(path_to_destination_folder)

                shutil.move(document_dir, path_to_destination_folder)

        # PDF
        elif file_extension == '.pdf' or file_extension == '.PDF':
                path_to_destination_folder = os.path.join(documents_dir, 'Pdf')
                print('Moved', document, 'in', path_to_destination_folder)
                check_for_folder_and_create(path_to_destination_folder)

                shutil.move(document_dir, path_to_destination_folder)

        # TXT
        elif file_extension == '.txt':
                path_to_destination_folder = os.path.join(documents_dir, 'Txt')
                print('Moved', document, 'in', path_to_destination_folder)
                check_for_folder_and_create(path_to_destination_folder)

                shutil.move(document_dir, path_to_destination_folder)

        # POWERPOINT
        elif file_extension == '.ppt':
                path_to_destination_folder = os.path.join(documents_dir, 'PowerPoint')
                print('Moved', document, 'in', path_to_destination_folder)
                check_for_folder_and_create(path_to_destination_folder)

                shutil.move(document_dir, path_to_destination_folder)









                        

                                



# TODO: da gi razpredelq sushto spored extension-a samo za dokumenti
# TODO: da mu davash argument
# TODO: more friendly print
