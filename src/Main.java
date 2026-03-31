//1
// def printnum(n):
//     if n == 0:
//         return
//     printnum(n - 1)
//     print(n, end=" ")

// n = int(input())
// printnum(n)

//2
// def print_numbers(n):
//     if n == 0:
//         return
//     print(n, end=" ")
//     print_numbers(n - 1)

// n = int(input())
// print_numbers(n)

// //3
// def sum_n(n):
//     if n == 1:
//         return 1
//     return n + sum_n(n - 1)

// n = int(input())
// print(sum_n(n))

// //4
// def fact(n):
//     if n == 1:
//         return 1
//     return n * fact(n - 1)

// n = int(input())
// print(fact(n))

// //5
// def power(a, b):
//     if b == 0:
//         return 1
//     return a * power(a, b - 1)

// a = int(input())
// b = int(input())
// print(power(a, b))

// //6
// def sum_digits(n):
//     if n < 10:
//         return n
//     return n % 10 + sum_digits(n // 10)

// n = int(input())
// print(sum_digits(n))

// //7
// def count_digits(n):
//     if n < 10:
//         return 1
//     return 1 + count_digits(n // 10)

// n = int(input())
// print(count_digits(n))

// //8
// def reverse(n):
//     if n == 0:
//         return
//     print(n % 10, end="")
//     reverse(n // 10)

// n = int(input())
// reverse(n)

// //9
// def fib(n):
//     if n == 0:
//         return 0
//     if n == 1:
//         return 1
//     return fib(n - 1) + fib(n - 2)

// n = int(input())
// print(fib(n))

// //10
// def is_palindrome(s):
//     if len(s) <= 1:
//         return True
//     if s[0] != s[-1]:
//         return False
//     return is_palindrome(s[1:-1])

// s = input()
// if is_palindrome(s):
//     print("Palindrome")
// else:
//     print("Not palindrome")
// //11
// def sum_array(arr, i):
//     if i == len(arr):
//         return 0
//     return arr[i] + sum_array(arr, i + 1)

// n = int(input())
// arr = list(map(int, input().split()))
// print(sum_array(arr, 0))
  
// //12
// def find_max(arr, i):
//     if i == len(arr) - 1:
//         return arr[i]
//     return max(arr[i], find_max(arr, i + 1))

// n = int(input())
// arr = list(map(int, input().split()))
// print(find_max(arr, 0))

// //13
// def count_occurrences(arr, i, target):
//     if i == len(arr):
//         return 0
//     if arr[i] == target:
//         return 1 + count_occurrences(arr, i + 1, target)
//     return count_occurrences(arr, i + 1, target)

// n = int(input())
// arr = list(map(int, input().split()))
// target = int(input())
// print(count_occurrences(arr, 0, target))

// //14
// def search(arr, i, target):
//     if i == len(arr):
//         return False
//     if arr[i] == target:
//         return True
//     return search(arr, i + 1, target)

// n = int(input())
// arr = list(map(int, input().split()))
// target = int(input())

// if search(arr, 0, target):
//     print("Found")
// else:
//     print("Not Found")

// //15
// def is_sorted(arr, i):
//     if i == len(arr) - 1:
//         return True
//     if arr[i] > arr[i + 1]:
//         return False
//     return is_sorted(arr, i + 1)

// n = int(input())
// arr = list(map(int, input().split()))

// if is_sorted(arr, 0):
//     print("Sorted")
// else:
//     print("Not sorted")

// //bonus 16
// def binary_search(arr, left, right, target):
//     if left > right:
//         return -1
//     mid = (left + right) // 2
//     if arr[mid] == target:
//         return mid
//     elif target < arr[mid]:
//         return binary_search(arr, left, mid - 1, target)
//     else:
//         return binary_search(arr, mid + 1, right, target)

// n = int(input())
// arr = list(map(int, input().split()))
// target = int(input())

// result = binary_search(arr, 0, n - 1, target)

// if result != -1:
//     print("Element found at index", result)
// else:
//     print("Not found")
