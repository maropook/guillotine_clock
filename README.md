# guillotine_clock
4年後期のシステム設計演習で作成したギロチン時計

## 使用言語等
・Python
・flask
・cron

## 参考
[Mac標準のリモート接続でラズパイに繋ぐ方法](https://qiita.com/karaage0703/items/9650e7aeceb6e1b81612#comments)
[Raspberry Pi と Python を使ったブラウザ設定【目覚まし時計】](https://canmakewakuwaku.com/rasppi_alarm/)


## 実行方法
ラズパイでプログラムを実行する`python3 app.py`

パソコンやスマホのブラウザを開き、Raspberry Pi の IPアドレス:ポート（デフォルト5000）でアクセスする。例`http://192.168.11.9:5000`

※注意点、ラズパイとブラウザを使用する機器は同じLANに接続されている必要があります。

## tree
```
/home/pi/work/
alarm/
├app.py
├alarm.py
├templates/
│└index.html
└cron/
  ├cron.py
  └cron.sh
```
