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
import sys

def convert_to_weka(input_path, output_path):
    # Starting message
    print(f"Starting conversion for data/{input_path}...\n")

    try:
        # Read the input file provided via command line
        df = pd.read_csv(f"data/{input_path}")
    except Exception as e:
        print(f"Error reading input file: {e}")
        return

    # Creating initial dictionary with the data provided
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
        'data': []
    }

    # Convert dataframe to list
    algerian_ff_data = df.values.tolist()

    try:
        arff_dict['data'] = algerian_ff_data

        # Region tracking for console output [cite: 121, 122]
        region_counter = 'Bejaia'
        for row in arff_dict['data']:
            if row[0] != region_counter:
                print(f'{region_counter} Region Finished!')
                region_counter = row[0]
        print(f'{region_counter} Region Finished!')
        print(f"Length of ARFF Data: {len(arff_dict['data'])}\n")

    except Exception as e:
        print(f"Data processing error: {e}")

    # Dump to the specified output path
    try:
        with open(f"data/{output_path}", 'w') as arf_file:
            arff.dump(arff_dict, arf_file)
            print(f'Successfully converted to data/{output_path} for Weka data mining.')
    except Exception as e:
        print(f"Error saving ARFF file: {e}")


if __name__ == '__main__':
    # Check if proper arguments are passed as per project instructions
    if len(sys.argv) != 3:
        print("Usage: python convert-to-weka.py <in.data> <out.arff>")
    else:
        convert_to_weka(sys.argv[1], sys.argv[2])