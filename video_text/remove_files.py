import os

def rm(path):
  dir = os.listdir(path)
  for file in dir:
    os.remove(path + file)
