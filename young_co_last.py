import matplotlib.pyplot as plt

# CSVファイルの読み込み&リスト化
with open('15u_data.csv') as file:
    lines = file.read().splitlines()

# yearに年代データを入れる&ディクショナリ定義
year = lines[4].split(',')[4:]
info = {}
name = {}

# CSVデータを各行でリスト化&ディクショナリに各国名をキーとして値を挿入
for line in lines[5:27]:
    items = line.split(',')
    info[items[3].lower()] = list(map(int, items[4:]))
    name[items[3].lower()] = items[0]

# 説明文&国名とアルファベット3文字表示
print ('２国間の若年層人口推移比較\n')
print ('以下の中から２つの国を選んで、アルファベット３文字を入力してください。')
print ('-----------')
for k, v in name.items():   
    print (k, v)
print ('----------\n')

# 関数で使う変数の文字列入力
print ('一つ目を入力してください')
c1 = input()
print ('\n二つ目を入力してください')
c2 = input()

# ２つの国の若年層人口推移比較関数
def co():
    
    plt.rcParams['font.family'] = 'IPAPGothic'
    plt.title('２国間の15歳未満の人口推移比較（万人/ten thousands）', fontsize = 15)
    plt.plot(year, info[c1], color='#FF0000', label= name[c1])
    plt.plot(year, info[c2], color='#00FF00', label= name[c2])
    plt.legend()
    plt.show()

co()
