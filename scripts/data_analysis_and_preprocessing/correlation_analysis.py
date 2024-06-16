# Replace the numerical values in the sparse datasets with the standardized values
kdd12_sparse[kdd12_numerical_columns] = kdd12_standardized[kdd12_numerical_columns]
avazu_sparse[avazu_numerical_columns] = avazu_standardized[avazu_numerical_columns]
criteo_sparse[criteo_numerical_columns] = criteo_standardized[criteo_numerical_columns]

# Compute the correlation matrix for the three datasets
kdd12_corr = kdd12_sparse.corr()
avazu_corr = avazu_sparse.corr()
criteo_corr = criteo_sparse.corr()

# Zero out the diagonal of the correlation matrices
np.fill_diagonal(kdd12_corr.values, 0)
np.fill_diagonal(avazu_corr.values, 0)
np.fill_diagonal(criteo_corr.values, 0)

# Set the correlation threshold
corr_threshold = 0.9

# Filter out relevant values
mask = np.any(np.abs(avazu_corr) > corr_threshold, axis = 0)
mask[0] = True # Keep the click column
avazu_corr_filtered = avazu_corr.loc[mask, :].loc[:, mask]
np.fill_diagonal(avazu_corr_filtered.values, 1)

# Plot the correlation matrix for Avazu using seaborn
plt.figure(figsize=(15,15))
sns.heatmap(avazu_corr_filtered, cmap='coolwarm', center=0)
plt.title('Correlation matrix for Avazu dataset')
plt.savefig('./figures/avazu_corr_matrix.png')

# Replicate the above for the KDD12 and Criteo datasets
mask = np.any(np.abs(kdd12_corr) > corr_threshold, axis = 0)
mask[0] = True # Keep the click column
kdd12_corr_filtered = kdd12_corr.loc[mask, :].loc[:, mask]
np.fill_diagonal(kdd12_corr_filtered.values, 1)

mask = np.any(np.abs(criteo_corr) > corr_threshold, axis = 0)
mask[0] = True # Keep the click column
criteo_corr_filtered = criteo_corr.loc[mask, :].loc[:, mask]
np.fill_diagonal(criteo_corr_filtered.values, 1)

# Plot the correlation matrix for KDD12 using seaborn
plt.figure(figsize=(15,15))
sns.heatmap(kdd12_corr_filtered, cmap='coolwarm', center=0)
plt.title('Correlation matrix for KDD12 dataset')
plt.savefig('./figures/kdd12_corr_matrix.png')

# Plot the correlation matrix for Criteo using seaborn
plt.figure(figsize=(15,15))
sns.heatmap(criteo_corr_filtered, cmap='coolwarm', center=0)
plt.title('Correlation matrix for Criteo dataset')
plt.savefig('./figures/criteo_corr_matrix.png')