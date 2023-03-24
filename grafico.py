import matplotlib.pyplot as plt 
import numpy as np
import os


def gerar_graficos(CHPout_AM, CHPout_PM, GSNR_AM, GSNR_PM, n_span, n_km, n_canais):

    espacamento = 0.3
    menor_valorGSNR = min(min(GSNR_AM), min(GSNR_PM)) - espacamento
    maior_valorGSNR = max(max(GSNR_AM), max(GSNR_PM)) + espacamento
    menor_valorPout = min(min(CHPout_AM), min(CHPout_PM)) - espacamento
    maior_valorPout = max(max(CHPout_AM), max(CHPout_PM)) + espacamento

    if n_km == '1':
        n_km = '11'

    if n_canais == '4':
        #print("o numero de canais eh igual a 4")
        x = np.arange(192.1, 196.1, 0.1)
    if n_canais == '8':
        #print("o numero de canais eh igual a 8")
        x = np.arange(192.1, 196.1 ,0.05)
    

    lightGray = "#404040"
    plt.figure(figsize = (15, 7))

    # grafico GSNR
    plot1 = plt.subplot(1, 2, 1)
    plot1.grid(True, linestyle=':', linewidth=0.5)
    plot1.scatter(x, GSNR_PM, color= 'blue', label = 'Power Mask GNPy', linewidth=0.5, edgecolors='azure')
    plt.plot(x,GSNR_PM,color='azure', alpha=0.5)
    plot1.scatter(x, GSNR_AM, color= 'gold', label = 'Advanced Model GNPy', linewidth=0.5, edgecolors='orange')
    plt.plot(x,GSNR_AM,color='red', alpha=0.5)
    plt.ylim(menor_valorGSNR, maior_valorGSNR)
    plot1.set_ylabel('GSNR (dB)\n')
    plot1.set_title('GSNR (dB) - ' + n_canais + '0 ch - ' + n_span + ' Span ' + n_km + '0Km\n')
    plot1.set_xlabel('\nFrequency Channel (THz)')
    plot1.legend()
    #plot1.set_facecolor(lightGray) #para deixar com fundo cinza

    # grafico CHPout
    plot2 = plt.subplot(1, 2, 2)
    plot2.grid(True, linestyle=':', linewidth=0.5)
    plot2.scatter(x, CHPout_PM, color= 'b', label = 'Power Mask GNPy', linewidth=0.5, edgecolors='azure')
    plt.plot(x,CHPout_PM,color='azure', alpha=0.5)
    plot2.scatter(x, CHPout_AM, color= 'gold', label = 'Advanced Model GNPy', linewidth=0.5, edgecolors='orange')
    plt.plot(x,CHPout_AM,color='red', alpha=0.5)
    plt.ylim(menor_valorPout, maior_valorPout)
    plot2.set_ylabel('Channel Power (dB)\n')
    plot2.set_title('CH PowerOut - ' + n_canais + '0 ch - ' + n_span + ' Span ' + n_km + '0Km\n')
    plot2.set_xlabel('\nFrequency Channel (THz)')
    plot2.legend()
    #plot2.set_facecolor(lightGray) #para deixar com fundo cinza

    plt.subplots_adjust(left=0.1, bottom=0.1,  right=0.9,  top=0.9, wspace=0.4,  hspace=0.4) 

    current_path = os.path.dirname(os.path.realpath(__file__))
    directory_path = current_path + "/graficos_gerados_png/"

    print(directory_path)
    nome = 'Grafico_' + n_canais + '0ch_' + n_span + '_Span_' + n_km + '0Km'
    Image = plt.savefig(f'{directory_path}/{nome}.png')
