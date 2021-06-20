import pandas as pd
import numpy as np
from sklearn import datasets

def create_function_count(data,b):
    return data.value_counts()


data = datasets.load_iris()
create_function_count(data,b='2342')
