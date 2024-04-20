import csv

files = ["./avg_price.csv",	
        "./GDP.csv", 
        "./gov_exp.csv",
        "./Population.csv",					
        "./CPI.csv"]

merge_csv = "./output.csv"
result = []
flag = False
length = 0
for file in files:
    with open(file, "r") as fi:
        reader = csv.reader(fi)
        if not flag:
            for row in reader:
                result.append(row)
                length += 1
            flag = True
        else:
            for idx, row in zip(range(length), reader):
                result[idx].append(row[1])

with open(merge_csv, "w") as fo:
    writer = csv.writer(fo)
    writer.writerows(result)

        