import os

def move_files(source, destination, file):
    new_source = os.path.join(source, file)
    new_destination = os.path.join(destination, file)
    os.rename(source, destination)