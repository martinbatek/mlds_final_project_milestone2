# Visualize record counts for Criteo:cat3, Avazu:device_ip, and KDD12:TitleID
criteo_cat1 = criteo.groupby('cat_3').agg({'click':'count'}).rename(columns={'click':'count'}).sort_values('count', ascending=False).reset_index()
avazu_site_domain = avazu.groupby('device_ip').agg({'click':'count'}).rename(columns={'click':'count'}).sort_values('count', ascending=False).reset_index()
kdd12_advertiser_id = kdd12.groupby('TitleID').agg({'Click':'count'}).rename(columns={'Click':'count'}).sort_values('count', ascending=False).reset_index().astype({'TitleID':str, 'count':int})

fig, axs = plt.subplots(1,3, figsize=(20,5))
axs[0].bar(criteo_cat1['cat_3'], criteo_cat1['count'])
axs[0].set_title('Criteo:cat3')
axs[0].set_ylabel('Record count')
axs[0].set_xlabel('C3 value')
axs[0].tick_params(axis='x',bottom=False,labelbottom=False) # Hide x-axis labels
axs[1].bar(avazu_site_domain['device_ip'], avazu_site_domain['count'])
axs[1].set_title('Avazu:device_ip')
axs[1].set_ylabel('Record count')
axs[1].set_xlabel('device_ip value')
axs[1].tick_params(axis='x',bottom=False,labelbottom=False) # Hide x-axis labels
axs[2].bar(kdd12_advertiser_id[:50]['TitleID'], kdd12_advertiser_id[:50]['count'])
axs[2].set_title('KDD12:TitleID')
axs[2].set_ylabel('Record count')
axs[2].set_xlabel('TitleID value')
axs[2].tick_params(axis='x',bottom=False,labelbottom=False) # Hide x-axis labels
plt.show()