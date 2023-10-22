import pandas as pd
from 資料處理 import dataFromFile_for_task1
from apriori import *
import time
import os
import re
from Task1 import *

def parse_arguments():
    parser = argparse.ArgumentParser(description="Your program description here")
    parser.add_argument("--dataset", type=str, default="C", help="Specify the dataset letter (e.g., 'C')")
    parser.add_argument("--min_support", type=float, default=0.01, help="Specify the minimum support value")
    args = parser.parse_args()
    return args
    
def main(csv_file_path, minSupport, minConfidence, step, dataset, task, result):
    infile = dataFromFile_for_task1(csv_file_path)
    frequent_closed_itemsets, elapsed_time = runApriori_for_frequent_closed_itemsets(infile, minSupport, minConfidence)
    print(f"Elapsed time: {elapsed_time} seconds")
    total_itemsets = len(frequent_closed_itemsets)
    output_filename = generate_result_filename(step, task, dataset, min_support, 1)
    output_filename = f'./output_in_step{step}/{output_filename}'
    save_frequent_itemsets_to_txt(output_filename, frequent_closed_itemsets, total_itemsets)

if __name__ == "__main__":
    args = parse_arguments()
    dataset = args.dataset
    min_support = args.min_support
    step = 2
    task = 2
    #file_path = f'./output_in_step2/Task1/itemset_list/step2_task1_{dataset}_{min_support}_result1.txt'
    csv_file_path = f'./datasets_hw1/dataset_{dataset}/dataset_{dataset}.csv'
    main(csv_file_path, min_support, 0.05, step, dataset, task, 1)
    
    
    
    """
    frequent_closed_itemsets, elapsed_time = runApriori_for_frequent_closed_itemsets(file_path)
    print(f"Elapsed time: {elapsed_time} seconds")
    total_itemsets = len(frequent_closed_itemsets)
    output_filename = generate_result_filename(step, task, dataset, min_support, 1)
    output_filename = f'./output_in_step{step}/{output_filename}'
    save_frequent_itemsets_to_txt(output_filename, frequent_closed_itemsets, total_itemsets)
    """
    