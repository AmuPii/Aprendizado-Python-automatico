from openpyxl import Workbook

arquivo = Workbook()
planilha_atual = arquivo.active
planilha_atual.title = 'Pessoas'

planilha_atual['A1'] = 'Nome'
planilha_atual['B1'] = 'Cidade'

planilha_atual['A2'] = 'João'
planilha_atual['B2'] = 'Recife'

planilha_atual['A3'] = 'Maria'
planilha_atual['B3'] = 'São Paulo'

planilha_atual['A4'] = 'Otávio'
planilha_atual['B4'] = 'Belo Horizonte'

planilha_atual.append(['Letícia', 'Porto Alegre'])
planilha_atual.append(['Gustavo', 'Salvador'])

arquivo.create_sheet('Visitas')
planilhas_visitas = arquivo['Visitas']

planilhas_visitas.append(['data', 'visitante'])
planilhas_visitas.append(['01/01/2025', '134'])
planilhas_visitas.append(['02/01/2025', '156'])

planilhas_visitas['A1'] = '142'
arquivo.save('cadastro.xlsx')

