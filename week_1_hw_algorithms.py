#SOLVE THESE QUESTIONS AND SPECIFY RUNNING TIME AND SPACE COMPLEXITY IN COMMENTS.

#Question 1:

#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#Example: [2,3,4,2,7] target = 10, output = [1,4]

#Second version, more eficicient, after watching the solution video
def twoSum2(nums, target):
    d = {}
    for i, n in enumerate(nums):
        subt = target - n
        if subt in d:
            return d[subt], i
        d[n] = i
#Time and space complexity: O(n)
print(f"Question 1b: {twoSum2([2,3,4,2,7], 10)}")


##############################################################################################################################

#Question 2:

#Given some arrays with strings on them, find the most common longest prefix among them.
#Example: ["flower","flow","flight"] output = "fl"

def findMostCommonPrefix(arr):
    shortest_word = min(arr, key=len)
    result = shortest_word
    for i in range(1, len(arr)):
        actual_prefix = ""
        for j in range(len(shortest_word)):
            if arr[i][j] == arr[0][j]:
                actual_prefix += arr[i][j]
        if actual_prefix < result:
            result = actual_prefix
    return result

word = ["flower","flow","flight"]
print(f"Question 2: {findMostCommonPrefix(word)}")

#Time and space complexity: O(n m)
##############################################################################################################################

#Question 3:

#Given an array of integers, return the indices of three numbers that add up to 0.
#example: [1, 2, -2, -1, 3] output = [0, 2, 3]

def threeSum(nums):
    sorted_list = sorted(nums)
    for i in range(len(sorted_list)):
        k = len(sorted_list)-1
        j = i + 1
        while j<k:
            total = sorted_list[i] + sorted_list[j] + sorted_list[k]
            if total == 0:  
                return sorted_list[i], sorted_list[j], sorted_list[k]
            if total > 0:
                k -= 1
            if total < 0:            
                j += 1
    return None

nums = [1, 2, -2, -1, 3]

print(f"Question 3: {threeSum(nums)}")               

#Time and space complexity: O(n^2)

##############################################################################################################################

#Question 4:

#Given a singly linked list, reverse the nodes of the linked list
#Example 1: [1, 2, 3] output = [3, 2, 1]

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def printList(head):
    while head:
        print(head.data)
        head = head.next

head = Node(1)
middle = Node(2)
tail = Node(3)

head.next = middle
middle.next = tail
tail.next = None


def reverseList(head):
    prev = None
    current = head
    while current:
        next_node = current.next 
        current.next = prev
        prev = current  
        current = next_node
    return prev

head = reverseList(head)

print("Question4:")
printList(head)

#Time and space complexity: O(n)



