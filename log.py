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

nome_arquivo = input('Digite o nome do arquivo que deseja acessar: ')
dados = ler_arquivo(nome_arquivo)

print()

print('RELATÓRIO DIÁRIO DE ACESSOS\n')

print(f'Quantidade total de acessos diários: {acessos_diarios(dados)}\n')

print(f'Tempo médio de resposta do servidor: {tempo_resposta(dados):.2f} milissegundos\n')

print('Usuários mais ativos:')
for usuario, acessos in usuarios_mais_ativos(dados):
    print(f'Usuário: {usuario}: {acessos} acessos')

print()

print('Páginas mais acessadas:')
for pagina, acessos in pags_mais_acessadas(dados):
    print(f'Página: {pagina}: {acessos} acessos')
