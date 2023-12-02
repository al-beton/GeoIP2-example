# Here is the demo example of the usage of the package.

import os

# First we unzip the .zip and .tar.gz files in zipped_data to the data folder.

zipped_data_folder = 'zipped_data'

for file in os.listdir('zipped_data'):
    print(f'Handling archive {file}...')
    if file.endswith('.zip'):
        os.system(f'unzip -n {zipped_data_folder}/{file} -d data')
    elif file.endswith('.tar.gz'):
        os.system(f'tar -k -xzf {zipped_data_folder}/{file} -C data')

# For each folder in data, we copy the .mmdb files to the geoip2 folder.

for folder in os.listdir('data'):
    # check it is a folder nota a file
    if not os.path.isdir(f'data/{folder}'):
        continue

    print(f'Handling folder {folder}...')
    for file in os.listdir(f'data/{folder}'):
        print(f'Handling copy {file}...')
        if file.endswith('.mmdb'):
            os.system(f'cp data/{folder}/{file} geoip2')

# Now we want to use the GeoIP2 package to try some stuff out

import geoip2.database

test_ip = '123.123.123.13'

with geoip2.database.Reader('data/GeoLite2-City_20231103/GeoLite2-City.mmdb') as reader:
    response = reader.city(test_ip)
    city = response.city.name

with geoip2.database.Reader('data/GeoLite2-Country_20231103/GeoLite2-Country.mmdb') as reader:
    response = reader.country(test_ip)
    country = response.country.name

with geoip2.database.Reader('data/GeoLite2-ASN_20231103/GeoLite2-ASN.mmdb') as reader:
    response = reader.asn(test_ip)
    asn_name = response.autonomous_system_organization
    asn = response.autonomous_system_number

print(f'Queried IP: {test_ip}')
print(f'{city}, {country}')
print(f'{response.autonomous_system_organization} ({response.autonomous_system_number})')

# If successful, this should print:
# Queried IP: 123.123.123.13
# Beijing, China
# China Unicom Beijing Province Network (4808)
