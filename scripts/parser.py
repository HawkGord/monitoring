import argparse
import re
import datetime
#python parser.py --start 2021-04-18_03:33:00 --end 2021-04-18_03:33:06

args_parser = argparse.ArgumentParser()
args_parser.add_argument('--start')
args_parser.add_argument('--end')
args = args_parser.parse_args()

print(repr(args.start))
print(repr(args.end))

start_time = datetime.datetime.strptime(args.start, "%Y-%m-%d_%H:%M:%S")
end_time = datetime.datetime.strptime(args.end, "%Y-%m-%d_%H:%M:%S")

with open("mem/gpu.txt", "r") as gpu:
    a = gpu.read()

print(a)

fa = re.findall(r'(\S*?): (\d+.\d)\n',a)
print(fa)
final_list = [(datetime.datetime.strptime(time, "%Y-%m-%d_%H:%M:%S"), percent) for time, percent in fa]

res = [percent for time, percent in final_list if start_time < time < end_time]
print(res)

