# PyGameNote

## PyGameの主なクラス一覧

| クラス名               | 内容                         |
| ------------------ | -------------------------- |
| copy()             | Rectオブジェクトを複製する            |
| move(x, y)         | (x, y)移動したRectを返す。自身は移動しない |
| move_ip(x, y)      | 自身（Rect）を（x, y）移動する        |
| inflate(x, y)      | 現在地から（x, y）だけ変更する          |
| union(Rect)        | 自身と引数のRectを含む最小のRectを返す    |
| contains(Rect)     | 引数のRectを含むか否かを返す           |
| collidepoint(x, y) | (x,y)という点が自身に含まれるか否かを返す    |
| colliderect(Rect)  | Rectと自身に重なりがあるか否か（衝突）を返す   |

__オブジェクト.メソッド名（引数1,引数2,・・・引数n）__

