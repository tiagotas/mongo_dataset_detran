import sys
import time
from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException 
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.options import Options

# Calculando tempo de execução
start_time = datetime.now()

# Saída do Script
saida = ""

# Grava as saídas do console em um txt e mostra a saída no console.
def grava_saida(msg):
    global saida
    saida += msg + '\n'
    print(msg)
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

# Opções para Manter o Chrome aberto mesmo após o término
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('log-level=3') # Apenas mensagens de erro

# Inicializando o Navegador
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=chrome_options)
navegador.delete_all_cookies() # Remove Todos os Cookies Anteriores
navegador.maximize_window()


try:

    navegador.get("https://www.4devs.com.br/gerador_de_pessoas")
    grava_saida("[OK] Página do gerador acessada com sucesso.")
    navegador.find_element('xpath', '//*[@id="txt_qtde"]').clear()
    navegador.find_element('xpath', '//*[@id="txt_qtde"]').send_keys("30")

    # Cliando 500x no botão de gerar....
    for i in range(0, 500):
        navegador.find_element('xpath', '//*[@id="bt_gerar_pessoa"]').click()
        time.sleep(3)
        pessoas_geradas = navegador.find_element('xpath', '//*[@id="dados_json"]').text
        grava_saida(pessoas_geradas)

except NoSuchElementException as e:
    grava_saida("\n[ERRO] Não foi possível encontrar o XPATH na página:  " + e.msg)
    mensagem_finalizacao()
except WebDriverException as e:
    grava_saida("\n[ERRO] Não foi possível acessar o servidor: " + e.msg)
    mensagem_finalizacao()
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