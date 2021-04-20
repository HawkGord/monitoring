import psutil
import GPUtil
import datetime
import time
import argparse
import os
#python monitoring.py --delay 1


def main():
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--delay')
    args = args_parser.parse_args()

    delay = float(args.delay)

    with open("flag.txt", "w") as f:
        f.write('True')

    flag = True
    with open('../results/cpu.txt', 'w') as c, open('../results/ram.txt', 'w') as r, open('../results/gpu.txt',
                                                                                          'w') as g:
        while flag:
            # average operating time of one cycle 5/100 seconds
            get_time = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
            c.write(get_time + ': ' + str(psutil.cpu_percent()) + '\n')
            r.write(get_time + ': ' + str(psutil.virtual_memory().percent) + '\n')
            g.write(get_time + ': ' + str(GPUtil.getGPUs()[0].load * 100) + '\n')
            with open('flag.txt', 'r') as f:
                if f.read() == "False":
                    break

            time.sleep(delay)


if __name__ == "__main__":
    main()
    print("Monitoring finished")
