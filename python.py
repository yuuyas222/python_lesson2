# 条件分岐
number = 4
if number > 1:
    print("すき")
elif number > 2:
    print("普通")
else:
    print("嫌い")

time = 14
if time < 12:
    print("午前中")
elif time == 12:
    print("正午")
elif time > 12:
    print("午後")



# おみくじ
import random
omikuji = random.randint(1,10)
# print(omikuji) デバック

if omikuji == 1:
    print("大吉")
elif omikuji == 2:
    print("中吉")
elif omikuji <= 4:
    print("小吉")
elif omikuji <= 7:
    print("凶")
else:
    print("大凶")



# RPGのクリティカルヒット再現

import random
hit = random.randint(1,10)
print(hit)

if hit < 6:
    print("スライムに、" + str(hit) + "のダメージを与えた！")
else:
    print("クリティカルヒットのダメージ100を与えた")


# 西暦を計算する
seireki = 2022
print("西暦" + str(seireki) + "年は、", end="")
heisei = seireki - 1988
# print(heisei)
print("平成" + str(heisei) + "年です")
