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

import arff
import pandas as pd
import sys

def convert_to_weka(input_path, output_path):
    try:
        # Starting message
        print(f"Starting conversion of data/{input_path} to .arff")

        # Read the input file & show metadata
        df = pd.read_csv(f"data/{input_path}")
        print(f"Input: data{input_path}")
        print(f"Length of DataFrame: {len(df)}\n")

        # Getting some data from the user (name of dataset and small description)
        relation_name = input("Enter the relation name: ")
        description_text = input("Enter a description for the dataset: ")

        # Getting all the attributes from the DataFrame
        arff_attributes = []
        for col in df.columns:
            # If column a numeric type (float or int) -> append as the REAL data type
            if pd.api.types.is_numeric_dtype(df[col]):
                arff_attributes.append((col, 'REAL'))
            # Otherwise, get categorical values (region, date, class)
            else:
                unique_values = df[col].unique().astype(str).tolist()
                arff_attributes.append((col, unique_values))

        # Create dictionary from the information above
        arff_dict = {
            'description': description_text,
            'relation': relation_name,
            'attributes': arff_attributes,
            'data': df.values.tolist()
        }

        # Create the output file
        with open(f"data/{output_path}", 'w') as arf_file:
            print("Converting to .arff...")
            arff.dump(arff_dict, arf_file)
            print(f'\nSuccessfully converted to data/{output_path} for Weka data mining.')
            # Showing final length of data
            print(f"Length of ARFF Data: {len(arff_dict['data'])}")

    # Exception if file not found or any other exception occurs
    except FileNotFoundError:
        print(f"Error: The file data/{input_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python convert-to-weka.py <in.csv> <out.arff>")
    else:
        convert_to_weka(sys.argv[1], sys.argv[2])