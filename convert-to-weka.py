# Sameer Ramkissoon - CSCI-415 Data Mining
# convert-to-weka.py

'''
This file handles the conversion of the cleaned CSV file (algerian_forest_fires_clean.csv) to ARFF format.
The newly converted file will then be used with Weka for Data Mining purposes.

Follow the format below:
@RELATION algerian_forest_fires

@ATTRIBUTE
@ATTRIBUTE
...

@DATA
...

'''

import arff
import pandas as pd

# Constants (file path to clean csv, output path for the arff file, and the dataframe after reading from clean)
INPUT_PATH = 'data/algerian_forest_fires_clean.csv'
OUTPUT_PATH = 'data/algerian_forest_fires.arff'
DF = pd.read_csv(INPUT_PATH)

def convert_to_weka():
    # Starting message
    print(f"Starting convert_to_weka for algerian_forest_fires.csv...\n")

    # Creating initial dictionary with description, relation name, attributes, and blank data
    # Gets filled in during the next step
    arff_dict = {
        'description': 'Algerian forest fire classification data. Taken from two regions of Algeria from 06-2012 to 09-2012.',
        'relation': 'algerian_forest_fires',
        'attributes': [
            ('region', ['Bejaia', 'Sidi-Bel Abbes']),
            ('date', 'STRING'),
            ('day', 'STRING'),
            ('month', 'STRING'),
            ('year', 'STRING'),
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

    # Reading DF values with values.tolist()
    algerian_ff_data = DF.values.tolist()
    # Length of arff_dict['data'] before input
    print(f"Length of ARFF Data: {len(arff_dict['data'])}")

    # Loading DF data into arff_dict['data']
    try:
        arff_dict['data'] = algerian_ff_data

        # Outputting when region is finished - starts with Bejaia
        region_counter = 'Bejaia'
        for row in arff_dict['data']:
            if row[0] != region_counter:
                print(f'{region_counter} Region Finished!')
                region_counter = row[0]
        # Finishes with Sidi-Bel Abbes
        print(f'{region_counter} Region Finished!')

        # Showing length of arff_dict['data'] after input
        print(f"Length of ARFF Data: {len(arff_dict['data'])}\n")
    except Exception as e:
        print(e)

    # Dump arff_dict as an arff file
    try:
        with open(OUTPUT_PATH, 'w') as arf_file:
            arff.dump(arff_dict, arf_file)
            print('Successfully converted to ARFF for Weka data mining.')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    print("Starting to conversion of algerian_forest_fires_clean.csv to algerian_forest_fires.arff...\n")
    convert_to_weka()
