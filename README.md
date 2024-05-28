# Análise de Logs de Acesso do Portal de Internet

Programa em Python que analisa os logs de acesso de um portal de internet. Utilizando um arquivo de log do Apache, o programa extrai e analisa informações como data de acesso, URL acessada, status do acesso e identificador de usuário. No final, o programa gera um relatório detalhado com base nesses dados.

## Funcionalidades

1. **Leitura e Análise do Arquivo**
    - O programa lê o arquivo de log e extrai as informações relevantes de cada linha para gerar os relatórios solicitados. Cada arquivo de log contém registros de acessos por dia, indicado pelo nome do arquivo.

2. **Geração de Relatórios**
    1. **Relatório Diário de Acessos:**
        - Calcula e exibe a quantidade total de acessos por dia.
    2. **Tempo Médio de Resposta:**
        - Calcula o tempo médio de resposta do servidor.
    3. **Usuários Mais Ativos:**
        - Identifica e lista os usuários que mais acessaram o portal no período dos logs fornecidos.
    4. **Páginas Mais Acessadas:**
        - Determina quais páginas tiveram mais acessos no log, verificando a URL com maior quantidade de acessos.

