import shutil
import os
import sys
from multiprocessing import Pool

def zipit(path):
    try:
        shutil.make_archive(path, "zip", path)
        shutil.rmtree(path)
    except:
        print("error on", path)

def get_path_list(input_path):
    path_list = []
    for root, dirs, files in os.walk(input_path):
        if not dirs:
            path_list.append(root)
    return path_list
    
if __name__ == '__main__':
    input_path = sys.argv[1]
    path_list = get_path_list(input_path)
    pool = Pool()
    pool.map(zipit, path_list)
