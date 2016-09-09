# Enter your code here. Read input from STDIN. Print output to STDOUT
num_students = int(raw_input())
for i in range(0,num_students):
    record = raw_input()
    split_record = record.split()
    key = split_record[0]
    if i == 0:
        records = {key:split_record[1:]}
    else:
        records[key] = split_record[1:]             
query = raw_input()
score_list = records[query]
sum = float(score_list[0]) + float(score_list[1]) + float(score_list[2])
mean = sum / 3
print '{:.2f}'.format(mean)