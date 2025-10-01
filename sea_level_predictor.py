# Importa as bibliotecas necessárias
import pandas as pd                  # Para manipulação de dados em DataFrame
import matplotlib.pyplot as plt      # Para gerar gráficos
from scipy.stats import linregress   # Para calcular regressão linear

# Função principal que cria o gráfico
def draw_plot():
    # Importa os dados do arquivo CSV (contém medidas do nível do mar ao longo dos anos)
    df = pd.read_csv('epa-sea-level.csv')

    # Cria o gráfico de dispersão (scatter plot) com os pontos originais
    x = df['Year']                           # Anos
    y = df['CSIRO Adjusted Sea Level']       # Nível do mar ajustado
    plt.scatter(x, y)                        # Plota pontos no gráfico

    # ---- Primeira linha de regressão (usando TODOS os dados disponíveis) ----
    slope, intercept, r_value, p_value, std_err = linregress(x, y)  
    # slope = inclinação da reta, intercept = intercepto no eixo Y
    # r_value, p_value e std_err são métricas estatísticas (não usadas no gráfico aqui)

    years_extended = pd.Series(range(1880, 2051))  # Gera anos de 1880 até 2050
    plt.plot(years_extended, intercept + slope * years_extended, 'r', 
             label='Best fit: 1880-2050')         # Plota a reta de regressão em vermelho

    # ---- Segunda linha de regressão (apenas com dados desde o ano 2000) ----
    df_recent = df[df['Year'] >= 2000]            # Filtra apenas dados recentes
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(
        df_recent['Year'], df_recent['CSIRO Adjusted Sea Level']
    )

    years_recent = pd.Series(range(2000, 2051))   # Anos de 2000 até 2050
    plt.plot(years_recent, intercept2 + slope2 * years_recent, 'g', 
             label='Best fit: 2000-2050')        # Plota reta de regressão em verde

    # ---- Personalização do gráfico ----
    plt.xlabel('Year')                           # Rótulo eixo X
    plt.ylabel('Sea Level (inches)')             # Rótulo eixo Y
    plt.title('Rise in Sea Level')               # Título do gráfico
    plt.legend()                                 # Exibe legenda das linhas

    # ---- Salva a figura em arquivo ----
    plt.savefig('sea_level_plot.png')

    # Retorna o objeto dos eixos atuais (gca = get current axis)
    return plt.gca()
