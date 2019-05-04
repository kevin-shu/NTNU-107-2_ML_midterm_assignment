import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn import tree
from sklearn.model_selection import cross_val_score
# import graphviz 

from itertools import combinations

# # == North region
# df = pd.read_csv("north_region.csv",header=0)
# X = df.drop(columns=["PM10", "PM2.5", "日期"])
# y = df["PM2.5"]

# # Discretize columns
# y = pd.qcut(y, 4, labels=False)

# #  Training decision tree
# clf = tree.DecisionTreeClassifier()
# scores = cross_val_score(clf,X,y,cv=10,scoring='accuracy',error_score=np.nan)

# print("# North region's mean accuracy (10-fold):")
# # print(scores)
# print( " => " + str( scores.mean() ) )

def si (region):

    df = pd.read_csv(region+"_region.csv",header=0)
    X = df.drop(columns=["PM10", "PM2.5", "日期"])
    y = df["PM2.5"]

    # Discretize columns
    # y = pd.qcut(y, 4, labels=False)

    clf = tree.DecisionTreeClassifier()
    scores = cross_val_score(clf,X,y,cv=10,scoring='neg_mean_squared_error',error_score=np.nan)
    print("# "+region+" region's mean accuracy (10-fold):")
    print( " => " + str( scores.mean() ) )


    # # == Test wich three features make the besy predict:
    # best_feature_set = []
    # best_score = 0

    # for n in range(4, len(X.columns.values)+1):

    #     feature_sets = list( combinations( X.columns.values, n) )

    #     for feature_set in feature_sets:
    #         scores = cross_val_score(clf,X,y,cv=10,scoring='neg_mean_squared_error',error_score=np.nan)
    #         # scores = cross_val_score(regr,X[np.asarray(feature_set)],y,cv=10,error_score=np.nan, scoring='neg_mean_squared_error')
    #         if abs( scores.mean() ) > abs( best_score ):
    #             best_feature_set = feature_set
    #             best_score = scores.mean()
    # print("# "+region+" region's mean accuracy (10-fold):")
    # print( " => " + str( best_score.mean() ) )
    # # print( " (using %s)" % ( str(best_feature_set) ) )

si("all")
si("north")