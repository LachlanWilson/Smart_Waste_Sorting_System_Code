import Sensor
import Vision
import MechElements

def Main():
    SensorInfo = Sensor.Main()
    
    if(SensorInfo == "NoWaste"):
        VisionInfo = Vision.Main(SensorInfo)
        # do anything that needs to happen for processing the data
        MechElements.Main(SensorInfo,VisionInfo)

def DataProcessing():

    # process data