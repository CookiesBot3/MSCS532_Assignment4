class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):
        return self.priority < other.priority  # For min-heap comparison

    def __repr__(self): # Returns a string all the attribute's values
        return f"Task(ID: {self.task_id}, Priority: {self.priority}, Arrival: {self.arrival_time}, Deadline: {self.deadline})"

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, task):
        self.heap.append(task)  # Add the task to the end
        self.heapify_up(len(self.heap) - 1)  # Heapify up to maintain heap property

    def heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self.heapify_up(parent)

    def extract_min(self):
        if self.is_empty():
            return None
        if len(self.heap) == 1:
            return self.heap.pop()  # If there's only one element, remove and return it
        root = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move the last element to the root
        self.heapify_down(0)  # Heapify down to maintain heap property
        return root

    def heapify_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify_down(smallest)

    def change_priority(self, task_id, new_priority):
        # Find the task with the given task_id
        for index, task in enumerate(self.heap):
            if task.task_id == task_id:
                old_priority = task.priority
                task.priority = new_priority

                if new_priority < old_priority:
                    self.heapify_up(index)  # Heapify up if priority decreased
                else:
                    self.heapify_down(index)  # Heapify down if priority increased
                break

    def is_empty(self):
        return len(self.heap) == 0

# Create a PriorityQueue
pq = PriorityQueue()

# Insert multiple tasks into the priority queue
pq.insert(Task(1, 10, '09:00', '12:00'))  # Task with priority 10
pq.insert(Task(2, 5, '09:30', '11:30'))   # Task with priority 5
pq.insert(Task(3, 1, '10:00', '12:30'))   # Task with priority 1
pq.insert(Task(4, 8, '10:30', '13:00'))   # Task with priority 8
pq.insert(Task(5, 2, '11:00', '14:00'))   # Task with priority 2

# Print the entire priority queue (min-heap)
print("Initial Priority Queue (Min-Heap):")
for task in pq.heap:
    print(task)

# Extract the task with the highest priority (smallest priority value)
print("\nExtracting tasks by priority:")
while not pq.is_empty():
    extracted_task = pq.extract_min()
    print(f"Extracted Task: {extracted_task}")

# Re-insert some tasks for demonstration of change priority operation
pq.insert(Task(6, 7, '11:15', '13:30'))   # Task with priority 7
pq.insert(Task(7, 3, '11:30', '15:00'))   # Task with priority 3
pq.insert(Task(8, 6, '12:00', '15:30'))   # Task with priority 6

# Print the updated priority queue
print("\nPriority Queue after inserting new tasks:")
for task in pq.heap:
    print(task)

# Change the priority of a task
pq.change_priority(7, 1)  # Changing Task 7's priority to 1 (highest priority)
print("\nPriority Queue after changing the priority of Task 7:")
for task in pq.heap:
    print(task)