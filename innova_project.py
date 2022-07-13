# -*- coding: latin-1 -*-
import os
from fnmatch import fnmatch
import todays_folder as td
import shutil
import pickle

# for extracting the invoice number from the file_name
import re

def pickle_folder():
  '''
  Checks if there s a folder named pickle. If theres not
  it creates one.
  '''
  todays_working_folder = td.get_todays_folder()
  directories = os.listdir(todays_working_folder)
  if "pickle" not in directories:
    os.mkdir(todays_working_folder + '\\' + 'pickle')

# delete all files in capi/innova
#capi_innova = 'c:\\Users\\rd\\Desktop\\capi\\innova\\'
#remove_list = os.listdir(capi_innova)
#if remove_list:
#  for file in remove_list:
#    os.remove(capi_innova + file)

class Innova_xls_files(object):
  def __init__(self):
    self.list_files = list()
    self.todays_working_folder = td.get_todays_folder()

  def add(self, xls_file):
    if xls_file.endswith("xls"):
      self.list_files.append(xls_file)

  def print_file_names(self):
    for file in self.list_files:
      print(file)
      sentence = file
      s = [int(s) for s in re.findall(r'-?\d+\.?\d*', sentence)]
      print("alternative name", s[0])

  def change_file_names(self):
    '''
       Changes a file name type like 
       FACTURA N�100028 ALDI DOS HERMANAS,S.L.  CARRITO COCINA 1200 UDS
       to 100028, so that it makes less mistakes manipulating long names.
       Returns a dictionary with the original name as key and the new name as value
    '''
    name_dict = dict()
    for file in self.list_files:
      #print(file)
      sentence = file
      s = [int(s) for s in re.findall(r'-?\d+\.?\d*', sentence)]
      name_dict[file] = s
    return(name_dict)
      #print("alternative name", s[0])

  def list_all_files_and_folders(self):
    #list all files and folders in todays folder 

    #print("todays folder is", todays_working_folder)
    #print("Full path to folder is", todays_working_folder)
    return(os.listdir(todays_working_folder))

  def innova_work_dir_exists(self):
    ''' 
      Boolean to see if the innova_work_dir exists. Returns True or False
    '''
    files_and_folders = self.list_all_files_and_folders()
    target = 'innova_work_dir'
    if target in files_and_folders:
      return True
    else:
      return False

  def copy_xls_files_to_work_dir(self):
    dest = self.todays_working_folder + '\\' + 'innova_work_dir'
    file_dict = self.change_file_names()
    if not self.innova_work_dir_exists():
      os.mkdir(self.todays_working_folder + '\\' + 'innova_work_dir')
    for file in file_dict:
      #print("source", file)
      #print("destination", dest + "\\" + str(file_dict[file][3]) + ".xls")
      shutil.copy(file, dest + "\\" + str(file_dict[file][3]) + ".xls")

#for k in name_dict:
 # print("provisional_name", k, "file name", name_dict[k])
#print(name_dict)

#save_path = todays_working_folder + "\\" + "saved_dict.pkl"
#with open(save_path, "wb") as f:
 # pickle.dump([name_dict, counter], f) 

#with open(save_path, "rb") as f:
 # loaded_dict = pickle.load(f)
#print(loaded_dict)

if __name__ == '__main__':
  todays_working_folder = td.get_todays_folder()
  root = todays_working_folder
  pattern = "factura*.xls"
  name_dict = dict()
  counter = 0

  excel_files = Innova_xls_files()
  
  for path, subdirs, files in os.walk(root):
      for name in files:
          if fnmatch(name, pattern):
            #print(os.path.join(path, name))
            #counter += 1
            #prov_name = "0" + str(counter)
            #name_dict[prov_name] = name
            #print(name_dict[prov_name])
              excel_files.add(path+"\\"+name)
   
  #excel_files.print_file_names()
  #excel_files.list_all_files_and_folders()
  #excel_files.copy_xls_files_to_work_dir()
  pickle_folder()