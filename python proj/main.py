import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Lista de URLs dos sites a serem monitorados
urls = [
    'https://www.ms.gov.br/',
    'https://www.segov.ms.gov.br/',
    'https://www.meudetran.ms.gov.br/',
]

# Configurar o driver do Chrome
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Executar o Chrome em modo headless
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Função para medir o tempo de carregamento da página
def medir_tempo_carregamento(url):
    inicio = time.time()
    driver.get(url)
    fim = time.time()
    tempo_carregamento = fim - inicio
    return tempo_carregamento

# Criar e escrever no arquivo CSV
with open('tempos_carregamento.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Nome do Site', 'Tempo de Carregamento (s)'])
    
    for url in urls:
        tempo = medir_tempo_carregamento(url)
        writer.writerow([url, tempo])

print("Arquivo CSV gerado com sucesso!")