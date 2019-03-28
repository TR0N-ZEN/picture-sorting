import os
import datetime
import shutil
import pathlib

mpath = "E:\\Users\\Haimitch\\Bilder\\others\\Muttis Kamera\\sortiert"
os.chdir(mpath)
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

faillist = []
x = 0
global time

def find_date_deep(pos,header):
    pos = header.find(":", pos)
    if header[pos-4:pos+6].find("x") != -1:
        find_date_deep(pos + 1,header)
    else:
        global time
        time = header[pos-4:pos+6]

def sort(excerpt,f,dirpath):
    z = excerpt.split(":")
    year = str(z[0])
    # print(year)
    month = str(z[1])
    # day = str(z[2])
    date = year + "\\" + mon[month] # + day
    # print(date)
    destinationfolder = "E:\\sorted pictures\\" + date + "\\"
    destination = "E:\\sorted pictures\\" + date + "\\" + f
    # print(source)
    # print(destination)
    # print(os.path.isdir(destinationfolder))
    if os.path.isdir(destinationfolder) == True:
        print("move it")
        shutil.move(source,destination)
        if os.path.isfile(destination) == True:
            print("success final")
        else:
            # print("make dirs and move it")
            os.makedirs(destinationfolder)
            shutil.move(source,destination)
            if os.path.isfile(destination) == True:
                print("success final")

for dirpath, dirnames, filenames in os.walk(mpath):
    for f in filenames:
        source = os.path.join(dirpath,f)
        f_name,f_ext = os.path.splitext(f)
        if f_ext == ".JPG":
            # print("JPG file found")
            with open(source,"rb") as picobj:
                header = str(picobj.read(5000))
            pos = header.find(":")
            if header[pos-4:pos+6].find("x") != -1: # check if header[x:x] returns something thats not the date info
                find_date_deep(pos,header)
                sort(time,f,dirpath)
            else:
                sort(header[pos-4:pos+6],f,dirpath)