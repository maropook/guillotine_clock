import RPi.GPIO as GPIO
import time
# moter_and_sw.py

# GPIOピン設定
gpio_mo = 17  # モーター用ピン
gpio_button = 18  # ボタン用ピン

# GPIO初期設定
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_mo, GPIO.OUT)
GPIO.setup(gpio_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # ボタン入力（プルアップ）

def main():
    try:
        print("モーターを開始します。ボタンを押すと停止します。")
        GPIO.output(gpio_mo, 1)  # モーターをオンにする

        while True:
            button_state = GPIO.input(gpio_button)  # ボタンの状態を確認
            if button_state == GPIO.LOW:  # ボタンが押された場合
                print("ボタンが押されました。モーターを停止します。")
                break
            time.sleep(0.1)  # ボタン状態を100msごとに確認

    finally:
        GPIO.output(gpio_mo, 0)  # モーターを停止
        GPIO.cleanup()  # GPIOの後始末
        print("終了しました。")

if __name__ == "__main__":
    main()
