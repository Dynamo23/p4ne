import glob

flist = glob.glob('C:\\Users\\Anatoly\\PycharmProjects\\p4ne\Lab1.5\\config_files\\*.txt')
print(flist)
alist = []
blist = []
for name in flist:
    with open(name) as f:
        str_list = list(f)
        for s in str_list:
            d = s.find(' ip address')
            if d != -1:
                d1 = s.find('no')
                d2 = s.find('dhcp')
                if d1 == -1 and d2 == -1:
                    alist.append(s)

for n in alist:
    w = n.replace(' ip address ', '').strip()
    blist.append(w)

print(sorted(list(set(blist))))











