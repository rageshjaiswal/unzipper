import os
import zipfile
count = 0
zip_file_count = 0

moth_dir = input("Enter the mother directory where unzipped files are present :\n")     #Enter the mother directory
moth_dir_list = os.listdir(moth_dir)
output_dir = input("Enter the output directory :\n")           #Enter the directory where output is to be saved.
file_count = len(moth_dir_list)
for a in moth_dir_list:
    if a.endswith('.zip'):                            #Checking file if it is a zip file or not
        zip_file_count = zip_file_count + 1




print("There are total of {0} files in the given folder, of which {1} are zip files".format(file_count,zip_file_count))
for a in moth_dir_list:
    if a.endswith('.zip'):
        zip_path = moth_dir + "\\" + a
        count = count + 1
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:  #unzipping started.
            #zip_ref.printdir()
            print("Extracting {0} of {1} files".format(count,zip_file_count))
            zip_ref.extractall(output_dir)
print("Done...All files successfully unzipped!!!")

path=os.path.realpath(output_dir)
os.startfile(path)
