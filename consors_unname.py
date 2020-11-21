import sys
import os
from pathlib import PurePath
from pathlib import PureWindowsPath

if len(sys.argv) == 1: 
    print("No files imported - Please drag and drop your files")

else: 
    print('Number of given files:', len(sys.argv)-1, 'Files')

    for filename in sys.argv[1:]: 
        data = PurePath(filename).name
        splitted = data.split("_")
        filterObj = filter(lambda a: 'dat' in a, splitted)
        strObj = list(filterObj)[0]
        year = strObj[3:7]
        month = strObj[7:9]
        day = strObj[9:11]
        prefix = (year+"-"+month+"-"+day+"_") 
        newfilename= str(PureWindowsPath(filename).parents[0])+"\\"+prefix+data

        print("Old Filename:")
        print(filename)

        print("New Filename:")
        print (newfilename)
        print("---------")
        os.rename(filename, newfilename)


wait = input("Click to exit...")
