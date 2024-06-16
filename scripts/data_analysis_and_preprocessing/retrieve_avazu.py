# Show first 5 rows of Avazu dataset
avazu = pd.read_csv(
    './data/avazu/avazu_train.csv',
    dtype={
        'id':'int64',
        'click':'int64',
        'hour':'int64',
        'C1':'category',
        'banner_pos':'category',
        'site_id':'category',
        'site_domain':'category',
        'site_category':'category',
        'app_id':'category',
        'app_domain':'category',
        'app_category':'category',
        'device_id':'category',
        'device_ip':'category',
        'device_model':'category',
        'device_type':'category',
        'device_conn_type':'int64',
        'C14':'category',
        'C15':'category',
        'C16':'category',
        'C17':'category',
        'C18':'category',
        'C19':'category',
        'C20':'category',
        'C21':'category'
    }
    )
print("Snapshot of Avazu training data:")
display(avazu.head(2))