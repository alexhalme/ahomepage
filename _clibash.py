# Only file that needs to be put in (and not updated, unless this below code needs to be changed) a dir to have
#   access to my local repos, then can load all local repos
import os
import sys

assert 'CLIBASH_PATH' in os.environ

for clibash_subdir in list(filter(lambda x:  not x[0] in ['_','.'] and os.path.isdir(os.path.join(os.environ['CLIBASH_PATH'], x)), os.listdir(os.environ['CLIBASH_PATH']))):
  sys.path.insert(0, os.path.join(os.environ['CLIBASH_PATH'], clibash_subdir))