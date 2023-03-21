from utils.date import current_datetime
from utils.files import has_folder, create_folder, delete_all_files, get_folder_files

def log_error(error_type, traceback_msg):
    date = current_datetime(tz='PHT')
    specific_timestamp = date.strftime('%m/%d/%Y, %I:%M %p')
    filename = date.strftime('%m%d%Y')
    logs_directory = 'error_logs'

    # if folder does not exist, create
    if not has_folder(logs_directory):
        create_folder(logs_directory)
    
    # log error
    with open(f'{logs_directory}/{filename}', 'a') as file:
        file.write(f'[{specific_timestamp}]\n')
        file.write(f'Error Type: {error_type}\n')
        file.write(f'{traceback_msg}\n\n')

    return