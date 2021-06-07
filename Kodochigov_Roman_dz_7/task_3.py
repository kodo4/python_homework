import os
import shutil

project_name = 'my_project'
templates = 'templates'

for root, dirs, files in os.walk(project_name):
    if templates in dirs and root != project_name:
        for entry in os.listdir(os.path.join(root, templates)):
            if not os.path.exists(os.path.join(project_name, templates, os.path.basename(root))):
                shutil.copytree(os.path.join(root, templates, entry),
                                os.path.join(project_name, templates, os.path.basename(root)))
