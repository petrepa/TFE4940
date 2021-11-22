import csv
import os

directory = 'results/'

for filename in os.listdir(directory):
    file = directory + filename
    
    with open(file, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        data_list = list(reader)
        rows = [''] + ['{:.15f}'.format(sum(float(x) for x in y) / len(data_list)) for y in list(zip(*data_list))[1:]] # with a 15 decimal accuracy
        average_data_list = [header] + [rows]

        print(rows)

        rows[0] = 'Average'

        print(rows)


        # append the new data to the file
        with open(file, 'a', newline='') as file_write:
            writer = csv.writer(file_write)
            writer.writerow(rows)


# with open('results/FG_Counting-Fingers_BG_Window.csv', 'r') as f:
#     reader = csv.reader(f)
#     header = next(reader)
#     data_list = list(reader)
#     rows = [''] + ['{:.15f}'.format(sum(float(x) for x in y) / len(data_list)) for y in list(zip(*data_list))[1:]] # with a 15 decimal accuracy
#     average_data_list = [header] + [rows]

#     print(rows)

#     rows[0] = 'Average'

#     print(rows)


#     # append the new data to the file
#     with open('results/FG_Counting-Fingers_BG_Window.csv', 'a', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(rows)
