import os
import datetime
import shutil

path = "C:\\Users\\Emil\\Desktop\\picture sorting\\"
os.chdir(path)
print(os.getcwd())

for dirpath, dirnames, filenames in os.walk(path):
    for e in filenames:
        picture = str(e)
        picobj = open(picture, "rb")
        f = picobj.read(761)
        t = str(f)
        try:
            pos1 = t.find("Digital Camera FinePix XP30")
            # print(pos1)
            x = pos1 + 62
            excerpt = t[pos1:x]
            # print(excerpt)
            y = excerpt.split("\\x00")
            # print(y)
            # print(y[1])
            z = y[1].split(":")
            # print(z)
            year = z[0]
            if os.path.isdir(str(dirpath) + year) == True:
                shutil.move(str(dirpath) + str(e), str(dirpath) + str(year))
            elif os.path.isdir(str(dirpath) + year) == False:    
                os.mkdir(str(dirpath) + year)
                shutil.move(str(dirpath) + str(e), str(dirpath) + str(year))
        except:
            print("failed")

# count = 0
# l = "Digital Camera FinePix XP30 Ver1.01\\x002014:07:31 17:46:30\\x00"
# for e in l:
#     count = count + 1
# print(count)