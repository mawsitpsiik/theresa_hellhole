import LCD1602 as L6
import subprocess

L6.init(0x27, 1)

pike = subprocess.check_output(["hostname", "-I"]).decode('utf-8').strip()
print(pike)

L6.write(0,0,pike)

