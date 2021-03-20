# import socket
# import numpy as np
# import encodings
print('Triggered')
import RPi.GPIO as GPIO

def triggering():
    #Set GPIO pins as outputs
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(19, GPIO.OUT)

    #Switch GPIO pins ON
    GPIO.output(16, True)
    GPIO.output(17, True)
    GPIO.output(18, True)
    GPIO.output(19, True)


    #Switch GPIO pins OFF
    # GPIO.output(16, False)
    # GPIO.output(18, False)
    # #Reset GPIO pins to their default state
    # GPIO.cleanup()




def my_server():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("Server Started waiting for client to connect ")
        s.bind((HOST, PORT))
        s.listen(5)
        conn, addr = s.accept()

        with conn:
            print('Connected by', addr)
            while True:

                data = conn.recv(1024).decode('utf-8')

                if str(data) == "Data":

                    print("Ok Sending data ")

                    my_data = random_data()

                    x_encoded_data = my_data.encode('utf-8')

                    conn.sendall(x_encoded_data)

                elif  str(data) == "Quit":
                    print("shutting down server ")
                    break


                if not data:
                    break
                else:
                    pass
