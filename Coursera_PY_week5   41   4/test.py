import os

import sys

dir(sys)

#x = os.listdir(path=None)
#os.path.isdir()
#x = os.path.dirname('.')
#print(x)


#path = os.listdir(path="D:\YandexDisk\___Programming\PycharmProjects")
tree = os.walk('D:\YandexDisk\___Programming\PycharmProjects')

#folder = []
#for i in tree:
#    folder.append(i)
#    print(i)
#for i in folder:
#    print()
#    print(i)


#print("Path at terminal when executing this file")
#print(os.getcwd() + "\n")

#print("This file directory only")
#full_path = os.path.realpath(__file__)
#print(os.path.dirname(full_path))