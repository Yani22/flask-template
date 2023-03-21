from pdf2image import convert_from_path
from PIL import Image
from pathlib import Path
import openpyxl
# from datetime import datetime
from utils.date import current_datetime
import os


def pdf_to_image(filepath):
    # get pdf and convert to images
    return convert_from_path(filepath, fmt="jpeg")

def export_images(images=[]):
    for index, page in enumerate(images):
        print(f"Exporting page {index + 1}")
        
        #filename = f'page-{str(index+1).zfill(2)}.jpeg'

        # filename format for tesseract training
        filename = f'eng.arial.exp{index}.png'

        # save image
        page.seek(0)
        page.save(filename, 'PNG')

    print("Images Exported Successfully")

    return

# returns the worksheet instance
def read_excel_worksheet(filepath, filename, worksheet):
    file = Path(filepath, filename)
    workbook = openpyxl.load_workbook(file)

    return workbook[worksheet]

# this function will create a folder in logs/[folder name]
def create_logs_folder(folder):
    Path(f'../logs/{folder}').mkdir(parents=True)

    return

# this function will create a folder in the specified path
# will also create parent folders if specified in path (ex. parent folder 1/parent folder 2/main folder)
def create_folder(folder_path):
    Path(f'{folder_path}').mkdir(parents=True)

    return

# this function will write to ../logs/[folder]/[filename].txt
def write_to_log(folder, filename, message):
    # create folder if it does not exist
    if not has_folder(f'../logs/{folder}'):
        create_logs_folder(folder)

    current_date = current_datetime(tz='PHT')

    with open(f'../logs/{folder}/{filename}.txt', 'r+') as file:
        print(file.read())

        file.write(message)

    return

# check if folder exists
def has_folder(folder_path):
    return Path(folder_path).exists()

# list all files in the specified directory
def get_folder_files(folder_path):
    # if folder is not found
    return Path(folder_path).iterdir() if has_folder(folder_path) else []

# if extensions are specified, remove all files with that extension
# if extension is None, remove all files
def delete_all_files(directory, extensions=[]):
    for file in get_folder_files(directory):
        # get file extension
        extension = file.name.split('.')[-1]
        
        # delete file 
        if not extensions or (extension in extensions):
            os.remove(f'{directory}/{file.name}')  

    return

# delete specific files based on filenames
def delete_specific_files(directory, filenames=[]):
    for file in get_folder_files(directory):
        # delete file
        if file.name in filenames:
            print('DELETING FILE')

            os.remove(f'{directory}/{file.name}')

    return
    
# save image to specified directory
def save_image_to(image, directory, filename):
    print(image)
    print(directory)
    print(filename)

    image = Image.open(image)
    image.save(f'{directory}/{filename}.jpg', 'JPEG')
    print(image)

    return