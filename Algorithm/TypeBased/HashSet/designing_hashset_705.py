"""
Design a HashSet without using any built-in hash table libraries.
Implement MyHashSet class:
void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
Example 1:

Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)
"""


class MyHashSet:

    def __init__(self):
        self.set1 = set()

    def add(self, key: int):
        self.set1.add(key)

    def remove(self, key: int):
        if key in self.set1:
            self.set1.remove(key)

    def contains(self, key: int): #-> bool:
        if self.set1.__contains__(key):
            return True
        else:
            return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


if __name__ == "__main__":
    myHashSet = MyHashSet()
    myHashSet.add(1)  # // set = [1]
    myHashSet.add(2)  # // set = [1, 2]
    print(myHashSet.contains(1)) # // return True
    print(myHashSet.contains(3))  # // return False, (not found)
    myHashSet.add(2)  # // set = [1, 2]
    print(myHashSet.set1)
    print("Hello: ", myHashSet.contains(2))  # // return True
    myHashSet.remove(2)  # // set = [1]
    print(myHashSet.contains(2))  # return False, (already removed)