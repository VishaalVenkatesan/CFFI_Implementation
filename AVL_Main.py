import time
from AVL_Module import ffi, lib

root = ffi.NULL  # Initialize root as a NULL pointer
start = time.time()
for i in range(0, 20000):
    root = lib.RInsert(root, i)

end = time.time()



print("This operation took", end - start, "seconds")







    
