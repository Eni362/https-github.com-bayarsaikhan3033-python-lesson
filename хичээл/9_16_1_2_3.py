# 6 мөр байсан
n = input("n: ")
urt = len(n)
niilber = 0
for i in range(urt):
    niilber = niilber + int(n[i])
print(niilber)

# 3 мөр болов
n = input("n: ")
niilber = sum(int(i) for i in str(n))
print(niilber)

# 1 мөр болов
print(sum(int(i) for i in str(input("n: "))))
