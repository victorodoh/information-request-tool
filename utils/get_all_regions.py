import pandas as pd
from cache_dict import cached_data

df = pd.read_csv('covid_dataset/specimenDate_ageDemographic-unstacked.csv', low_memory=False)

def region_list():
    cache_key = "region_list_key"
    
    if cache_key in cached_data:
        return cached_data[cache_key]
    else:
        region_list = df.areaName.unique().tolist()
        cached_data[cache_key] = region_list
        return region_list