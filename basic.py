import os


def browse_files(path: str) -> list[str]:
    files = []
    for (dirs, dir_names, filenames) in os.walk(path):
        for filename in filenames:
            files.append(f'{dirs}/{filename}')
        for dir_name in dir_names:
            sub_files = browse_files(f'{dirs}/{dir_name}')
            files = files + sub_files
    return files


def get_file_extension(file_path) -> str:
    _, file_extension = os.path.splitext(file_path)
    return file_extension


def get_name_file(filename) -> str:
    name = os.path.splitext(os.path.basename(filename))[0]
    return name
