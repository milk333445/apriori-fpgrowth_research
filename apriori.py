"""
Description     : Simple Python implementation of the Apriori Algorithm

Usage:
    $python apriori.py -f DATASET.csv -s minSupport  -c minConfidence

    $python apriori.py -f DATASET.csv -s 0.15 -c 0.6
"""

import sys
import os
import re
from itertools import chain, combinations
from collections import defaultdict
from optparse import OptionParser
import time


def subsets(arr):
    """ Returns non empty subsets of arr"""
    return chain(*[combinations(arr, i + 1) for i, a in enumerate(arr)])


def returnItemsWithMinSupport(itemSet, transactionList, minSupport, freqSet):
    """calculates the support for items in the itemSet and returns a subset
    of the itemSet each of whose elements satisfies the minimum support"""
    _itemSet = set()
    localSet = defaultdict(int)

    for item in itemSet:
        for transaction in transactionList:
            if item.issubset(transaction):
                freqSet[item] += 1
                localSet[item] += 1

    for item, count in localSet.items():
        support = float(count) / len(transactionList)

        if support >= minSupport:
            _itemSet.add(item)

    return _itemSet


def joinSet(itemSet, length):
    """Join a set with itself and returns the n-element itemsets"""
    return set(
        [i.union(j) for i in itemSet for j in itemSet if len(i.union(j)) == length]
    )


def getItemSetTransactionList(data_iterator):
    transactionList = list()
    itemSet = set()
    for record in data_iterator:
        transaction = frozenset(record)
        transactionList.append(transaction)
        for item in transaction:
            itemSet.add(frozenset([item]))  # Generate 1-itemSets
    return itemSet, transactionList


def runApriori(data_iter, minSupport, minConfidence):
    """
    run the apriori algorithm. data_iter is a record iterator
    Return both:
     - items (tuple, support)
     - rules ((pretuple, posttuple), confidence)
    """
    itemSet, transactionList = getItemSetTransactionList(data_iter)

    freqSet = defaultdict(int)
    largeSet = dict()
    # Global dictionary which stores (key=n-itemSets,value=support)
    # which satisfy minSupport

    assocRules = dict()
    # Dictionary which stores Association Rules

    oneCSet = returnItemsWithMinSupport(itemSet, transactionList, minSupport, freqSet)

    currentLSet = oneCSet
    k = 2
    while currentLSet != set([]):
        largeSet[k - 1] = currentLSet
        currentLSet = joinSet(currentLSet, k)
        currentCSet = returnItemsWithMinSupport(
            currentLSet, transactionList, minSupport, freqSet
        )
        currentLSet = currentCSet
        k = k + 1

    def getSupport(item):
        """local function which Returns the support of an item"""
        return float(freqSet[item]) / len(transactionList)

    toRetItems = []
    for key, value in largeSet.items():
        toRetItems.extend([(tuple(item), getSupport(item)) for item in value])

    toRetRules = []
    for key, value in list(largeSet.items())[1:]:
        for item in value:
            _subsets = map(frozenset, [x for x in subsets(item)])
            for element in _subsets:
                remain = item.difference(element)
                if len(remain) > 0:
                    confidence = getSupport(item) / getSupport(element)
                    if confidence >= minConfidence:
                        toRetRules.append(((tuple(element), tuple(remain)), confidence))
    return toRetItems, toRetRules, freqSet


def printResults(items, rules):
    """prints the generated itemsets sorted by support and the confidence rules sorted by confidence"""
    for item, support in sorted(items, key=lambda x: x[1]):
        print("item: %s , %.3f" % (str(item), support))
    print("\n------------------------ RULES:")
    for rule, confidence in sorted(rules, key=lambda x: x[1]):
        pre, post = rule
        print("Rule: %s ==> %s , %.3f" % (str(pre), str(post), confidence))


def to_str_results(items, rules):
    """prints the generated itemsets sorted by support and the confidence rules sorted by confidence"""
    i, r = [], []
    for item, support in sorted(items, key=lambda x: x[1]):
        x = "item: %s , %.3f" % (str(item), support)
        i.append(x)

    for rule, confidence in sorted(rules, key=lambda x: x[1]):
        pre, post = rule
        x = "Rule: %s ==> %s , %.3f" % (str(pre), str(post), confidence)
        r.append(x)

    return i, r


def dataFromFile(fname):
    """Function which reads from the file and yields a generator"""
    with open(fname, "rU") as file_iter:
        for line in file_iter:
            line = line.strip().rstrip(",")  # Remove trailing comma
            record = frozenset(line.split(","))
            yield record


def runApriori_for_task1_2(data_iter, minSupport, minConfidence, output_filename):
    """
    run the apriori algorithm. data_iter is a record iterator
    Return both:
     - items (tuple, support)
     - rules ((pretuple, posttuple), confidence)
    """
    itemSet, transactionList = getItemSetTransactionList(data_iter)

    freqSet = defaultdict(int)
    largeSet = dict()
    # Global dictionary which stores (key=n-itemSets,value=support)
    # which satisfy minSupport

    assocRules = dict()
    # Dictionary which stores Association Rules

    oneCSet = returnItemsWithMinSupport(itemSet, transactionList, minSupport, freqSet)

    currentLSet = oneCSet
    k = 2
    iteration = 0 # for task1_2
    with open(output_filename, 'w') as output_file:
        while currentLSet != set([]):
            largeSet[k - 1] = currentLSet
            currentLSet = joinSet(currentLSet, k)
            # 剪枝前的候選集數量
            num_candidates_before_pruning = len(currentLSet)
            
            
            currentCSet = returnItemsWithMinSupport(
                currentLSet, transactionList, minSupport, freqSet
            )
            
            # 剪枝後的候選集數量
            num_candidates_after_pruning = len(currentCSet)
            
            currentLSet = currentCSet
            k = k + 1
            iteration += 1
            
            # 印出每一次的候選集數量
            #print(f'Iteration {iteration}:')
            #print(f'Before pruning: {num_candidates_before_pruning} candidates')
            #print(f'After pruning: {num_candidates_after_pruning} candidates')
            
            
            
            # 寫入檔案
            output_file.write(f'{iteration}\t{num_candidates_before_pruning}\t{num_candidates_after_pruning}\n')
        output_file.close()
        
    

    def getSupport(item):
        """local function which Returns the support of an item"""
        return float(freqSet[item]) / len(transactionList)

    toRetItems = []
    for key, value in largeSet.items():
        toRetItems.extend([(tuple(item), getSupport(item)) for item in value])
    total_frequent_itemsets = len(toRetItems)   
    
    # 將frequent itemsets數量寫入檔案
    with open(output_filename, 'a') as output_file:  
        output_file.write(f'[{total_frequent_itemsets}]\n')
        output_file.close()
    # 將最後一行的候選集數量換到第一行
    with open(output_filename, 'r') as file:
        data = file.readlines()
    last_line = data[-1]
    data.pop(-1)
    data.insert(0, last_line)
    with open(output_filename, 'w') as file:
        file.writelines(data)
    #print(f'Total frequent itemsets: {total_frequent_itemsets}')

    toRetRules = []
    for key, value in list(largeSet.items())[1:]:
        for item in value:
            _subsets = map(frozenset, [x for x in subsets(item)])
            for element in _subsets:
                remain = item.difference(element)
                if len(remain) > 0:
                    confidence = getSupport(item) / getSupport(element)
                    if confidence >= minConfidence:
                        toRetRules.append(((tuple(element), tuple(remain)), confidence))
    return toRetItems, toRetRules
    


# 定義freq closed itemsets
# 是否為closed itemsets
def is_closed(itemset, freqSet):
    item_support = freqSet[itemset]
    for frequent_itemset in freqSet:
        if itemset != frequent_itemset and itemset.issubset(frequent_itemset):
            if item_support <= freqSet[frequent_itemset]:
                return False
    return True

# 挖掘frequent closed itemsets

def runApriori_for_frequent_closed_itemsets(data_iter, minSupport, minConfidence):
    start_time = time.time()
    items, rules, freqSet = runApriori(data_iter, minSupport, minConfidence)
    freqSet = list_to_dict(items)
    frequent_closed_itemsets = []
    result_list = []
    for itemset in items:
        itemset = frozenset(itemset[0])
        if is_closed(itemset, freqSet):
            frequent_closed_itemsets.append((tuple(itemset), freqSet[itemset]))
    elapsed_time = time.time() - start_time
    return frequent_closed_itemsets, elapsed_time

def list_to_dict(items):
    freqSet = defaultdict(float)
    for itemset, support in items:
        freqSet[frozenset(itemset)] = float(support)
    return freqSet


def list_to_dict(items):
    freqSet = defaultdict(float)
    for itemset, support in items:
        freqSet[frozenset(itemset)] = float(support)
    return freqSet

def process_txt_file(file_path):
    result_list = []

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()  # 去除首尾空白字符
            if line:
                # 使用正则表达式来提取支持度百分比和项集
                match = re.match(r'\[(\d+\.\d+)%\]\s+\((.*?)\)', line)
                if match:
                    support_percentage = float(match.group(1)) / 100
                    itemset_str = match.group(2)
                    # 去除单引号和空格，然后将项集转换为元组
                    itemset = tuple(item.strip("' ") for item in itemset_str.split(','))
                    # 去除元组中的空字符串
                    itemset = tuple(item for item in itemset if item)
                    result_list.append((itemset, support_percentage))

    return result_list







if __name__ == "__main__":

    optparser = OptionParser()
    optparser.add_option(
        "-f", "--inputFile", dest="input", help="filename containing csv", default=None
    )
    optparser.add_option(
        "-s",
        "--minSupport",
        dest="minS",
        help="minimum support value",
        default=0.15,
        type="float",
    )
    optparser.add_option(
        "-c",
        "--minConfidence",
        dest="minC",
        help="minimum confidence value",
        default=0.6,
        type="float",
    )

    (options, args) = optparser.parse_args()

    inFile = None
    if options.input is None:
        inFile = sys.stdin
    elif options.input is not None:
        inFile = dataFromFile(options.input)
    else:
        print("No dataset filename specified, system with exit\n")
        sys.exit("System will exit")

    minSupport = options.minS
    minConfidence = options.minC

    items, rules = runApriori(inFile, minSupport, minConfidence)

    printResults(items, rules)
