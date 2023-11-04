import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def df():
    excel = pd.ExcelFile("cdc.xlsx")

    sheetName = excel.sheet_names
    dataframes = []

    for i in sheetName:
        df = excel.parse(i)
        dataframes.append(df)

    df_d = dataframes[0]
    df_o = dataframes[1]
    df_i = dataframes[2]

    df_d.drop(columns=["YEAR", "COUNTY", "STATEW"], inplace=True)
    merge_df_do = pd.merge(df_d, df_o, on='FIPS',how='inner')
    merge_df_do.drop(columns=["YEAR", "COUNTY", "STATE"], inplace=True)
    
    de_new_f = df_i.rename({'FIPDS': 'FIPS'}, axis='columns')

    merge_df_all = pd.merge(merge_df_do, de_new_f, on='FIPS',how='inner')
    merge_df_all.drop(columns=["YEAR", "COUNTY", "STATE"], inplace=True)

    return merge_df_all

def getinfo():
    data = df()
    return (type(data))

# merge = getinfo()
# print(merge)