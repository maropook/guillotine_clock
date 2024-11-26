from time import sleep
import subprocess
import os
import traceback

MP3_PATH = '/usr/share/sounds/alsa/Side_Left.wav'
SLEEP = 5

# ログファイルを指定
LOG_FILE = '/home/student/cron_debug.log'

def log_message(message):
    with open(LOG_FILE, 'a') as log:
        log.write(message + '\n')

try:
    # XDG_RUNTIME_DIR の設定
    os.environ['XDG_RUNTIME_DIR'] = f'/run/user/{os.getuid()}'
    log_message(f"XDG_RUNTIME_DIR is set to: {os.environ['XDG_RUNTIME_DIR']}")
    
    # PulseAudio サーバーの開始（必要な場合）
    subprocess.Popen(['pulseaudio', '--start'])
    log_message("PulseAudio started (if not already running).")
    
    # 音声ファイルの再生
    args = ['aplay', MP3_PATH]
    process = subprocess.Popen(args)
    log_message(f"Started playing sound with command: {args}")
    
    sleep(SLEEP)
    
    # 音声プロセスの終了
    args = ['kill', str(process.pid)]
    subprocess.Popen(args)
    log_message("Sound process terminated.")
    
except Exception as e:
    # エラーログ出力
    error_message = f"An error occurred: {e}\n{traceback.format_exc()}"
    log_message(error_message)
