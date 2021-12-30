
print("西暦を入力してください")
seireki = int(input())
# print(heisei)
if isinstance(seireki, int):
    if int(seireki) >= 2018:
        print("西暦" + str(seireki) + "年は、", end="")
        reiwa = int(seireki) - 2017
        print("令和" + str(reiwa) + "年です")
    elif int(seireki) < 2018:
        print("西暦" + str(seireki) + "年は、", end="")
        heisei = int(seireki) - 1988   
        print("平成" + str(heisei) + "年です")
    else:
        print("さよなら")
else:
    seireki = str(seireki)
    print("さよなら")