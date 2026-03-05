# 📊 Inteligência de Exportações: Agronegócio SC

![Status](https://img.shields.io/badge/Status-Concluído-success)
![Power BI](https://img.shields.io/badge/Power_BI-Dashboard-F2C811?logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-ETL-3776AB?logo=python&logoColor=white)

## 🎯 O Projeto
Uma análise de dados ponta a ponta sobre o impacto do status sanitário (Zona Livre de Febre Aftosa sem vacinação) no faturamento de exportações de proteína animal do estado de Santa Catarina entre os anos de 2019 e 2024.

## 💼 Visão de Negócio
Santa Catarina é um gigante global na exportação de carnes, mas a manutenção desse mercado bilionário depende de barreiras sanitárias rigorosas. O objetivo deste projeto foi cruzar dados financeiros brutos com marcos de controle de doenças para provar, visualmente, que **segurança sanitária se traduz diretamente em receita e abertura de mercados premium** (como Japão e China).

## 🛠️ Tecnologias e Arquitetura
* **Python (Pandas):** Responsável pelo processo de ETL (Extração, Transformação e Carga).
* **Power BI:** Modelagem relacional (Star Schema) e design do painel de inteligência de negócios.
* **Fontes de Dados (Dados Abertos):** Comex Stat (Governo Federal) e CIDASC.

## 🧠 Pipeline de Dados (O que foi feito)
1. **Extração:** Coleta da série histórica de exportações (NCMs do Capítulo 02) filtrados exclusivamente para o estado de SC.
2. **Faxina de Dados (Python):** - Remoção de resíduos de formatação do sistema do governo (`\r`).
   - Padronização de códigos NCM (reinserção de zeros à esquerda).
   - Criação de função de categorização dinâmica (Suínos, Aves, Bovinos).
3. **Contexto de Negócio:** Criação de uma tabela de dimensão via script contendo o histórico de certificações da CIDASC.
4. **Modelagem e UX (Power BI):** Relacionamento unidirecional entre fato e dimensão, aplicação de DAX básico para formatação financeira e design visual com fundo escuro (Executive Dashboard).

## 🚀 Como explorar este repositório
- O script de limpeza de dados está no arquivo `analise.py`.
- O painel interativo completo está no arquivo `.pbix`. Para visualizá-lo e interagir com o mapa-múndi de calor, basta fazer o download e abri-lo no [Power BI Desktop](https://powerbi.microsoft.com/desktop/).

---
Desenvolvido com ☕ por **Thiago Ramiro** - [Acessar meu Portfólio](https://seu-link-aqui.com)