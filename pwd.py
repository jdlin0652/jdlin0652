# -*- coding : utf-8 -*-
import os

#  pwd：print working directory  輸出當前工作目錄的完整路徑   
pwd = os.getcwd()

# 取得上一層目錄 os.path.pardir or  ".."
path = os.path.abspath(os.path.join(pwd, "..")) # 上層目錄
print (path)

# iterate over files in that directory
filespathlist =[]

for filename in os.listdir(pwd):
    if filename.endswith(".py"):
        filespath = os.path.join(pwd, filename)
        # checking if it is a file
        if os.path.isfile(filespath):
            filespathlist.append(filespath)
print(filespathlist)
