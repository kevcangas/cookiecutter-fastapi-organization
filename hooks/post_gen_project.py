import subprocess
import time

#Entorno Virtual
print("\033[1;34m"+"Installing template..."+"\033[0;m")
subprocess.run('pip install -e ./', shell=True)
print("\033[1;34m"+"Template installed succesfully"+"\033[0;m")