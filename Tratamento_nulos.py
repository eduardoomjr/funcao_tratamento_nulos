def tratamento_nulos(df):
    import statistics as sts
    quantidade_colunas = df.shape
    for i in range(quantidade_colunas[1]):
        if df.iloc[:,i].isnull().sum() != 0:
            if df.iloc[:,i].dtypes == "O":
                moda = sts.mode(df.iloc[:,i])
                df.iloc[:,i].fillna(moda, inplace=True)
            else:
                mediana = sts.median(df.iloc[:,i])
                df.iloc[:,i].fillna(mediana, inplace=True)