import pandas as pd

print("Carregando a base de dados original...")
try:
    df = pd.read_csv('exportacoes_carnes_sc_2019_2024.csv', sep=';', encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv('exportacoes_carnes_sc_2019_2024.csv', sep=';', encoding='latin1')

print("Iniciando a faxina dos dados...")

# 1. Removendo a sujeira (\r) de todas as colunas que contêm texto
colunas_texto = df.select_dtypes(include=['object', 'string']).columns
for col in colunas_texto:
    df[col] = df[col].astype(str).str.replace(r'\r', '', regex=True).str.strip()

# 2. Arrumando o NCM (O Pandas corta o zero à esquerda, vamos colocar ele de volta)
# Transformamos em texto (str) e pedimos para preencher com zeros (zfill) até ter 8 números
df['NCM_Corrigido'] = df['Código NCM'].astype(str).str.zfill(8)

# 3. Criando a coluna Inteligente de Categoria
def classificar_carne(ncm):
    if ncm.startswith('0203'):
        return 'Carne Suína'
    elif ncm.startswith('0207'):
        return 'Carne de Aves'
    elif ncm.startswith('0201') or ncm.startswith('0202'):
        return 'Carne Bovina'
    else:
        return 'Outras Carnes e Miudezas'

df['Categoria de Carne'] = df['NCM_Corrigido'].apply(classificar_carne)

# 4. Selecionando apenas as colunas de Ouro para o Power BI
df_powerbi = df[[
    'Ano',
    'Países',
    'Categoria de Carne',
    'Valor US$ FOB',
    'Quilograma Líquido'
]].copy()

# Renomeando as colunas para ficarem elegantes no Dashboard
df_powerbi.rename(columns={
    'Países': 'País de Destino',
    'Valor US$ FOB': 'Faturamento (US$)',
    'Quilograma Líquido': 'Volume (Kg)'
}, inplace=True)

# 5. Exportando a base final limpa e pronta para o Power BI
# Usamos 'utf-8-sig' para garantir que os acentos fiquem perfeitos no Power BI
nome_arquivo = 'base_pronta_powerbi.csv'
df_powerbi.to_csv(nome_arquivo, index=False, sep=';', encoding='utf-8-sig')

print(f"\nSucesso! Arquivo limpo gerado: {nome_arquivo}")
print("\n--- VEJA COMO FICOU A BASE DE DADOS AGORA ---")
print(df_powerbi.head())