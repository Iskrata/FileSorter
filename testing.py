import glob, os
import shutil
import argparse

files_dir = './'

extensions = {
'Documents': ['.xls', '.xlsx', '.docx', '.txt', '.pdf'],
'Images': ['.jpg', '.jpeg', '.png', '.xcf'],
'Music': ['.mp3'],
'Videos': ['.mp4'],
'Books': ['.epub'],
'Setups': ['.exe', '.jar', '.osz', '.msi']
}

for dict_ in extensions:
    print(dict_)
    print(extensions[dict_])

def dsads():
    Documents = ['.xls', '.xlsx', '.docx', '.txt', '.pdf']
    Images = ['.jpg', '.jpeg', '.png', '.xcf']
    Music = ['.mp3']
    Videos = ['.mp4']
    Books = ['.epub']
    Setups = ['.exe', '.jar', '.osz', '.msi']


    """
    ap = argparse.ArgumentParser()

    ap.add_argument("-i", "--ext", required=True,
        help="path to the input image")
    args = vars(ap.parse_args())
    print(args['ext'])
    """

    files = os.listdir(files_dir)

    for f in files:
            print(f)
            filename, file_extension = os.path.splitext(files_dir+f)
            if file_extension in Images:
                    print('I found it with ext', file_extension)




    # TODO: da gi razpredelq sushto spored extension-a BEZ SNIMKITE xd
