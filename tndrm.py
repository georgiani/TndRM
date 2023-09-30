import os
import sys
from pathlib import Path

if len(sys.argv) == 1:
    files = os.listdir(os.getcwd())
elif len(sys.argv) == 2:
    files = os.listdir(Path(sys.argv[1]))
else:
    exit(1)

for f in files:
    response = input("Remove file " + f + " ? (y/n)")
    
    if response == "y":
        os.remove(sys.argv[1] + f)
    else:
        continue

