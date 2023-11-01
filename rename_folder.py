import os

root = "data"
for folder in os.listdir(root):
    if not folder.startswith('.'):
        new_name = f"{root} {folder}"
        old_folder_path = os.path.join(root, folder)
        new_folder_path = os.path.join(root, new_name)
        os.rename(old_folder_path, new_folder_path)

