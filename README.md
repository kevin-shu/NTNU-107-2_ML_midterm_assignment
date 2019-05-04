
# How to run the program
In the terminal:
``` 
# Install required modules: 
pip freeze > requirements.txt 

# Preprocess the data, this should generate two files: "north_region.csv" and "all_region.csv"
python preprocess.py

# Run the linear-regression training and 10-fold validation:
python source/linear_regression.py

# Run the decition-tree training and 10-fold validation:
python source/decision_tree_classifier.py
```

# Algorithm
## Preprocess
1. Search and read all the ```.xsl``` file under **data** folder into program, and do the pivot analysis to make all the features into indivisual columns.
2. Merge all the data from different stations into one dataframe, and leave only the common features (that every station has).
3. Output the organized data into ```north_region.csv``` and ```all_region.csv```.

## Decision Tree classifier



# Finding

A. Think about your conversion and look at the data to find a reasonable discretization:
> I'd prefer to use ```qcut``` to discretization the target data, because it would cut the data more evenly than ```cut```. But since that sklearn's DecisionTreeClassifier can analyze the continuous data. It seens unnecessary to discretize in this case.

B. Predict the PM10 and PM2.5 scores given your data using the least squared error function and a linear model:
> PM10 is more difficult to predict than PM2.5, because it has worse mean squared error when doing 10-fold validation.


C. Compare the linear regression and decision tree models for the north region as well as for all of Taiwan. We define the north region as any site that is north of Tai Chung. Describe and try to explain the differences between the two trees and the two regressions:
> When I use decision tree model to analyze north and all region in Taiwan with 10-fold validation. North region's result is slightly better than all region in taiwan. I assume that's because the amount of north regions' data is fewer, so we could get the more accurate result.  
> And when it comes to linear regression, local region's result is way better than the nation.  
> Overall, the linear regression model perform better than decision tree model.

D. Compare the performance of the decision tree and linear regression on the data set. Which algorithms performs better on the training data? Which algorithms performs better under 10-fold cross validation?
> Overall, the linear regression model perform better than decision tree model.


# Reference
* https://pandas.pydata.org/pandas-docs/version/0.20/generated/pandas.melt.html
* https://pandas.pydata.org/pandas-docs/version/0.20/generated/pandas.pivot_table.html
* https://stackoverflow.com/questions/28006793/pandas-dataframe-to-list-of-lists/28006809
* https://stackoverflow.com/questions/1249388/removing-all-non-numeric-characters-from-string-in-python
* https://stackoverflow.com/questions/39835021/pandas-random-sample-with-remove
* https://stackoverflow.com/questions/43888010/python-pandas-delete-row-on-string-condition
* https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols.html
* https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
* https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html