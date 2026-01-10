import pandas as pd
import os 


# Leitura do Dataset
BASE = os.path.dirname(__file__)      
DATASET = os.path.join(BASE, "..", "data", "cs-training.csv")

# Target: SeriousDlqin2yrs
# 1 = entrou em inadimplência (default) em 2 anos
# 0 = não entrou

COLUMN_TARGET = "SeriousDlqin2yrs"

#Sanity Checking (Checagem de sanidade) - Visa verificar em menos de 30 segundas se uma aplicação está funcionando, nesse contexto, estou verificando a integridade desse dataset

def main():
    df = pd.read_csv(DATASET)

    print("Shape (linhas, colunas):", df.shape)
    # Shape (linhas, colunas): (150000, 12)
    print("\nColunas:")
    print(df.columns.tolist())

    print("\nTarget distribution (Distribuição de inadimplência):")
    print(df[COLUMN_TARGET].value_counts(dropna=False))
    #
    print("\nTarget rate (Média):", df[COLUMN_TARGET].mean())

    print("\nMissing values (Relação de nulos por Coluna):")
    miss = df.isna().sum().sort_values(ascending=False)
    print(miss.head(10))

    print("\Top 3 lines:")
    print(df.head(3))

if __name__ == "__main__":
    main()