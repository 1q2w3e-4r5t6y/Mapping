import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

data = pd.read_csv('test.csv', header=None)

# 3Dグラフを作成
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 行と列の数を取得
num_rows, num_cols = data.shape

# 行と列のインデックスを生成
x = range(num_cols)
y = range(num_rows)
X, Y = np.meshgrid(x, y)

# データの値を取得
Z = data.values

# 3Dサーフェスプロットを作成
surf = ax.plot_surface(X, Y, Z, cmap='viridis')

# 軸ラベルを設定
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_zlabel('WCA')

# カラーバーを追加
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)

# グラフを表示
plt.show()