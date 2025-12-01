#!/usr/bin/env bash
BASE=$1
for i in {1..10}; do
sleep 600 # 10分钟等待以触发冷启动
t=$(curl -o /dev/null -s -w "%{time_total}" -X POST $BASE/create -H "Content-Type: application/json" -d '{"url":"https://example.com"}')
echo "trial $i: $t"
done