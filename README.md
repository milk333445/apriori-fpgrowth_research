# Apriori v.s FP-Growth

## Introduction
- In the field of data mining and association analysis, Apriori and FP-Growth are two commonly used algorithms for discovering associations among sets of items. These algorithms have wide-ranging applications in uncovering relationships among items, such as market basket analysis, recommendation systems, bioinformatics, and more. In this report, we will compare the performance of these two algorithms under different dataset sizes, with a particular focus on their execution times. We have selected three datasets of varying magnitudes, including small, medium, and large datasets, to evaluate the performance of these algorithms in handling data of different scales. This comparison will help us gain a better understanding of when to choose Apriori or FP-Growth in practical applications and how to optimize their performance.

- You can find more detailed results in the "apriori_fpgrowth_compare_Report.pdf" document.
## Program Execution Instructions

### Step II: Apriori Program Execution Instructions
- Apriori is primarily handled by the Task1.py file, and the execution steps are as follows:
```python=
python Task1.py --dataset A --min_support 0.002 --result 1
```
  - Generates the frequent dataset.txt for dataset A with a minimum support of 0.002 in the output_in_step2 folder. The command line will output the execution time (in seconds).
```python=
python Task1.py --dataset A --min_support 0.002 --result 2
```
  - Generates the statistical data.txt for dataset A with a minimum support of 0.002 in the output_in_step2 folder. The command line will output the execution time (in seconds).
- Apriori Frequent Closed Itemset is mainly processed by the Task2.py file, and the execution steps are as follows:
```python=
python Task2.py --dataset A --min_support 0.002
```
  - Generates the frequent dataset.txt for dataset A with a minimum support of 0.002 in the output_in_step2 folder. The command line will output the execution time (in seconds).
### Step III: FP-Growth Program Execution Instructions
- FP-Growth is primarily handled by the step3.py file, and the execution steps are as follows:
```python=
python step3.py --dataset A --min_support 0.002
```
  - enerates the frequent dataset.txt for dataset A with a minimum support of 0.002 in the output_in_step3 folder. The command line will output the execution time (in seconds).
