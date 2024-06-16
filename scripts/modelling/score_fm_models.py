# Score the models
print("KDD12:")
kdd12_log_loss = log_loss(kdd12_val_y_fm, kdd12_fm.predict_proba(kdd12_val_X_csc))
kdd12_roc_auc = roc_auc_score(kdd12_val_y_fm, kdd12_fm.predict_proba(kdd12_val_X_csc))
kdd12_accuracy = accuracy_score(kdd12_val_y_fm, kdd12_fm.predict(kdd12_val_X_csc))
print(f"Log loss: {kdd12_log_loss}")
print(f"ROC AUC: {kdd12_roc_auc}")
print(f"Accuracy: {kdd12_accuracy}")

print("\nAvazu:")
val_log_loss = log_loss(avazu_val_y_fm, avazu_fm.predict_proba(avazu_val_X_csc))
val_roc_auc = roc_auc_score(avazu_val_y_fm, avazu_fm.predict_proba(avazu_val_X_csc))
val_accuracy = accuracy_score(avazu_val_y_fm, avazu_fm.predict(avazu_val_X_csc))
print(f"Log loss: {val_log_loss}")
print(f"ROC AUC: {val_roc_auc}")
print(f"Accuracy: {val_accuracy}")

print("\nCriteo:")
val_log_loss = log_loss(criteo_val_y_fm, criteo_fm.predict_proba(criteo_val_X_csc))
val_roc_auc = roc_auc_score(criteo_val_y_fm, criteo_fm.predict_proba(criteo_val_X_csc))
val_accuracy = accuracy_score(criteo_val_y_fm, criteo_fm.predict(criteo_val_X_csc))
print(f"Log loss: {val_log_loss}")
print(f"ROC AUC: {val_roc_auc}")
print(f"Accuracy: {val_accuracy}")