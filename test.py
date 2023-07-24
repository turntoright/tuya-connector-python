from tuya_connector import TuyaOpenAPI, TuyaOpenPulsar, TuyaCloudPulsarTopic

ACCESS_ID = "9j34agpgvaupnvejruj8"
ACCESS_KEY = "1b1c795f284e4227800350ee013805bd"
API_ENDPOINT = "https://openapi.tuyaus.com"


# Init OpenAPI and connect
openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()

DEVICE_ID = 'ebcb55294a126e4826lxnh'
params = {
    'codes': 'ele',
    'end_time': '1690143595000',
    'start_time': '1690142455000',
    'type': '7'
}    
response = openapi.get( f'/v1.0/devices/{DEVICE_ID}/logs', params=params)
print(response)