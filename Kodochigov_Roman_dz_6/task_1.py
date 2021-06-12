from itertools import zip_longest
ip_list = []
method_list = []
link_list = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        content = line.split(' ')
        ip_list.append(content[0])
        method_list.append(content[5].replace('"', ''))
        link_list.append(content[6])
output_list = [i for i in zip_longest(ip_list, method_list, link_list)]
