import os

folder = "data"
lists = os.listdir(folder)

for file in lists:
    old_path = os.path.join(folder, file)
    new_name = f'ព្រះត្រៃបិដក - ' + file
    new_path = os.path.join(folder, new_name)

    os.rename(old_path, new_path)
