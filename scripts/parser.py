import argparse
import re
import datetime
import os
import numpy
import json


# python parser.py --start 2021-04-18_03:33:00 --end 2021-04-18_03:33:06 --work_dir ../results


def main():
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--start')
    args_parser.add_argument('--end')
    args_parser.add_argument('--work_dir')
    args = args_parser.parse_args()

    start_time = datetime.datetime.strptime(args.start, "%Y-%m-%d_%H:%M:%S")
    end_time = datetime.datetime.strptime(args.end, "%Y-%m-%d_%H:%M:%S")

    result_files = ['gpu.txt', 'cpu.txt', 'ram.txt']

    report = dict()
    for file in result_files:
        report[file] = performance_report(file, args.work_dir, start_time, end_time)

    with open(os.path.join(args.work_dir, 'report.json'), "w") as f:
        json.dump(report, f, indent=4)




def performance_report(file_name, work_dir, start_time, end_time):
    file_path = os.path.join(work_dir, file_name)
    with open(file_path, "r") as f:
        file_text_list = re.findall(r'(\S*?): (\d+.\d)\n', f.read())

    datetime_percent = [(datetime.datetime.strptime(time, "%Y-%m-%d_%H:%M:%S"), float(percent)) for time, percent in
                        file_text_list]
    filtered_percents = [percent for time, percent in datetime_percent if start_time <= time <= end_time]

    result = dict()
    # result['file_name'] = file_name
    result['start'] = start_time.strftime('%Y-%m-%d %H:%M:%S')
    result['end'] = end_time.strftime('%Y-%m-%d %H:%M:%S')
    result['min'] = round(min(filtered_percents), 1)
    result['max'] = round(max(filtered_percents), 1)
    result['mean'] = round(numpy.mean(filtered_percents), 1)
    return result


if __name__ == "__main__":
    main()
