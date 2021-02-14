#!C:\Users\User\PycharmProjects\flower_project\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pypcapkit==0.13.3.post2','console_scripts','pcapkit'
__requires__ = 'pypcapkit==0.13.3.post2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pypcapkit==0.13.3.post2', 'console_scripts', 'pcapkit')()
    )
