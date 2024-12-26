import cython_gc

# Initialize the garbage collector
heap = cython_gc.GCHeap()

print("Allocating objects...")
obj1 = heap.allocate()
obj2 = heap.allocate()
obj3 = heap.allocate()
obj4 = heap.allocate()
obj5 = heap.allocate()
print(f"Allocated objects: obj1 ({id(obj1)}), obj2 ({id(obj2)}), obj3 ({id(obj3)}), obj4 ({id(obj4)}), obj5 ({id(obj5)})")


print("\nSetting up references...")
obj1.add_reference(obj2)
obj1.add_reference(obj3)
obj2.add_reference(obj4)
obj3.add_reference(obj4)
obj4.add_reference(obj5)



print(f"obj1 references: {[id(ref) for ref in obj1.get_references()]}")
print(f"obj2 references: {[id(ref) for ref in obj2.get_references()]}")
print(f"obj3 references: {[id(ref) for ref in obj3.get_references()]}")
print(f"obj4 references: {[id(ref) for ref in obj4.get_references()]}")
print(f"obj4 references: {[id(ref) for ref in obj4.get_references()]}")

print("\nAdding roots...")
heap.add_root(obj1)
heap.add_root(obj3)

# Trigger initial garbage collection
print("\nInitial GC cycle:")
heap.gc()


# Simulating breaking some references
print("\nBreaking some references...")
obj1.remove_reference(obj2)
obj3.remove_reference(obj4)

print(f"After breaking references:")
print(f"obj1 references: {[id(ref) for ref in obj1.get_references()]}")
print(f"obj3 references: {[id(ref) for ref in obj3.get_references()]}")


print("\nRemoving some roots...")
heap.remove_root(obj3)

# Trigger garbage collection again
print("\nAfter breaking references and removing roots:")
heap.gc()

# Allocate new objects and create cycles
print("\nAllocating new objects and creating cycles...")
obj6 = heap.allocate()
obj7 = heap.allocate()

obj6.add_reference(obj7)
obj7.add_reference(obj6)

print(f"Allocated objects: obj6 ({id(obj6)}), obj7 ({id(obj7)})")
print(f"obj6 references: {[id(ref) for ref in obj6.get_references()]}")
print(f"obj7 references: {[id(ref) for ref in obj7.get_references()]}")

# Add obj6 as a root
heap.add_root(obj6)

# Trigger another garbage collection
print("\nAfter creating a cycle and adding obj6 as a root:")
heap.gc()

# Remove the cycle
print("\nBreaking the cycle...")
obj6.remove_reference(obj7)
obj7.remove_reference(obj6)

print("\nFinal GC cycle after breaking the cycle:")
heap.gc()

print("\nSimulation complete.")
