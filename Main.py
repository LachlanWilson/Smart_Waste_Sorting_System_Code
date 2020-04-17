import Sensor
#import Vision
import MechElements

def Main():
    #while(True):
        SensorInfo = Sensor.Main() # return number

        if(SensorInfo != 0):
            # do anything that needs to happen for processing the data
            Type = wasteType(SensorInfo) 
            DataRecording(Type,SensorInfo)
            if(Type != "invalid"):
                MechElements.Main(SensorInfo)

def wasteType(SensorInfo):
    if(SensorInfo < 50):
        return "plastic"
    elif(SensorInfo >= 50 and SensorInfo <= 100):
        return "paper"
    elif(SensorInfo > 100 and SensorInfo <= 150):
        return "metal"
    else:
        return "invalid"

def DataRecording(wasteType,SensorInfo):
    print(wasteType + " | " + str(SensorInfo))

    with open('Data.txt','a') as the_file: the_file.write(wasteType + " | " + str(SensorInfo) + '.\n')

Main()