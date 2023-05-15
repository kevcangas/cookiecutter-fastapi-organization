import subprocess
import time

#Virtual environemnt
print("\033[1;34m"+"Creating virtual environment..."+"\033[0;m")
subprocess.run(['py','-m','venv','venv'])
print("\033[1;34m"+"Virtual environment created"+"\033[0;m")
time.sleep(3)


#Begin repository
print("\033[1;34m"+"Starting repository..."+"\033[0;m")
subprocess.run(['git','init'])
print("\033[1;34m"+"Repository ready"+"\033[0;m")
