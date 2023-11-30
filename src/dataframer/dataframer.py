def dataframer (df, transformers):
    df_out = pd.DataFrame()
    
    for (col, transformer) in transformers:
        transformer(col, df, df_out)
    return df_out

def numeric_to_one_hot(bins):
    def transformer(col, df_old, df_new):
        if col not in df_old.columns:
            raise ValueError(f"DataFrame must contain a {col} column")
    
        labels = [f'{col}_{bins[i]}' for i in range(len(bins) - 1)]
        categories = pd.cut(df_old[col], bins=bins, labels=labels, right=False, include_lowest=True)

        for label in labels:
            df_new[label] = (categories == label).astype(int)
    
    return transformer

def string_to_one_hot(bins):
    def transformer(col, df_old, df_new):
        if col not in df_old.columns:
            raise ValueError(f"DataFrame must contain a {col} column")
            
        for bin in bins:
            df_new[f'{col}_{bin}'] = (df_old[col] == bin).astype('int')
            
    return transformer

def numeric_to_normalise(min_val=0, max_val=100):
    def transformer(col, df_old, df_new):
        if col not in df_old.columns:
            raise ValueError(f"DataFrame must contain a {col} column")
        
        df_new[col] = df_old[col] / max_val
    
    return transformer