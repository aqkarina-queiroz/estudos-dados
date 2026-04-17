# 📊 Case: Análise de Evolução do NPS — Canais Digitais PJ

## Contexto do projeto

Este projeto foi desenvolvido como case técnico para processo seletivo de **Analista de Dados Pleno**, com prazo de entrega definido. O desafio era analisar a experiência de clientes PJ em canais digitais a partir de uma base real em CSV, combinando indicadores quantitativos de NPS com análise qualitativa de verbatims (comentários dos clientes).

## Problema de negócio

> *O NPS do canal Internet Banking está evoluindo de forma consistente? Quais temas nos verbatims explicam as variações? O que pode ser feito para alavancar a satisfação dos clientes?*

## O que foi feito

- Leitura e tratamento da base CSV com encoding latin1 e separador `;`
- Criação de função para conversão de classificação NPS (PROMOTOR, NEUTRO, DETRATOR) em valores numéricos
- Cálculo do NPS médio por **safra** (período) e por **canal digital**
- Análise de frequência dos **temas citados nos verbatims**
- Comparação de temas entre **detratores e promotores**
- Identificação das safras de maior e menor NPS
- Cálculo da taxa de clientes que deixaram comentário

## Principais resultados

| Indicador | Resultado |
|---|---|
| Safra com maior NPS | 202301 (NPS: 8,3) |
| Safra com menor NPS | 202303 (NPS: -10,1) |
| Taxa de comentários | 23,2% dos respondentes |
| Tema mais citado | Atendimento/Relacionamento (263 menções) |
| Principal tema de detratores | Outros / Usabilidade/Navegabilidade |
| Principal tema de promotores | Atendimento/Relacionamento |

## Principais insights

- O NPS apresentou **volatilidade significativa** entre safras, com queda acentuada em 202303 e recuperação parcial em 202305
- **Atendimento e Relacionamento** é o tema dominante tanto para promotores quanto para detratores — indicando que a qualidade do atendimento humano é o principal driver de satisfação e insatisfação
- **Usabilidade e Navegabilidade** aparece como segundo tema mais relevante, sinalizando oportunidade de melhoria na experiência digital
- Apenas 23,2% dos clientes deixam comentários — há espaço para estratégias de aumento de engajamento na pesquisa

## Recomendações

1. Investigar o que ocorreu na safra 202303 — eventos operacionais ou de produto que possam ter impactado a experiência
2. Priorizar iniciativas de melhoria em **usabilidade do Internet Banking**, dado o volume de menções negativas
3. Criar programa de reconhecimento e capacitação para atendimento, principal alavanca de NPS positivo
4. Aumentar taxa de comentários com incentivos ou simplificação do formulário de pesquisa

## Tecnologias utilizadas

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-2.2-lightblue?logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.10-orange)
![Seaborn](https://img.shields.io/badge/Seaborn-0.13-teal)
![Google Colab](https://img.shields.io/badge/Google%20Colab-notebook-yellow?logo=googlecolab)

## Arquivos do projeto

| Arquivo | Descrição |
|---|---|
| `case_nps_karina.ipynb` | Notebook com análise completa e visualizações |
| `case_nps_karina.py` | Script Python equivalente |
| `dashboard_nps.py` | Dashboard interativo (Streamlit) |
| `Case NPS - Karina_Queiroz.pptx` | Apresentação executiva com resumo dos achados |

---

*Projeto desenvolvido em outubro/2024 como entrega técnica para processo seletivo.*
