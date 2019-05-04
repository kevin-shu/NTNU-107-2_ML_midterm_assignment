
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score

from itertools import combinations

# == Create linear regression object
regr = linear_model.LinearRegression()

# == Get data
df = pd.read_csv("all_region.csv",header=0)

X = df.drop(columns=["PM10", "PM2.5", "日期"])

scores = cross_val_score(regr,X,df["PM2.5"],cv=10,error_score=np.nan, scoring='neg_mean_squared_error')
print( "All regions' PM2.5 mean squared error: " + str( scores.mean() ) )
scores = cross_val_score(regr,X,df["PM10"],cv=10,error_score=np.nan, scoring='neg_mean_squared_error')
print( "All regions' PM10 mean squared error: " + str( scores.mean() ) )

# == Get data
df = pd.read_csv("north_region.csv",header=0)

X = df.drop(columns=["PM10", "PM2.5", "日期"])

scores = cross_val_score(regr,X,df["PM2.5"],cv=10,error_score=np.nan, scoring='neg_mean_squared_error')
print( "North regions' PM2.5 mean squared error: " + str( scores.mean() ) )
scores = cross_val_score(regr,X,df["PM10"],cv=10,error_score=np.nan, scoring='neg_mean_squared_error')
print( "North regions' PM10 mean squared error: " + str( scores.mean() ) )


# # == Test wich three features make the besy predict:
# best_feature_set = []
# best_score = 999

# for n in range(1, len(X.columns.values)+1):
#     feature_sets = list( combinations( X.columns.values, n) )
#     for feature_set in feature_sets:
#         scores = cross_val_score(regr,X[np.asarray(feature_set)],y,cv=10,error_score=np.nan, scoring='neg_mean_squared_error')
#         if abs( scores.mean() ) < abs( best_score ):
#             best_feature_set = feature_set
#             best_score = scores.mean()
        
# print("# All region's mean accuracy (10-fold):")
# print( " => " + str( best_score ) )
# print( best_feature_set )
# print( " (using %s)" % ( str(best_feature_set) ) )
