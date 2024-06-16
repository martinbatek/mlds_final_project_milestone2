# Plot boxplots for the numerical features in the three datasets
kdd12_numerical_columns = [
    'Depth',
    'Position'
]

avazu_numerical_columns = [
    'hour'
]

criteo_numerical_columns = [f'int_{i}' for i in np.arange(1,14)]

fig, axs = plt.subplots(1,3, figsize=(20,5))
sns.boxplot(data=kdd12[kdd12_numerical_columns], ax=axs[0])
axs[0].set_title('KDD12')
sns.boxplot(data=avazu[avazu_numerical_columns], ax=axs[1])
axs[1].set_title('Avazu')
sns.boxplot(data=criteo[criteo_numerical_columns], ax=axs[2])
axs[2].set_title('Criteo')
plt.show()