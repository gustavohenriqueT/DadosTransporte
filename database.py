import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Configuração
numRegistros = 5000
linhasTransporte = ["Linha 101", "Linha 202", "Linha 303", "Linha 404", "Linha 505"]
veiculos = [f"Onibus {i}" for i in range(1, 31)]

# Funções para gerar dados
def gerarDataHora(correta=True):
    inicio = datetime(2024, 3, 1, 5, 0, 0)
    if correta:
        delta = timedelta(minutes=random.randint(0, 30 * 24 * 60))
    else:
        # 10% de chance de data muito antiga ou futura
        if random.random() < 0.1:
            delta = timedelta(days=random.randint(-365, 365))
        else:
            delta = timedelta(minutes=random.randint(-120, 60*24*60))
    return inicio + delta

def gerarLocalizacao(correta=True):
    if correta:
        lat = round(random.uniform(-23.55, -23.60), 6)
        lon = round(random.uniform(-46.63, -46.68), 6)
    else:
        # 5% de chance de localização completamente errada
        if random.random() < 0.05:
            lat = round(random.uniform(-90, 90), 6)
            lon = round(random.uniform(-180, 180), 6)
        else:
            # Localização próxima mas fora da área
            lat = round(random.uniform(-23.50, -23.65), 6)
            lon = round(random.uniform(-46.60, -46.70), 6)
    return lat, lon

def gerarPassageiros(correta=True):
    if correta:
        return random.randint(0, 40)
    else:
        # 5% de chance de valor absurdo
        if random.random() < 0.05:
            return random.randint(100, 200)
        else:
            return random.randint(-10, 50)  # Valores possivelmente errados

def gerarTempoViagem(correta=True):
    if correta:
        return random.randint(10, 90)
    else:
        # 5% de chance de tempo impossível
        if random.random() < 0.05:
            return random.randint(-30, 500)
        else:
            return random.randint(5, 150)

def gerarVeiculo(correta=True):
    if correta:
        return random.choice(veiculos)
    else:
        # 5% de chance de ID inválido
        if random.random() < 0.05:
            return f"Veiculo {random.randint(100, 200)}"
        else:
            return random.choice(veiculos)

def gerarLinha(correta=True):
    if correta:
        return random.choice(linhasTransporte)
    else:
        # 5% de chance de linha inválida
        if random.random() < 0.05:
            return f"Linha {random.randint(600, 700)}"
        else:
            return random.choice(linhasTransporte)

# Gerar dados - cerca de 85% corretos e 15% com problemas
dados = {
    "Data_Hora": [],
    "ID_Veiculo": [],
    "Linha": [],
    "Latitude": [],
    "Longitude": [],
    "Numero_Passageiros": [],
    "Tempo_Viagem_Minutos": [],
    "Dado_Correto": []  # Flag para identificar dados corretos
}

for _ in range(numRegistros):
    # 85% de chance de dado correto, 15% de erro
    correto = random.random() < 0.85
    
    dados["Data_Hora"].append(gerarDataHora(correto))
    dados["ID_Veiculo"].append(gerarVeiculo(correto))
    dados["Linha"].append(gerarLinha(correto))
    
    lat, lon = gerarLocalizacao(correto)
    dados["Latitude"].append(lat)
    dados["Longitude"].append(lon)
    
    dados["Numero_Passageiros"].append(gerarPassageiros(correto))
    dados["Tempo_Viagem_Minutos"].append(gerarTempoViagem(correto))
    dados["Dado_Correto"].append(correto)

# Criar DataFrame
df = pd.DataFrame(dados)

# Converter Data_Hora para datetime e extrair a hora
df["Data_Hora"] = pd.to_datetime(df["Data_Hora"], errors='coerce')  # Coerce para lidar com datas inválidas
df["Hora"] = df["Data_Hora"].dt.hour

# Definir um limiar para horário de pico com base no percentil 75 dos passageiros (apenas dados corretos)
limiar_pico = df[df["Dado_Correto"]]["Numero_Passageiros"].quantile(0.75)

# Criar a coluna target: 1 para horário de pico, 0 caso contrário
df["Horario_Pico"] = (df["Numero_Passageiros"] >= limiar_pico).astype(int)

# Salvar o CSV
df.to_csv("dados_transporte_com_erros.csv", index=False)
print("Dataset 'dadosTransporte.csv' gerado com sucesso!")
print(f"Proporção de dados corretos: {df['Dado_Correto'].mean():.2%}")