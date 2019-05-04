import pandas as pd
import numpy as np

import glob, os
import re

def to_number(v):
    if v in ["NR"]:
        v = 0
    elif type(v) not in [int,float]:
        v = re.sub("[^0-9\.]", "", str(v))
    v = float(v)
    if v<0:
        v=0
    return v

# def discretize_PM25(col):
#     # bins = [-1, 50, 100, 200, 300, 99999]
#     # labels = ["Good", "Moderate", "Unhealthy", "Very Unhealthy", "Hazardous"]
#     # target_names = ["Good", "Moderate", "Unhealthy", "Very Unhealthy", "Hazardous"]
#     return pd.qcut(col, 8, labels=False)


def organize_data(df):
    # == Pre-process
    hour_list = list(map(lambda x:str(x).zfill(2), list(range(0,24))))
    df.columns = ["日期","測站","測項"]+hour_list
    df = pd.melt(df, id_vars=['日期',"測項"], value_vars=(hour_list))
    df = df.rename(columns={'variable': 'Hour'})
    table = pd.pivot_table(df, values='value', index=["日期", 'Hour'], columns=["測項"], aggfunc=np.sum)
    # table = shuffle(table) # 為了之後的 k-fold cross validation 先做洗牌

    # == Cleaning field
    table = table.drop(table[ table["PM2.5"].str[-1:]=="#" ].index)
    table = table.applymap(to_number)
    table = table.dropna(axis=0, how='any')

    return table


def preprocess(region):

    # == Read data into raw_df
    dirname=os.path.dirname
    THIS_FOLDER = dirname(os.path.abspath(__file__))
    ROOT_FOLDER = dirname(THIS_FOLDER)
    table = pd.DataFrame()

    files = []

    if region=="all":
        files = glob.glob("data/**/*.xls")
    elif region=="north":
        files = glob.glob("data/107年 北部空品區/*.xls")
    
    i = 1
    for file_path in files:

        print("Reading \"%s\"...(%d/%d)" % (file_path, i, len(files)) )
        raw_df = pd.read_excel( os.path.join(ROOT_FOLDER, file_path), "Sheet1" )
        region_table = organize_data(raw_df)

        cols_to_remove = []

        if not table.empty:
            new_cols_set = set(region_table.columns.values)
            old_cols_set = set(table.columns.values)
            cols_to_remove = list(new_cols_set-old_cols_set) + list(old_cols_set-new_cols_set)
            cols_to_remove = list( set(cols_to_remove) ) # 去掉重複的

        table = pd.concat([table,region_table],sort=False)
        table = table.drop(columns=cols_to_remove)

        i+=1

    # == Print the data out
    table.to_csv(region+"_region.csv", encoding='utf-8')

    X = table.drop(columns=["PM10", "PM2.5"])
    y = table["PM2.5"]
    # print( np.where(np.isnan(X) ))

    # return X, y

preprocess("north")
preprocess("all")