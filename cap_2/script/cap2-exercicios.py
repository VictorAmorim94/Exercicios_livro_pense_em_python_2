passo_inicial = (8*60) + 15 #transformandp 00:08:15 em segundos
passo_rapido = (7*60) + 12 # transformando 00:07:60 em segundos 

qtd_km_inicial = 2
qtd_km_rapido = 3 

inicial = passo_inicial* qtd_km_inicial
print('primeiro e ultimo km de 08:15 minutos em segundos: '+ str(inicial))

rapido = passo_rapido * qtd_km_rapido
print('3 km na velocidade de 7:60 minutos em segundos '+ str(rapido))

tempo_total_ida_e_volta = (inicial + rapido) *2 
print('tempo total de ida e volta em segundos: '+ str(tempo_total_ida_e_volta))

horario_em_segundos = (6 * 3600) + (52 * 60) # transformando 06:52:00 em segundos
print('horario inicial em segundos : ' + str(horario_em_segundos))

horario_de_volta_em_segundos = horario_em_segundos + tempo_total_ida_e_volta
print('horario total em segundos: '+ str(horario_de_volta_em_segundos))

hora = int(horario_de_volta_em_segundos / 3600)
resto_hora = horario_de_volta_em_segundos % 3600
minuto = int(resto_hora / 60)
resto_minuto = resto_hora % 60
segundo =  resto_minuto


print('A volta para casa para tomar café da manhã é as : ' + '0'+str(hora)+ ':0'+ str(minuto) + ':'+str(segundo))
