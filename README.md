# Análise e Geração de Dados de Transporte

## 📌 Descrição
Projeto de ciência de dados para simulação e tratamento de dados de transporte público, com foco em:
- Geração de dados realistas com erros controlados
- Identificação de padrões operacionais
- Limpeza e preparação de dados para análise

## 🏗️ Geração de Dados

### 📜 Script Python (`gerar_dados.py`)
Gera dataset simulado contendo:

| Coluna | Tipo | Descrição | Emoji |
|--------|------|-----------|-------|
| `Data_Hora` | datetime | Registro temporal | 📅 |
| `ID_Veiculo` | string | Identificação do ônibus | 🚍 | 
| `Linha` | string | Número da linha | 🏷️ |
| `Latitude/Longitude` | float | Coordenadas GPS | 📍 |
| `Numero_Passageiros` | int | Quantidade de passageiros | 👥 |
| `Tempo_Viagem_Minutos` | int | Duração da viagem | ⏳ |
| `Dado_Correto` | bool | Indicador de qualidade | ✅❌ |
| `Horario_Pico` | bool | Período de pico | 🌅🌆 |

**Características especiais**:
- 15% dos dados contêm erros simulados
- Inconsistências em horários e localizações
- Valores atípicos em passageiros e tempos

## 🔍 Análise e Tratamento

### 📊 Script R (`analise_dados_transporte.Rmd`)
Fluxo de processamento:

1. **📥 Importação** 
   - Carregamento do dataset
   - Estatísticas descritivas

2. **🔄 Transformação**
   - Conversão de formatos de data
   - Padronização categóricas (fatores)
   - Tratamento de valores nulos (mediana/moda)

3. **📈 Visualização**
   - Histogramas de distribuição
   - Gráficos temporais
   - Análise de outliers

4. **📤 Exportação**
   - Dataset tratado em CSV
   - Relatório em HTML/PDF

## 🚀 Execução

### 🔧 Pré-requisitos
```bash
# Python
pip install pandas numpy

# R
install.packages(c("dplyr", "ggplot2", "rmarkdown"))
