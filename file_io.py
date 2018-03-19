import os, shutil

def move_files(source, destination, file):
    new_source = os.path.join(source, file)
    new_destination = os.path.join(destination, file)
    os.rename(source, destination)

def copy_file(source, destination, file):
    file_addr = os.path.join(source, file)
    shutil.copy(file_addr, destination)

def delete_file(addr, file):
    os.unlink(os.path.join(addr, file))