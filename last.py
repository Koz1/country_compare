import matplotlib.pyplot as plt
import sys

# csvファイルをリストで読み込み
file = open('15o_data.csv')
line = file.readlines()
file.close()

# 読み込んだデータをカンマ(,)で区切ってリスト化する
year = line[4].split(',')
jpn = line[5].split(',')
usa = line[6].split(',')
chn = line[14].split(',')
kor = line[16].split(',')

year = year[4:]

# 文字列を整数データに変換
jpn = list(map(int, jpn[4:]))
usa = list(map(int, usa[4:]))
chn = list(map(int, chn[4:]))
kor = list(map(int, kor[4:]))

# ディクショナリのデータ作成
country = {'jpn': jpn, 'usa': usa, 'chn': chn, 'kor': kor}

# タイトル文
print ('２国間の生産人口推移比較\n')

# 説明文&国名とアルファベット3文字表示&判定
for i in range(5):
    print ('以下の中から２つの国を選んで、アルファベット３文字を入力してください。')
    print ('【日本：jpn , 米国：usa , 中国：chn , 韓国：kor】\n')
    country1 = input()

    if country1 == 'jpn' or country1 == 'usa' or country1 == 'chn' or country1 == 'kor':
        break
        
    elif i == 4:
        print('\n5回失敗しました。プログラムを終了します。\n')
        sys.exit()   
        
    else:
        continue

for i in range(5):
    print(country1 + '以外のどれかを入力してください。\n')
    country2 = input()

    if i == 4:
        print('\n5回失敗しました。プログラムを終了します。\n')
        sys.exit()   
    
    elif country1 == country2:
        print(country1 + 'と同じ値が入れられました。')
        continue

    elif country2 == 'jpn' or country2 == 'usa' or country2 == 'chn' or country2 == 'kor':
        print('\n' + country1 + 'と' + country2 + 'の比較グラフを表示します。')
        break

    else:
        continue

# 2国間の人口推移比較関数
def compare_2countries():
    plt.plot(year, country[country1], color='#FF0000', label=country1)
    plt.plot(year, country[country2], color='#00FF00', label=country2)
    plt.legend()
    plt.show()

compare_2countries()