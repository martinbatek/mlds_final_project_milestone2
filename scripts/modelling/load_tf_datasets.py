# Create training and validation datasets
kdd12_train_tfd = tf.data.Dataset.from_tensor_slices(
    (pd.get_dummies(kdd12_train_X, columns=kdd12_categorical_columns).to_numpy('float'), kdd12_train_y.to_numpy())
).shuffle(20).batch(100)
kdd12_val_tfd = tf.data.Dataset.from_tensor_slices(
    (pd.get_dummies(kdd12_val_X, columns=kdd12_categorical_columns).to_numpy('float'), kdd12_val_y.to_numpy())
).shuffle(20).batch(100)

avazu_train_tfd = tf.data.Dataset.from_tensor_slices(
    (pd.get_dummies(avazu_train_X, columns=avazu_categorical_columns).to_numpy('float'), avazu_train_y.to_numpy())
).shuffle(20).batch(100)
avazu_val_tfd = tf.data.Dataset.from_tensor_slices(
    (pd.get_dummies(avazu_val_X, columns=avazu_categorical_columns).to_numpy('float'), avazu_val_y.to_numpy())
).shuffle(20).batch(100)

criteo_train_tfd = tf.data.Dataset.from_tensor_slices(
    (pd.get_dummies(criteo_train_X, columns=criteo_categorical_columns).to_numpy('float'), criteo_train_y.to_numpy())
).shuffle(20).batch(100)
criteo_val_tfd = tf.data.Dataset.from_tensor_slices(
    (pd.get_dummies(criteo_val_X, columns=criteo_categorical_columns).to_numpy('float'), criteo_val_y.to_numpy())
).shuffle(20).batch(100)