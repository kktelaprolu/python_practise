import os
import sys

def main():
    folder_paths= input("enter the folder names: ").split()
    for folder in folder_paths:
        files,error_message = list_folder_files(folder)

        if files:
            for file in files:
                print(file)
        else:
            print(f'{folder} not found: {error_message}')


def list_folder_files(folder):
    try:
        files = os.listdir(folder)
        return files,None
    except FileNotFoundError:
        return None, "folder not found"

if __name__ == "__main__":
    main()