import sys,os
from os import path
import shutil
import subprocess
from subprocess import Popen

#this is the main folder that contains the GRL reports
root = r"C:\"
#this is the destination file where the user saves the csv files
dst = r"C:\Users\"
bat_file= "merged_csv.bat"
script_path= r"C:\Projects\Code Excercises\Code-Excercises\collate_spreadsheet\merged_csv.bat"


for folders, subfolders, filenames in os.walk(root):
                          
          for filename in filenames:
                print filename

                if filename.endswith("_Summary.csv"):
                    shutil.copy(os.path.join(folders, filename), dst)
                    cwd = os.getcwd()
                    print os.path.join(folders, filename)
                    

                    # Separate base from extension
                    base, extension = os.path.splitext(filename)
                    #print (base, extension)

                    # Initial new name
                    new_name = os.path.join(dst,filename)
                    old_name = os.path.join(folders, filename)
                    #print(old_name," and", new_name)

                    if not os.path.exists(new_name):
                        #print("in the loop")
                        ii = 1


                        
                        while True:
                                new_name = os.path.join(dst,base+ "_" + str(ii) + extension)
                                #print(new_name)
                                if not os.path.exists(new_name):
                                   shutil.copy(old_name, new_name)
                                   #print "Copied", old_name, "as", new_name
                                   break 
                                ii += 1
           

       

#call the batch file that merges all the csv files together into a single
shutil.copy((os.path.join(script_path, bat_file)), (os.path.join(dst, bat_file)))
             
filepath = (os.path.join(dst, bat_file))#
print filepath

p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)

stdout, stderr = p.communicate()

