from itertools import combinations_with_replacement

a, r = input().split()
[print(item) for item in (list([''.join(item) for item in list(combinations_with_replacement(sorted(a),int(r)))]))]
