# Show firt 5 rows of the training dataset
kdd12 = pd.read_csv(
    './data/kdd12/kdd12_training.csv',
    dtype={
        'click':'int64',
        'Impression':'int64',
        'DisplayURL':'category',
        'AdId':'category',
        'AdvertiserId':'category',
        'Depth':'int64',
        'Position':'int64',
        'QueryID':'category',
        'KeywordID':'category',
        'TitleID':'category',
        'DescriptionID':'category',
        'UserID':'category'
    }
    )
print("Snapshot of KDD12 training data:")
display(kdd12.head())