import os
import shutil


dest = os.environ['ST_PLUGIN_DEST']
files = ['ledger_core.py', 'ledger_plugin.py']

for file in files:
    destfile = os.path.join(dest, file)
    shutil.copyfile(file, destfile)