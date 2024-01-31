import streamlit as st
import pandas as pd

from DataSynthesizer.DataDescriber import DataDescriber
from DataSynthesizer.DataGenerator import DataGenerator
from DataSynthesizer.ModelInspector import ModelInspector
from DataSynthesizer.lib.utils import read_json_file

import pandas as pd

file = st.file_uploader("Upload a file", type="csv")

if file:
    df = pd.read_csv(file)
    df.to_csv(f"{file.name}.csv", index=False)

    input_data = f"{file.name}.csv"
    # location of two output files
    mode = 'independent_attribute_mode'
    description_file = f'description.json'
    synthetic_data = f'sythetic_data.csv'

    threshold_value = 20

    epsilon = 1
    degree_of_bayesian_network = 2 
    num_tuples_to_generate = 3000

    describer = DataDescriber(category_threshold=threshold_value)
    describer.describe_dataset_in_independent_attribute_mode(dataset_file=input_data, 
                                                            epsilon=epsilon, )
    describer.save_dataset_description_to_file(description_file)

    generator = DataGenerator()
    generator.generate_dataset_in_independent_mode(num_tuples_to_generate, description_file)
    generator.save_synthetic_data(synthetic_data)

    # Read both datasets using Pandas.
    input_df = pd.read_csv(input_data, skipinitialspace=True)
    synthetic_df = pd.read_csv(synthetic_data)
    # Read attribute description from the dataset description file.
    attribute_description = read_json_file(description_file)['attribute_description']

    st.write(f"Input data: {len(input_df)} rows, Synthetic data: {len(synthetic_df)} rows")
    st.download_button(label="Download synthetic", data=synthetic_df.to_csv(), file_name="results.csv")

    inspector = ModelInspector(input_df, synthetic_df, attribute_description)
    inspector.mutual_information_heatmap()

