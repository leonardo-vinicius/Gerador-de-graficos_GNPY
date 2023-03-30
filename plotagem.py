import os                       
import matplotlib.pyplot as plt 
import numpy as np              
import csv
from PIL import Image
import grafico

current_path = os.path.dirname(os.path.realpath(__file__))

arquivo = []

directory_path = current_path + "/graficos_gerados_csv/"
files = os.listdir(directory_path)

def abrir_arquivo(arquivo_AM, arquivo_PM, n_span, n_km, n_canais):

    CHPout_AM1 = []
    GSNR_AM1 = []

    CHPout_PM1 = []
    GSNR_PM1 = []

    arquivo_AM = directory_path + arquivo_AM 
    arquivo_PM = directory_path + arquivo_PM

    with open(arquivo_AM, mode='r') as arq:
        leitor = csv.reader(arq, delimiter=';')
        linhas = 0
        for coluna in leitor:
            if linhas != 0:
                CHPout_AM1.append((float(coluna[2])))
                GSNR_AM1.append((float(coluna[5])))
            linhas += 1
    print(f'acabou. lidas {linhas} lidas.')

    with open(arquivo_PM, mode='r') as arq:
        leitor = csv.reader(arq, delimiter=';')
        linhas = 0
        for coluna in leitor:
            if linhas != 0:
                CHPout_PM1.append((float(coluna[2])))
                GSNR_PM1.append((float(coluna[5])))
            linhas += 1
    print(f'acabou. lidas {linhas} lidas.\n gerando grafico.')


    grafico.gerar_graficos(CHPout_AM1, CHPout_PM1, 'Channel Power', n_span, n_km, n_canais)
    grafico.gerar_graficos(GSNR_AM1, GSNR_PM1, 'GSNR', n_span, n_km, n_canais)

for file in files:
    arquivo.append(file) 
    name = file

def passar_parametros(chave, valor1, valor2):
    arquivo1 = valor1
    arquivo2 = valor2
    numero_de_canais = len(dic[chave][0]) - 8
    n_canais = valor1[numero_de_canais] # para pegar o n° de canais
    n_span = valor1[0]                  # para pegar o n° de spans
    n_km = valor1[8]                    # para pegar o tamanho em km

    print(f'N KM: {n_km}')
    abrir_arquivo(arquivo1, arquivo2, n_span, n_km, n_canais)


dic = {
            '1_span_70_40': ['1_spans_70.0 Km_new_model_example_40ch.csv', '1_spans_70.0 Km_EDFA_PADTEC_AdvancedModel_40ch.csv'],
            '1_span_70_80': ['1_spans_70.0 Km_new_model_example_80ch.csv', '1_spans_70.0 Km_EDFA_PADTEC_AdvancedModel_80ch.csv'],
            '1_span_90_40': ['1_spans_90.0 Km_new_model_example_40ch.csv', '1_spans_90.0 Km_EDFA_PADTEC_AdvancedModel_40ch.csv'],
            '1_span_90_80': ['1_spans_90.0 Km_new_model_example_80ch.csv', '1_spans_90.0 Km_EDFA_PADTEC_AdvancedModel_80ch.csv'],
            '1_span_110_40': ['1_spans_110.0 Km_new_model_example_40ch.csv', '1_spans_110.0 Km_EDFA_PADTEC_AdvancedModel_40ch.csv'],
            '1_span_110_80': ['1_spans_110.0 Km_new_model_example_80ch.csv', '1_spans_110.0 Km_EDFA_PADTEC_AdvancedModel_80ch.csv'],
            '4_span_70_40': ['4_spans_70.0 Km_new_model_example_40ch.csv', '4_spans_70.0 Km_EDFA_PADTEC_AdvancedModel_40ch.csv'],
            '4_span_70_80': ['4_spans_70.0 Km_new_model_example_80ch.csv', '4_spans_70.0 Km_EDFA_PADTEC_AdvancedModel_80ch.csv'],
            '4_span_90_40': ['4_spans_90.0 Km_new_model_example_40ch.csv', '4_spans_90.0 Km_EDFA_PADTEC_AdvancedModel_40ch.csv'],
            '4_span_90_80': ['4_spans_90.0 Km_new_model_example_80ch.csv', '4_spans_90.0 Km_EDFA_PADTEC_AdvancedModel_80ch.csv'],
            '4_span_110_40': ['4_spans_110.0 Km_new_model_example_40ch.csv', '4_spans_110.0 Km_EDFA_PADTEC_AdvancedModel_40ch.csv'],
            '4_span_110_80': ['4_spans_110.0 Km_new_model_example_80ch.csv', '4_spans_110.0 Km_EDFA_PADTEC_AdvancedModel_80ch.csv']
        }

for chave, valor in dic.items():
    print(f"Chave = {chave} - Valor 1 = {valor[0]} - Valor 2 = {valor[1]}")
    print(f"Gerando grafico...{chave}\n")
    passar_parametros(chave, valor[0], valor[1])
