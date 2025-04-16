import sys
import time
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import json

# Calculando tempo de execução
start_time = datetime.now()

# Saída do Script
saida = ""

# Grava as saídas do console em um txt e mostra a saída no console.
def grava_saida(msg):
    global saida
    saida += msg + '\n'
    #print(msg)
    f = open('log_' + time.strftime(" dia %d-%m-%Y") + '.txt','w', encoding='utf-8')
    print(saida, file=f)

# Mensagem de Finalização
def mensagem_finalizacao():
    global start_time  
    grava_saida("\nScript finalizado em" + time.strftime(" dia %d/%m/%Y às %Hh %Mm"))
    end_time = datetime.now()
    grava_saida('\nDuração: {}'.format(end_time - start_time))


# Mensagem de Inicialização
grava_saida("Script iniciado em " + time.strftime(" dia %d/%m/%Y às %Hh %Mm"))

try:
    # Cliando 300x no botão de gerar....
    for i in range(0, 10000):
        
        url = 'https://www.4devs.com.br/ferramentas_online.php'
        myobj = {'acao': 'gerar_veiculo', 'pontuacao': 'S', 'estado': '', 'fipe_codigo_marca': ''}

        x = requests.post(url, data = myobj)

        soup = BeautifulSoup(x.text, 'html.parser')

        marca = soup.find('input', {'id': 'marca'}).get('value')
        modelo = soup.find('input', {'id': 'modelo'}).get('value')
        ano = soup.find('input', {'id': 'ano'}).get('value')
        renavan = soup.find('input', {'id': 'renavam'}).get('value')
        placa = soup.find('input', {'id': 'placa_veiculo'}).get('value')
        cor = soup.find('input', {'id': 'cor'}).get('value')

        resultado = [
            {
                "marca": marca,
                "modelo": modelo,
                "ano": ano,
                "renavan": renavan,
                "placa": placa,
                "cor": cor
            }
        ]

        grava_saida(json.dumps(resultado, indent=4, ensure_ascii=False))

except Exception as e:
    grava_saida("\n[ERRO] Ocorreu um erro: " + str(e))
    mensagem_finalizacao()

# Gravando log da Inseração
#grava_saida("\n[OK] Gravação do Log concluída.")

# Fim da execução do script
#mensagem_finalizacao()

# Fecha o navegador
#navegador.quit()

sys.exit("\nTérmino do Script.\n")