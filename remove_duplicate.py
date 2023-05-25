import os
from datetime import datetime

from difPy import dif

search = dif("S:\\Elib")
start = datetime.now()
locations = search.result.values()
end = datetime.now()
diff = end - start
print(f'finished check duplicate {diff.seconds}')
print(f'duplicate items: {len(search.result)}')

for i in search.result:
    filename = search.result[i]['location']
    head, tail = os.path.split(filename)
    if 'renamed' in filename:
        for j in search.result[i]['matches']:
            os.remove(search.result[i]['matches'][j]['location'])
    else:
        for j in search.result[i]['matches']:
            matched_name = search.result[i]['matches'][j]['location']
            should = False
            if 'renamed' in matched_name:
                should = True
            else:
                os.remove(search.result[i]['matches'][j]['location'])
            if should:
                os.remove(filename)

end1 = datetime.now()
diff = end - end1
print(f'finished remove {diff.seconds}')
