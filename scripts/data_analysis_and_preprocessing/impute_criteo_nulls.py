# Sklearn imputers only work with numerical data, so we need to convert 
# the categorical data to numerical data first.
criteo_category_map = {}
criteo_factorized = criteo.copy()
for col in criteo.columns[criteo.dtypes == 'category']:
    criteo_factorized[col], criteo_category_map[col] = pd.factorize(criteo[col])
    criteo_factorized[col] = criteo_factorized[col].astype('float').replace(-1.0, np.nan).astype('category')

# Export the category map to a pickle file in case we need it
with open('./data/criteo/criteo_category_map.pkl', 'wb') as f:
    pkl.dump(criteo_category_map, f,protocol=pkl.HIGHEST_PROTOCOL)

# Impute the missing values in the criteo dataset using Iterative Imputation using the SKLearn library
## THIS PART WAS RUN ON A HIGH CPU INSTANCE ON AWS. IT TOOK A LONG TIME TO RUN

esitmator = HistGradientBoostingRegressor()
imputer = IterativeImputer(estimator=esitmator)
criteo_imputed = pd.DataFrame(imputer.fit_transform(criteo_factorized),columns=criteo.columns)

# Concatenate the missing indicators to the dataset
miss_imputer = MissingIndicator()
miss_cols = [f'{col}_missing' for col in criteo.columns[criteo.isna().any()]]
miss_cols_df = pd.DataFrame(miss_imputer.fit_transform(criteo),columns=miss_cols)
criteo_imputed_inds = pd.concat([criteo_imputed,miss_cols_df],axis=1)

# Export result to CSV
criteo_imputed_inds.to_csv('./data/criteo/criteo_train_imputed.csv',index=False)