import os
import shutil

extensions_list = ['.txt', '.doc', '.docx', '.pdf']
from_dir = 'source_directory'
to_dir = 'destination_directory'

for file_name in os.listdir(from_dir):
    extension = os.path.splitext(file_name)[1]
    
    if extension == '':
        continue  # Jump to the next file if the extension is blank
    
    if extension in extensions_list:
        path1 = os.path.join(from_dir, file_name)
        path2 = os.path.join(to_dir, "Document_Files")
        path3 = os.path.join(path2, file_name)
        
        if os.path.exists(path2):
            print("Moving", file_name)
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Moving", file_name)
            shutil.move(path1, path3)
