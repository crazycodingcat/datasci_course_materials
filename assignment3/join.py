import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[1]

    mr.emit_intermediate(key, (record[0], record))

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    result = []

    # Any more efficient algorithm??
    for v in list_of_values:
      for vv in list_of_values:
        if v[0] == "order" and vv[0] == "line_item":
          mr.emit(v[1] + vv[1])

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
