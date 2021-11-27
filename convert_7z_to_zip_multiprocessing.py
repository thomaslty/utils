import shutil
import os
import sys
import patoolib
from multiprocessing import Pool
from rarfile import RarFile

def conversion(path):
    try:
        path_noext = path.rsplit(".", 1)[0]
        ext = path.rsplit(".", 1)[1]
        if (ext == "rar"):
            RarFile(path).extractall(path=path_noext)
        else:
            patoolib.extract_archive(path, outdir=path_noext)
        os.remove(path)
        shutil.make_archive(path_noext, "zip", path_noext)
        shutil.rmtree(path_noext)
    except Exception as e:
      print("error", e)

def get_path_list(input_path):
    path_list = []
    for root, dirs, files in os.walk(input_path):
      for file in files:
          path = os.path.join(root, file)
          filename, ext = os.path.splitext(path)
          if (ext == ".7z" or ext == ".rar"):
            path_list.append(path)
    return path_list
        
if __name__ == '__main__':
    input_path = sys.argv[1]
    path_list = get_path_list(input_path)
    pool = Pool()
    pool.map(conversion, path_list)
