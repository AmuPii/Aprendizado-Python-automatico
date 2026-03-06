from datetime import datetime, timedelta

data_atual = datetime.now()
data_futura = datetime(data_atual.year, 12, 31)
dias_faltando = (data_futura - data_atual).days
print("Faltam ", dias_faltando, " dias para o dia 31 de dezembro do ano atual.")


#===============================


Data_evento = datetime.strptime(input("Digite a data do evento (DD/MM/YYYY): "), "%d/%m/%Y")
dias_para_evento = (Data_evento - data_atual).days
if dias_para_evento > 0:
    print("Faltam ", dias_para_evento, " dias para o evento Acontecer.")
elif dias_para_evento < 0:
    print("O evento já ocorreu há ", abs(dias_para_evento), " dias.")
else:
    print("O evento é hoje!")

#===============================

data_fabricacao = datetime.strptime(input("Digite a data de fabricação (DD/MM/YYYY): "), "%d/%m/%Y")
data_validade = data_fabricacao + timedelta(days=180)

print("Data de fabricação: ", data_fabricacao.strftime("%d/%m/%Y"))
print("Data de validade: ", data_validade.strftime("%d/%m/%Y"))

if data_atual < data_validade:
    print("O produto está dentro do prazo de validade. e faltam ", (data_validade - data_atual).days, " dias para vencer.")
else:    
    print("O produto está vencido ha ", (data_atual - data_validade).days, " dias.")
