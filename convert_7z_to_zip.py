import py7zr
import zipfile
import shutil
import os
import sys
import patoolib

input_path = sys.argv[1]

for root, dirs, files in os.walk(input_path):
  for file in files:
    try:
      path = os.path.join(root, file)
      filename, ext = os.path.splitext(path)
      path_noext = path.rsplit(".", 1)[0]

      if (ext == ".7z" or ext == ".rar"):
        patoolib.extract_archive(path, outdir=path_noext)
        os.remove(path)
        shutil.make_archive(path_noext, "zip", path_noext)
        shutil.rmtree(path_noext)
    except:
      print("error on", root)

