import os
import schedule
from datetime import datetime
import asyncio

async def job(arg='argument'):
    file_list = os.listdir('.')
    for file_name in file_list:
        if file_name.endswith('.txt'):
            text_file_path = os.path.join('.', file_name)
            with open(text_file_path, 'r') as file:
                file_contents = file.read()
            print(f"Contents of {file_name}:")
            print(file_contents)
            os.remove(file_name)
    else:
        print("No text files found in the folder.")
        print(arg)

def run_schedule():
    while True:
        schedule.run_pending()

def schedule_job():
    loop = asyncio.get_event_loop()
    task = asyncio.create_task(job())
    loop.run_until_complete(task)

schedule.every(1).seconds.to(5).do(schedule_job)
schedule.every(1).minutes.to(5).do(schedule_job)
schedule.every(2).hours.to(5).do(schedule_job)
schedule.every().minute.at(':20').do(schedule_job)
schedule.every().hour.at(':20').do(schedule_job)
schedule.every(5).hours.at(':20').do(schedule_job)
schedule.every().day.at('12:20:30').do(schedule_job)
schedule.every().monday.at('01:20').do(schedule_job)
schedule.every(10).seconds.until('10:20').do(schedule_job)
schedule.every(10).seconds.until(datetime(2024, 11, 21, 10, 21, 5)).do(schedule_job)

if __name__ == '__main__':
    run_schedule()

