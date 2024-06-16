# Calculate Click-Through Rates for the three datasets
datasets = ['KDD12','Avazu','Criteo']
CTRs = [
    kdd12['Click'].sum()/kdd12['Impression'].sum(),
    avazu['click'].sum()/avazu.shape[0],
    criteo['click'].sum()/criteo.shape[0]
]

# Plot the CTRs as bar charts
plt.bar(datasets, CTRs)
plt.ylabel('CTR %')
plt.title('CTR comparison between datasets')
plt.show()