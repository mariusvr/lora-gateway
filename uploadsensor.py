import urllib2
import time

while True:
    fileHandle = open ( '/home/pi/lora-gateway/telemetry.txt',"r" )
    lineList = fileHandle.readlines()
    fileHandle.close()

    telemetry = lineList[-1]
    vars = telemetry.split(",")
    temp = vars[18].split("*")
    baseURL = "https://api.thingspeak.com/update?api_key=KA8898GKT8TYZUYQ"
    baseURL += "&field1=" + vars[12]
    baseURL += "&field2=" + vars[13]
    baseURL += "&field3=" + vars[14]
    baseURL += "&field4=" + vars[15]
    baseURL += "&field5=" + vars[16]
    baseURL += "&field6=" + vars[17]
    baseURL += "&field7=" + temp[0]
    baseURL += "&field8=" + vars[5]
        
    print(baseURL)
    urllib2.urlopen(baseURL).read()

    time.sleep(15)

