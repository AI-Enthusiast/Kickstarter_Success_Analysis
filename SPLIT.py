# split kickstarter into 2 parts
import pandas as pd

ks = 'kickstarter.csv'
ks_df = pd.read_csv(ks)

ks_len = len(ks_df)
ks_pt1 = ks_df.iloc[:ks_len//2]
ks_pt2 = ks_df.iloc[ks_len//2:]

ks_pt1.to_csv('kickstarter_pt1.csv', index=False)
ks_pt2.to_csv('kickstarter_pt2.csv', index=False)