import os

# Inputs
desktop_directory = "/Users/peterjmyers/Desktop"
do_not_clean_files_and_folders = ['Documents', 'Temp', 'Inbox', 'Trash', '.DS_Store']

def create_temp_directory_if_not_exists():
    full_directory_to_temp = "{}/Temp".format(desktop_directory)
    if not os.path.exists(full_directory_to_temp):
        os.makedirs(full_directory_to_temp)

def move_files_to_temp():
    documents = os.listdir(desktop_directory)
    for doc in documents:
        if doc not in do_not_clean_files_and_folders:
            os.rename("{}/{}".format(desktop_directory, doc), "{}/Temp/{}".format(desktop_directory, doc))

if __name__ == "__main__":
    create_temp_directory_if_not_exists()
    move_files_to_temp()
    print("Success")
