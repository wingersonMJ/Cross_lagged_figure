import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_excel("path", sheet_name="Final_dat")

# mvpa1_7
# mvpa8_14
# awake1_7
# awake8_14

fig, axes = plt.subplots(1, 2, figsize=(10, 7))

sns.boxplot(data=df[['mvpa1_7', 'mvpa8_14']], ax=axes[0], color='lightgrey', showfliers=False)
sns.stripplot(data=df[['mvpa1_7', 'mvpa8_14']], ax=axes[0], color='dimgrey', size=4, jitter=True)
axes[0].set_xticklabels(["Early MVPA", "Later MVPA"], fontsize=12)
axes[0].set_ylabel("Average daily MVPA (minutes)", fontsize=12)

sns.boxplot(data=df[['awake1_7', 'awake8_14']], ax=axes[1], color='lightgrey', showfliers=False)
sns.stripplot(data=df[['awake1_7', 'awake8_14']], ax=axes[1], color='dimgrey', size=4, jitter=True)
axes[1].set_xticklabels(["Early time in bed awake", "Later time in bed awake"], fontsize=10)
axes[1].set_ylabel("Average daily time in bed awake (minutes)", fontsize=12)

axes[0].text(
    -0.10, 1.05, "A.", 
    transform=axes[0].transAxes, 
    fontsize=16, fontweight='bold', va='top', ha='right'
)

axes[1].text(
    -0.10, 1.05, "B.", 
    transform=axes[1].transAxes,
    fontsize=16, fontweight='bold', va='top', ha='right'
)

plt.tight_layout()
plt.savefig("path", dpi=300, bbox_inches='tight')
plt.show()