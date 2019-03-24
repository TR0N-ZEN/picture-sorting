import os
import datetime
import shutil
import pathlib

path = "C:\\Users\\Emil\\Desktop\\picture sorting\\"
os.chdir(path)
os.getcwd()

mon = {
    "01" : "Januar",
    "02" : "Februar",
    "03" : "März",
    "04" : "April",
    "05" : "Mai",
    "06" : "Juni",
    "07" : "Juli",
    "08" : "August",
    "09" : "September",
    "10" : "Oktober",
    "11" : "November",
    "12" : "Dezember"
}

for dirpath, dirnames, filenames in os.walk(path):
    for f in filenames:
        if f.find(".JPG") != -1:
            picobj = open(f, "rb")
            header = str(picobj.read(761))
            # print(header)
            pos = header.find("Digital Camera FinePix XP30 Ver1.01") + 39
            # print(pos)
            x = pos + 10
            # print(x)
            y = header[pos:x]
            # print(y)
            z = y.split(":")
            year = str(z[0])
            month = str(z[1])
            day = str(z[2])
            date = year + "\\" + mon[month] + "\\" + day
            # print(date)
            source = str(dirpath) + str(f)
            destinationfolder = "C:\\Users\\Emil\\Desktop\\sorted\\" + date + "\\"
            destination = "C:\\Users\\Emil\\Desktop\\sorted\\" + date + "\\" + f
            # print(source)
            # print(destination)
            if os.path.isdir(destinationfolder) == True:
                shutil.move(source, destination)
            else:
                os.makedirs(destinationfolder)
                shutil.move(source, destination)