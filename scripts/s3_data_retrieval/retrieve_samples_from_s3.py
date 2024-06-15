# %%
# Import necessary libraries
import pandas as pd
import boto3
import sys

# Set sample size
n = sys.argv[1]

# %%
# Read in kdd training data from S3
bucket = 'mlds-final-project-bucket'
prefix = 'kdd12/train/training_shuffled/'

## Create an S3 client
s3_client = boto3.client('s3')

## List objects within a S3 bucket prefix and read to pandas for the first n rows
response = s3_client.list_objects_v2(Bucket=bucket, Prefix=prefix)
kdd12_data = pd.DataFrame()
rows = n
if 'Contents' in response:
    keys = [obj['Key'] for obj in response['Contents']][1:]
    for key in keys:
        if rows == 0:
            break
        obj = s3_client.get_object(Bucket=bucket, Key=key)
        df = pd.read_csv(
            obj['Body'],
            nrows = rows,
            header=0,
            names=['Click','Impression','DisplayURL','AdID','AdvertiserID','Depth','Position','QueryID','KeywordID','TitleID','DescriptionID','UserID']
            )
        kdd12_data = pd.concat([kdd12_data, df])
        rows -= df.shape[0]
else:
    print("Folder is empty.")

## Save the data to a csv file
kdd12_data.to_csv('../../data/kdd12/kdd12_training.csv', index=False)

# %%
# Read in avazu training data from S3
bucket = 'mlds-final-project-bucket'
prefix = 'avazu/train_shuffled/'

## Create an S3 client
s3_client = boto3.client('s3')

## List objects within a S3 bucket prefix and read to pandas for the first n rows
response = s3_client.list_objects_v2(Bucket=bucket, Prefix=prefix)
avazu_training_data = pd.DataFrame()
rows = n
if 'Contents' in response:
    keys = [obj['Key'] for obj in response['Contents']][1:]
    for key in keys:
        if rows == 0:
            break
        obj = s3_client.get_object(Bucket=bucket, Key=key)
        df = pd.read_csv(
            obj['Body'],
            nrows = rows
            )
        avazu_training_data = pd.concat([avazu_training_data, df])
        rows -= df.shape[0]
else:
    print("Folder is empty.")

## Save the data to a csv file
avazu_training_data.to_csv('../../data/avazu/avazu_train.csv', index=False)

# %%
# Read in criteo training data from S3
bucket = 'mlds-final-project-bucket'
prefix = 'dac/train_shuffled/'

## Create column name list as per the README file
criteo_names = ['click']
for i in range(1, 14):
    criteo_names.append('int_{0}'.format(i))

for i in range(1, 27):
    criteo_names.append('cat_{0}'.format(i))

## Create an S3 client
s3_client = boto3.client('s3')

## List objects within a S3 bucket prefix and read to pandas for the first n rows
response = s3_client.list_objects_v2(Bucket=bucket, Prefix=prefix)
criteo_training_data = pd.DataFrame()
rows = n
if 'Contents' in response:
    keys = [obj['Key'] for obj in response['Contents']][1:]
    for key in keys:
        if rows == 0:
            break
        obj = s3_client.get_object(Bucket=bucket, Key=key)
        df = pd.read_csv(
            obj['Body'],
            nrows = rows,
            header=0,
            names=criteo_names
            )
        criteo_training_data = pd.concat([criteo_training_data, df])
        rows -= df.shape[0]
else:
    print("Folder is empty.")

## Save the data to a csv file
criteo_training_data.to_csv('../../data/criteo/criteo_train.csv', index=False)


