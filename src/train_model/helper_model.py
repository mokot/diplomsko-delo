#!/usr/bin/env python3
# -*- coding: utf-8 -*

import random
import datasets
import pandas as pd
from IPython.display import display, HTML

# Constants
# Model names
GED_MODEL = "ged_model_finetuned"
GEC_MODEL = "gec_model_finetuned"
GER_MODEL = "ger_model_finetuned"
# Dataset directory
GED_DIRECTORY = "../../data/dataset/ged"
GEC_DIRECTORY = "../../data/dataset/gec"
GER_DIRECTORY = "../../data/dataset/ger"
# Error files
SOLAR_FILE_MULTIPLE_ERROR = "../../data/solar/solar_data_multiple_error.csv"
SOLAR_FILE_SINGLE_ERROR = "../../data/solar/solar_data_single_error.csv"
LEKTOR_FILE_MULTIPLE_ERROR = "../../data/lektor/lektor_data_multiple_error.csv"
LEKTOR_FILE_SINGLE_ERROR = "../../data/lektor/lektor_data_single_error.csv"


def show_random_elements(dataset, num_examples=10):
    assert num_examples <= len(
        dataset
    ), "Can't pick more elements than there are in the dataset."
    picks = []
    for _ in range(num_examples):
        pick = random.randint(0, len(dataset) - 1)
        while pick in picks:
            pick = random.randint(0, len(dataset) - 1)
        picks.append(pick)

    df = pd.DataFrame(dataset[picks])
    for column, typ in dataset.features.items():
        if isinstance(typ, datasets.ClassLabel):
            df[column] = df[column].transform(lambda i: typ.names[i])
    display(HTML(df.to_html()))