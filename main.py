# Stuart McElhany
import csv
import math

# trigonal unit cell dimensions
SIDE_LENGTH = 17.516
ANGLE = 60 * (math.pi/180) # first number in degrees

# creates primitive vectors for trigonal cell
PRIM_VEC_X = [SIDE_LENGTH, 0.0, 0.0] # x translation (x, y, z)
PRIM_VEC_Y = [SIDE_LENGTH*math.cos(ANGLE), SIDE_LENGTH*math.sin(ANGLE), 0.0] # y translation
cx = SIDE_LENGTH*math.cos(ANGLE)
cy = SIDE_LENGTH*(math.cos(ANGLE)-math.cos(ANGLE)**2)/math.sin(ANGLE)
PRIM_VEC_Z = [cx, cy, math.sqrt(SIDE_LENGTH**2-cx**2-cy**2)] # z translation

results = []

def clean_row_up(row):
    for value in list(row):
        if value == '':
            row.remove(value)
    return row

print("Enter file name (.xyz)") # file io
filename = input()

molecule_name = []

with open(filename) as File:
    reader = csv.reader(File, delimiter = ' ', lineterminator = '\n')
    next(reader) # skips atom count line
    molecule_name = next(reader) # skips comment line per .xyz convention
    atom_count = 0
    for row in reader:
        row = clean_row_up(row)
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    row_entry = [""]*4
                    row_entry[0] = row[0] #get atom
                    row_entry[1] = "{:.4f}".format(float(row[1]) + float((i-1)*PRIM_VEC_X[0]) + float((j-1)*PRIM_VEC_Y[0]) + float((k-1)*PRIM_VEC_Z[0])) # get x
                    row_entry[2] = "{:.4f}".format(float(row[2]) + float((i-1)*PRIM_VEC_X[1]) + float((j-1)*PRIM_VEC_Y[1]) + float((k-1)*PRIM_VEC_Z[1])) # get y
                    row_entry[3] = "{:.4f}".format(float(row[3]) + float((i-1)*PRIM_VEC_X[2]) + float((j-1)*PRIM_VEC_Y[2]) + float((k-1)*PRIM_VEC_Z[2])) # get z
                    atom_count += 1
                    results.append(row_entry)

filename = filename.replace('.xyz' , '') # adds .xyz to new file name
output_file = filename + str('-3x3x3') + '.xyz'
with open(output_file, 'w') as File:
    writer = csv.writer(File, delimiter = ' ', lineterminator = '\n')
    writer.writerow([atom_count]) # write atom count line
    writer.writerow(molecule_name) # write comment line
    writer.writerows(results) # fill in rest of data
