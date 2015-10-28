import re
import os

def phFiles(filename,hd):
    readFile = open("dbFile"+'/'+filename)
    lines = readFile.readlines()
    id = 1
    for eachline in lines:
        splitedString = re.split('\s+',eachline.strip('\n'))
        temp = len(splitedString)-2
        if(temp % 3 == 0):
            index =0
            while(index < temp):
                val = (id,filename,int(splitedString[0]),int(splitedString[index+1]),int(splitedString[index+2]),int(splitedString[index+3]))
                insert_cmd = "INSERT INTO "+filename+" VALUES (%d,'%s',%d,%d,%d,%d)"
                hd.execute(insert_cmd % val)
                id +=1
                index += 3
                hd.commit()
    readFile.close()
    return 0
	
def readDir(hd):
    files = os.listdir("dbFile")
    for file in files:
        print file
        create_cmd = "CREATE TABLE "+file+"(id serial PRIMARY KEY,sourceName char(20),phashValue int,position int,candidate int,frequency bigint)"
        hd.execute(create_cmd)
        hd.commit()
        phFiles(file,hd)
    return 0
            
