# -*- coding: utf-8 -*-
from collections import defaultdict

click = defaultdict(list)
ads = defaultdict(list)
users = {}
with open("click", "r") as f:
    for i in f:
        v = i.strip().split()
        click[v[0]].append(int(v[2]))

with open("user", "r") as f:
    for i in f:
        v = i.strip().split()
        users[v[0]] = v[1]

with open("ad", "r") as f:
    for i in f:
        v = i.strip().split()
        ads[v[1]].append(v[0])
print ads

moneys = defaultdict(list)
for ad in ads:
    for g in click:
        if g in ads[ad]:
            moneys[ad].append(sum(click[g]))

um = []
for m in moneys:
    um.append((m, sum(moneys[m])))
sorted_um = sorted(um, key=lambda x: x[1], reverse=True)[0]

print sorted_um[0], users[sorted_um[0]], sorted_um[1]
