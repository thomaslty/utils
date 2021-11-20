import py7zr
import zipfile
import shutil
import os
import sys


input_path = sys.argv[1]

for root, dirs, files in os.walk(input_path):
  if not dirs:
    try:
      shutil.make_archive(root, "zip", root)
      shutil.rmtree(root)
    except:
      print("error on", root)
    
