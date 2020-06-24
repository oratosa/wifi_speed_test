import pprint
import subprocess
import json

def get_speed_test_result():
    process = subprocess.run(['speedtest','--json'], capture_output=True)
    return json.loads(process.stdout)

def job():
    result = get_speed_test_result()
    print(result['download'],result['upload'],result['client']['isp'], result['server']['host'])

job()