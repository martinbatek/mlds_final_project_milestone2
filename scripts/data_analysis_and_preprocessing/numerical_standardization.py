# Standardize the numerical features in the three datasets
kdd12_standardized = kdd12_encoded.copy()
scaler = StandardScaler()
kdd12_standardized[kdd12_numerical_columns] = scaler.fit_transform(kdd12_encoded[kdd12_numerical_columns])

avazu_standardized = avazu_encoded.copy()
scaler = StandardScaler()
avazu_standardized[avazu_numerical_columns] = scaler.fit_transform(avazu_encoded[avazu_numerical_columns])

criteo_standardized = criteo_encoded.copy()
scaler = StandardScaler()
criteo_standardized[criteo_numerical_columns] = scaler.fit_transform(criteo_encoded[criteo_numerical_columns])

# Apply log transformation to numerical features in the criteo dataset as described above
def criteo_log_transform(z):
    if z>2:
        return np.log(z)**2
    else:
        return z

criteo_log_transformer = FunctionTransformer(func=lambda x: x.map(criteo_log_transform))
criteo_standardized[criteo_numerical_columns] = criteo_log_transformer.transform(criteo_standardized[criteo_numerical_columns])

# Check the result
fig, axs = plt.subplots(1,1, figsize=(20,5))
sns.boxplot(data=criteo_standardized[[col for col in criteo_numerical_columns]])
plt.title("Boxplots of numerical features in the Criteo dataset after log transformation")
plt.show()