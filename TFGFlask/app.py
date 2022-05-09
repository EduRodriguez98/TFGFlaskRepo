import multiprocessing
from flask import Flask, render_template, jsonify
import RPi.GPIO as GPIO
import time, threading, pyautogui, datetime
import sqlite3
# from subprocess import run
# from gpiozero import MotionSensor
from multiprocessing import Process
app = Flask(__name__)

#Exit function for threads

exit_event = threading.Event()
#Connection to DB
def db_conn():
    conn = None
    try:
        conn = sqlite3.connect("kiosk.db")
    except sqlite3.error as e:
        print(e)
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start():
    return render_template('start.html')

@app.route('/vidCas')
def vidCas():
    return render_template('vidCas.html')

@app.route('/vidEus')
def vidEus():
    return render_template('vidEus.html')

@app.route('/idioma')
def idioma():
    return render_template('idioma.html')

@app.route('/aunQuieresEus')
def aunQuieresEus():
    return render_template('aunQuieresEus.html')

@app.route('/aunQuieresCas')
def aunQuieresCas():
    return render_template('aunQuieresCas.html')

@app.route('/siLaQuieroCas')
def siLaQuieroCas():
    return render_template('siLaQuieroCas.html')

@app.route('/noLaQuieroCas')
def noLaQuieroCas():
    return render_template('noLaQuieroCas.html')

@app.route('/siLaQuieroEus')
def siLaQuieroEus():
    return render_template('siLaQuieroEus.html')

@app.route('/noLaQuieroEus')
def noLaQuieroEus():
    return render_template('noLaQuieroEus.html')

@app.route('/graciasSi')
def graciasSi():
    return render_template('graciasSi.html')

@app.route('/graciasNo')
def graciasNo():
    return render_template('graciasNo.html')

@app.route('/fashionCas')
def fashionCas():
    return render_template('fashionCas.html')

@app.route('/fashionEus')
def fashionEus():
    return render_template('fashionEus.html')

@app.route('/finCas')
def finCas():
    return render_template('finCas.html')

@app.route('/finEus')
def finEus():
    return render_template('finEus.html')


#Setup pin number for GPIO buttons
pin_btn_green = 15
pin_btn_red = 14
pin_btn_screenOn = 5
#pir = MotionSensor(16)
pin_btn_instantHome = 26
motionS = 16

#Setup gpio and input mode
GPIO.setmode(GPIO.BCM) 
GPIO.setup(pin_btn_green,GPIO.IN)
GPIO.setup(pin_btn_red,GPIO.IN)
GPIO.setup(pin_btn_screenOn,GPIO.IN)
GPIO.setup(pin_btn_instantHome,GPIO.IN)
GPIO.setup(motionS,GPIO.IN)

global decision
def buttonClicks():
    global decision
    decision = None
    counter = 0
    try:
        #Condition so the button can only be pressed once per function invocation
        while(counter < 1):
            
            if ((GPIO.input(pin_btn_green) == 1)):
                counter = counter + 1
                #Logging presses and counter values
                print("green button pressed")
                pyautogui.click(1110, 880)
                time.sleep(1)
                decision = True

            elif ((GPIO.input(pin_btn_red) == 1)):
                counter = counter + 1
                print("red button pressed")
                pyautogui.click(265, 880)
                decision = False
                time.sleep(0.5)
            
            elif(exit_event.is_set()):
                print("buttonclicks exit")
                break

    # Can be keyboard interrupted in case there is a need (safety precaution / logging )    
    except KeyboardInterrupt:
        print("\n stopped by keyboard")
        return False
    
    else:
        print(decision)
        return decision

def onlyGreenClicks():
    counter = 0
    try:

        while(counter < 1):

            if ((GPIO.input(pin_btn_green) == 1)):
                counter = counter + 1

                print("green button pressed")

                pyautogui.click(1110, 880)
                time.sleep(0.5)

            elif(exit_event.is_set()):
                print("greenclick exit")
                break

    except KeyboardInterrupt:
        print("\n stopped by keyboard")
        return False
    
    else:
        return True

def countdownB():
    #t is a variable for the amount of seconds that want to be waited before going back to intial state
    t = 30
    while(t):
        if(exit_event.is_set()):
            print("countdown B exit")
            break
        time.sleep(1)
        t -= 1
    print('countdown B finished')

def countdownC():
    #t is a variable for the amount of seconds that want to be waited before going back to intial state
    t = 30
    while(t):
        if(exit_event.is_set()):
            print("countdown C exit")
            break
        time.sleep(1)
        t -= 1
    print('countdown C finished')

def countdownD():
    #t is a variable for the amount of seconds that want to be waited before going back to intial state
    t = 60
    while(t):
        if(exit_event.is_set()):
            print("countdown D exit")
            break
        time.sleep(1)
        t -= 1
    print('countdown D finished')

def countdownE():
    #t is a variable for the amount of seconds that want to be waited before going back to intial state
    t = 30
    while(t):
        if(exit_event.is_set()):
            print("countdown E exit")
            break
        time.sleep(1)
        t -= 1
    print('countdown E finished')

def countdownF():
    #t is a variable for the amount of seconds that want to be waited before going back to intial state
    t = 30
    while(t):
        if(exit_event.is_set()):
            print("countdown F exit")
            break
        time.sleep(1)
        t -= 1
    print('countdown F finished')

def countdownG():
    #t is a variable for the amount of seconds that want to be waited before going back to intial state
    t = 30
    while(t):
        if(exit_event.is_set()):
            print("countdown G exit")
            break
            
        time.sleep(1)
        t -= 1
    print('countdown G finished')

#Variation of the function above, waits only one second to execute almost instantly
def instantHomeButton():
    number = 0
    try:

        while(number < 1):
            if(exit_event.is_set()):
                print("countdown F exit")
                break
            
            if ((GPIO.input(pin_btn_instantHome) == 1)):
                number = number + 1
                print("InstantHome pressed")
                pyautogui.click(1840, 60)
                time.sleep(0.5)

    except KeyboardInterrupt:
        print("\n stopped by keyboard")
        return False
    
    else:
        return True

def screenOnButton():
    num = 0
    print("num", num)
    try:

        while(num < 1):
            if(exit_event.is_set()):
                print("screenButton exit")
                break

            elif ((GPIO.input(pin_btn_screenOn) == 1)):
                num = num + 1
                print("panic screenOn pressed")
                pyautogui.click(80, 60)
                #Screen on and off removed for demo
                #run('vcgencmd display_power 1', shell=True)
                print("display on")
                time.sleep(0.5)

    except KeyboardInterrupt:
        print("\n stopped by keyboard")
        return False
    
    else:
        return True

# If motion sensor = movement, turn on display
# def on_detect():
#     global pirnum
#     print("pirnum value on detect: ", pirnum)
#     if(pirnum != 1):
#         print("pirnum != 1", pirnum)
#         #Click to go to start.html
#         pyautogui.click(80, 60)
#         # Display off is slow for demo, changing to black screen for now
#         # run('vcgencmd display_power 1', shell=True)
#         pirnum = 1
#         time.sleep(0.3)
#     elif(pirnum == 1):
#         print("pirnum is already = 1")
#         time.sleep(0.1)
#     return pirnum

#Add wait for input to let screen turn on before buttons are pressed!!!
def programExec():
    global decision
    decision = None
    global pirnum
    pirnum = None
    global counter
    counter = 0
    conn = db_conn()
    cursor = conn.cursor()

    exit_event.clear()

    #Initiate display off at beginning of program
    #run('vcgencmd display_power 0', shell=True)

    #Initiate panic button which turns on screen (if unplugged, will cause screen to always be on!)
    #This is also thought as a safety precaution in case the pir sensor fails
    s = threading.Thread(target=screenOnButton)
    s.daemon = True
    s.start()

    #pir.when_activated = on_detect

    print("empezado a detectar, pirnum val: ", pirnum)
    while(pirnum != 1):
        time.sleep(0.1)
        pirnum = GPIO.input(16)
        print("prinum", pirnum)
        if(pirnum == 1):
            time.sleep(1)
            pyautogui.click(80, 60)
            break
    print("procediendo al programa")


    try:

        endTime = None
        decInit = None
        decFin = None
        language = None

        #ih# threads are responsible for enabling the instantHomeButton
        ih1 = threading.Thread(target=instantHomeButton)
        print("instant home button initialized")
        ih1.daemon = True
        ih1.start()

        while (ih1.is_alive() == True):

            if (counter < 6):
            #WOULD YOU LIKE A T-SHIRT FOR 1EURO?
                b = threading.Thread(target=buttonClicks)
                print('b start')
                b.daemon = True
                b.start()
                print('proceso b vivo?: ', b.is_alive(), "\n waiting for b thread to end")
            
            #t# threads are responsible of initializing the countdown of 30seconds
                t0 = multiprocessing.Process(target=countdownB)
                t0.start()
                print("t0 started")

                #Execute the threads until one thread ends
                while (b.is_alive() == True):
                    # when one ends, run the following code:
                    if (t0.is_alive() == False):
                        print("t0 no está vivo, generando evento de salida y apagando display")
                        counter = 7
                        #Actualizar el hilo actual ejecutando el countdown para terminarlo y que no quede ejecutandose pasandole un evento.
                        exit_event.set()
                        break

                    elif (b.is_alive() == False):
                        print('Is b thread alive?: ', b.is_alive())
                        counter = counter + 1
                        print('contador: ', counter)

                        if(decision == True):
                            decInit = "si"
                            exit_event.set()

                        elif(decision == False):
                            decInit = "no"
                            exit_event.set()
                        break

                t0.terminate()
                #t0.join()
            
                print(t0.is_alive(), "estado t0 - b")
            initTime = datetime.datetime.now()
            if (counter < 6):
                exit_event.clear()
            #CHOOSE LANGUAGE
                c = threading.Thread(target=buttonClicks)
                print("c starting")
                c.daemon = True
                c.start()
                print('proceso c vivo?: ', c.is_alive(), "\n waiting for c thread to end, or 30 seconds")

                t1 = multiprocessing.Process(target=countdownC)
                t1.start()
                print("t1 started")

                while (c.is_alive() == True):
                    #The actions taken inside thread C must be inside the 30seconds window
                    if (t1.is_alive() == False):
                        print("t1 no está vivo")
                        #Click en boton invisible que redirecciona a index
                        pyautogui.click(1840, 60)
                        counter = 6
                        #Actualizar el hilo actual ejecutando el countdown para terminarlo y que no quede ejecutandose pasandole un evento.
                        exit_event.set()
                        break

                    elif (c.is_alive() == False):
                        print('Is c thread alive?: ', c.is_alive())
                        counter = counter + 1
                        print('contador: ', counter)

                        if(decision == True):
                            language = "Euskera"
                            exit_event.set()

                        elif(decision == False):
                            language = "Castellano"
                            exit_event.set()
                        break

                t1.terminate()
                #t1.join()

                print(t1.is_alive(), "estado t1 - c")
            if (counter < 6):
                exit_event.clear()
            #VIDEO PLAYS IN SELECTED LANGUAGE
                print("playing video")
                time.sleep(1.5)
                pyautogui.click(1200, 500)
                time.sleep(44)
                print("video ended, resuming interaction")

            #DO YOU STILL WANT THE TSHIRT?
                d = threading.Thread(target=buttonClicks)
                d.daemon = True
                d.start()
                print('proceso d vivo?: ', d.is_alive(), "\n waiting for d thread to end")

                t2 = multiprocessing.Process(target=countdownD)
                t2.start()
                print("t2 started")

                while (d.is_alive() == True):

                    if (t2.is_alive() == False):
                        pyautogui.click(1840, 60)
                        counter = 6
                        exit_event.set()
                        break

                    elif (d.is_alive() == False):
                        print('Is d thread alive?: ', d.is_alive())
                        counter = counter + 1
                        print('contador: ', counter)

                        if(decision == True):
                            decFin = "si"
                            exit_event.set()

                        elif(decision == False):
                            decFin = "no"
                            exit_event.set()
                        
                        break
                
                t2.terminate()
                #t2.join()
            
                print(t2.is_alive(), "estado t2 - d")
            if (counter < 6):
                exit_event.clear()
            #GRACIAS 1
                e = threading.Thread(target=onlyGreenClicks)
                e.daemon = True
                e.start()
                print('proceso e vivo?: ', e.is_alive(), "\n waiting for e thread to end")

                t3 = multiprocessing.Process(target=countdownE)
                t3.start()
                print("t3 started")

                while (e.is_alive() == True):

                    if (t3.is_alive() == False):
                        pyautogui.click(1840, 60)
                        counter = 6
                        exit_event.set()
                        break

                    elif (e.is_alive() == False):
                        print('Is e thread alive?: ', e.is_alive())
                        counter = counter + 1
                        print('contador: ', counter)
                        exit_event.set()
                        break
                
                t3.terminate()
                #t3.join()
            
                print(t3.is_alive(), "estado t3 - e")
            if (counter < 6):
                exit_event.clear()
            #GRACIAS 2
                f = threading.Thread(target=onlyGreenClicks)
                f.daemon = True
                f.start()
                print('proceso f vivo?: ', f.is_alive(), "\n waiting for f thread to end")

                t4 = multiprocessing.Process(target=countdownF)
                t4.start()
                print("t4 started")

                while (f.is_alive() == True):

                    if (t4.is_alive() == False):
                        pyautogui.click(1840, 60)
                        counter = 6
                        exit_event.set()
                        break

                    elif (f.is_alive() == False):
                        print('Is f thread alive?: ', f.is_alive())
                        counter = counter + 1
                        print('contador: ', counter)
                        exit_event.set()
                        break

                t4.terminate()
                #t4.join()
            
                print(t4.is_alive(), "estado t4 - f")
            if (counter < 6):
                exit_event.clear()
            #CÓDIGO QR
                g = threading.Thread(target=onlyGreenClicks)
                g.daemon = True
                g.start()
                print('proceso g vivo?: ', g.is_alive(), "\n waiting for g thread to end")

                t5 = multiprocessing.Process(target=countdownG)
                t5.start()
                print("t5 started")

                while (g.is_alive() == True):

                    if (t5.is_alive() == False):
                        pyautogui.click(1110, 880)
                        counter = 6
                        time.sleep(1)
                        exit_event.set()
                        break

                    elif (g.is_alive() == False):
                        print('Is g thread alive?: ', g.is_alive())
                        counter = counter + 1
                        print('contador: ', counter)
                        counter = 6
                        exit_event.set()
                        break
                
                t5.terminate()
                #t5.join()
                
                print(t5.is_alive(), "estado t5 - g")

            if (counter == 6):
                endTime = datetime.datetime.now()
                sql = """INSERT INTO interaction (iniTime, endTime, decisionOne, decisionTwo, language) VALUES (?, ?, ?, ?, ?)"""
                cursor = conn.execute(sql, (initTime, endTime, decInit, decFin, language))
                conn.commit()
                print("committed to database")
                break

            print(ih1.is_alive(), "estado ih1")
            print("usando instantHomeButton para fin del programa")
            pyautogui.click(1840, 60)
            exit_event.set()
            break

    except KeyboardInterrupt:
        print("\n stopped programExec by keyboard")
        return False
    
    else:
        print("end of programExec")
        exit_event.set()
        print("b estado: ", b.is_alive())
        print("s estado: ", s.is_alive())
        print("ih1 estado: ", ih1.is_alive())
        print("t0 estado: ", t0.is_alive())
        print("t1 estado: ", t1.is_alive())
        print("t2 estado: ", t2.is_alive())
        print("t3 estado: ", t3.is_alive())
        print("t4 estado: ", t4.is_alive())
        print("t5 estado: ", t5.is_alive())
        return True


if __name__ == "__main__":
    threading.Thread(target=lambda: app.run(host='127.0.0.1', port='5000', debug=False, use_reloader=False)).start()
    while(True):
        print("starting a thread")
        a = threading.Thread(target=programExec)
        a.start()
        while (a.is_alive() == True):

            if(a.is_alive() == False):
                print('is thread a alive? ')
                print(a.is_alive())
                break

    
    
