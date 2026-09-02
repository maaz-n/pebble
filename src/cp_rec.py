import os
import shutil


def cp_files(static_dir: str, public_dir: str):
    abs_static_path = os.path.abspath(static_dir)
    abs_public_path = os.path.abspath(public_dir)
    if not os.path.exists(abs_static_path):
        print("Static directory not found... Please try again.")
        return

    shutil.rmtree(abs_public_path, ignore_errors=True)

    os.mkdir(abs_public_path)

    static_files = os.listdir(abs_static_path)
    for file_obj in static_files:
        file_path = os.path.join(abs_static_path, file_obj)
        cp_files_rec(file_path, abs_public_path)

    print("--- COPY SUCCESSFULL ---")


def cp_files_rec(file_obj: str, dst: str):
    if not os.path.isfile(file_obj):
        # directory
        dir_name = file_obj.split("/")[-1]
        os.mkdir(os.path.join(dst, dir_name))
        nested_files = os.listdir(file_obj)
        for file in nested_files:
            file_path = os.path.join(file_obj, file)
            cp_files_rec(file_path, os.path.join(dst, dir_name))

    else:
        # normal file
        file_name = file_obj.split("/")[-1]
        print(f"[COPYING FILE]: {file_name}")
        shutil.copy(file_obj, os.path.join(dst, file_name))
