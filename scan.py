import os
import eyed3
from time import sleep
from pathlib import Path

def main():
    print('satiel')

    #path = '/home/satiel/Music/'
    path = '/media/satiel/LaCie/Backup/Music/'

    files = []
    # r=root, d=directories, f = files

    # count files in directory, used for progress bar
    numFiles = sum([len(f) for r, d, f in os.walk("/media/satiel/LaCie/Backup/Music/")])
    print(numFiles)
    

    for r, d, f in os.walk(path):
        for file in f:
            #if '.mp3' in file:
            if file.endswith('.mp3'):
                try:
                    # os.path = current path you're at 
                    #files.append(os.path.join(r, file))
                    audiofile = eyed3.load(os.path.join(r, file))
                    #print(audiofile.tag.title)
                    files.append(audiofile.tag.artist.lower())
                    

                    
                except AttributeError as error:
                    #output error
                    #print(os.path.join(r, file))
                    print("Attribute error")
                except UnicodeDecodeError as error:
                    #output error
                    #print(os.path.join(r, file))
                    print("UnicodeDecode error")

    #print(files)
    files = list( dict.fromkeys(files) )
    #for f in files:
        #print(f)
    files.sort()
    print(files)

    with open("ArtistList.txt", "w") as artistList:
        for f in files:
            try:
                artistList.write(str(f))
                artistList.write("\n")
            except UnicodeEncodeError as error:
                print("Encoding error")





if __name__ == '__main__':
    main()