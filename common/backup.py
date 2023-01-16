import os
import shutil
from datetime import datetime

def backup():
    source = '/path/to/source'
    destination = '/path/to/destination'
    now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    backup_name = 'backup_' + now + '.zip'
    shutil.make_archive(backup_name, 'zip', source)
    shutil.move(backup_name + '.zip', destination)
    print(f'Backup created: {backup_name}')

backup()
