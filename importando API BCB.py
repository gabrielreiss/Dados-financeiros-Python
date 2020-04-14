import pandas as pd
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
import yfinance as yf

import matplotlib
matplotlib.rcParams['figure.figsize'] = (16,8)

def consulta_bc(codigo_bcb):
    url = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato=json'.format(codigo_bcb)
    df = pd.read_json(url)
    df['data'] = pd.to_datetime(df['data'], dayfirst = True)
    df.set_index('data', inplace = True)
    return df

data_inicio = '1994-07-01'


ipca = consulta_bc(433)
ipca_acumulado = (1 + ipca[ ipca.index >= data_inicio ]).cumprod()
ipca_acumulado.iloc[0] = 1

ibov = yf.download(tickers = '^BVSP')[['Adj Close']]
ibov_retorno = ibov.pct_change()
ibov_retono_acumulado = (1 + ibov_retorno[ ibov_retorno.index >= data_inicio ]).cumprod()
ibov_retono_acumulado.iloc[0] = 1

cdi = consulta_bc(12)
cdi_acumulado = (1 + cdi[ cdi.index >= data_inicio ] / 100).cumprod()
cdi_acumulado.iloc[0] = 1


fig, ax = plt.subplots()
ax.plot(ibov_retono_acumulado)
ax.plot(cdi_acumulado);
#plt.show()