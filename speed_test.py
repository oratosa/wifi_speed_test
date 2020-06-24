import subprocess
import json
import csv
import datetime
import schedule
import time

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

schedule.every().day.at("09:00").do(job)
schedule.every().day.at("10:00").do(job)
schedule.every().day.at("11:00").do(job)
schedule.every().day.at("12:00").do(job)
schedule.every().day.at("13:00").do(job)
schedule.every().day.at("14:00").do(job)
schedule.every().day.at("15:00").do(job)
schedule.every().day.at("16:00").do(job)
schedule.every().day.at("17:00").do(job)
schedule.every().day.at("18:00").do(job)
schedule.every().day.at("19:00").do(job)
schedule.every().day.at("20:00").do(job)
schedule.every().day.at("21:00").do(job)
schedule.every().day.at("22:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)