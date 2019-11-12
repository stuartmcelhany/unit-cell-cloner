# Stuart McElhany
import csv

# triclinic unit cell
UNIT_DIST_X = [17.53, 0.0, 0.0] # x translation
UNIT_DIST_Y = [8.765, 15.182, 0.0] # y translation
UNIT_DIST_Z = [8.765, 5.061, 14.313] # z translation

results = []

print("Enter file name (.xyz)") # file io
filename = input()

print("Enter cube length")
n = int(input())

molecule_name = []

with open(filename) as File:
    reader = csv.reader(File, delimiter = ' ', lineterminator = '\n')
    next(reader) # skips atom count line
    molecule_name = next(reader) # skips comment line per .xyz convention
    atom_count = 0
    for row in reader:
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    row_entry = [""]*4
                    row_entry[0] = row[0] #get atom
                    row_entry[1] = "{:.4f}".format(float(row[1]) + float(i*UNIT_DIST_X[0]) + float(j*UNIT_DIST_Y[0]) + float(k*UNIT_DIST_Z[0])) # get x
                    row_entry[2] = "{:.4f}".format(float(row[2]) + float(i*UNIT_DIST_X[1]) + float(j*UNIT_DIST_Y[1]) + float(k*UNIT_DIST_Z[1])) # get y
                    row_entry[3] = "{:.4f}".format(float(row[3]) + float(i*UNIT_DIST_X[2]) + float(j*UNIT_DIST_Y[2]) + float(k*UNIT_DIST_Z[2])) # get z
                    atom_count += 1
                    results.append(row_entry)

filename = filename.replace('.xyz' , '') # adds .xyz to new file name
output_file = filename + str(n) + 'x' + str(n) + 'x' + str(n) + '.xyz'
with open(output_file, 'w') as File:
    writer = csv.writer(File, delimiter = ' ', lineterminator = '\n')
    writer.writerow([atom_count]) # write atom count line
    writer.writerow(molecule_name) # write comment line
    writer.writerows(results) # fill in rest of data