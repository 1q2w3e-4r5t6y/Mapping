#Tkinterライブラリをインポートする
import tkinter as tk
import tkinter.filedialog as fl
import pandas as pd
import matplotlib.pyplot as plt


root = tk.Tk()
root.title("Mapping APP")
root.geometry("300x500")

text0 = tk.Label(root, text = "初めにマッピングしたいcsvファイルを選んでね♪")
text0.pack(pady=30)

def get():
    filetype=[("all file","*")]    
    path=fl.askopenfilename(initialdir="C:",filetypes=filetype)
    csv_path.insert(tk.END,path)

button_get = tk.Button(text="csv ファイルを選択",command = get)
button_get.pack(pady=10)

csv_path = tk.Entry(width = 30)
csv_path.pack(pady=20)

text1 = tk.Label(root, text="1段目にx軸の目盛りの分割幅を入力してね♪")
text2 = tk.Label(root, text="2段目にy軸の目盛りの分割幅を入力してね♪")

x_scale_Entry = tk.Entry(width=30)
y_scale_Entry = tk.Entry(width=30)

text1.pack(pady=10)
x_scale_Entry.pack(pady=10)
text2.pack(pady=10)
y_scale_Entry.pack(pady=10)


def plot():
    path = csv_path.get()
    x_scale = x_scale_Entry.get()
    y_scale = y_scale_Entry.get()

    # CSVファイルを読み込む（ファイル名を適宜変更）
    data = pd.read_csv(path, header=None)

    # 新しい行と列のラベルを定義（適宜変更）
    new_row_labels = range(data.shape[0])
    new_col_labels = range(data.shape[1])

    # ヒートマップを描画
    plt.imshow(data, cmap='jet', origin='upper', aspect='auto')
    plt.colorbar()  # カラーバーを追加


    # 新しい行と列のラベルを設定
    plt.xticks(range(0, len(new_col_labels), int(x_scale)))
    plt.yticks(range(0, len(new_row_labels), int(y_scale)))

    # 軸ラベルの設定
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')

    # グラフを表示
    plt.show()
    

button_plot = tk.Button(text="2D マッピング！",command = plot)
button_plot.pack(pady=20)

root.mainloop()