import csv
import numpy as np

def clean():
    with open('test.csv') as raw:
        reader = csv.reader(raw)
        write(list(reader), 'test_clean.csv')

def write(reader, out):
    my_file = open(out, 'w')
    with my_file:
        writer = csv.writer(my_file)
        writer.writerows(np.array(reader)[1:140000,[-2,-1]])

if __name__ == '__main__':
    clean()
