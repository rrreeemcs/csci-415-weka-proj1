# Sameer Ramkissoon - CSCI-415 Data Mining
# convert-to-weka.py

'''
This file handles the conversion of the cleaned CSV file (algerian_forest_fires_clean.csv) to ARFF format.
The newly converted file will then be used with Weka for Data Mining purposes.

Follow the format below:

TITLE: Algerian Forest Fires
Sources: (author names)
Cleaned By: Sameer Ramkissoon

@RELATION algerian_forest_fires

@ATTRIBUTE
@ATTRIBUTE
...

@DATA
...
'''

import csv
import arff

def convert_to_weka():
    arff_dict = {
        'description': 'Algerian forest fire classification data. Taken from two regions of Algeria from 06-2012 to 09-2012.',
        'relation': 'algerian_forest_fires',
        'attributes': [
            ('region', ['Bejaia', 'Sidi-Bel Abbes']),
            ('date', 'STRING'),
            ('day', 'INTEGER'),
            ('month', 'INTEGER'),
            ('year', 'INTEGER'),
            ('temp_c', 'REAL'),
            ('rel_humidity_percent', 'REAL'),
            ('wind_speed_kmh', 'REAL'),
            ('rainfall_mm', 'REAL'),
            ('ffmc', 'REAL'),
            ('dmc', 'REAL'),
            ('dc', 'REAL'),
            ('isi', 'REAL'),
            ('bui', 'REAL'),
            ('fwi', 'REAL'),
            ('classes', ['fire', 'not fire'])
        ],
        'data':[]
    }

    # TODO 1: Reading CSV File
    file_path = 'data/algerian_forest_fires_clean.csv'
    with open(file_path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)
    # TODO 2: Labeling the description, relation name, attributes, and data
    # TODO 3: Dump it as an ARFF file
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    convert_to_weka()
