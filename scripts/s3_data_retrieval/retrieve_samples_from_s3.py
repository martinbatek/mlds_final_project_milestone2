# %%
# Import necessary libraries
import pandas as pd
import sys

# Retrieve the sample size argument
n = int(sys.argv[1])

# %%
# Read in kdd training from S3
kdd12_data = pd.read_csv(
    's3://mlds-final-project-bucket/kdd12/train/training/training.txt',
    delimiter='\t',
    nrows = n,
    header=None,
    names=['Click','Impression','DisplayURL','AdID','AdvertiserID','Depth','Position','QueryID','KeywordID','TitleID','DescriptionID','UserID']
    )
kdd12_data.to_csv('./data/kdd12/kdd12_training.csv', index=False)

# %%
# Read in avazu training data from S3
avazu_training_data = pd.read_csv(
    's3://mlds-final-project-bucket/avazu/train/train.csv',
    nrows = n
    )
avazu_training_data.to_csv('./data/avazu/avazu_train.csv', index=False)

# %%
# Create column name list as per the README file
criteo_names = ['click']
for i in range(1, 14):
    criteo_names.append('int_{0}'.format(i))

for i in range(1, 27):
    criteo_names.append('cat_{0}'.format(i))

# Read in criteo training data from S3
criteo_training_data = pd.read_csv(
    's3://mlds-final-project-bucket/dac/train/train.txt',
    nrows = n,
    sep='\t',
    header=None,
    names=criteo_names
    )
criteo_training_data.to_csv('./data/criteo/criteo_train.csv', index=False)


