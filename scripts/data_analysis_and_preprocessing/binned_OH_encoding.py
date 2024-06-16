# Factorize the categorical features in the three datasets
kdd12_factorized = kdd12.copy()
kdd12_category_map = {}
for col in kdd12_categorical_columns:
    kdd12_factorized[col], kdd12_category_map[col] = pd.factorize(kdd12[col])
    kdd12_factorized[col] = kdd12_factorized[col].astype('float').replace(-1.0, np.nan).astype('int')

avazu_factorized = avazu.copy()
avazu_category_map = {}
for col in avazu_categorical_columns:
    avazu_factorized[col], avazu_category_map[col] = pd.factorize(avazu[col])
    avazu_factorized[col] = avazu_factorized[col].astype('float').replace(-1.0, np.nan).astype('int')

# Export the category map to a pickle file in case we need it
with open('./data/kdd12/kdd12_category_map.pkl', 'wb') as f:
    pkl.dump(kdd12_category_map, f,protocol=pkl.HIGHEST_PROTOCOL)

with open('./data/avazu/avazu_category_map.pkl', 'wb') as f:
    pkl.dump(avazu_category_map, f,protocol=pkl.HIGHEST_PROTOCOL)

# Implement one-hot encoding for the categorical features in the three datasets
def one_hot_encode(df, columns, threshold=20):
    out_df = df.copy()
    enc = OneHotEncoder(min_frequency=threshold)
    enc_df = pd.DataFrame(enc.fit_transform(df[columns]).toarray())
    enc_df.columns = enc.get_feature_names_out(columns)
    out_df_sparse = df.drop(columns=columns)
    out_df_sparse = pd.concat([out_df_sparse, enc_df], axis=1)
    out_df[columns] = enc.inverse_transform(enc_df)
    return out_df_sparse, enc, out_df

# One-hot encode the categorical features in the three datasets
kdd12_sparse, kdd12_encoder, kdd12_encoded = one_hot_encode(kdd12_factorized, kdd12_categorical_columns,50)

avazu_sparse, avazu_encoder, avazu_encoded = one_hot_encode(avazu_factorized, avazu_categorical_columns,100)

criteo_sparse, criteo_encoder, criteo_encoded = one_hot_encode(criteo_imputed_inds, criteo_categorical_columns,100)

# Print the shape of the original datasets
print("Before one-hot encoding:")
print(f"KDD12 shape: {kdd12.shape}")
print(f"Avazu shape: {avazu.shape}")
print(f"Criteo shape: {criteo_imputed_inds.shape}\n")

# Print the resulting shapes of the datasets
print("After one-hot encoding:")
print(f"KDD12 shape: {kdd12_encoded.shape}")
print(f"Avazu shape: {avazu_encoded.shape}")
print(f"Criteo shape: {criteo_encoded.shape}")

print("Sparse output:")
print(f"KDD12 shape: {kdd12_sparse.shape}")
print(f"Avazu shape: {avazu_sparse.shape}")
print(f"Criteo shape: {criteo_sparse.shape}")

# Export encoded datasets to CSV
kdd12_encoded.to_csv('./data/kdd12/kdd12_encoded.csv', index=False)
avazu_encoded.to_csv('./data/avazu/avazu_encoded.csv', index=False)
criteo_encoded.to_csv('./data/criteo/criteo_encoded.csv', index=False)

# Export the encoders to pickle files
with open('./data/kdd12/kdd12_encoder.pkl', 'wb') as f:
    pkl.dump(kdd12_encoder, f, protocol=pkl.HIGHEST_PROTOCOL)

with open('./data/avazu/avazu_encoder.pkl', 'wb') as f:
    pkl.dump(avazu_encoder, f, protocol=pkl.HIGHEST_PROTOCOL)

with open('./data/criteo/criteo_encoder.pkl', 'wb') as f:
    pkl.dump(criteo_encoder, f, protocol=pkl.HIGHEST_PROTOCOL)