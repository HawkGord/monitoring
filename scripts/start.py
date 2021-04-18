import subprocess
print(">>> start.py start")


with open("flag.txt", "w") as f:
    f.write('True')


subprocess.Popen(["python", 'monitoring.py'])
subprocess.call('blender C:\TestResources\BaseLightTest.blend')


with open("flag.txt", "w") as f:
    f.write('False')

print(">>> start.py finish")
