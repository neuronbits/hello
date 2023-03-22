import os

this_file_path = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(this_file_path)
ENTIRE_PROJECT_DIR = os.path.dirname (BASE_DIR)

email_path = os.path.join(BASE_DIR, 'templates', 'email.txt')

if not os.path.exists(email_path):
    print('This is not a valid path')
else:
    content = ''
    with open(email_path, 'r') as f:
        content = f.read()
    print(content.format(name='Justin'))

