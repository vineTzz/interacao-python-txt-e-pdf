# Abrir arquivo #
alunos = open(r'C:\Users\alxia\OneDrive\Área de Trabalho\github\Integração python + txt e pdf\alunos.txt', 'r')

# Transformar arquivo em Lista #
linhas = alunos.readlines()
del linhas [:4]

# Criar Rastreios de Indicadores #
site = 0
youtube = 0
instragram = 0
facebook = 0
tot_anuncios = 0
tot_org = 0

# Percorrer a Lista #
for linha in linhas:
    if '_org' in linha:
        tot_org += 1

        if 'hashtag_site_org' in linha:
            site += 1
        if 'hashtag_yt_org' in linha:
            youtube += 1
        if 'hashtag_ig_org' in linha:
            instragram += 1
        if 'hashtag_igfb_org' in linha:
            facebook += 1
    else:
        tot_anuncios += 1

alunos.close()

# Criar Arquivo de Indicadores #
with open(r'C:\Users\alxia\OneDrive\Área de Trabalho\github\Integração python + txt e pdf\Indicadores.txt', 'w') as indicadores:
    indicadores.write(f'Quantidade De Anuncios: {tot_anuncios}\n')
    indicadores.write(f'Quantidade Organicos: {tot_org}\n')
    indicadores.write(f'Quantidade Youtube: {youtube}\n')
    indicadores.write(f'Quantidade Instagram: {instragram}\n')
    indicadores.write(f'Quantidade Facebook: {facebook}\n')
    indicadores.write(f'Quantidade Site: {site}\n')
print('Fim Codigo')

