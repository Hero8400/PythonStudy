# Pythonメモ

## 1:演算

### 1-1:演算子

下記のように演算子を使用します。

|     | 数学上の記号 | Python上の記号 |
| --- | ------ | ---------- |
| 加算  | +      | +          |
| 減算  | -      | -          |
| 乗算  | ×      | *          |
| 除算  | ÷      | /          |

他にもこのような演算子も存在します。

| 内容          | 記号  |
| ----------- | --- |
| 余りを求める      | %   |
| 商を整数で求める    | //  |
| べき乗（指数）を求める | **  |

演算結果の例

![演習結果](images/ex1-1.png)

### 1-2:変数

変数に使用できる文字は、大小英文字/数字/アンダースコア「_」です。  
ただし、数字は先頭に使用できません。（※ほかの言語でも一緒ですね。）

![演習結果2](images/ex1-2.png)

### 1-3:代入の簡易記法

下記のように変数の代入を簡易化できます。

| 演算子 | 内容                            |
| --- | ----------------------------- |
| +=  | 自分自身に右辺の値を足して、その結果を自分自身に代入する  |
| -=  | 自分自身から右辺の値を減じて、その結果を自分自身に代入する |
| *=  | 自分自身に右辺の値を掛けて、その結果を自分自身に代入する  |
| /=  | 自分自身を右辺の値で割って、その結果を自分自身に代入する  |

![演習結果3](images/ex1-3.png)

### 1-4:関数

関数一覧

| 演算子      | 内容             |
| -------- | -------------- |
| max(a,b) | aとbで大きいほうの値を返す |
| min(a,b) | aとbで小さいほうの値を返す |

![演習結果4](images/ex1-4.png)

### 1-5:データ型

- 数値  
変数や値がどのような型になっているか確認する際は、type()を使用します。

![演習結果5](images/ex1-5.png)

- 文字列  
文字列を使用する場合は「""」または、「''」で囲みます。  
2種類存在する理由は、「"」や「'」も文字列として扱う場合があるためです。

![演習結果5_2](images/ex1-5_2.png)

- ブール値  
他の言語と同じですが、「True」、「False」の判定を行います。  
最初の一文字目は大文字で変数を定義します。

![演習結果5_3](images/ex1-5_3.png)

### 1-6:キャスト

- 整数への変換  
浮動小数点型の値やブール値、文字列を整数へ変換する場合はint()関数を使います。

- 文字列への変換  
数値やブール値を文字列に変換する場合はstr()関数を使います。
変換結果は「''」で囲まれています。

- ブール値への変換  
数値や文字列をブール値へ変換する場合はbool()関数を使います。  
0や0.0、空文字はFalseになりますが、それ以外はTrueです。

~~~python
>>> int(3.14)
3
>>> int('-90')
-90
>>> int(True)
1
>>> int(False)
0
>>> int('Hello')
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    int('Hello')
ValueError: invalid literal for int() with base 10: 'Hello'
>>> float(9)
9.0
>>> float('-90.568')
-90.568
>>> float(True)
1.0
>>> float(False)
0.0
>>> float("hello")
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    float("hello")
ValueError: could not convert string to float: 'hello'
~~~

~~~python
>>> str(3)
'3'
>>> str(0)
'0'
>>> str(-3.14)
'-3.14'
>>> str(True)
'True'
>>> str(False)
'False'
>>> bool(100)
True
>>> bool(0)
False
>>> bool(0.0)
False
>>> bool(-3.14)
True
>>> bool(True)
True
>>> bool(False)
False
>>> bool("Hello!")
True
~~~

### 1-7:リスト/タプル/辞書

- リスト  
0個以上の要素を持つシーケンス（並び）です。  
要素を追加削除したり、要素を書き換えることが可能です。  
[]で要素を囲むことで作成します。

- タプル  
0個以上の要素を持つシーケンス（並び）です。  
リストとは違い、一度作成すると変更は不可能です。  
()で要素を囲むことで作成します。

- 辞書  
「キー(Key)」と「バリュー(Value)」を指定します。  
調べる単語を「キー」に、調べた結果の値を「バリュー」に設定します。  
{}でキーとバリューを指定して作成します。

変更できる配列のことを、__ミュータブル（mutable）__  
変更できない配列のことを、__イミュータル（immutable）__ と呼びます。

~~~python
>>> math =80
>>> english =62
>>> japanese = 72
>>> science = 55
>>> total = math + english + japanese + science
>>> avarage = total / 4
>>> total
269
>>> avarage
67.25
>>> subject = (80, 62, 72, 55)
>>> total2 = subject[0] + subject[1] + subject[2] + subject[3]
>>> avarage2 = total2 / 4
>>> total2
269
>>> avarage2
67.25
>>> subject2 = [80, 62, 72, 55]
>>> total3 = subject[0] + subject[1] + subject[2] + subject[3]
>>> avarage3 = total3 / 4
>>> total3
269
>>> avarage3
67.25
~~~

~~~python
>>> subject = [61, 34, 86, 98]
>>> subject
[61, 34, 86, 98]
>>> subject[0] = 100
>>> subject
[100, 34, 86, 98]
>>> subject2 = (28, 36, 48, 66)
>>> subject2
(28, 36, 48, 66)
>>> subject2[0] = 80
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    subject2[0] = 80
TypeError: 'tuple' object does not support item assignment
~~~

リストのほうが融通は利きますが、タプルには下記のメリットがあります。

1. 消費メモリが少なくで済む。  
2. 誤って書き換えてしまうことがない。

- リスト  
  - 0個以上の要素をカンマで区切り、全体を[]で囲って作成します。  
  含まれる要素は数値でも、文字列でも問題ないです。
  - appendメソッドを使うと、リストの末尾に要素を追加できます。
  - insertメソッドを使うと、指定した要素を追加できます。
  - del命令を使うと、リスト内の特定要素を削除できます。

~~~python
>>> weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
>>> scores = [99, 72, 52, 85, 66, 42, 19]
>>> animals = ["dog", "cat", "rabbit", "tiger", "lion"]
>>> scores[1]
72
>>> scores[1] = 77
>>> scores
[99, 77, 52, 85, 66, 42, 19]
>>> weekdays.append("Saturday")
>>> weekdays
['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
>>> animals.insert(3, "gorilla")
>>> animals
['dog', 'cat', 'rabbit', 'gorilla', 'tiger', 'lion']
>>> del animals[2]
>>> animals
['dog', 'cat', 'gorilla', 'tiger', 'lion']
~~~

- タプルの変数代入
  - 上記で記述したように、タプルは要素の変更ができません。  
  insert、append、delの操作も不可能です。
  - たとえば、ゲームでは位置座標（X座標の値、Y座標の値）を扱います。  
  まとめて管理したほうがいろいろと楽です。  
  このような場面では、複数の値を管理できるため、タプルを使用することが適しています。  
  逆に、1つのタプルを複数の変数に代入することも可能です。  
  これを __「アンパック」__ と呼びます。  
  また、応用すると1つの命令で変数の値を入れ替えたりもできます。

~~~python
>>> pos = (56, 74)
>>> pos
(56, 74)
>>> pos[0]
56
>>> pos[1]
74
>>> pos_x, pos_y = pos
>>> pos_x
56
>>> pos_y
74
>>> x = 3
>>> y = 6
>>> (x, y) = (y, x)
>>> x
6
>>> y
3
~~~

- 辞書  
辞書は、文字通り索引機能があります。  
別名 __「ハッシュテーブル」__ __「キー・バリューペア」__ と呼ばれます。  
キーの値は「""」で囲み、その値を「:」の後ろに記述します。  
データ型は任意ですが基本的にキーには文字列を使用することが多いです。

~~~python
>>> score = {
"math" : 78,
"english" : 95,
"chemistry" : 68,
"science" : 62,
}
>>> score
{'math': 78, 'english': 95, 'chemistry': 68, 'science': 62}
>>> score["english"]
95
>>> score["math"]
78
>>> score["math"] = 82
>>> score
{'math': 82, 'english': 95, 'chemistry': 68, 'science': 62}
~~~

- リストのリスト  
リストの中にさらに、リストやタプルを格納することが可能です。

~~~python
>>> animals = ("Horse", "Lion", "Elephant")
>>> scores = (35, 87, 63)
>>> data = (animals, scores)
>>> data
(('Horse', 'Lion', 'Elephant'), (35, 87, 63))
>>> data[0]
('Horse', 'Lion', 'Elephant')
>>> data[0][1]
'Lion'
>>> data[1]
(35, 87, 63)
>>> data[1][2]
63
~~~

### 1-8:リスト（タプル）に使用する関数

- len  
リストやタプルに含まれ要素の数を返します。  
引数に2次元配列を与えると、一番外側のリスト項目数を返します。  
内側のリスト項目数を求める場合は、len()の引数に内側のリストに渡す必要があります。

~~~python
>>> len([1, 2, 3, 4, 5])
5
>>> len(("small", "medium", "large"))
3

>>> data = [[1, 2], [3, 4, 5], [6, 7, 8, 9]]
>>> len(data)
3
>>> len(data[2])
4
~~~

- copy  
ある変数にリストやタプルを格納していたとします。  
その変数を別の変数に代入しても、そのリスト自体がコピーされることはありません。

~~~python
>>> a = [1, 2, 3]
>>> b = a
>>> a[2] = 9
>>> a
[1, 2, 9]
>>> b
[1, 2, 9]
~~~

aはリスト本体ではなくリストを代入した変数のため、上記のような結果になります。  
変数aはリストの場所を指示しているだけです。この状態を __「参照」__ と呼びます。  
リストの複製を行いたい場合は、copy()メソッドを使用します。

~~~python
>>> a = [1, 2, 3]
>>> b = a.copy()
>>> a[2] = 9
>>> a
[1, 2, 9]
>>> b
[1, 2, 3]
~~~

このとき、変数aのリストと変数bのリストは別物です。  
もちろんですが、タプルにはcopy()メソッドは用意されていません。

- in  
ある値がリストやタプルに含まれているかチェックするときに使用します。  
__調べたい値　in　リスト（またはタプル）__ と呼び出します。  
値が含まれている場合は __True__ が、含まれていない場合は __False__ を返します。  
また、何番目に格納されているか確認したいときは __index()メソッド__ を使用します。

~~~python
>>> greets = ("morning", "afternoon", "evening")
>>> "noon" in greets
False
>>> "afternoon" in greets
True
>>> scores = [92, 45, 87, 36, 72]
>>> 36 in scores
True
>>> 67 in scores
False
>>> greets.index("afternoon")
1
>>> scores.index(36)
3
>>> scores.index(99)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    scores.index(99)
ValueError: 99 is not in list
~~~

- sort  
Pythonではリストを並べ替えるために2つの方法があります。  
  - sorted関数
  引数で与えられたリストやタプルを並べ替えて、コピーを返します。  
  元のリストの並び順は変わりません。

  - sortメソッド  
  元のリストをその場で並べ替えます。  
  戻り値は返しません。

~~~python
>>> fruits = ["banana", "apple", "peach", "orange"]
>>> sorted(fruits)
['apple', 'banana', 'orange', 'peach']
>>> fruits
['banana', 'apple', 'peach', 'orange']
>>> fruits.sort()
>>> fruits
['apple', 'banana', 'orange', 'peach']
~~~

- print  
print()は引数で与えられた情報をコンソールに表示する関数です。  
単一の値を表示する場合は、その内容を単に括弧の中に記述するだけです。  
複数の値を表示する場合は、カンマ区切りで指定します。

  - %演算子を使う方法  
  元の文字列内に「%s」や「%d」などを書式を埋め込んでおきます。  
  文字列の後ろに%演算子を配置し、その後ろにタプル形式で実データを配置します。  
  書式の型と実際のデータは一致させる必要があります。一致しない場合はエラーになります。

| 表記方法 | 内容       |
| ---- | -------- |
| %s   | 文字列      |
| %d   | 10進数     |
| %x   | 16進数     |
| %f   | 10進float |

~~~python
>>> print("hello")
hello
>>> print(3)
3
>>> print(False)
False
>>> print("Hi!", "Python", 3)
Hi! Python 3
>>> "1=%s 2=%s" % ("Hello", "World")
'1=Hello 2=World'
>>> "value=(%d, %d)" % (2, 5)
'value=(2, 5)'
>>> "score=%f" % (2.457)
'score=2.457000'
>>> "age=%d" % ("Hello")
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    "age=%d" % ("Hello")
TypeError: %d format: a number is required, not str
>>> val, name = 4, "Python"
>>> print("val=%d, nam=%s" % (val, name))
val=4, nam=Python
~~~

- formatメソッドを使う方法  
書式付き文字列を同じように用意します。  
データを挿入したい箇所に%を使わず、{}を配置します。  
名前で指定することも可能です。

~~~python
>>> "1={} 2={}".format("Hello", "World")
'1=Hello 2=World'
>>> "value=({}, {})".format(2, 5)
'value=(2, 5)'
>>> "score={}".format(2.457)
'score=2.457'
>>> "value=({1}, {0})".format(3, 8)
'value=(8, 3)'
>>> "value=({weight}, {tall})".format(weight=62.8, tall=173.4)
'value=(62.8, 173.4)'
~~~

### 1-9:コメント

プログラム中にコメントを書く場合は、 __「#」__ を記述します。  
Pythonは、複数行コメントを書けません。毎回「#」を文頭につけます。  

~~~python
>>> scores = [92, 45, 87, 36, 72] # math test scores
~~~

### 1-10:行の折り返し

1行が長すぎる場合は、 __「\」（バックスラッシュ）__ を挿入することで行を折り返すことができます。  

## 2:制御文

### 2-1:インデント

Pythonは、 __インデントを使ってグループ化する__ という特徴があります。  
C++、C#、Java、JavaScriptなどは、複数文をグループ化するとき{}で囲います。  
Pythonは{}を使用せず、インデントのみで記述できます。

> if 条件式:  
> 　　命令1  
> 　　命令2  
> 命令3

たとえば、上記のif文の場合、Trueで命令1、Falseで命令2、命令3は必ず実行されます。  
インデントに使用できるのは、Tabまたはスペースです。  
一般的に、1段階のインデントに4文字のスペースを使います。

### 2-2:条件式の評価

- 比較演算子

比較演算子は2つの値を比較してブール値を返します。

| 演算子    | 内容                       |
| ------ | ------------------------ |
| A == B | 2つの値が等しいときにTrue          |
| A != B | 2つの値が異なるときにTrue          |
| A < B  | AがBより小さいときにTrue          |
| A <= B | AがB以下のときにTrue            |
| A > B  | AがBより大きいときにTrue          |
| A >= B | AがB以上のときにTrue            |
| A in B | AがB(リスト/タプル）に含まれるときにTrue |

~~~python
>>> A = 1
>>> B = 2
>>> A == B
False
>>> A != B
True
>>> A < B
True
>>> A > B
False
>>> A <= B
True
>>> A >= B
False
>>> A in (1, 3, 5)
True
>>> B in (1, 3, 5)
False
~~~

- ブール演算子

比較演算子を使用して、2つの値を比較できます。

| ブール演算子      | 内容                         |
| ----------- | -------------------------- |
| 条件式1and条件式2 | 条件式1と条件式2がともにTrueのときにTrue  |
| 条件式1or条件式2  | 条件式1と条件式2のどちらかTrueのときにTrue |
| not条件式1     | 条件式1と逆のブール値を返す             |

~~~python
>>> A = 1
>>> B = 2
>>> A < 10 and B < 10
True
>>> A < 0 and B < 10
False
>>> A > 0 or B > 10
True
>>> A > 10 or B > 10
False
>>> not A == 1
False
>>> not B == 1
True
~~~

- if文
  1. if: else:  
  条件式の結果によって、何かしら処理を行います。
  
  2. if: elif:  
  複数の条件を使って、処理を切り分けます。

~~~python
 >>>  """
  if 条件式:  
  　　条件式がTrueのときの処理  
  else:  
  　　条件式がFalseのときの処理
  """
>>> if a == "man":
	print("I'm man.")
else:
	print("I'm woman.")

I'm man.

>>> """
if 条件式1:
  条件式1がTrueのときの処理
elif 条件式2:
  条件式2がTrueのときの処理
else:
  上記の条件がすべてFalseのときの処理
"""
>>> if fruit == "apple":
	print("red")
elif fruit == "banana":
	print("yellow")
else:
	print("unknown")

yellow
~~~

インドより愛をこめて

![インドの夜更け](images/GoodNightFromIndia.jpg)
