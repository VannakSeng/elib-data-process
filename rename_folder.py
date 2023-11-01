import os

root = "data"
folders = [folder for folder in os.listdir(root) if not folder.startswith('.')]
folders.remove("output")
print(folders)
for sub_folder in folders:
    path = os.path.join(root, sub_folder)
    folder = [folder for folder in os.listdir(path) if not folder.startswith('.')]
    for change in folder:
        new_name = f"{sub_folder} {change}"
        sub_path = os.path.join(root, sub_folder)
        old_folder_path = os.path.join(sub_path, change)
        new_folder_path = os.path.join(sub_path, new_name)
        os.rename(old_folder_path, new_folder_path)

