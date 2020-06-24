import pprint
import subprocess
import json
import csv

def get_speed_test_result():
    process = subprocess.run(['speedtest','--json'], capture_output=True)
    return json.loads(process.stdout)

def job():
    result = get_speed_test_result()
    with open('logs.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([result['download'],result['upload'],result['client']['isp'], result['server']['host']])

job()