import shutil
def backup_file(source_file, destination_folder):
      try:
         shutil.copy2(source_file,destination_folder)
         print("File backup successfull")
      except FileNotFoundError:
         print("Source file not found")
      except IsADirectoryError:
          print("Destination folder is not valid")
      except IsADirectoryError:
          print("Directory folder is not valid")
      except Exception as e:
          print("An error occured", str(e))
source_file = input("Enter the path of the file to backup:")
destination_folder = input("Enter the path of destination folder")
backup_file(source_file, destination_folder)
