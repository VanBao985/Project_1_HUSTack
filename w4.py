# Cho dãy a1, a2, ..., an trong đó các phần tử đôi một khác nhau và 1 giá trị nguyên dương M. Hãy đếm số Q các cặp (i,j) sao cho 1 <= i < j <= n và ai + aj = M.


n, M = map(int, input().split())
data = set(map(int, input().split()))
count = 0
for i in data:
    if M - i in data and i != M - i:
        count += 1
print(int(count/2))