path_A_V = r"D:\NLP\A_V.txt"
path_Vg = r"D:\NLP\Vg.txt"
path_Vm = r"D:\NLP\Vm.txt"
i = 0
a = {}
v = {}
vg = {}
vm = {}


def edit_distance(str1, str2):
    m = len(str1)
    n = len(str2)
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
    for x in range(m + 1):
        for j in range(n + 1):
            if x == 0:
                dp[x][j] = j

            elif j == 0:
                dp[x][j] = x

            elif str1[x - 1] == str2[j - 1]:
                dp[x][j] = dp[x - 1][j - 1]

            else:
                dp[x][j] = 1 + min(dp[x][j - 1],  # Insert
                                   dp[x - 1][j],  # Remove
                                   dp[x - 1][j - 1])  # Replace

    return dp[m][n]


def tb(ed):
    t = 0
    for x in ed:
        t = t + x
    return t/100

with open(path_A_V, mode='r', encoding="utf8") as av:
    while i < 100:
        a[i] = av.readline()
        v[i] = av.readline()
        i = i + 1
    av.close()
i = 0
with open(path_Vg, mode='r', encoding="utf8") as v1:
    while i < 100:
        vg[i] = v1.readline()
        i = i + 1
i = 0
with open(path_Vm, mode='r', encoding="utf8") as v2:
    while i < 100:
        vm[i] = v2.readline()
        i = i + 1

vig = {}
vim = {}
i = 0
while i < 100:
    vig[i] = edit_distance(v[i], vg[i])
    vim[i] = edit_distance(v[i], vm[i])
    i = i + 1
print(tb(vig))
print(tb(vim))
if tb(vig) > tb(vim):
    print("kết quả dịch của hệ thống Google Translate tốt hơn")
elif tb(vig) < tb(vim):
    print("kết quả dịch của hệ thống Microsoft Bing tốt hơn")
else:
    print("kết quả dịch của hệ thống Microsoft Bing và Google Translate như nhau")
av.close()