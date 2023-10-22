import csv
from apriori import *
def dataFromFile_for_task1(fname):
    """Function which reads from the file and yields a generator"""
    with open(fname, "rU") as file_iter:
        for line in file_iter:
            line = line.strip().rstrip(",")  # Remove trailing comma
            line = ",".join(line.split(",")[2:])
            record = frozenset(line.split(","))
            yield record

def process_dataset(dataset_name):
    # 資料檔案路徑
    file_path = fr'C:\Users\User\data_mining\datasets_hw1\{dataset_name}\{dataset_name}.data'
    formatted_contents = []
    with open(file_path, 'r') as f:
        for line in f:
            fields = line.strip().split(",")  # Split by comma and remove newline characters
            formatted_contents.append("  ".join(fields))

    # 轉換成 CSV 格式
    csv_file_path = fr'C:\Users\User\data_mining\datasets_hw1\{dataset_name}\{dataset_name}.csv'
    with open(csv_file_path, 'w', newline='') as csvfile:
        for line in formatted_contents:
            csvfile.write(line.replace(' ', ',') + '\r')
            

def main():
    dataset_name = input("請輸入資料集名稱 (dataset_A, dataset_B, dataset_C): ")
    process_dataset(dataset_name)

if __name__ == "__main__":
    main()
