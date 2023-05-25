import os

import basic

path = 'C:\\Users\\MSI\\OneDrive - Royal University of Phnom Penh\\e-library of cambodia\\Backup\\0Scan'
files = basic.browse_files(path)

for f in files:
    if '..tif' not in f:
        try:
            os.remove(f)
        except:
            print(f)