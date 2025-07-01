#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('pip', 'install pandas')


# In[5]:


import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)

    # Clean column names
    df.columns = df.columns.str.strip()

    # Remove commas and convert to float where necessary
    if 'VALUE' in df.columns:
        df['VALUE'] = df['VALUE'].astype(str).str.replace(',', '').astype(float)

    # Clean and convert 'close' and 'PREV. CLOSE'
    df['close'] = pd.to_numeric(df['close'].astype(str).str.replace(',', '').str.strip(), errors='coerce')
    df['PREV. CLOSE'] = pd.to_numeric(df['PREV. CLOSE'].astype(str).str.replace(',', '').str.strip(), errors='coerce')

    # Drop rows with missing values in important columns
    df.dropna(subset=['close', 'PREV. CLOSE'], inplace=True)

    # Create features
    df['Price Change %'] = ((df['close'] - df['PREV. CLOSE']) / df['PREV. CLOSE']) * 100

    if 'HIGH' in df.columns and 'LOW' in df.columns:
        df['Volatility'] = pd.to_numeric(df['HIGH'], errors='coerce') - pd.to_numeric(df['LOW'], errors='coerce')

    return df


# In[ ]:




