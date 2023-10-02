import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

# Etapa de Extração
def extrair_dados():
    tabela = pd.read_csv('base.csv')
    return tabela

# Etapa de Transformação
def transformar_dados(tabela):
    # Exemplo de transformação: calcular o total de vendas
    total_vendas = tabela['Vendas'].sum()
    return total_vendas

@app.route('/')
def homepage():
    return 'A API está no ar'

@app.route('/etl')
def etl():
    # Extração
    dados_extraidos = extrair_dados()
    
    # Transformação
    resultado_transformacao = transformar_dados(dados_extraidos)
    
    # Carregamento (resposta em formato JSON)
    resposta = {'total_vendas': resultado_transformacao}
    return jsonify(resposta)

app.run(host='0.0.0.0')