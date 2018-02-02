# Replaces underscores in input text file with $\_$

import os
import sys

with open(sys.argv[1],'r') as in_file:
    text = in_file.read()

text = text.replace("_", "\$_")
with open(sys.argv[2],'w') as out_file:
    out_file.write(text)
