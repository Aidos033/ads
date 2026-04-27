# #1

# def two_sum(nums, target):
#     seen = {}
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in seen:
#             return [seen[complement], i]
#         seen[num] = i


# numbers = [2, 7, 11, 15]
# targett = 9
# print(two_sum(numbers, targett))

# #2

# def first_unique_char(s):
#     count = {}
#     for char in s:
#         count[char] = count.get(char, 0) + 1
#     for i, char in enumerate(s):
#         if count[char] == 1:
#             return i
#     return -1

# s = "leetcode"
# print(first_unique_char(s))

# s = "loveleetcode"
# print(first_unique_char(s))

# #3

# def is_isomorphic(s, t):
#     s_to_t = {}
#     t_to_s = {}
#     for c1, c2 in zip(s, t):
#         if c1 in s_to_t and s_to_t[c1] != c2:
#             return False
#         if c2 in t_to_s and t_to_s[c2] != c1:
#             return False
#         s_to_t[c1] = c2
#         t_to_s[c2] = c1
#     return True

# s = "egg"
# t = "add"
# print(is_isomorphic(s, t))

# #4

# def is_happy(n):
#     seen = set()
#     while n != 1:
#         n = sum(int(d) ** 2 for d in str(n))
#         if n in seen:
#             return False
#         seen.add(n)
#     return True

# n = 19
# print(is_happy(n))

# #5

# from collections import deque

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def level_order(root):
#     if not root:
#         return []
#     result = []
#     queue = deque([root])
#     while queue:
#         level = []
#         for _ in range(len(queue)):
#             node = queue.popleft()
#             level.append(node.val)
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#         result.append(level)
#     return result

# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)
# print(level_order(root))

# #6

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def max_depth(root):
#     if not root:
#         return 0
#     return 1 + max(max_depth(root.left), max_depth(root.right))

# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)
# print(max_depth(root))

# #7

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def is_symmetric(root):
#     def mirror(left, right):
#         if not left and not right:
#             return True
#         if not left or not right:
#             return False
#         return left.val == right.val and mirror(left.left, right.right) and mirror(left.right, right.left)
#     return mirror(root.left, root.right)

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(2)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(4)
# root.right.left = TreeNode(4)
# root.right.right = TreeNode(3)
# print(is_symmetric(root))

# #8

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# def longest_consecutive(root):
#     def dfs(node, parent, length):
#         if not node:
#             return length
#         if node.val == parent + 1:
#             length += 1
#         else:
#             length = 1
#         left = dfs(node.left, node.val, length)
#         right = dfs(node.right, node.val, length)
#         return max(length, left, right)
#     return dfs(root, float('-inf'), 0)

# root = TreeNode(1)
# root.right = TreeNode(3)
# root.right.left = TreeNode(2)
# root.right.right = TreeNode(4)
# root.right.right.right = TreeNode(5)
# print(longest_consecutive(root))

# #9

# def sort_colors(nums):
#     low, mid, high = 0, 0, len(nums) - 1
#     while mid <= high:
#         if nums[mid] == 0:
#             nums[low], nums[mid] = nums[mid], nums[low]
#             low += 1
#             mid += 1
#         elif nums[mid] == 1:
#             mid += 1
#         else:
#             nums[mid], nums[high] = nums[high], nums[mid]
#             high -= 1

# nums = [2, 0, 2, 1, 1, 0]
# sort_colors(nums)
# print(nums)

# #10

# def quick_sort(nums, low, high):
#     if low < high:
#         pivot = nums[high]
#         i = low - 1
#         for j in range(low, high):
#             if nums[j] <= pivot:
#                 i += 1
#                 nums[i], nums[j] = nums[j], nums[i]
#         nums[i + 1], nums[high] = nums[high], nums[i + 1]
#         pi = i + 1
#         quick_sort(nums, low, pi - 1)
#         quick_sort(nums, pi + 1, high)

# nums = [3, 6, 8, 10, 1, 2, 1]
# quick_sort(nums, 0, len(nums) - 1)
# print(nums)

# #11

# def merge_sort(nums):
#     if len(nums) <= 1:
#         return
#     mid = len(nums) // 2
#     left = nums[:mid]
#     right = nums[mid:]
#     merge_sort(left)
#     merge_sort(right)
#     i = j = k = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             nums[k] = left[i]
#             i += 1
#         else:
#             nums[k] = right[j]
#             j += 1
#         k += 1
#     while i < len(left):
#         nums[k] = left[i]
#         i += 1
#         k += 1
#     while j < len(right):
#         nums[k] = right[j]
#         j += 1
#         k += 1

# nums = [3, 6, 8, 10, 1, 2, 1]
# merge_sort(nums)
# print(nums)

# #12

# def heap_sort(nums):
#     n = len(nums)
#     for i in range(n // 2 - 1, -1, -1):
#         heapify(nums, n, i)
#     for i in range(n - 1, 0, -1):
#         nums[0], nums[i] = nums[i], nums[0]
#         heapify(nums, i, 0)

# def heapify(nums, n, i):
#     largest = i
#     left = 2 * i + 1
#     right = 2 * i + 2
#     if left < n and nums[left] > nums[largest]:
#         largest = left
#     if right < n and nums[right] > nums[largest]:
#         largest = right
#     if largest != i:
#         nums[i], nums[largest] = nums[largest], nums[i]
#         heapify(nums, n, largest)

# nums = [3, 6, 8, 10, 1, 2, 1]
# heap_sort(nums)
# print(nums)
