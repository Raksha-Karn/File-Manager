import os
import shutil

FS_FOLDER = 'fs'

def init_fs():
    if not os.path.exists(FS_FOLDER):
        os.makedirs(FS_FOLDER)
    print(f"File system initialized at {FS_FOLDER}/")

def create_file():
    file_name = input("Enter the file name (without extension): ").strip()
    if not file_name:
        print("File name cannot be empty.")
        return

    file_extension = input("Enter the file extension (e.g., .txt, .log): ").strip()
    if not file_extension.startswith('.'):
        print("Invalid file extension. It should start with a dot (e.g., .txt).")
        return

    full_file_name = f"{file_name}{file_extension}"

    folder_name = input("Enter the folder name (enter '.' for root directory): ").strip()

    if folder_name == '.' or not folder_name:
        folder_path = FS_FOLDER
    else:
        folder_path = os.path.join(FS_FOLDER, folder_name)
        if not os.path.exists(folder_path):
            create_folder = input(f"Folder '{folder_name}' does not exist. Do you want to create it? (yes/no): ").lower()
            if create_folder == 'yes':
                os.makedirs(folder_path)
                print(f"Folder '{folder_name}' created.")
            elif create_folder == 'no':
                print("File not created.")
                return
            else:
                print("Invalid input. File not created.")
                return

    file_path = os.path.join(folder_path, full_file_name)

    if os.path.exists(file_path):
        overwrite = input(f"File '{full_file_name}' already exists in '{folder_name}'. Do you want to overwrite it? (yes/no): ").lower()
        if overwrite != 'yes':
            print("File not created.")
            return

    add_content = input("Do you want to add content to the file? (yes/no): ").lower()

    if add_content == 'yes':
        content = input("Enter the content: ")
        try:
            with open(file_path, 'w') as file:
                file.write(content)
            print(f"File '{full_file_name}' created with content in '{folder_name}'.")
        except Exception as e:
            print(f"Error writing to file: {e}")
    elif add_content == 'no':
        try:
            with open(file_path, 'w') as file:
                pass
            print(f"Empty file '{full_file_name}' created in '{folder_name}'.")
        except Exception as e:
            print(f"Error creating file: {e}")
    else:
        print("Invalid input. File not created.")

def read_file():
    file_name = input("Enter the file name to read (with extension): ").strip()
    if not file_name:
        print("File name cannot be empty.")
        return

    folder_name = input("Enter the folder name (enter '.' for root directory): ").strip()

    if folder_name == '.' or not folder_name:
        folder_path = FS_FOLDER
    else:
        folder_path = os.path.join(FS_FOLDER, folder_name)
        if not os.path.exists(folder_path):
            print(f"Folder '{folder_name}' does not exist.")
            return

    file_path = os.path.join(folder_path, file_name)

    try:
        with open(file_path, 'r') as file:
            content = file.read()
            if content.strip() == "":
                print(f"File '{file_name}' is empty.")
            else:
                print(f"Contents of '{file_name}' in folder '{folder_name}':\n{content}")
    except FileNotFoundError:
        print(f"File '{file_name}' not found in folder '{folder_name}'.")
    except Exception as e:
        print(f"Error reading file: {e}")

def update_file():
    file_name = input("Enter the file name to update (with extension): ").strip()
    if not file_name:
        print("File name cannot be empty.")
        return

    folder_name = input("Enter the folder name (enter '.' for root directory): ").strip()

    if folder_name == '.' or not folder_name:
        folder_path = FS_FOLDER
    else:
        folder_path = os.path.join(FS_FOLDER, folder_name)
        if not os.path.exists(folder_path):
            print(f"Folder '{folder_name}' does not exist.")
            return

    file_path = os.path.join(folder_path, file_name)

    if os.path.exists(file_path):
        new_content = input("Enter new content for the file: ")
        try:
            with open(file_path, 'w') as file:
                file.write(new_content)
            print(f"File '{file_name}' updated with new content in folder '{folder_name}'.")
        except Exception as e:
            print(f"Error updating file: {e}")
    else:
        print(f"File '{file_name}' does not exist in folder '{folder_name}'.")

def delete_file():
    file_name = input("Enter the file name to delete (with extension): ").strip()
    if not file_name:
        print("File name cannot be empty.")
        return

    folder_name = input("Enter the folder name (enter '.' for root directory): ").strip()

    if folder_name == '.' or not folder_name:
        folder_path = FS_FOLDER
    else:
        folder_path = os.path.join(FS_FOLDER, folder_name)
        if not os.path.exists(folder_path):
            print(f"Folder '{folder_name}' does not exist.")
            return

    file_path = os.path.join(folder_path, file_name)

    try:
        os.remove(file_path)
        print(f"File '{file_name}' deleted from folder '{folder_name}'.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found in folder '{folder_name}'.")
    except Exception as e:
        print(f"Error deleting file: {e}")

def delete_directory():
    folder_name = input("Enter the folder name to delete: ").strip()
    if not folder_name:
        print("Folder name cannot be empty.")
        return

    folder_path = os.path.join(FS_FOLDER, folder_name)

    try:
        shutil.rmtree(folder_path)
        print(f"Folder '{folder_name}' deleted.")
    except FileNotFoundError:
        print(f"Folder '{folder_name}' not found.")
    except Exception as e:
        print(f"Error deleting folder: {e}")

def format_disk():
    try:
        for filename in os.listdir(FS_FOLDER):
            file_path = os.path.join(FS_FOLDER, filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        print("Disk formatted. All contents of the 'fs' folder have been deleted.")
    except Exception as e:
        print(f"Error formatting disk: {e}")

def main():
    init_fs()
    while True:
        print("\n=============================")
        print(" WELCOME TO THE FILE MANAGER 📁")
        print("=============================")
        print("\nID  Task")
        print("1  - Create a file")
        print("2  - Read a file")
        print("3  - Update a file")
        print("4  - Delete a file")
        print("5  - Delete a directory")
        print("6  - Format disk")
        print("7  - Exit")
        
        try:
            task_id = int(input("\nEnter the ID of the task you want to perform: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if task_id == 1:
            create_file()
        elif task_id == 2:
            read_file()
        elif task_id == 3:
            update_file()
        elif task_id == 4:
            delete_file()
        elif task_id == 5:
            delete_directory()
        elif task_id == 6:
            format_disk()
        elif task_id == 7:
            print("Exiting the File Manager.")
            break
        else:
            print("Invalid task ID. Please try again.")

if __name__ == "__main__":
    main()
