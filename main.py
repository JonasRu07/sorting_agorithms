import time as time

import setup
import sort_alg

print("Setup:")
list_ = setup.ordered_list(1, 100_000)
print("  list created")
list_ = setup.mix(list_)
print("  list mixed")
print("Sorting")
start_time = time.time()
list_ = sort_alg.insertion(list_)
sort_time = time.time() - start_time
print("Sorting completed in ", round(sort_time, 2), "sec")
print("Verification: ", setup.is_truly_sorted(list_))

10_000_000_000