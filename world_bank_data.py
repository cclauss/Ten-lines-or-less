# Download and display zipped csv data from databank.worldbank.org
# See: https://forum.omz-software.com/topic/3413/download-and-unzip-files

import csv, io, requests, zipfile

url = 'http://databank.worldbank.org/data/download/WDI_csv.zip'
filename = 'WDI_Data.csv'

# Warning: this can take two minutes to download!!
with zipfile.ZipFile(io.BytesIO(requests.get(url).content)) as zip_file:
    zip_file.extractall()

# On Python 2, remove: ", newline=''"
with open(filename, newline='') as in_file:
    for row in csv.reader(in_file):
        print(', '.join(row))
