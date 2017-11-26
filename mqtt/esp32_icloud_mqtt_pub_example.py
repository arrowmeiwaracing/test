from umqtt.simple import MQTTClient
import machine
import network
import time

SSID="Your WIFI SSID"         #WIFI SSID
PASSWORD="Your WIFI PASSWORD" #WIFI PASS

t1 = machine.TouchPad(machine.Pin(4)) #esp32 Touch0

SERVER = "XX9999.messaging.internetofthings.ibmcloud.com" #XX9999 is org-id 
PORT = 8883 #ssl port
CLIENT_ID = "d:XX9999:XXTYPE:XXdeviceID" #XX9999=org-id ,XXTYPE=device type, XXdiviceID
TOPIC = "iot-2/evt/XX9999/fmt/json" #XX9999 is org-id
username='use-token-auth' #kotei
mqttpass='xxxxxxx' #device id touroku ji ni settei suru password
c=None

def connectWifi(ssid,passwd):
  global wlan
  wlan=network.WLAN(network.STA_IF)
  wlan.active(True)
  wlan.connect(ssid,passwd)
  while(wlan.ifconfig()[0]=='0.0.0.0'):
    time.sleep(10)
try:
  print("start")
  connectWifi(SSID,PASSWORD)

  print("mqtt connecting...")
  c = MQTTClient(CLIENT_ID,SERVER,port = PORT, ssl = True, user=username, password=mqttpass)
  c.connect()
  print("mqtt connected!")

  zv1 = 9999
  while True:
    v1 = t1.read()
    print("adc0=",v1)

    if v1>999:                     # Touch value is over 1000 as 1000, not as 0.
      v1=1000                      #
    else:                          #
      v1=0                         #

    if v1 != zv1:                  # value change ON or OFF only event pushing.
      msg = '{"d":{"value":' + str(v1) + ', "dummyD":1, "dummyC": "A"}}'
      c.publish(TOPIC, msg, 0, True)
      zv1 = v1
      
    time.sleep(0.1)                #wait 100msec
    
finally:                           #error or Ctrl+c
  if(c is not None):
    c.disconnect()
  wlan.disconnect()
  wlan.active(False)
  print("ended")
