import gc

print("Garbage collector: collected %d objects." % (gc.collect()))
print("Garbage collector: is enabled %s." % (str(gc.isenabled())))
