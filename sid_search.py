import os
import zipfile
from pathlib import Path
import time

def read_strings(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]

def search_zip_file(zip_file, search_strings):
    matches = {}
    with zipfile.ZipFile(zip_file, 'r') as z:
        for file in z.namelist():
            with z.open(file) as f:
                contents = f.read().decode('utf-8', 'ignore')
                for s in search_strings:
                    if s in contents:
                        matches[s] = zip_file
    return matches

def search_directory(directory, search_strings):
    matches = {}
    newest_zip = None
    newest_mtime = 0

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.zip'):
                path = os.path.join(root, file)
                mtime = os.path.getmtime(path)
                if not newest_zip or mtime > newest_mtime:
                    newest_zip = path
                    newest_mtime = mtime

                zip_matches = search_zip_file(path, search_strings)
                for s, zip_file in zip_matches.items():
                    matches[s] = zip_file

    return matches

def main():
    search_strings = read_strings("sids.txt")
    search_option = input("Enter 'file' to search a single zip file or 'dir' to search a directory: ")

    if search_option.lower() == 'file':
        zip_file = input("Enter the zip file name: ")
        matches = search_zip_file(zip_file, search_strings)
    elif search_option.lower() == 'dir':
        directory = input("Enter the directory path: ")
        matches = search_directory(directory, search_strings)
    else:
        print("Invalid option. Exiting...")
        return

    if not matches:
        print("No matches found.")
    else:
        for s in search_strings:
            if s in matches:
                print(f"'{s}' found in {matches[s]}")
            else:
                print(f"'{s}' not found")

if __name__ == "__main__":
    main()
