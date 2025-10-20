from machine import UART
from machine import Pin
import time


# send and recieve messages between two 
uart = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9))
uart.init(bits=8, parity=None, stop=1) 

message = "This is a code written without a test"
time.sleep(3)
sent_message = uart.write(message) # send a mesage
def time_rn(): # format the time so that it shows up more logically
    y, m, d, hh, mm, ss, *_ = time.localtime()
    return f"{y:04d}-{m:02d}-{d:02d} {hh:02d}:{mm:02d}:{ss:02d}"


if sent_message == len(message): # check if the lenght of the sent mesage equals the length of the message, then the message was succesfully sent.
    print("Message sent successfully!")
else:
    print("the message was sent incompletly")

#time.sleep(2)


# this is for the recieving end.

while True: # always loop to keep checking for messages.
    time.sleep(1)
    if uart.any(): #check for any message
        data=uart.read() # data is whatever message pico recieved
        print("I have recieved data: ", data.decode("utf-8")) # decode the message
    else:
        print("keep alive")
        time.sleep(0.5)

