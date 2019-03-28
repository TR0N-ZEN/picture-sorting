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

for dirpath, dirnames, filenames in os.walk(mpath):
    for f in filenames:
        source = os.path.join(dirpath,f)
        f_name,f_ext = os.path.splitext(f)
        if f_ext == ".JPG":
            # print("JPG file found")
            with open(source,"rb") as picobj:
                header = str(picobj.read(5000))
                # pos = header.find("Digital Camera FinePix XP30 Ver1.01") + 39
                # x = pos + 10
                # y = header[pos:x]
            pos = header.find(":")
            # print(y)
            if header[pos-4:pos+6].find("x") != -1:
                pos = header.find(":",header[pos-4:pos+6].find("x"))
                if header[pos-4:pos+6].find("x") != -1:
                    print(header[pos-4:pos+6])
            else:
                z = header[pos-4:pos+6].split(":")
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