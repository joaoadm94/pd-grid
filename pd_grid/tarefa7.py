import mesa
# importa o modelo de simulação desenvolvido
from model import PdGrid
import numpy as np

# inicio do design do experiments

# definição das variáveis dos experimentos 
# que serão controladas (valor fixo) ou manipuladas
#params = {"N": 200, "width": 10, "height": 10, "D": np.arange(0, 1, 0.2)}
params = {"defect_multiplier": range(12,22,1), "width": 50, "height": 50, "schedule_type": "Simultaneous", "payoffs": None, "seed": None}


# define a quantidade de experimentos 
# que serão repetidos para cada configuração de valores
# para as variáveis (de controle e independentes) 
experiments_per_parameter_configuration = 30

# quantidade de passos suficientes para que a simulação
# alcance um estado de equilíbrio (steady state)
max_steps_per_simulation = 100

# executa a simulacoes / experimentos, e coleta dados em memória 
results = mesa.batch_run(
    PdGrid,
    parameters=params,
    iterations=experiments_per_parameter_configuration,
    max_steps=max_steps_per_simulation,
    data_collection_period=-1,
    display_progress=True,
)

import pandas as pd

# converte os dados das simulações em planilhas (dataframes)
results_df = pd.DataFrame(results)

# gera uma string com data e hora
from datetime import datetime
now = str(datetime.now()).replace(":","-").replace(" ","-")

# define um prefixo para o nome do arquivo que vai guardar os dados do modelo
# contendo alguns dados dos experimentos
file_name_suffix =  ("_iter_"+str(experiments_per_parameter_configuration)+
                     "_steps_"+str(max_steps_per_simulation)+"_"+
                  now)

# define um prefixo para o nome para o arquivo de dados
model_name_preffix = "PdGridCustomModel"

# define o nome do arquivo
file_name = model_name_preffix+"_model_data"+file_name_suffix+".csv"

results_df.to_csv(file_name)
