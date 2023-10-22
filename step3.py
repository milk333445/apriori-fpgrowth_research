from pyfpgrowth import *
import pandas as pd
from 資料處理 import dataFromFile_for_task1
from apriori import *
from Task1 import *
import time
import os
import re

def convert_to_list_of_lists(itemsets):
    result = []
    for itemset in itemsets:
        result.append(list(itemset))
    return result

def runFPGrowth(data_iter, minSupport):
    """
    run the FP-Growth algorithm. data_iter is a record iterator
    Return:
     - items (tuple, support)
    """
    itemSet, transactionList = getItemSetTransactionList(data_iter)
    
    itemSet = convert_to_list_of_lists(itemSet)
    start_time = time.time()
    patterns = find_frequent_patterns(transactionList, minSupport*len(transactionList))
    elapsed_time = time.time() - start_time
    toRetItems = []
    for itemset, support in patterns.items():
        toRetItems.append((tuple(itemset), support/len(transactionList)))
    # support由大到小排序
    toRetItems.sort(key=lambda x: x[1], reverse=True)
    return toRetItems, elapsed_time

def main(csv_file_path, minSupport, step, dataset, task, result):
    infile = dataFromFile_for_task1(csv_file_path)
    if result == 1:
        toRetItems, elapsed_time = runFPGrowth(infile, minSupport)
        output_filename = generate_result_filename(step, task, dataset, minSupport, result)
        output_filename = f'./output_in_step{step}/{output_filename}'
        save_frequent_itemsets_to_txt(output_filename, toRetItems)
        print(f"Elapsed time: {elapsed_time} seconds")
    else:
        pass
    
    return toRetItems
    
def parse_arguments():
    parser = argparse.ArgumentParser(description="Your program description here")
    parser.add_argument("--dataset", type=str, default="C", help="Specify the dataset letter (e.g., 'C')")
    parser.add_argument("--min_support", type=float, default=0.01, help="Specify the minimum support value")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_arguments()
    dataset = args.dataset
    minSupport = args.min_support
    csv_file_path = f'./datasets_hw1/dataset_{dataset}/dataset_{dataset}.csv'
    step = 3
    task = 1
    result = 1
    toRetItems = main(csv_file_path, minSupport, step, dataset, task, result)
    
    
    
        

    
    