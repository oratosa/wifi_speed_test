import pprint
import subprocess
import json
import csv
import datetime

def get_speed_test_result():
    process = subprocess.run(['speedtest','--json'], capture_output=True)
    return json.loads(process.stdout)

def bit_to_mbit(bit):
    return bit/1024/1024

def job():
    result = get_speed_test_result()
    dt = datetime.datetime.now()
    with open('logs.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([dt.strftime('%Y-%m-%d %H:%M:%S'),bit_to_mbit(result['download']),bit_to_mbit(result['upload']),result['client']['isp'], result['server']['host']])

job()