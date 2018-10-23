from root_numpy import root2array
import numpy as np
import sys
from socket import gethostname

if "lxplus" not in gethostname() and "nicadd" not in gethostname():
    print "You're running this on your laptop, that's going to be really slow. You brought this on yourself."
    print "Hostname: ", gethostname()

input_file = sys.argv[1]
treename = sys.argv[2]
input_name = input_file.strip('.root')
print "Converting tree %s in file %s to numpy" % (treename, input_file)
try:
    array = root2array(input_file, treename) 
    np.save(input_name, array)
except IOError:
    print "Tree %s does not exist!" % treename
    
    try: 
        from rootpy.io import root_open 
        print "Available items in %s: " % input_file
        infile = root_open(input_file)
        for item in infile:
            print item

    except ImportError:
        print "Cannot import rootpy.io to list TTrees. Try setting up you venv?"
