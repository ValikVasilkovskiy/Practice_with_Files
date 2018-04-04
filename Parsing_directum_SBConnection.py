info = open('main.xml', 'r')
string_file = info.read()
data = []
all_data = []
for i in string_file.split(' '):
    if 'UserName="' in i:
        data.append(i[i.index('=')+2:-1])
    elif 'ClientHostNameFull="' in i:
        if data:
            data.append(i[i.index('=')+2:-1])
            all_data.append(data)
            data = []
        else:
            all_data[-1].append(i[i.index('=')+2:-1])
info.close()
stack_market = []
stack_lu = []
stack_other = []
stack_ts = []
for i in all_data:
    if len(i) >= 2:
        for j in range(1, len(i)):
            if str(i[j]).lower().startswith('market'):
                stack_market.append(i[j])
            elif str(i[j]).lower().startswith('lu'):
                stack_lu.append(i[j])
            elif str(i[j]).lower().startswith('direct'):
                stack_ts.append(i[j])
            else:
                stack_other.append(i[j])
print('market = {}\nlu = {}\nother = {}\nts = {}\nall = {}'.format(len(stack_market), len(stack_lu), len(stack_other), len(stack_ts), len(all_data)))
#print(list(map(lambda x: print(x), stack_other)))