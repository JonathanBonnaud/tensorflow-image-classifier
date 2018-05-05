import csv
import os
from shutil import copy2

if __name__ == "__main__":
    """
    This script is used to organize files into folders corresponding to their label.
    """
    src_dir = 'decor-jpg/'
    tgt_dir = 'decor_images/'
    with open('decor.csv', 'r') as file:
        file = csv.reader(file)
        if not os.path.exists(tgt_dir):
            os.mkdir(tgt_dir)
        next(file, None)  # to ignore header
        for line in file:
            decor_dir = os.path.join(tgt_dir, line[3])  # label name
            decor_file = os.path.join(src_dir, '.'.join([line[6].split('.')[0], 'jpg']))
            if line[5] == 'product':  # To take only product and not pattern
                if not os.path.exists(decor_dir):
                    os.mkdir(decor_dir)
                    copy2(decor_file, decor_dir)
                else:
                    copy2(decor_file, decor_dir)
