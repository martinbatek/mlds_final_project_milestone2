# Add CTR as a target to KDD12
kdd12_standardized['click'] = kdd12['Click']/kdd12['Impression']

# move CTR to the first column
cols = kdd12_standardized.columns.tolist()
cols = cols[-1:] + cols[:-1]
kdd12_standardized = kdd12_standardized[cols]

# Drop the Click and Impression columns
kdd12_standardized = kdd12_standardized.drop(columns=['Click','Impression'])

# Export the standardized datasets to CSV
kdd12_standardized.to_csv('./data/kdd12/kdd12_standardized.csv', index=False)
avazu_standardized.to_csv('./data/avazu/avazu_standardized.csv', index=False)
criteo_standardized.to_csv('./data/criteo/criteo_standardized.csv', index=False)