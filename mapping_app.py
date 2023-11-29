#Tkinterライブラリをインポートする
import tkinter as tk
import tkinter.filedialog as fl
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import numpy as np


root = tk.Tk()
root.title("Mapping APP")
root.geometry("300x550")

text0 = tk.Label(root, text = "初めにマッピングしたいcsvファイルを選んでね♪")
text0.pack(pady=30)

def get():
    filetype=[("all file","*")]    
    path=fl.askopenfilename(initialdir="C:",filetypes=filetype)
    csv_path.delete(0, tk.END)
    csv_path.insert(tk.END,path)

button_get = tk.Button(text="csv ファイルを選択",command = get)
button_get.pack(pady=10)

csv_path = tk.Entry(width = 30)
csv_path.pack(pady=20)

text1 = tk.Label(root, text="1段目にx軸の目盛りの分割幅を入力してね♪")
text2 = tk.Label(root, text="2段目にy軸の目盛りの分割幅を入力してね♪")
text3 = tk.Label(root, text="スケールバーの下限を入れてね♪")
text4 = tk.Label(root, text="スケールバーの上限を入れてね♪")


x_scale_Entry = tk.Entry(width=30)
y_scale_Entry = tk.Entry(width=30)
scale_bar_min_Entry = tk.Entry(width=30)
scale_bar_Max_Entry = tk.Entry(width=30)


text1.pack(pady=10)
x_scale_Entry.pack(pady=10)
text2.pack(pady=10)
y_scale_Entry.pack(pady=10)
text3.pack(pady=10)
scale_bar_min_Entry.pack(pady=10)
text4.pack(pady=10)
scale_bar_Max_Entry.pack(pady=10)



def plot_2D():
    path = csv_path.get()
    x_scale = x_scale_Entry.get()
    y_scale = y_scale_Entry.get()
    scale_bar_min = scale_bar_min_Entry.get()
    scale_bar_Max = scale_bar_Max_Entry.get()

    # CSVファイルを読み込む（ファイル名を適宜変更）
    data = pd.read_csv(path, header=None)

    # 新しい行と列のラベルを定義（適宜変更）
    new_row_labels = range(data.shape[0])
    new_col_labels = range(data.shape[1])

    # ヒートマップを描画
    plt.imshow(data, cmap='jet', origin='upper', aspect='auto', norm = Normalize(vmax=scale_bar_Max, vmin=scale_bar_min))
    plt.colorbar()  # カラーバーを追加


    # 新しい行と列のラベルを設定
    plt.xticks(range(0, len(new_col_labels), int(x_scale)))
    plt.yticks(range(0, len(new_row_labels), int(y_scale)))

    # 軸ラベルの設定
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')

    # グラフを表示
    plt.show()

def plot_3D():
    path = csv_path.get()
    data = pd.read_csv(path, header=None)

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
    

button_plot_2D = tk.Button(text="2D マッピング！",command = plot_2D)
button_plot_2D.pack(pady=20)

button_plot_3D = tk.Button(text="3D マッピング！",command = plot_3D)
button_plot_3D.pack(pady=20)
text_3D = tk.Label(root, text = "3Dマッピングは調整中です。")
text_3D.pack(pady =10)

root.mainloop()