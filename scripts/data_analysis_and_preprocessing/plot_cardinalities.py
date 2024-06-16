# Display the cardinality of the categorical features in the three datasets
kdd12_categorical_columns = [
    'DisplayURL',
    'AdID',
    'AdvertiserID',
    'QueryID',
    'KeywordID',
    'TitleID',
    'DescriptionID',
    'UserID'
]

avazu_categorical_columns = [
    'id',
    'c1',
    'banner_pos',
    'site_id',
    'site_domain',
    'site_category',
    'app_id',
    'app_domain',
    'app_category',
    'device_id',
    'device_ip',
    'device_model',
    'device_type',
    'device_conn_type',
    'c14',
    'c15',
    'c16',
    'c17',
    'c18',
    'c19',
    'c20',
    'c21'
]

criteo_categorical_columns = [f'cat_{i}' for i in np.arange(1,27)]

kdd12_cardinality = [kdd12[column].nunique() for column in kdd12_categorical_columns]
avazu_cardinality = [avazu[column].nunique() for column in avazu_categorical_columns]
criteo_cardinality = [criteo[column].nunique() for column in criteo_categorical_columns]

# Plot the cardinality of the categorical features in the three datasets
fig, ax = plt.subplots(1, 3, figsize=(20,5))

ax[0].bar(kdd12_categorical_columns, kdd12_cardinality)
ax[0].set_ylabel('Cardinality')
ax[0].set_title('Cardinality of categorical features in KDD12 dataset')
ax[0].set_xticklabels(ax[0].get_xticks(),rotation=45)

ax[1].bar(avazu_categorical_columns, avazu_cardinality)
ax[1].set_ylabel('Cardinality')
ax[1].set_title('Cardinality of categorical features in Avazu dataset')
ax[1].set_xticklabels(ax[1].get_xticks(),rotation=45)

ax[2].bar(criteo_categorical_columns, criteo_cardinality)
ax[2].set_ylabel('Cardinality')
ax[2].set_title('Cardinality of categorical features in Criteo dataset')
ax[2].set_xticklabels(ax[2].get_xticks(),rotation=45)

plt.show()