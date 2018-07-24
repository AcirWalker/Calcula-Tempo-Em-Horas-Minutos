#Recebendo o valor das horas e minutos nas variáveis.
hora_inicio, minuto_inicio, hora_final, minuto_final = [int(x) for x in input().split()]

#Calculando a hora total
hora_total = hora_final - hora_inicio

if(hora_total < 0):
  hora_total = 24 + (hora_final - hora_inicio)

#Calculando o total de minutos
minuto_total = minuto_final - minuto_inicio

if(minuto_total < 0):
  minuto_total = 60 + (minuto_final - minuto_inicio)
  hora_total -= 1

#Exibindo o resultado.
if(hora_inicio == hora_final and minuto_inicio == minuto_final):
  print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
  print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(hora_total, minuto_total))
