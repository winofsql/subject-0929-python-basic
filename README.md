# python20210929
2021/09/29(水)の午前に実施したPythonプログラム

## ■ Pythonをはじめよう
### Pythonとは
- 1990年代初頭に、オランダ人の開発者、グイド・ヴァンロッサムが開発したプログラミング言語
- 名前の由来は、イギリスのコメディアングループ「モンティ・パイソン」から
- 日本語で「ニシキヘビ」なのでロゴはヘビ

### Pythonの特徴
  - プログラム(ソースコード)が読みやすい
  - 実は初心者向け
  - Google、NASAでも活用されている
  - Instagram、Pinterest、Reddit、PyPl、PyQでも使用されている
  - 高度な計算も可能

- Pythonのバージョンについて
  - 現在バージョン2系と3系が混在している
  - 今から勉強するなら3系
  - まれに2系じゃないとできない事がある
    - 2系はサポート終了(2020年まで)

## ■ Pythonの実行環境を作ろう

### Visual Studio Code
- 起動
- 拡張機能 Python 追加

### Pythonの動作確認
- VSCのターミナルから下記コマンド

```bash
python -V
python --version
```

## ■ Pythonプログラムを実行するには
Pythonでプログラムを実行する方法

1. インタラクティブシェルモード(1行ずつ実行)
2. IDLE(アイドル)というPython付属のソフトを使う(あまり使わない)
3. ソースコードを作ってから実行する(今後これでやる)
4. Jupyter Notebook
  https://www.javadrive.jp/python/jupyter-notebook/index3.html#section2

### インタラクティブシェルモード(1行ずつ実行)
※インタラクティブモードともいいます
- VSCのターミナルから下記コマンド
```bash
python
```

文字を表示する

```python
print('hello world')
```

カレンダーを表示する
```python
import calendar
print(calendar.month(2021,9))
```

「Pythonの心、考え方」を表示する(深い意味はない遊び)
```python
import this
```

Pythonを終了させる

```python
exit()
Ctrl + Z + Enter
```

インタラクティブモードはここまで

### IDLE(アイドル)というPython付属のソフトを使う(あまり使わない触れるだけ)
Windowsスタートボタン→Python 3.x→IDLE で起動

```python
print('hello world')
```

IDLEはここまで

### ソースコードを作ってから実行する(今後これでやる)
- 「hello.py」ファイルを新規作成する
- 文字コードは「UTF-8」(特に何もしなくて良い)

```python
print('hello world')
```

- VSCの右上にある緑の再生マークをクリック(ターミナルで Python ファイルを実行)
  - Pythonの実行
  - VSCのターミナルに実行結果が表示されている

## ■ Pythonプログラミングの第一歩
```python
a = 10
b = 10

# OK
if a == b :
  print('Hello World!')

# NG
if a == b :
print('Hello World!')
```

```python
# OK
def happy() :
  print('life')

# NG
def happy() :
print('life')
```

## ■ Pythonで計算してみよう

```python
# 足す/引く/掛ける/割る/余り(剰余)
# 他の言語と同じ
print(100 + 5)  # 105
print(100 - 5)  # 95
print(100 * 5)  # 500
print(100 / 5)  # 20.0
print(100 % 3)  # 1

# べき乗
print(2 ** 3)   # 8
```

## ■ データを便利に扱うために : 変数

```python
# 変数は型名とか$不要
# 書式
# 変数 = 値

# 実例
tax = 1.1
price = 100
tel = '090-9999-9999'

print(tax)
print(price)
print(tel)
print(tax * price)
```

### 変数に使える文字
- 1文字目に数字は使えない
- 予約後は使えない

```python
# OK
tax = 0.1
price = 100

# NG
# Syntax Error: invalid syntax(構文のエラー: 無効な構文があります。)
# 1文字目数字
1tax = 0.1

# 予約後
if = 200
```

Pythonの予約後を表示する

```python
import keyword
print(keyword.kwlist)
```

## ■ どちらが多いか？大きいか？ : 比較演算子

```python
# 大なり、大なりイコール、小なり、小なりイコール、イコール、異なる
# 他の言語と同じ
print(35 > 35)    # False
print(35 >= 35)   # True
print(35 < 40)    # True
print(35 <= 40)   # True
print(40 == 40)   # True
print(40 != 40)   # False
```

True、Falseは、論理型・bool型と言われるデータ型

## ■ Pythonで扱ういろいろなデータの種類 : データ型
- 数値型
  - int 整数値 : 100、0、-50
  - float 浮動小数点(少数、実数) : 3.14、0.0、-3.14
- 文字列型
  - 'シングルクォートで囲まれたら文字列'
  - "ダブルクォートで囲まれたら文字列"

文字列サンプル

```python
print('シングルクォートで囲まれたら文字列')
print("ダブルクォートで囲まれたら文字列")

# ヒアドキュメント
str = '''Hello World
こんにちは世界'''
print(str)

str = """Hello World
こんにちは世界"""
print(str)
```

文字列操作

```python
# 文字列連結
print('Hello' + 'World')

# 文字列の繰り返し
print('Hello' * 2)

# 小文字→大文字
str = 'hello'
print(str.upper())
```

- 論理型
  - True(真) or False(偽)
  - bool型と呼ばれる
  - 頭文字大文字にすることに注意

- リスト型
  - 配列の便利版

```python
# リスト型は[]を使う
Agroup = ['kazu','gorou']

# データ追加
Agroup.append('dai')
print(Agroup)

# データ削除
Agroup.remove('kazu')
print(Agroup)
```

- 辞書型(連想配列)

```python
import pprint

# 辞書型は{}を使う
dic = {
  '1' : 'バスケ',
  '2' : '野球',
  '3' : 'サッカー'
}

# pprint(データ, インデント, 幅)
# データを整形して出力(PHPのprint_rみたいな関数)
pprint.pprint(dic, indent=2, width=1)
```

- タプル型(定数の配列)

```python
# タプル型は()を使う
tuple = ('apple', 3, 90.4)
print(tuple)
```

## ■ こういうとき、どうする？ : 条件分岐

```python
# キーボード入力(C言語のscanf)
# 入力値は文字列として扱われるので
# int型(整数)に変換
age = int(input('入力>>>'))

if(age == 65) :
  print('65歳')
elif(age >= 18) :
  print('18歳以上')
else :
  print('18歳未満')
```

## ■ 何度も同じことをする : 繰り返し
### for文
```python
# 指定回数ループ
for count in range(5) :
  print(count)

# リスト型の繰り返し
music_list = ['ROCK', 'POP', 'JAZZ']

for music in music_list :
  print(music)

# 辞書型の繰り返し
menu = {
    'ラーメン' : 500,
    'チャーハン' : 430,
    '餃子' : 210
  }

for order in menu :
  print(order)
  print(menu[order] * 1.1)
```

### while文

```python
counter = 0

while(counter < 5) :
  print(counter)
  counter += 1
```

## ■ 装置を作る : 関数

```python
# 引数無し、戻り値無し
def display() :
  print('Hello')
  print('World')
  print('!!')

display()
display()

# 引数有り、戻り値有り
# area : 面積
# radius : 半径
def area(radius) :
  result = radius * radius * 3.14
  return result

print(area(5))

# 標準関数
# 文字数カウント
print(len('byebye'))

# 最大値取得
print(max(100, 10, 50))

# 最小値取得
print(min(100, 10, 50))
```

## ■ 間違ったとき、想定外のとき : エラーと例外

- エラーとは
  - Python構文(書き方のルール)が間違っている時
    - Syntax Error
  - Pythonが実行中にデータをうまく処理できない時

- 例外とは
  - 例外が発生しそうな箇所に、例外が発生した時どう処理するか
  - メッセージ出して動き続けるのか、終了するのか

```python
try :
  # ここで例外発生
  # 「print」とする所を「prin」と間違った
  prin('例外が発生してしまう処理')
except Exception as e:
  print('例外をキャッチしました')
  print(e.args)
```
## ■ tkinterを使ったGUIプログラミング

GUI画面

```python
import tkinter as tk
base = tk.Tk()
base.mainloop()
```

ボタン

basic027.py
```python
import tkinter as tk
base = tk.Tk()
button = tk.Button(base, text='Push1').pack()
base.mainloop()
```

複数ボタン

basic028.py
```python
import tkinter as tk
base = tk.Tk()
button1 = tk.Button(base, text='Push1', width=20).pack()
button2 = tk.Button(base, text='Push2').pack(side=tk.LEFT)
button3 = tk.Button(base, text='Push3').pack(side=tk.RIGHT)
base.mainloop()
```

ボタンクリック後の動作

basic029.py
```python
import tkinter as tk
base = tk.Tk()

def push() :
  print('クリック')

button = tk.Button(base, text='Push', command=push).pack()
base.mainloop()
```

メッセージボックス

basic033.py
```python
import tkinter as tk
import tkinter.messagebox as msg
base = tk.Tk()
base.withdraw()

# OK/キャンセル
response = msg.askokcancel('大変！！！', '大丈夫ですか？')

# はい/いいえ
response = msg.askquestion('大変！！！', '大丈夫ですか？')

# はい/いいえ
response = msg.askyesno('大変！！！', '大丈夫ですか？')

# 再試行/キャンセル
response = msg.askretrycancel('大変！！！', '大丈夫ですか？')

# はい/いいえ/キャンセル
response = msg.askyesnocancel('大変！！！', '大丈夫ですか？')


if(response == True) :
    print('大丈夫')
else :
    print('大丈夫ではない')

base.mainloop()
```
