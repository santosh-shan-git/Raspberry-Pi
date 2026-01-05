##Traffic light
# import RPi.GPIO as GPIO
# import time
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(16, GPIO.OUT)
# GPIO.setup(15, GPIO.OUT)
# GPIO.setup(19, GPIO.OUT)
# GPIO.output(16, GPIO.LOW)
# GPIO.output(15, GPIO.LOW)
# GPIO.output(19, GPIO.LOW)
# time.sleep(1)
# while True:
#     GPIO.output(16, GPIO.HIGH)
#     time.sleep(1)
#     GPIO.output(16,GPIO.LOW)
#     GPIO.output(15, GPIO.HIGH)
#     time.sleep(1)
#     GPIO.output(15,GPIO.LOW)
#     GPIO.output(19, GPIO.HIGH)
#     time.sleep(1)
#     GPIO.output(19,GPIO.LOW)
# GPIO.cleanup()
##End of Traffic Light Code

# import RPi.GPIO as GPIO
# import time
# import random
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(16, GPIO.OUT)
# GPIO.setup(15, GPIO.OUT)
# GPIO.setup(19, GPIO.OUT)
# lst=[16,15,19]
# random.shuffle(lst)
# for v in lst:
#     GPIO.output(v, GPIO.HIGH)
#     time.sleep(1)
# lst.reverse()
# for v in lst:
#     GPIO.output(v,GPIO.LOW)
#     time.sleep(1)
# GPIO.cleanup()

# import RPi.GPIO as GPIO
# import time
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(19, GPIO.OUT)
# var=1
# while True:
#     GPIO.output(19, GPIO.HIGH)
#     time.sleep(var)
#     GPIO.output(19,GPIO.LOW)
#     time.sleep(1)
#     var=var-0.05
#     print(var)
# GPIO.cleanup()

# import RPi.GPIO as GPIO
# import time
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(16, GPIO.OUT)
# GPIO.setup(15, GPIO.OUT)
# GPIO.setup(19, GPIO.OUT)
# GPIO.output(16, GPIO.LOW)
# GPIO.output(15, GPIO.LOW)
# GPIO.output(19, GPIO.LOW)
# dictt={'red':15, 'yel low':19, 'green':16}
# print('pick one of these 3 colors:red, yellow or green.')
# answer=input()
# for v in range(1,11,1):
#     GPIO.output(dictt[answer], GPIO.HIGH)
#     time.sleep(0.5)
#     GPIO.output(dictt[answer],GPIO.LOW)
#     time.sleep(0.25)
# GPIO.cleanup()

# import RPi.GPIO as GPIO
# import time
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(16, GPIO.OUT)
# GPIO.setup(15, GPIO.OUT)
# dictt= { 'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.','F':'..-.', 'G':'--.', 'H':'....','I':'..', 'J':'.---', 'K':'-.-',
#                     'L':'.-..', 'M':'--', 'N':'-.',
#                     'O':'---', 'P':'.--.', 'Q':'--.-',
#                     'R':'.-.', 'S':'...', 'T':'-',
#                     'U':'..-', 'V':'...-', 'W':'.--',
#                     'X':'-..-', 'Y':'-.--', 'Z':'--..',
#                     '1':'.----', '2':'..---', '3':'...--',
#                     '4':'....-', '5':'.....', '6':'-....',
#                     '7':'--...', '8':'---..', '9':'----.',
#                     '0':'-----', ', ':'--..--', '.':'.-.-.-',
#                     '?':'..--..', '/':'-..-.', '-':'-....-',
#                     '(':'-.--.', ')':'-.--.-',' ':' '}
# print('enter string')
# counter=0
# answer=input()
# morsestr=''
# for c in answer:
#     morsestr=morsestr + dictt[c]
# for ch in morsestr:
#     if ch=='-':
#         GPIO.output(15,GPIO.HIGH)
#         time.sleep(2)
#         GPIO.output(15,GPIO.LOW)
#     elif ch=='.':
#         GPIO.output(16,GPIO.HIGH)
#         time.sleep(1)
#         GPIO.output(16,GPIO.LOW)
#         time.sleep(1.5)
        
# import RPi.GPIO as GPIO
# import time
# import random
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(16, GPIO.OUT)
# GPIO.setup(15, GPIO.OUT)
# GPIO.setup(19, GPIO.OUT)
# username='santoshshanmugam6'
# password=222917
# dictt={'Green':16, 'Red':15, 'Yellow':19}
# print('enter username')
# userinput=input()
# print('enter number code')
# passinput=int(input())
# if userinput==username and passinput==password:
#     GPIO.output(dictt['Green'],GPIO.HIGH)
#     time.sleep(2)
#     GPIO.output(dictt['Green'],GPIO.LOW)
#     time.sleep(0.1)
# if userinput==username and passinput!=password:
#     print('wrong password')
#     GPIO.output(dictt['Yellow'],GPIO.HIGH)
#     time.sleep(2)
#     GPIO.output(dictt['Yellow'],GPIO.LOW)
#     time.sleep(0.1)
# if userinput!=username:
#     print('wrong username w/ wrong password')
#     GPIO.output(dictt['Red'],GPIO.HIGH)
#     time.sleep(2)
#     GPIO.output(dictt['Red'],GPIO.LOW)#     GPIO.output(dictt['Red'],GPIO.LOW)

#     time.sleep(0.1)
# GPIO.cleanup()

# #Lever switch/Traffic light
# #38=gnd cable
# green1=40
# yellow1=11
# red1=13
# green2=3
# yellow2=5
# red2=7
# import RPi.GPIO as GPIO
# import time
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(8, GPIO.OUT)
# GPIO.setup(38, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
# GPIO.output(8, GPIO.HIGH)

# GPIO.setup(red1, GPIO.OUT)
# GPIO.setup(yellow1, GPIO.OUT)
# GPIO.setup(green1, GPIO.OUT)
# GPIO.setup(red2, GPIO.OUT)
# GPIO.setup(yellow2, GPIO.OUT)
# GPIO.setup(green2, GPIO.OUT)

# GPIO.output(yellow1, GPIO.LOW)
# GPIO.output(red1, GPIO.LOW)
# GPIO.output(yellow2, GPIO.LOW)
# GPIO.output(green2, GPIO.LOW)

# GPIO.output(green1, GPIO.HIGH)
# GPIO.output(red2, GPIO.HIGH)

# while True:
#     while GPIO.input(38)!=1:
#         pass

#     GPIO.output(green1, GPIO.LOW)
#     GPIO.output(yellow1, GPIO.HIGH)
#     time.sleep(1)

#     GPIO.output(yellow1, GPIO.LOW)
#     GPIO.output(red1, GPIO.HIGH)
#     time.sleep(1)

#     GPIO.output(red2, GPIO.LOW)
#     GPIO.output(green2, GPIO.HIGH)
#     time.sleep(3)
    
#     GPIO.output(green2, GPIO.LOW)
#     GPIO.output(red1, GPIO.LOW)
#     GPIO.output(green1, GPIO.HIGH)
#     GPIO.output(yellow2, GPIO.HIGH)
#     time.sleep(1)

#     GPIO.output(yellow2, GPIO.LOW)
#     GPIO.output(red2, GPIO.HIGH)
#     time.sleep(0.5)

# #RGB LIGHT
# red=40
# green=19
# blue=16
# import RPi.GPIO as GPIO
# import time
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(red, GPIO.OUT)
# GPIO.setup(green, GPIO.OUT)
# GPIO.setup(blue, GPIO.OUT)

# GPIO.output(red, GPIO.LOW)
# GPIO.output(green, GPIO.LOW)
# GPIO.output(blue, GPIO.LOW)
# while True:
#     GPIO.output(blue, GPIO.HIGH)
#     GPIO.output(green, GPIO.HIGH)

# #beginning of PWM
# import RPi.GPIO as GPIO
# import time
# green=19
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(green, GPIO.OUT)
# GPIO.output(green, GPIO.LOW)
# p=GPIO.PWM(19, 2)
# p.start(25)
# time.sleep(10)
# p.stop()


# #NEW TERMS
# import RPi.GPIO as GPIO
# import time
# yellowbulb=19
# greenbulb=40
# redbulb=37
# GPIO.setmode(GPIO.BOARD)

# GPIO.setup(yellowbulb, GPIO.OUT)
# GPIO.output(yellowbulb, GPIO.LOW)
# p=GPIO.PWM(yellowbulb, 50)

# GPIO.setup(greenbulb, GPIO.OUT)
# GPIO.output(greenbulb, GPIO.LOW)
# ptwo=GPIO.PWM(greenbulb, 25)

# GPIO.setup(redbulb, GPIO.OUT)
# GPIO.output(redbulb, GPIO.LOW)
# pthree=GPIO.PWM(redbulb, 17)

# #brightening lightbulb p.start(0)
# # for var in range(0,100,1):
# #     var=var+1
# #     time.sleep(0.5)

# #dimming lightbulb p.start(100)
# # for var in range(100,0,-1):
# #     p.ChangeDutyCycle(var)
# #     time.sleep(0.5)

# p.start(0)
# for var in range(0,100,1):
#     var=var+1
#     time.sleep(0.5)
#     ptwo.start(100)
#     for var2 in range(100,0,-1):
#         p.ChangeDutyCycle(var2)
#         time.sleep(0.5)

# # p.start(50)
# # ptwo.start(50)
# # pthree.start(50)
# # time.sleep(10)
# #changesdutycycle p.ChangeDutyCycle(75)
# #changesfrequency p.ChangeFrequency(5)
# p.stop()
# ptwo.stop()
# pthree.stop()

# num=100
# lst=[]
# for var in range(0,101,1):
#     print(var,num)
#     num=num-1

# # p.start(50)
# # ptwo.start(50)
# # pthree.start(50)
# # time.sleep(10)
# #changesdutycycle p.ChangeDutyCycle(75)
# #changesfrequency p.ChangeFrequency(5)
# p.stop()
# ptwo.stop()
# pthree.stop()

# import RPi.GPIO as GPIO
# import time
# yellowbulb=19
# greenbulb=40
# redbulb=37
# var=10
# GPIO.setmode(GPIO.BOARD)

# GPIO.setup(yellowbulb, GPIO.OUT)
# GPIO.output(yellowbulb, GPIO.LOW)
# p=GPIO.PWM(yellowbulb, 10)

# GPIO.setup(greenbulb, GPIO.OUT)
# GPIO.output(greenbulb, GPIO.LOW)
# ptwo=GPIO.PWM(greenbulb, 10)

# GPIO.setup(redbulb, GPIO.OUT)
# GPIO.output(redbulb, GPIO.LOW)
# pthree=GPIO.PWM(redbulb, 10)
# while True:
#     if var==10:
#         p.start(50)
#         ptwo.start(50)
#         pthree.start(50)
#         time.sleep(1)
#         p.ChangeFrequency(var)
#         var=var+10
#     if var==90:
#         p.start(50)
#         ptwo.start(50)
#         pthree.start(50)
#         time.sleep(1)
#         p.ChangeFrequency(var)
#         var=var-10

# #button tutorial
# import RPi.GPIO as GPIO
# import time
# yellowbulb=19
# greenbulb=40
# redbulb=37
# buttoninput=8
# buttonoutput=10
# GPIO.setmode(GPIO.BOARD)

# GPIO.setup(yellowbulb, GPIO.OUT)
# GPIO.output(yellowbulb, GPIO.LOW)
# p=GPIO.PWM(yellowbulb, 1)
# GPIO.setup(buttonoutput, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(buttoninput, GPIO.OUT)
# GPIO.output(buttoninput, GPIO.HIGH)
# p.start(30)
# while True:
#     while GPIO.input(buttonoutput)==GPIO.LOW:
#         pass
#     for var in range(30,101,1):
#         p.ChangeDutyCycle(var)
#         time.sleep(0.5)
#     print('reached maximum brightness')
#     while GPIO.input(buttonoutput)==GPIO.LOW:
#         pass
#     for var in range(100,30,-1):
#         p.ChangeDutyCycle(var)
#         time.sleep(0.5)
#     print('reached minimum brightness')
        
##morse_code_translatorrasppi       
# import RPi.GPIO as GPIO
# import time
# blue=36
# green=37
# red=40
# buttonoutput=8
# buttoninput=10
# GPIO.setmode(GPIO.BOARD)

# GPIO.setup(red, GPIO.OUT)
# GPIO.setup(blue, GPIO.OUT)
# GPIO.setup(green, GPIO.OUT)
# GPIO.setup(38, GPIO.OUT)

# GPIO.output(red, GPIO.LOW)
# GPIO.output(blue, GPIO.LOW)
# GPIO.output(green, GPIO.HIGH)
# GPIO.output(38, GPIO.LOW)

# GPIO.setup(buttonoutput, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(buttoninput, GPIO.OUT)
# GPIO.output(buttoninput, GPIO.HIGH)
# time.sleep(5)

# import RPi.GPIO as GPIO
# import time
# morse={ 'A':'.-', 'B':'-...',
#                     'C':'-.-.', 'D':'-..', 'E':'.',
#                     'F':'..-.', 'G':'--.', 'H':'....',
#                     'I':'..', 'J':'.---', 'K':'-.-',
#                     'L':'.-..', 'M':'--', 'N':'-.',
#                     'O':'---', 'P':'.--.', 'Q':'--.-',
#                     'R':'.-.', 'S':'...', 'T':'-',
#                     'U':'..-', 'V':'...-', 'W':'.--',
#                     'X':'-..-', 'Y':'-.--', 'Z':'--..',
#                     '1':'.----', '2':'..---', '3':'...--',
#                     '4':'....-', '5':'.....', '6':'-....',
#                     '7':'--...', '8':'---..', '9':'----.',
#                     '0':'-----', ', ':'--..--', '.':'.-.-.-',
#                     '?':'..--..', '/':'-..-.', '-':'-....-',
#                     '(':'-.--.', ')':'-.--.-',' ':' '}

# green=8
# red=7
# GPIO.setmode(GPIO.BOARD)

# GPIO.setup(green, GPIO.OUT)
# GPIO.setup(red, GPIO.OUT)
# GPIO.output(green, GPIO.LOW)
# GPIO.output(red, GPIO.LOW)
# print('enter a sentence in all caps')
# written=input()
# for v in written:
#     morsecode=morse[v]
#     for w in morsecode:
#         if '.'==w:
#             print('.')
#             GPIO.output(green, GPIO.HIGH)
#             time.sleep(1)
#             GPIO.output(green, GPIO.LOW)
#             time.sleep(1)

#         if '-'==w:
#             print('-')
#             GPIO.output(red, GPIO.HIGH)
#             time.sleep(1)
#             GPIO.output(red, GPIO.LOW)
#             time.sleep(1)

#         if ' '==w:
#             time.sleep(2)


# import RPi.GPIO as GPIO
# import time
# GPIO.setmode(GPIO.BOARD)
# red=8
# yellow=10
# green=12
# ground=9
# GPIO.setup(red, GPIO.OUT)
# GPIO.output(red, GPIO.HIGH)
# p=GPIO.PWM(red, 50)

# GPIO.setup(yellow, GPIO.OUT)
# GPIO.output(yellow, GPIO.LOW)
# ptwo=GPIO.PWM(yellow, 50)

# GPIO.setup(green, GPIO.OUT)
# GPIO.output(green, GPIO.LOW)
# pthree=GPIO.PWM(green, 50)

# p.start(100)
# for var in range(100,0,-1):
#     p.ChangeDutyCycle(var)
#     time.sleep(0.1)

# ptwo.start(100)
# for var2 in range(100,0,-1):
#     ptwo.ChangeDutyCycle(var2)
#     time.sleep(0.1)

# pthree.start(100)
# for var3 in range(100,0,-1):
#     pthree.ChangeDutyCycle(var3)
#     time.sleep(0.1)

