import matplotlib.pyplot as plt 
import numpy as np
import os


def gerar_graficos(file_AM, file_PM, flag, n_span, n_km, n_canais):

    plt.rcParams.update({'figure.max_open_warning': 0})

    espacamento =  (max(file_AM) - min(file_PM)) * 0.20
    menor_valor = min(min(file_AM), min(file_PM)) - espacamento
    maior_valor = max(max(file_AM), max(file_PM)) + espacamento

    print(n_span)

    if n_km == '1':
        n_km = '11'
    if n_canais == '4':
        x = np.arange(192.1, 196.1, 0.1)
    if n_canais == '8':
        x = np.arange(192.1, 196.1 ,0.05)
    
    lightGray = "#404040"
    fig = plt.figure(figsize=(10, 7))
    
    plot1 = fig.add_subplot()
    plot1 = plt.subplot()
    plot1.grid(True, linestyle=':', linewidth=0.5)
    plot1.scatter(x, file_PM, color= 'blue', label = 'Power Mask GNPy', linewidth=0.5, edgecolors='azure')
    plt.plot(x,file_PM,color='purple', alpha=0.5) # antes tava azure mas o fundo é claro agora
    plot1.scatter(x, file_AM, color= 'gold', label = 'Advanced Model GNPy', linewidth=0.5, edgecolors='orange')
    plot1.tick_params(labelsize=14) ##
    plt.plot(x,file_AM,color='red', alpha=0.5)
    plt.ylim(menor_valor, maior_valor)
    plot1.set_ylabel(flag + ' (dB)\n', fontsize=16)
    plot1.set_title(flag + ' (dB)' + n_canais + '0 ch - ' + n_span + ' Span ' + n_km + '0Km\n', fontsize = 16)
    plot1.set_xlabel('\nFrequency Channel (THz)', fontsize=16)
    plot1.legend(prop = { "size": 16 })
    #plot1.set_facecolor(lightGray) #para deixar com fundo cinza
    #plt.subplots_adjust(left=0.1, bottom=0.1,  right=0.9,  top=0.9, wspace=0.4,  hspace=0.4) 

    ##### Para deixar versão png desmarcar linha 46 e marcar linha 45 e desmarcar linha 51 e marcar linha 50

    current_path = os.path.dirname(os.path.realpath(__file__))
    directory_path = current_path + "/graficos_gerados_pdf/"
    #directory_path = current_path + "/graficos_gerados_png/"

    print(directory_path)
    nome = 'Grafico_' + flag + '_' + n_canais + '0ch_' + n_span + '_Span_' + n_km + '0Km'
    Image = plt.savefig(f'{directory_path}/{nome}.pdf')
    #Image = plt.savefig(f'{directory_path}/{nome}.png')                
    plt.close()
