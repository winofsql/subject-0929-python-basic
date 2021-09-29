###########################
# 配列
###########################
# リスト型 => 配列の様なモノ
# 辞書型(ディクショナリ型) => 連想配列
# タプル型 => 定数の配列

# リスト型は、[]を使う
Agroup = ['kazu', 'gorou']
print(Agroup)

Agroup.append('dai')
print(Agroup)

Agroup.remove('kazu')
print(Agroup)

# 辞書型
import pprint

# 辞書型は{}を使う
dic = {
    '1' : "バスケ",
    '2' : "野球",
    '3' : "サッカー"
}
# print(dic)
pprint.pprint(dic, indent=2, width=1)

# タプル型は()を使う
tuple = ('apple', 3, 90.4)
print(tuple)