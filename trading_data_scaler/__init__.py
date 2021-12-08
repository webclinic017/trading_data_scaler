__version__ = '1.0.0'

#%% Formula for scaling 
"""
The standard score of a sample x is calculated as:

z = (x - u) / s

where u is the mean of the training samples or zero if with_mean=False, 
and s is the standard deviation of the training samples or one if with_std=False.

"""
#%% Import module

import pandas as pd
import numpy as np


#%%

def scaler(df_data = None):
    df_data = df_data.copy()
    for str_column_name in df_data.columns:
        ndarray_values = df_data[str_column_name].to_numpy()
        ndarray_mean = df_data[str_column_name].expanding().apply(lambda x:   np.mean(x) ).to_numpy()
        ndarray_stdv = df_data[str_column_name].expanding().apply(lambda x:   np.std(x) ).to_numpy()
        ndarray_values_scaled = (ndarray_values - ndarray_mean) / ndarray_stdv
        df_data[str_column_name] = np.nan_to_num(ndarray_values_scaled)
    return df_data

#%%
if __name__  == '__main__':
    df_data = pd.DataFrame({'A':[1,2,3,-4,5],
                            'B':[11,-22,55,33,44]
                            })
                            
    df_data_scaled = scaler(df_data = df_data)

#%%