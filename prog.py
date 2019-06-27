import string
from time import sleep
from progressbar import progressbar
import os, os.path
from tqdm import tqdm

#for i in progressbar(range(100)):
    #sleep(0.10)

# simple version for working with CWD   
# print sum([len(files) for r, d, files in os.walk("/media/satiel/LaCie/Backup/Music/")])
progress_bar = tqdm(list(string.ascii_lowercase))
for letter in progress_bar:
    progress_bar.set_description(f'Processing {letter}...')
    sleep(0.09)
