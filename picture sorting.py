import os
import datetime
import shutil
import pathlib

path = "E:\\Users\\Haimitch\\Bilder\\others\\Muttis Kamera\\Neue\\"
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

faillist = []
x = 0
for dirpath, dirnames, filenames in os.walk(path):
    for f in filenames:
        f_name,f_ext = os.path.splitext(f)
        if f_ext == ".JPG":
            # print("JPG file found")
            try:
                with open(dirpath + "\\" + f, "rb") as picobj:
                    header = str(picobj.read(5000))
                    # pos = header.find("Digital Camera FinePix XP30 Ver1.01") + 39
                    # x = pos + 10
                    # y = header[pos:x]
                    pos = header.find(":")
                    if header[pos-4:pos+6].find("x") == -1:
                        print(header[pos-4:pos+6])
                    # print(y)
                    z = header[pos-4:pos+6].split(":")
                    year = str(z[0])
                    # print(year)
                    month = str(z[1])
                    #  day = str(z[2])
                    date = year + "\\" + mon[month] + "\\" # + day
                    # print(date)
                    source = dirpath + "\\" + f
                    destinationfolder = "E:\\sorted pictures\\" + date + "\\"
                    destination = "E:\\sorted pictures\\" + date + "\\" + f
                    # print(source)
                    # print(destination)
                    # print(os.path.isdir(destinationfolder))
                    if os.path.isdir(destinationfolder) == True:
                        # print("move it")
                        shutil.move(source, destination)
                    else:
                        # print("make dirs and move it")
                        os.makedirs(destinationfolder)
                        shutil.move(source, destination)
            except:
                x = x + 1
print(x)