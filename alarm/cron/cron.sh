#!/bin/bash
cron_job="$1"
echo "Adding cron job: $cron_job"

# 一時ファイルに新しい内容のみを書き込む
temp_cron_file=$(mktemp)
echo "$cron_job" > "$temp_cron_file"
echo "New crontab content:"
cat "$temp_cron_file"

# 新しいcrontabをユーザーに強制適用
sudo crontab "$temp_cron_file" -u student

# 一時ファイルを削除
rm "$temp_cron_file"

# cronサービスの再起動
sudo systemctl restart cron
