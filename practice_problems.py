"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    # Your implementation here
    dupe = set()
    for product in product_ids:
        if product in dupe:
            return True
        dupe.add(product)
    return False

print(has_duplicates([10,20,30,20,40]))
print(has_duplicates([1,2,3,4,5]))

#This code works by adding the numbers into a set, which does not allow duplicates. The loop goes through all the numbers in the list and compares them to the numbers in the set, and
#adds the new numbers into the set to be compared. If a duplicate is detected, the loop stops running and returns true because there is a duplicate. If the loop is able to go through
#the whole list, then this means there were no duplicates found and the code will return false. 
"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

class TaskQueue:

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_oldest_task(self):
        return self.tasks.pop(0)
    
taskqueue = TaskQueue()
taskqueue.add_task("Email follow-up")
taskqueue.add_task("Code review")
print(taskqueue.remove_oldest_task())
"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:

    def __init__(self):
        self.track = set()

    def add(self, value):
        self.track.add(value)

    def get_unique_count(self):
        return len(self.track)
    
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
print(tracker.get_unique_count())