import csv

with open("/Users/kirangunturu/Documents/WEEK12-SPARK/orders_new.csv", 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # next(csv_reader) # skip header / first line

    for line in csv_reader:
        print(line[1])  # reqd columns based on index

### read and write


with open("/Users/kirangunturu/Documents/WEEK12-SPARK/orders_new.csv", 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open("/Users/kirangunturu/Documents/WEEK12-SPARK/orders_new_123.csv",'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='_')

        for line in csv_reader:
            csv_writer.writerow(line)