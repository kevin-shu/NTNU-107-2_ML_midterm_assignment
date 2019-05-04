import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn import tree
from sklearn.model_selection import cross_val_score

from itertools import combinations

def ana (region):

    df = pd.read_csv(region+"_region.csv",header=0)
    X = df.drop(columns=["PM10", "PM2.5", "日期"])
    y = df["PM2.5"]

    clf = tree.DecisionTreeClassifier()
    scores = cross_val_score(clf,X,y,cv=10,scoring='neg_mean_squared_error',error_score=np.nan)
    print("# "+region+" region's mean accuracy (10-fold):")
    print( " => " + str( scores.mean() ) )

ana("all")
ana("north")