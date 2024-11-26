import subprocess

def set_job(time: str):
    command = '/home/student/myenv/bin/python3 /home/student/guillotine_clock/alarm/alarm.py'
    time_list = time.split(':')
    hour = time_list[0]
    minute = time_list[1]
    job = f'{int(minute)} {int(hour)} * * * {command}'
    print(job)
    subprocess.call(['sudo', '/home/student/guillotine_clock/alarm/cron/cron.sh', job])


# if __name__ == "__main__":
#  set_job("07:30")  # テスト用の時刻を入力
