import math

tempo_rede = 0.09  # em segundos
tempo_transferencia = 0.01  # em segundos
tempo_completar_dom = 2.88  # em segundos
tempo_carga_pagina = 4.28  # em segundos
tempo_servidor = 0.04  # em segundos
tempo_processamento_dom = 1.27  # em segundos
tempo_carga = 0.008  # em segundos
#performance_lighthouse = 43.0  # % de performance

# Máximos ideais
max_tempo_rede = 0.1  # Tempo máximo ideal para a rede (em segundos)
max_tempo_servidor = 0.1 # Tempo máximo ideal para resposta do servidor (em segundos)
max_temp_transf = 0.05  # Tempo máximo ideal para transferência (em segundos)
max_tempo_process_dom = 1.5  # Tempo máximo ideal para processamento do DOM (em segundos)
max_temp_comp_dom = 2  # Tempo máximo ideal para completar o DOM (em segundos)
max_tempo_carga = 2  # Tempo máximo ideal para a carga de elementos (em segundos)
max_temp_carga_pag = 4  # Tempo máximo ideal para a carga da página (em segundos)

# Função de normalização logarítmica
def normalizar_log(tempo, max_tempo):
    # Evitar divisão por zero
    if tempo == 0:
        return 0
    # Normalização logarítmica
    return max(0, (math.log(tempo) / math.log(max_tempo)) * 100)

# Normalização das métricas (quanto menor o tempo, melhor)
normalizado_tempo_rede = normalizar_log(tempo_rede, max_tempo_rede)
normalizado_tempo_transferencia = normalizar_log(tempo_transferencia, max_temp_transf)
normalizado_tempo_completar_dom = normalizar_log(tempo_completar_dom, max_temp_comp_dom)
normalizado_tempo_carga_pagina = normalizar_log(tempo_carga_pagina, max_temp_carga_pag)
normalizado_tempo_servidor = normalizar_log(tempo_servidor, max_tempo_servidor)
normalizado_tempo_processamento_dom = normalizar_log(tempo_processamento_dom, max_tempo_process_dom)
normalizado_tempo_carga = normalizar_log(tempo_carga, max_tempo_carga)

# Cálculo da média simples
total_metrica_normalizada = (
    normalizado_tempo_rede +
    normalizado_tempo_transferencia +
    normalizado_tempo_completar_dom +
    normalizado_tempo_carga_pagina +
    normalizado_tempo_servidor +
    normalizado_tempo_processamento_dom +
    normalizado_tempo_carga
)

# Número total de métricas
num_metricas = 7

# Média simples
media_desempenho = total_metrica_normalizada / num_metricas

# Mostrar os valores de cada métrica
print(f"Tempo de Rede Normalizado: {normalizado_tempo_rede:.2f}%")
print(f"Tempo de Transferência Normalizado: {normalizado_tempo_transferencia:.2f}%")
print(f"Tempo para Completar DOM Normalizado: {normalizado_tempo_completar_dom:.2f}%")
print(f"Tempo de Carga da Página Normalizado: {normalizado_tempo_carga_pagina:.2f}%")
print(f"Tempo de Servidor Normalizado: {normalizado_tempo_servidor:.2f}%")
print(f"Tempo de Processamento do DOM Normalizado: {normalizado_tempo_processamento_dom:.2f}%")
print(f"Tempo de Carga Normalizado: {normalizado_tempo_carga:.2f}%")
print(f"Média de Desempenho: {media_desempenho:.2f}%")
