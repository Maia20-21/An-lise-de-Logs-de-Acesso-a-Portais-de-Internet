from collections import Counter

def ler_arquivo(nome_arquivo):
    registros = []
    with open(nome_arquivo, 'r') as arquivo:
        linha = arquivo.readline()
        for linha in arquivo:
            parte = linha.strip().split('\t')
            acesso = {
                 'date': parte[0],
                 'time': parte[1],
                 'cs-method': parte[2],
                 'cs-uri': parte[3],
                 'sc-status': parte[4],
                 'time-taken': parte[5],
                 'c-ip': parte[6],
                 'contentYype': parte[7],
                 'codMensagem': parte[8],
                 'codTransacao': parte[9],
                 'nomUsuarioSistema': parte[10],
            }
            registros.append(acesso)
    return registros

def acessos_diarios(registros):
    datas = []
    for acesso in registros:
        data = acesso['date']
        datas.append(data)
    return len(datas)

def tempo_resposta(registros):
    tempos = []
    for acesso in registros:
        tempo = float(acesso['time-taken'])
        tempos.append(tempo)
    return sum(tempos) / len(tempos)

def usuarios_mais_ativos(registros):
    usuarios = []
    for acesso in registros:
        usuario = acesso['nomUsuarioSistema']
        if usuario != '-':
            usuarios.append(usuario)
    contagem_usuarios = Counter(usuarios)
    mais_ativos = contagem_usuarios.most_common(3)
    return mais_ativos

def pags_mais_acessadas(registros):
    paginas = []
    for acesso in registros:
        pagina = acesso['cs-uri']
        if pagina != '-':
            paginas.append(pagina)
    contagem_paginas = Counter(paginas)
    mais_acessadas = contagem_paginas.most_common(3)
    return mais_acessadas
  
def falhas_momentos(registros):
    falhas_registros = {
        'falha': [],
        'hora': [],
        'tempo_gasto': [],
    }
    for acesso in registros:
        status = int(acesso['sc-status'])
        hora = acesso['time']
        tempo_gasto = float(acesso['time-taken'])
        if status < 200 or status >= 400:
            falhas_registros['falha'].append(status)
            falhas_registros['hora'].append(hora)
            falhas_registros['tempo_gasto'].append(tempo_gasto)
    return falhas_registros

nome_arquivo = input('Digite o nome do arquivo que deseja acessar (DD-MM-AAAA.txt ou nome_do_arquivo.txt): ')
dados = ler_arquivo(nome_arquivo)

print()

print('RELATÓRIO DIÁRIO DE ACESSOS\n')
print(f'Quantidade total de acessos diários: {acessos_diarios(dados)} acessos\n')
print(f'Tempo médio de resposta do servidor: {tempo_resposta(dados):.2f} milissegundos\n')

print('Usuários mais ativos:')
for usuario, acessos in usuarios_mais_ativos(dados):
    print(f'Usuário: {usuario}: {acessos} acessos')
print()

print('Páginas mais acessadas:')
for pagina, acessos in pags_mais_acessadas(dados):
    print(f'Página: {pagina}: {acessos} acessos')
print()

pergunta = input('Deseja conferir em quais momentos do dia em que ocorreram as falhas? (S ou N): ')
if pergunta == 'S' or pergunta == 's':
    print('HORÁRIO DAS FALHAS\n')
    resultados_falhas = falhas_momentos(dados)
    for i in range(len(resultados_falhas['falha'])):
        print(f'Erro: {resultados_falhas["falha"][i]}, Horário: {resultados_falhas["hora"][i]}, Tempo de resposta do servidor: {resultados_falhas["tempo_gasto"][i]} milissegundos')
else: 
    print()

# Obs: para o programa funcionar, é necessário que os arquivos.txt estejam na mesma pasta que o código fonte