import os

path = "E:\\Users\\Haimitch\\Bilder\\others\\Muttis Kamera\\sortiert\\"

with open("E:\\Users\\Haimitch\\Bilder\\others\\Muttis Kamera\\sortiert\\Meine JW\\DSCF0036.JPG", "rb") as f:
    header = str(f.read(5000))
    pos = header.find(":")
    print(header[pos-4:pos+6])

# for filenames in os.scandir(path):
#     for i in filenames:
#         print(i) 