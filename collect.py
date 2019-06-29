import os
from pathlib import Path
from time import sleep
from progressbar import progressbar

def main():
    print("hello, Satiel!")
    artists = []

    with open('ArtistList.txt', 'r') as work_data:
        for line in work_data:
            #print(line)
            artists.append(line[:-1])

        print(artists)
            


if __name__ == '__main__':
    main()