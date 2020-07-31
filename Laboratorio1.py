import RPi.GPIO as GPIO
import time

def Main():
    ciclo = 0
    tiempo1 = 2
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(2, GPIO.IN)
    GPIO.setup(3, GPIO.IN)
    GPIO.setup(21, GPIO.IN)
    GPIO.setup(14, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)

    while True:
        if(GPIO.input(2)==False):
            ciclo +=1
            if(ciclo==1):
                Secuencia1(tiempo1)
            if(ciclo==2):
                Secuencia2(tiempo1)
            if(ciclo==3):
                Secuencia3(tiempo1)
            if(ciclo==4):
                Secuencia4(tiempo1)
            if(ciclo==5):
                ciclo=0
                
                
        if(GPIO.input(3)==False):
            if (tiempo1 > 0.5):
                tiempo1 -= 0.5
            elif(tiempo1==0.5):
                tiempo1=2


                
            
        



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
    GPIO.output(15,GPIO.HIGH)
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
    
def ctiempo(time):
    if(time>0.5):
        time-=-0.5
    if (time==0.5):
        time = 2
    return time


Main()