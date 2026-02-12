# load.py
from sqlalchemy import create_engine
import pandas as pd

def load_pib_to_mysql(df_pib: pd.DataFrame,
                      tabela='pib_mensal',
                      usuario='root',
                      senha='sua_senha', #sua senha do banco
                      host='localhost',
                      porta=3306,
                      banco='economia'):
    
    connection_str = (
        f"mysql+pymysql://{usuario}:{senha}@{host}:{porta}/{banco}"
    )

    engine = create_engine(connection_str)
        
    df_pib.to_sql(tabela, engine, if_exists='replace', index=False)

    print(f"Tabela '{tabela}' atualizada no banco '{banco}'.")