import pandas as pd

# 1. Compilando os dados históricos oficiais (CIDASC/Epagri)
dados_sanitarios = {
    'Ano': [2019, 2020, 2021, 2022, 2023, 2024],
    'Status Febre Aftosa': ['Livre sem vacinação', 'Livre sem vacinação', 'Livre sem vacinação', 'Livre sem vacinação', 'Livre sem vacinação', 'Livre sem vacinação'],
    'Marco Sanitario / Comercial': [
        'SC consolida liderança isolada em sanidade animal no Brasil.',
        'Explosão de demanda da Ásia; SC absorve por ter barreiras sanitárias intactas.',
        'Certificação internacional reforçada como Zona Livre de Peste Suína Clássica.',
        'Auditorias internacionais aprovadas; abertura de novos mercados premium.',
        'Contenção exemplar de Gripe Aviária (focos isolados, sem afetar granjas comerciais).',
        'Manutenção do status premium e contratos renovados com Japão e China.'
    ]
}

df_sanitario = pd.DataFrame(dados_sanitarios)

# 2. Exportando a tabela de contexto
nome_arquivo = 'marcos_sanitarios_cidasc.csv'
df_sanitario.to_csv(nome_arquivo, index=False, sep=';', encoding='utf-8-sig')

print(f"Sucesso! Tabela de contexto gerada: {nome_arquivo}")
print(df_sanitario)