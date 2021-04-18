import subprocess

print(">>> start.py started")

with open("flag.txt", "w") as f:
    f.write('True')

subprocess.Popen(["python", "monitoring.py", "--delay", "0.5"])
subprocess.call('blender C:\TestResources\BaseLightTest.blend')

with open("flag.txt", "w") as f:
    f.write('False')

print(">>> start.py finished")
