#!/usr/bin/env bash
BASE=$1
OUT=results_create.txt
> $OUT
for i in {1..50}; do
t=$(curl -o /dev/null -s -w "%{time_total}" -X POST $BASE/create -H "Content-Type: application/json" -d '{"url":"https://example.com"}')
echo $t >> $OUT
done