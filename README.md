# pd-scorecard
Projeto para Portifólio - Construção de modelo de probabilidade de default de scorecard (binning + WOE + regressão logística), avaliação por AUC/KS/Gini e análise de lift por decis, convertendo PD em score e com definição de cutoff para tomada de decisão
# Score de Risco de Crédito — PD, Score e Política de Aprovação

Este projeto transforma dados de crédito em um **modelo de Probabilidade de Default (PD)** e em seguida cria um **score simples** e uma **política de decisão (cutoff)**, usei o dataset para competições do Kaggle **GiveMeSomeCredit**.

---

## O que o modelo faz?
- **Tratamento de dados** (missing + outliers + valores anômalos)
- **Modelo baseline (Regressão Logística)** para estimar **PD (Probabilidade de Default)**
- **Avaliação no formato usado em risco**: AUC, KS e tabela por decis (top 10% mais arriscado vs top 10% menos arriscado)
- **Score e política de aprovação**: aprovado/reprovado por cutoff 
---

## Resultados principais (teste)
- **AUC:** `0.839`
- **KS:** `0.525`
- **Separação por decis (ranking de risco):**
  - **Maior Decil - mais risco:** bad rate `33.2%`
  - **Menor Decil - menos risco:** bad rate `0.6%`

A Ideia é do modelo é sinalizar no topo os clientes com maior risco de inadimplência.

---

## Estrutura do projeto
Sugestão (ajuste se seus nomes forem diferentes):

- `notebooks/01_eda.ipynb`  
  EDA e checagens de qualidade (missing/outliers/valores suspeitos)

- `notebooks/02_clean_data.ipynb`  
  Limpeza com base no '01_eda' + geração do dataset final: `train_clean.csv`

- `notebooks/03_model+score.ipynb`  
  Treino do modelo + AUC/KS + tabela por decis e Score + cutoff (aprovação/reprovação)

---

## Como rodar
### 1) Dados
O dataset é o **GiveMeSomeCredit** usado em competições do Kaggle.  
Baixe e coloque em `data/` como `cs-training.csv`.

> Não está no repositório pois o Kaggle possuí regras de licença que não permite upar no Github
link: https://www.kaggle.com/competitions/GiveMeSomeCredit/data
### 2) Instalar dependências
No CMD:
pip install -r requirements.txt

### 3) Execute os Notebooks.

Execute os Notebooks na ordem sugerida pelos títulos (crescente).
