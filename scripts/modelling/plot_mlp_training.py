# Retrieve the training histories
with open('./models/mlp/kdd12_hist.json','r') as f:
    kdd12_mlp_hist = json.load(f)
with open('./models/mlp/avazu_hist.json','r') as f:
    avazu_mlp_hist = json.load(f)
with open('./models/mlp/criteo_hist.json','r') as f:
    criteo_mlp_hist = json.load(f)

# Plot the training and validation losses for the three datasets
hist_objs = [
    kdd12_mlp_hist,
    avazu_mlp_hist,
    criteo_mlp_hist
]

datasets = ['KDD12', 'Avazu', 'Criteo']

fig, ax = plt.subplots(1,3, figsize=(15,5))
metrics = [
    'loss',
    'auc',
    'accuracy']
val_metrics = [f'val_{x}' for x in metrics]

for i in range(3):
    for metric in metrics:
        ax[i].plot(hist_objs[i][metric],label=metric)
    for metric in val_metrics:
        ax[i].plot(hist_objs[i][metric],label=metric,linestyle='--')
    ax[i].set_title(datasets[i])
    ax[i].set_xlabel('Epoch')
    ax[i].legend()
fig.savefig('figures/mlp_training_metrics.png')
fig.show()