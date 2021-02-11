import os
# print(os.getcwd())
# os.mkdir("floder1")
# os.makedirs("outer1/inside/inside2")
# open("file1.txt",'a').close()

# print(os.path.isfile('file1.txt'))
# print(os.path.exists('file1.txt'))

# os.rename("file1.txt","darshan.txt")

# os.chdir(r"E:\ml\New folder\os_modul\floder1")
# print(os.getcwd())

# print(os.listdir())
# for item in os.listdir():
#     print(item)

# for item in os.listdir(r"E:\ml"):
#     var=os.path.join(r"E:\ml",item)
#     print(var)

# print(os.walk(r"E:\ml"))

# depth_serch=os.walk(r"E:\ml")
# for current_path,folder_name,filename in depth_serch:
#     print(f"current path  {current_path}")
#     print(f"foldername {folder_name}")
#     print(f"filename {filename}")

# os.rmdir("floder1")
# os.removedirs("outer")

import shutil
shutil.rmtree("outer")