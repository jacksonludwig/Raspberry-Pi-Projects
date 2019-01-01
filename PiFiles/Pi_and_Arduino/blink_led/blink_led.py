import serial
ser = serial.Serial('/dev/ttyACM0', 9600)

print(ser.readline())

ser.write('5'.encode())