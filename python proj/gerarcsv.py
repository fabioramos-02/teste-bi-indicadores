import pandas as pd

# Dados fornecidos
data = {
    "ORGÃO": [
        "DETRAN", "PORTAL ÚNICO MS", "SEFAZ", "AGENCIADENOTICIAS", "SED", "NOTA PREMIADA", "SEJUSP", "SES",
        "SEAD", "JUCEMS", "AGEPEN", "SEMADESC", "IMASUL", "CBMMS", "IMPRENSA OFICIAL", "CGP", "SAD", 
        "BIO PARQUE PANTANAL", "FUNTRAB", "HOSPITAL REGIONAL", "POLICIA CIVIL", "NÃO SE CALE", "SETDIG", 
        "CONCURSOS", "AGRAER", "IAGRO", "PGE"
    ],
    "SITE": [
        "https://www.detran.ms.gov.br/", "https://www.ms.gov.br/", "https://www.sefaz.ms.gov.br/", 
        "https://agenciadenoticias.ms.gov.br/", "https://www.sed.ms.gov.br/", "https://www.notamspremiada.ms.gov.br/", 
        "https://www.sejusp.ms.gov.br/", "http://www.saude.ms.gov.br/", "https://www.sead.ms.gov.br/", 
        "http://www.jucems.ms.gov.br/", "https://www.agepen.ms.gov.br/", "https://www.semadesc.ms.gov.br/", 
        "http://www.imasul.ms.gov.br/", "https://www.bombeiros.ms.gov.br/", "http://www.imprensaoficial.ms.gov.br/", 
        "https://www.cgp.sejusp.ms.gov.br/", "http://www.sad.ms.gov.br/", "https://bioparquepantanal.ms.gov.br/", 
        "http://www.funtrab.ms.gov.br/", "https://www.hospitalregional.ms.gov.br/", "http://www.pc.ms.gov.br/", 
        "http://www.naosecale.ms.gov.br/", "https://www.setdig.ms.gov.br/", "http://www.concursos.ms.gov.br/", 
        "http://www.agraer.ms.gov.br/", "https://www.iagro.ms.gov.br/", "http://www.pge.ms.gov.br/"
    ],
    "VISITAS EM 2024": [
        5348991, 3801433, 2996171, 2323478, 2112150, 1788571, 1542250, 1172860, 932177, 907766, 847247, 818590, 
        619725, 568806, 491883, 488928, 479562, 474066, 430864, 420614, 388852, 359535, 356742, 326995, 316629, 
        282101, 280273
    ]
}

# Criação do DataFrame
df = pd.DataFrame(data)

# Salvar o DataFrame como um arquivo CSV
file_path = 'visitas_2024.csv'
df.to_csv(file_path, index=False)

file_path
