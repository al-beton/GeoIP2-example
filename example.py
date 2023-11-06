# Here is the demo example of the usage of the package.

import os

# First we unzip the .zip and .tar.gz files in zipped_data to the data folder.

zipped_data_folder = 'zipped_data'

for file in os.listdir('zipped_data'):
    print(f'Handling {file}...')
    if file.endswith('.zip'):
        os.system(f'unzip -n {zipped_data_folder}/{file} -d data')
    elif file.endswith('.tar.gz'):
        os.system(f'tar -k -xzf {zipped_data_folder}/{file} -C data')



