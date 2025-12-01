import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('analytics/all_results.csv')
fig, ax = plt.subplots()
x = range(len(df))
ax.bar([i-0.2 for i in x], df['p50'], width=0.2, label='p50')
ax.bar([i for i in x], df['p90'], width=0.2, label='p90')
ax.bar([i+0.2 for i in x], df['p99'], width=0.2, label='p99')
ax.set_xticks(x)
ax.set_xticklabels(df['env'])
ax.set_ylabel('Latency (s)')
ax.legend()
plt.tight_layout()
plt.savefig('analytics/latency_comparison.png')
print('Saved analytics/latency_comparison.png')
