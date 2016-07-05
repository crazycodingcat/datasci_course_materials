import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    person = record[0]
    friend = record[1]
    mr.emit_intermediate(tuple(sorted(record)), record)

def reducer(key, list_of_values):
    if len(list_of_values) == 1: #asymmetric
        person = list_of_values[0][0]
        friend = list_of_values[0][1]
        mr.emit((friend, person))
        mr.emit((person, friend))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
