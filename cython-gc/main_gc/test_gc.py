import gc  # Import the compiled Cython module

# Initialize the garbage collector
heap = gc.GCHeap()

# Allocate objects
obj1 = heap.allocate()
obj2 = heap.allocate()
obj3 = heap.allocate()

# Set up references
obj1.add_reference(obj2)
obj2.add_reference(obj3)

# Add roots
heap.add_root(obj1)

# Trigger garbage collection
print("Initial GC cycle:")
heap.gc()

# Break references and remove roots
obj1.remove_reference(obj2)
heap.remove_root(obj1)

# Trigger garbage collection again
print("\nAfter breaking references and removing roots:")
heap.gc()
