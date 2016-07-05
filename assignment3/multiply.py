import MapReduce
import sys


mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    matrix = record[0]
    value = record[3]
    if matrix == 'a':
      i = record[1]
      j = record[2]
      for k in range(5):
        mr.emit_intermediate((i, k), ('a', j, value))
    elif matrix == 'b':
      j = record[1]
      k = record[2]
      for i in range(5):
        mr.emit_intermediate((i, k), ('b', j, value))

def reducer(key, list_of_values):
    hash_a = {v[1]: v[2] for v in list_of_values if v[0] == 'a'}
    hash_b = {v[1]: v[2] for v in list_of_values if v[0] == 'b'}
    sums = 0
    for i in range(5):
      try:
        tmp = hash_a[i] * hash_b[i]
      except KeyError:
        tmp = 0
      sums += tmp
    mr.emit((key[0], key[1], sums))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
