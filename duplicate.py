import os
import hashlib
import shutil

def find_duplicates(path):
    duplicates = {}
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            with open(file_path, "rb") as f:
                file_hash = hashlib.md5(f.read()).hexdigest()
                if file_hash in duplicates:
                    duplicates[file_hash].append(file_path)
                else:
                    duplicates[file_hash] = [file_path]
    return [duplicates[k] for k in duplicates if len(duplicates[k]) > 1]

def delete_duplicates(duplicates):
    for duplicate_set in duplicates:
        print("The following files are duplicates:")
        for duplicate in duplicate_set:
            print(duplicate)
        print("Do you want to delete all duplicates except the first one? (y/n)")
        response = input().lower()
        if response == "y":
            for duplicate in duplicate_set[1:]:
                os.remove(duplicate)
                print(f"{duplicate} deleted.")
        else:
            print("Duplicates were not deleted.")

duplicates = find_duplicates("Path/To/Folder")
delete_duplicates(duplicates)
