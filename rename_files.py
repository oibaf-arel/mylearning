import os

def rename_files():
    #(1) get file names from a folder
    #path where images are located: /Users/oibaf/Documents/MyLearning/prank
    files_location = "/Users/oibaf/Documents/MyLearning/prank"
    file_list = os.listdir(files_location)
    print(file_list)
    saved_path = os.getcwd()
    
    #change directory to the directory where the images are located
    os.chdir(files_location)
    #(2) for each file, rename filename
    for file_name in file_list:
        new_file_name = file_name.translate(None,"0123456789")
        os.rename(file_name, new_file_name)
        print "File renamed from " + file_name + " to " + new_file_name

    #change path back to what it was
    os.chdir(saved_path)
rename_files()
