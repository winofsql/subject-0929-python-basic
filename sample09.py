# C言語の場合
# for(int i = 0; i < 10; i++ ) {
#     printf("%d",i);
# }

# Pythonの場合
for i in range(5) :
    print(i)

# リスト型の繰り返し
music_list = ['ROCK', 'POP', 'JAZZ']
for music in music_list :
    print(music)

# 辞書型(連想配列)の繰り返し
menu = {
    'ラーメン' : 500,
    'チャーハン' : 430,
    '餃子' : 210
}
for order in menu :
    print(order)            # キー(key)
    print(menu[order]*1.1)  # バリュー(value)