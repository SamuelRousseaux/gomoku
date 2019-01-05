import os

os.system("pip install pyinstaller")
os.system("pyinstaller pbrain_main.py pbrain_ai.py pbrain_checks.py pbrain_misc.py --name pbrain-PARIS-Rousseaux.Samuel.exe --onefile")
os.system('copy .\\dist\\pbrain-PARIS-ROUSSEAUX.SAMUEL.exe .')