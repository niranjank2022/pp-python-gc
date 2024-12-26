# cython_gc.pyx

cdef class GCObject:
    cdef int ref_count
    cdef list refs  # To store references to other GCObjects

    def __init__(self, int ref_count=0):
        self.ref_count = ref_count
        self.refs = []

    def add_reference(self, GCObject obj):
        self.refs.append(obj)
        obj.ref_count += 1

    def remove_reference(self, GCObject obj):
        if obj in self.refs:
            self.refs.remove(obj)
            obj.ref_count -= 1

    def get_references(self):
        return self.refs

cdef class GCHeap:
    cdef list objects  # allocated objects
    cdef list roots    # root objects

    def __init__(self):
        self.objects = []
        self.roots = []

    def allocate(self, int ref_count=0):
        obj = GCObject(ref_count)
        self.objects.append(obj)
        return obj

    def add_root(self, GCObject obj):
        if obj not in self.roots:
            self.roots.append(obj)

    def remove_root(self, GCObject obj):
        if obj in self.roots:
            self.roots.remove(obj)

    def gc(self):
        print("Starting garbage collection...")

        # Step 1: Mark all objects as unreachable
        reachable = set()

        # Step 2: Traverse the roots and mark reachable objects
        for root in self.roots:
            self._mark(root, reachable)

        # Step 3: Sweep unreachable objects
        self._sweep(reachable)

        print("Garbage collection complete.")

    def _mark(self, GCObject obj, set reachable):
        if obj in reachable:
            return
        reachable.add(obj)
        for ref in obj.refs:
            self._mark(ref, reachable)

    def _sweep(self, set reachable):
        to_delete = [obj for obj in self.objects if obj not in reachable]
        for obj in to_delete:
            self.objects.remove(obj)
            print(f"Collecting {obj}")
        print(f"Collected {len(to_delete)} objects.")
