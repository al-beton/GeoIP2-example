# django-GeoIP2-example

Example project showing the use of GeoIP2 API and setup of city/country lookup.

### Setup

To get up and running, you will need to get the data from the MaxMinds project. 

See: [MaxMinds](https://dev.maxmind.com/geoip/geolite2-free-geolocation-data)

You should create an API key and download their latest dataset.

In this GitHub repository, the MaxMinds data from 06/11/2023 is included.

### Execution

Ensure that up to date MaxMinds data is placed in the zipped_data folder

Run example.py

A successful run will output the following response to the query of the IP address 123.123.123.123

``` Beijing, China ```

``` China Unicom Beijing Province Network (4808) ``` 



### Dependencies

This uses the unzip and tar CLI tools which you must have installed.
