import pandas as pd
from 資料處理 import dataFromFile_for_task1
from apriori import *
import time
import argparse
def generate_result_filename(step, task, dataset, min_support, result):
    filename = f"step{step}_task{task}_{dataset}_{min_support}_result{result}.txt"
    return filename

def save_frequent_itemsets_to_txt(filename, frequent_itemsets, total_itemsets=None):
    with open(filename, 'w') as file:
        if total_itemsets:
            file.write(f"[{total_itemsets}]\n")
        for item, support in sorted(frequent_itemsets, key=lambda x: x[1], reverse=True):
            support_percentage = round(support * 100, 1)
            file.write(f"[{support_percentage}%]\t{str(item)}\n")

def main(csv_file_path, min_support, min_confidence, step, dataset, task, result):
    infile = dataFromFile_for_task1(csv_file_path)
    if result == 1:
        start_time = time.time()
        items, rules, freqSet = runApriori(infile, min_support, min_confidence)
        elapsed_time = time.time() - start_time
        print(f"Elapsed time: {elapsed_time} seconds")
        output_filename = generate_result_filename(step, task, dataset, min_support, result)
        output_filename = f'./output_in_step{step}/{output_filename}'
        save_frequent_itemsets_to_txt(output_filename, items)
    elif result == 2: 
        output_filename = generate_result_filename(step, task, dataset, min_support, result)
        output_filename = f'./output_in_step{step}/{output_filename}'
        start_time = time.time()
        items, rules = runApriori_for_task1_2(infile, min_support, min_confidence, output_filename)
        elapsed_time = time.time() - start_time
        print(f"Elapsed time: {elapsed_time} seconds")
    else:
        print("Task must be 1 or 2")
        return

def parse_arguments():
    parser = argparse.ArgumentParser(description="Your program description here")
    parser.add_argument("--dataset", type=str, default="C", help="Specify the dataset letter (e.g., 'C')")
    parser.add_argument("--min_support", type=float, default=0.01, help="Specify the minimum support value")
    parser.add_argument("--result", type=int, default=1, help="Specify the result number (e.g., 1)")
    args = parser.parse_args()
    return args
    
       

if __name__ == "__main__":
    args = parse_arguments()
    dataset = args.dataset
    min_support = args.min_support
    result = args.result
    csv_file_path = f'./datasets_hw1/dataset_{dataset}/dataset_{dataset}.csv'
    min_confidence = 0.05
    step = 2
    task = 1
    main(csv_file_path, min_support, min_confidence, step, dataset, task, result)
