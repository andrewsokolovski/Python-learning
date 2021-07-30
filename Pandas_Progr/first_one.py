import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('GGSN CPU_Brest_H_071020_271020.csv')
#print(df.head((3)))
#print(df.columns)
print(df[['DATETIME','Peak CPU usage']])
plt.plot(df['DATETIME'], df['Peak CPU usage'])
plt.show()