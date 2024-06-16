# Show first 5 rows of Criteo dataset
criteo = pd.read_csv(
    './data/criteo/criteo_train.csv',
    dtype={
        'cat_1':'category',
        'cat_2':'category',
        'cat_3':'category',
        'cat_4':'category',
        'cat_5':'category',
        'cat_6':'category',
        'cat_7':'category',
        'cat_8':'category',
        'cat_9':'category',
        'cat_10':'category',
        'cat_11':'category',
        'cat_12':'category',
        'cat_13':'category',
        'cat_14':'category',
        'cat_15':'category',
        'cat_16':'category',
        'cat_17':'category',
        'cat_18':'category',
        'cat_19':'category',
        'cat_20':'category',
        'cat_21':'category',
        'cat_22':'category',
        'cat_23':'category',
        'cat_24':'category',
        'cat_25':'category',
        'cat_26':'category'
    }
    )

print("Snapshot of Criteo training data:")
display(criteo.head())