# Here is the demo example of the usage of the package.

# First we unzip the .zip and .tar.gz files in zipped_data to the data folder.

import os

for file in os.listdir('zipped_data'):
    if file.endswith('.zip'):
        os.system('unzip zipped_data/' + file + ' -d data')
    elif file.endswith('.tar.gz'):
        os.system('tar -xzf zipped_data/' + file + ' -C data')



