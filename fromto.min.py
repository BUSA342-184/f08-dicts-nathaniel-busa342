from collections import Counter
from_user, from_host, to_user, to_host = [], [], [], []
for line in open('mbox-short.txt'):
    if line.startswith('From:') or line.startswith('To:'):
        if line.startswith('From:'):
            from_user.append(line.split()[1].split('@')[0])
            from_host.append(line.split()[1].split('@')[1])
        elif line.startswith('To:'):
            to_user.append(line.split()[1].split('@')[0])
            to_host.append(line.split()[1].split('@')[1])
fu, fh, tu, th = Counter(from_user), Counter(from_host), Counter(to_user), Counter(to_host)
print('--- FROM USER ---')
[print(k, v, sep=',') for k, v in sorted(fu.most_common())]
print('--- FROM HOST ---')
[print(k, v, sep=',') for k, v in sorted(fh.most_common())]
print('--- TO USER ---')
[print(k, v, sep=',') for k, v in sorted(tu.most_common())]
print('--- TO HOST ---')
[print(k, v, sep=',') for k, v in sorted(th.most_common())]
