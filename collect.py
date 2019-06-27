import os
from pathlib import Path
from time import sleep
from progressbar import progressbar

def main():
    print("hello, Satiel!")

    #data = open('sample.txt', 'r+')
    #data.close()

    #with open('sample.txt', 'r+') as data:
        # File object is now open
        # Work with the file
        #print(f"This is the file name: {data.name}")
        #line_data = data.readlines()
        #print(line_data)
        

        # File object is now closed

        #entries = os.listdir('env/')

        #for entry in entries:
            #print(entry)

    #with os.scandir('env/') as entries:
        #for entry in entries:
            #print(entry.name)
    entries = Path('env/')
    for entry in entries.iterdir():
        print(entry.name)

    # iteratively collect and print out files in a directory
    basepath = Path('env/bin/')
    files_in_basepath = basepath.iterdir()

    #for i in progressbar(range(100)):
    #sleep(0.02)

    # print out the file names
    #for item in files_in_basepath:
        #if item.is_file():
            #print(item.name)
        
            


if __name__ == '__main__':
    main()