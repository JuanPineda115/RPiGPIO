import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.Board)
GPIO.setup(7, GPIO.IN)
GPIO.setup(8, GPIO.IN)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

def Main():
    ciclo = 0
    tiempo1 = 0.5

    if(GPIO,input(7)):
        if(ciclo == 0):
            Secuencia1(tiempo1)
            ciclo += 1
        elif(ciclo == 1):
            Secuencia2(tiempo1)
            ciclo =+1
        elif(ciclo == 2):
            Secuencia3(tiempo1)
            ciclo =+1
        elif(ciclo == 3):
            Secuencia4(tiempo1)
            ciclo =+1
        ##elif(ciclo == 4):
            ##Secuencia5()
            ##ciclo =+1##
        elif(ciclo == 4):
            ciclo = 0


    if(GPIO.input(8)):
        if (tiempo1 > 0.3):
            tiempo1 -= 0.1
        elif(tiempo1 == 0.3):
            tiempo1 = 0.5

def Secuencia1(tiempo):
    GPIO.output(14,GPIO.HIGH)
    time.sleep(tiempo)
    GPIO.output(14, GPIO.LOW)
    time.sleep(tiempo)
    GPIO.output(15,GPIO.HIGH)
    time.sleep(tiempo)
    GPIO.output(15, GPIO.LOW)
    time.sleep(tiempo)
    GPIO.output(18,GPIO.HIGH)
    time.sleep(tiempo)
    GPIO.output(18, GPIO.LOW)
    time.sleep(tiempo)
    GPIO.output(23,GPIO.HIGH)
    time.sleep(tiempo)
    GPIO.output(23, GPIO.LOW)
    time.sleep(tiempo)
    GPIO.output(24,GPIO.HIGH)
    time.sleep(tiempo)
    GPIO.output(24, GPIO.LOW)
    time.sleep(tiempo)

def Secuencia2(tiempo):
    GPIO.output(24,GPIO.HIGH)
    time.sleep(tiempo)
    GPIO.output(24, GPIO.LOW)
    time.sleep(tiempo)
    GPIO.output(23,GPIO.HIGH)
    time.sleep(tiempo)
    GPIO.output(23, GPIO.LOW)
    time.sleep(tiempo)
    GPIO.output(18,GPIO.HIGH)
    time.sleep(tiempo)
    GPIO.output(18, GPIO.LOW)
    time.sleep(tiempo)
    GPIO.output(15,GPIO.HIGH)
    time.sleep(tiempo)
    GPIO.output(15, GPIO.LOW)
    time.sleep(tiempo)
    GPIO.output(14,GPIO.HIGH)
    time.sleep(tiempo)
    GPIO.output(14, GPIO.LOW)
    time.sleep(tiempo)

def Secuencia3(tiempo):
    GPIO.output(14,GPIO.HIGH)
    GPIO.output(24,GPIO.HIGH)
    time.sleep(tiempo)
    GPIO.output(14,GPIO.LOW)
    GPIO.output(24,GPIO.LOW)
    time.sleep(tiempo)
    GPIO.output(15,GPIO.HIGH)
    GPIO.output(23,GPIO.HIGH)
    time.sleep(tiempo)
    GPIO.output(15,GPIO.LOW)
    GPIO.output(23,GPIO.LOW)
    time.sleep(tiempo)
    GPIO.output(18,GPIO.HIGH)
    time.sleep(tiempo)
    GPIO.output(18,GPIO.LOW)
    time.sleep(tiempo)
    
def Secuencia4(tiempo):
    GPIO.output(14,GPIO.HIGH)
    GPIO.putput(15,GPIO.HIGH)
    time.sleep(tiempo)
    GPIO.output(14,GPIO.LOW)
    GPIO.output(15,GPIO.LOW)
    time.sleep(tiempo)
    GPIO.output(23,GPIO.HIGH)
    GPIO.output(24,GPIO.HIGH)
    time.sleep(tiempo)
    GPIO.output(23,GPIO.LOW)
    GPIO.output(24,GPIO.LOW)
    time.sleep(tiempo)
    GPIO.output(18,GPIO.HIGH)
    time.sleep(tiempo)
    GPIO.output(18,GPIO.LOW)
    time.sleep(tiempo)

while True:
    Main()