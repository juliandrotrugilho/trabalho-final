import numpy as np
import pandas as pd

def get_rebalance_dates(df, rebalancing_window):
    
    # D - Daily 
    # W - Every Monday
    # M - Monthly - Every Begin Month 
    # A - Yearly - Every Begin Year
    
    if rebalancing_window == 'W':
        rebalancing_window = 'W-MON'
    elif rebalancing_window == 'M':
        rebalancing_window = 'MS'
    elif rebalancing_window == 'Y':
        rebalancing_window = 'AS'
    
    # Defining the rebalance dates
    if rebalancing_window != 'none':
        rebalancing_dates = df.resample(rule=rebalancing_window).first().index
    else:
        rebalancing_dates = []
    
    # Getting closest rebalance dates on trading dates
    df_rebalancing = pd.DataFrame(np.zeros((df.shape[0], 1)), index=df.index, columns=['rebalancing'])
    
    for date in rebalancing_dates:
        I = df[(df.index >= date)].index

        if len(I) > 0:
            df_rebalancing.loc[I[0], 'rebalancing'] = 1
            
    return df_rebalancing