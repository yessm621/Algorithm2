s = input()

result = []
while True:
    if s.strip() == '':
        break
        
    start = s.find('<')
    end = s.find('>')
    if start == 0:
        result.append(s[start:end+1])
        s = s[end+1:]
    else:
        if s.find('<') < 0:
            a = s.split(' ')
            tmp = []
            if len(a) == 1:
                result.append(a[0][::-1])
            else:
                for x in a:
                    tmp.append(x[::-1])
                result.append(' '.join(tmp))
            break
        else:
            a = s[0:start].split(' ')
            tmp = []
            if len(a) == 1:
                result.append(a[0][::-1])
            else:
                for x in a:
                    tmp.append(x[::-1])
                result.append(' '.join(tmp))
            s = s[start:]

for r in result:
    print(r, end = '')