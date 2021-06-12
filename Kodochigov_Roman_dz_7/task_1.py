import os

my_list = ['settings', 'mainapp', 'adminapp', 'authapp']

folder = 'my_project'

if not os.path.exists(folder):
    os.mkdir(folder)
dir_path = os.path.join(folder)

for _ in range(len(my_list)):
    if not os.path.exists(os.path.join(folder, my_list[_])):
        os.mkdir(os.path.join(folder, my_list[_]))
