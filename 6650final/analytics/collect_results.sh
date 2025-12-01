#!/usr/bin/env bash
OUT=analytics/all_results.csv
echo "env,api,p50,p90,p99,mean" > $OUT
python3 analytics/compute_summary.py $1 $2 >> $OUT