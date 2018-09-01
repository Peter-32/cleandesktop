import os

# Inputs
desktop_directory = "/Users/peterjmyers/Desktop"
do_not_clean_files_and_folders = ['To-do', 'Janitor', 'Code', 'Other', '.DS_Store']

def create_janitor_directory_if_not_exists():
    full_directory_to_janitor = "{}/Janitor".format(desktop_directory)
    if not os.path.exists(full_directory_to_janitor):
        os.makedirs(full_directory_to_janitor)

def move_files_to_janitor():
    documents = os.listdir(desktop_directory)
    for doc in documents:
        if doc not in do_not_clean_files_and_folders:
            os.rename("{}/{}".format(desktop_directory, doc), "{}/Janitor/{}".format(desktop_directory, doc))

if __name__ == "__main__":
    create_janitor_directory_if_not_exists()
    move_files_to_janitor()
    print("Success")
