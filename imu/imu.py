'''
Basado en código encontrado aquí
https://naylampmechatronics.com/blog/45_tutorial-mpu6050-acelerometro-y-giroscopio.html
'''
import smbus			#import SMBus module of I2C
import shutil
import time
from time import sleep          
import datetime

#some MPU6050 Registers and their Address
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H  = 0x43
GYRO_YOUT_H  = 0x45
GYRO_ZOUT_H  = 0x47

bus = smbus.SMBus(1) 	# or bus = smbus.SMBus(0) for older version boards
Device_Address = [0x68]   # Direcciones de MPU6050 (ej para dos IMU: [0x68,0x69])
mano=["i","d"]
n=[0,0]

def MPU_Init(deviceAddr):
    #write to sample rate register
    bus.write_byte_data(deviceAddr, SMPLRT_DIV, 7)
    
    #Write to power management register
    bus.write_byte_data(deviceAddr, PWR_MGMT_1, 1)
    
    #Write to Configuration register
    bus.write_byte_data(deviceAddr, CONFIG, 0)
    
    #Write to Gyro configuration register
    bus.write_byte_data(deviceAddr, GYRO_CONFIG, 24)
    
    #Write to interrupt enable register
    bus.write_byte_data(deviceAddr, INT_ENABLE, 1)

def read_raw_data(deviceAddr,regAddr):
    try:
	#Accelero and Gyro value are 16-bit
        high = bus.read_byte_data(deviceAddr, regAddr)
        low = bus.read_byte_data(deviceAddr, regAddr+1)
    
        #concatenate higher and lower value
        value = ((high << 8) | low)
        
        #to get signed value from mpu6050
        if(value > 32768):
                value = value - 65536
        return value
    except:
        print("errors "+hex(deviceAddr)+" "+hex(regAddr))
        return 0



for i in range(len(Device_Address)):
    MPU_Init(Device_Address[i])

print (" Reading Data of Gyroscope and Accelerometer")

initTime=str(round(time.time()*1000))
ts=[initTime,initTime]
while True:
    for i in Device_Address:
            #Read Accelerometer raw value
            acc_x = read_raw_data(Device_Address[i], ACCEL_XOUT_H)
            acc_y = read_raw_data(Device_Address[i], ACCEL_YOUT_H)
            acc_z = read_raw_data(Device_Address[i], ACCEL_ZOUT_H)
            
            #Read Gyroscope raw value
            gyro_x = read_raw_data(Device_Address[i], GYRO_XOUT_H)
            gyro_y = read_raw_data(Device_Address[i], GYRO_YOUT_H)
            gyro_z = read_raw_data(Device_Address[i], GYRO_ZOUT_H)
            
            #Full scale range +/- 250 degree/C as per sensitivity scale factor
            Ax = acc_x/16384.0
            Ay = acc_y/16384.0
            Az = acc_z/16384.0
            
            Gx = gyro_x/131.0
            Gy = gyro_y/131.0
            Gz = gyro_z/131.0
            
            resultado=str(Gx)+","+str(Gy)+","+str(Gz)+","+str(Ax)+","+str(Ay)+","+str(Az)+"\n"
            file_object = open("ramdisk/"+ts[i]+"_"+mano[i]+".csv", "a")
            file_object.write(resultado)
            

            if n[i]==600:
                file_object.close()
                shutil.move("ramdisk/"+ts[i]+"_"+mano[i]+".csv","upload/")
                print(str(n[i])+" registros guardados")
                n[i]=0
                ts[i]=str(round(time.time()*1000))

            n[i]+=1
    sleep(0.1)