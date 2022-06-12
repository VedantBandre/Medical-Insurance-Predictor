# Medical-Insurance-Predictor

This is a Machine Learning Regressor Model developed using the insurance dataset at https://www.kaggle.com/datasets/mirichoi0218/insurance. 

It considers the features of age, sex, bmi, region of residence, and number of children to estimate the cost of insurance of that certain individual.

It was developed and tested woth 4 types of ML Regressors, namely Linear Regressor, Lasso Regressor, Ridge Regressor and RandomForestRegressor.

The highest accuracy of 85% was achieved by RandomForestRegressor. We also found by data analytics that the price of BMI increases by around 70% if one's BMI exceeds 30. 

The Flask API of this model was made to be integrated into the Cloud Computing Project of Hospital Website in the repo https://github.com/nnish16/health_ccl_proj.git
