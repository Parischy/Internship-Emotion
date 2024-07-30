import os


def rename_files_in_folder(folder_path, prefix):
    """
    Renames all files in the specified folder that end with .jpeg
    by adding the provided prefix and incrementing the number.

    Args:
        folder_path (str): Path to the folder containing the files
        prefix (str): Prefix to add to each file name

    Returns:
        None
    """
    i = 0
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpeg"):
            new_filename = f"{prefix}{i}.jpeg"
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
            i += 1


folder_paths = [
    "image/child",
    "image/teen",
    "image/adults"
]

prefix = "new_name_"

for folder_path in folder_paths:
    print(f"Renaming files in {folder_path}...")
    rename_files_in_folder(folder_path, prefix)
    print(f"Done renaming files in {folder_path}.\n")
