# Load the models
kdd12_mlp = tf.keras.models.load_model('./models/mlp/kdd12_mlp.keras')
avazu_mlp = tf.keras.models.load_model('./models/mlp/avazu_mlp.keras')
criteo_mlp = tf.keras.models.load_model('./models/mlp/criteo_mlp.keras')

# Evaluate MLP models
print("KDD12:")
kdd12_mlp.evaluate(kdd12_val_tfd)
print("\nAvazu:")
avazu_mlp.evaluate(avazu_val_tfd)
print("\nCriteo:")
criteo_mlp.evaluate(criteo_val_tfd)