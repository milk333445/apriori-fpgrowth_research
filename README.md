# Apriori v.s FP-Growth

## Introduction
- In the field of data mining and association analysis, Apriori and FP-Growth are two commonly used algorithms for discovering associations among sets of items. These algorithms have wide-ranging applications in uncovering relationships among items, such as market basket analysis, recommendation systems, bioinformatics, and more. In this report, we will compare the performance of these two algorithms under different dataset sizes, with a particular focus on their execution times. We have selected three datasets of varying magnitudes, including small, medium, and large datasets, to evaluate the performance of these algorithms in handling data of different scales. This comparison will help us gain a better understanding of when to choose Apriori or FP-Growth in practical applications and how to optimize their performance.

- You can find more detailed results in the "apriori_fpgrowth_compare_Report.pdf" document.
## 程式運行說明

### 步驟Ⅱ:Apriori程式運行說明
- Task1 主要由 Task1.py 檔案處理，執行步驟如下:
```python=
python Task1.py --dataset A --min_support 0.002 --result 1
```
  - 生成 min_support 0.02, dataset A 的頻繁資料集.txt 到output_in_step2 這個資料夾中，command line 會輸出執行時間(秒)
```python=
python Task1.py --dataset A --min_support 0.002 --result 2
```
  - 生成 min_support 0.02, dataset A 的統計資料.txt 到output_in_step2 這個資料夾中，command line 會輸出執行時間(秒)
- Task2 主要由 Task2.py 檔案處理，執行步驟如下:
```python=
python Task2.py --dataset A --min_support 0.002
```
  - 生成 min_support 0.02, dataset A 的頻繁資料集.txt 到output_in_step2 這個資料夾中，command line 會輸出執行時間(秒)
### 步驟Ⅲ：FP-Growth程式運行說明
- 步驟Ⅲ主要由 step3.py 檔案處理，執行步驟如下:
```python=
python step3.py --dataset A --min_support 0.002
```
  - 生成 min_support 0.02, dataset A 的頻繁資料集.txt 到output_in_step3 這個資料夾中，command line 會輸出執行時間(秒)
