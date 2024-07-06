import time
import winsound

def tocar_alarme():
    duracao = 1000 # Duração do som em milessegundos ( 1 segundo)
    freq = 440 # Frequencia do som em Hertz
    winsound.Beep(freq, duracao)
    
hora_alarme = int(input("Digite a hora do alarme (formato 24 horas): "))
minuto_alarme = int(input("Digite o minuto do alarme: "))

print(f"Alarme configurado para {hora_alarme:02}:{minuto_alarme:02}")

while True:
    
    hora_atual  = time.localtime().tm_hour
    minuto_atual = time.localtime().tm_min
    
    if hora_atual == hora_alarme and minuto_atual == minuto_alarme:
        print("Hora do alarme")
        tocar_alarme()
        break
    
    time.sleep(60)