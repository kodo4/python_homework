import os
from collections import defaultdict

import django

root_dir = django.__path__[0]
django_files = defaultdict(int)

for root, dirs, files in os.walk(root_dir):
    for file in files:
        size = int(os.stat(os.path.join(root, file)).st_size)

        if 0 <= size <= 10:
            django_files[10] += 1
        elif 10 < size <= 100:
            django_files[100] += 1
        elif 100 < size <= 1000:
            django_files[1000] += 1
        elif 1000 < size <= 10000:
            django_files[10000] += 1
        elif 10000 < size <= 100000:
            django_files[100000] += 1
        else:
            django_files[1000000] += 1

for key, value in sorted(django_files.items()):
    print(f'{key}: {value}')
