import os
from string import digits

def rename_files():
    # (1) get file names from a given folder
    file_list = os.listdir("/Users/Austin/Desktop/Python/Prank/prank")
    # generate a list of names under the directory
    # print (file_list)
    saved_path = os.getcwd()
    # (2) for each file, rename filename
    os.chdir("/Users/Austin/Desktop/Python/Prank/prank")
    # change working directory from Prank to prank
    for file_name in file_list:
        s = 'abc123def456ghi789zero0'
        remove_digits = str.maketrans('', '', digits)
        new_name = file_name.translate(remove_digits)
        # remove digits
        os.rename(file_name, new_name)
        print ("changed name from "+file_name+" to "+new_name)
    os.chdir(saved_path)
rename_files()
