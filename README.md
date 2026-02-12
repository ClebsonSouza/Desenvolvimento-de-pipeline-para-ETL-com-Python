### 📊 Pipeline ETL – PIB Brasileiro (BCB → MySQL)
🚀 Visão Geral
Este projeto implementa um Pipeline de Dados em Python para extração, transformação e carga (ETL) do PIB brasileiro a partir da API do Banco Central do Brasil (BCB), armazenando os dados em um banco MySQL para posterior análise e visualização.
O objetivo principal é:

🔹 Automatizar a coleta e processamento de dados econômicos
🔹 Reduzir erros humanos
🔹 Aumentar produtividade
🔹 Criar uma base estruturada para dashboards e análises


🏗️ Arquitetura do Projeto
O projeto segue uma arquitetura modular, dividida em 4 camadas:
📦 projeto_pib
 ├── extract.py      # Extração dos dados via API
 ├── transform.py    # Limpeza e transformação
 ├── load.py         # Carga no MySQL
 ├── pipeline.py     # Orquestração do processo
 └── banco_economia.sql  # Script de criação do banco

🔄 Fluxo do Pipeline


Extract → Coleta dados da API do Banco Central


Transform → Padroniza, trata e organiza os dados


Load → Insere dados no MySQL


Orquestração → pipeline.py executa tudo automaticamente



📈 Resultado Final
O pipeline alimenta um banco estruturado que permite:


Construção de dashboards


Análise histórica do PIB


Indicadores acumulados


Métricas estatísticas (média, máximo, mínimo)


Integração com Power BI, Streamlit ou outras ferramentas


Exemplo de visualização gerada a partir dos dados:


🎯 Ganhos de Produtividade
Antes do pipeline:


Coleta manual de dados


Download de planilhas


Tratamento manual no Excel


Inserção manual no banco


Alto risco de erro de digitação


Processo repetitivo e demorado


Depois do pipeline:
✅ Atualização com 1 comando
✅ Processo automatizado
✅ Código reutilizável
✅ Padronização do fluxo
✅ Integração direta com banco de dados
✅ Escalável para novos indicadores

🛡️ Redução de Erro Humano
A automação reduz drasticamente:


❌ Erros de digitação


❌ Inconsistência de datas


❌ Problemas de formatação


❌ Inserções duplicadas


❌ Alterações manuais indevidas


Como isso acontece?
✔ Transformações são feitas via código
✔ Tipos de dados são definidos programaticamente
✔ Banco possui estrutura controlada
✔ Processo é reproduzível
Isso aumenta:


Confiabilidade dos dados


Governança


Rastreabilidade



🧠 Conceito Técnico Aplicado
Este projeto aplica conceitos fundamentais de Engenharia de Dados:


ETL (Extract, Transform, Load)


Modularização de código


Integração com APIs


Integração com banco relacional


Separação de responsabilidades


Reprodutibilidade


Automação de pipeline



🛠️ Tecnologias Utilizadas


Python 3.x


Pandas


Requests


SQLAlchemy


MySQL


API Banco Central (BCB SGS)



⚙️ Como Executar
1️⃣ Criar banco
Execute o script:
banco_economia.sql

2️⃣ Instalar dependências
pip install pandas requests sqlalchemy pymysql

3️⃣ Executar o pipeline
python pipeline.py


📊 Possíveis Expansões
O pipeline pode facilmente ser expandido para:


IPCA


SELIC


Taxa de desemprego


Dólar


Múltiplas séries econômicas


Agendamento automático (cron job)


Integração com Airflow



💡 Valor Profissional do Projeto
Este projeto demonstra:


Capacidade de estruturar pipelines reais


Integração entre sistemas


Pensamento em automação


Redução de risco operacional


Organização profissional de código


Prática de Engenharia de Dados


Ele pode ser apresentado como:


Projeto de portfólio


Case de automação


Demonstração de ETL


Base para dashboards econômicos



📌 Conclusão
Este projeto vai além de um simples script.
Ele representa:

🔹 Automação inteligente
🔹 Organização de dados
🔹 Redução de risco
🔹 Aumento de produtividade
🔹 Aplicação real de engenharia de dados
