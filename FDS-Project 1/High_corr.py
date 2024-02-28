high_corr_pairs = {}
for column in df_corr.columns:
    high_corr_columns = df_corr[column][(df_corr[column]) >= 0.5].index
    for corr_column in high_corr_columns:
        if column != corr_column:
            key = f"{column}/{corr_column}"
            value = df_corr[column][corr_column]
            high_corr_pairs[key] = value
low_corr_pairs = {}
for column in df_corr.columns:
    low_corr_columns = df_corr[column][(df_corr[column]) <= 0].index
    for corr_column in low_corr_columns:
        if column != corr_column:
            key = f"{column}/{corr_column}"
            value = df_corr[column][corr_column]
            low_corr_pairs[key] = value
