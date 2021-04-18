import psutil
import GPUtil
import datetime
import time


def main():
    with open("flag.txt", "w") as f:
        f.write('True')

    flag = True
    with open('mem/cpu.txt', 'w') as c, open('mem/ram.txt', 'w') as r, open('mem/gpu.txt', 'w') as g:
        while flag:
            get_time = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
            c.write(get_time+': '+str(psutil.cpu_percent())+'\n')
            r.write(get_time+': '+str(psutil.virtual_memory().percent)+'\n')
            g.write(get_time+': '+str(GPUtil.getGPUs()[0].load*100)+'\n')
            with open('flag.txt', 'r') as f:
                if f.read() == "False":
                    flag = False
            time.sleep(1)


# if __name__ == "main":
print('>>> monitoring.py start')
main()
print(">>> monitoring.py finish")
