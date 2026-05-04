a = [i for i in range(1005, 147871) if '1' not in str(i) and max(int(d) for d in str(i)) - min(int(d) for d in str(i)) < 4]
a.sort(reverse=True)
print(len(a), a[24])