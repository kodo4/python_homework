ip_list = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        content = line.split(' ')
        ip_list.append(content[0])

my_dict = {i: 0 for i in ip_list}
for i in ip_list:
    if i in my_dict:
        my_dict[i] += 1
list_my_dict = list(my_dict.items())
list_my_dict.sort(key=lambda i: i[1])
print(list_my_dict[-1])
