import csv

# directory = './results'

# for filename in directory:
#     with open(filename, 'rb') as f:
#         reader = csv.reader(f)
        
#         next(reader) # to skip header

#         numbers = [float(row[range(1, 6)]) for row in reader]

#         average = sum(numbers)/len(numbers)


with open('./results/FG_Counting-Fingers_BG_Complex_copy.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    data_list = list(reader)
    rows = [''] + ['{:.15f}'.format(sum(float(x) for x in y) / len(data_list)) for y in list(zip(*data_list))[1:]] # with a 15 decimal accuracy
    average_data_list = [header] + [rows]

    print(rows)

    rows[0] = 'Average'

    print(rows)


    # append the new data to the file
    with open('./results/FG_Counting-Fingers_BG_Complex_copy.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(rows)
