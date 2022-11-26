import requests
import time
import random
#GET https://api.thingspeak.com/update?api_key=YVFPSOWJ8WF64X2G&field1=0 POST

# GET https://api.thingspeak.com/channels/1957131/feeds.json?api_key=CYTPF22JWETSNJCA&results=2 Read

def main():
    t = float(random.randrange(20, 40))
    h = float(random.randrange(60, 80))
    p = float(random.randrange(1000, 2137))

    print(f"Temperature {t}\n Humidity {h} \n Pressure {p}")

    url = 'https://api.thingspeak.com/update?api_key=YVFPSOWJ8WF64X2G&field1=0'

    sensor_readings = {'field1': t, 'field2': h, 'field3': p}
    req_header = {'Content-type': 'application/json'}
    res = requests.post(url, sensor_readings, req_header)
    print(f"Print: {res.text}")
    print(f"Status code: {res.status_code}")
    time.sleep(200)


if __name__ == "__main__":
    while True:
        main()