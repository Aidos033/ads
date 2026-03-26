//1
//import java.util.Scanner ;
//public class Main {
//    static void printnum(int n) {
//        if(n==0) return ;
//        printnum(n-1);
//        System.out.print(n+" ");
//
//    }
//
//    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//        int n = sc.nextInt();
//        printnum(n);
//
//    }
//}

//2
//import java.util.Scanner;
//public class Main {
//    static void printNumbers(int n) {
//        if (n == 0) return;
//        System.out.print(n + " ");
//        printNumbers(n - 1);
//    }
//
//    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//        int n = sc.nextInt();
//        printNumbers(n);
//    }
//}

//3
//import java.util.Scanner;
//
//public class Main {
//    static int sumN(int n) {
//        if (n == 1) return 1;
//        return n + sumN(n - 1);
//    }
//
//    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//        int n = sc.nextInt();
//        System.out.println(sumN(n));
//    }
//}

//4
//import java.util.Scanner;
//public class Main {
//    static int factN(int n) {
//        if (n == 1) return 1;
//        return n * factN(n - 1);
//    }
//
//    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//        int n = sc.nextInt();
//        System.out.println(factN(n));
//    }
//}

//5
//import java.util.Scanner;
//public class Main {
//    static int power(int a, int b) {
//        if (b == 0) return 1;
//        return a * power(a, b - 1);
//    }
//    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//        int a = sc.nextInt();
//        int b = sc.nextInt();
//        System.out.println(power(a, b));
//    }
//}

//6
//import java.util.Scanner;
//public class Main {
//    static int sumDigits(int n) {
//        if (n < 10) return n;
//        return n % 10 + sumDigits(n / 10);
//    }
//
//    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//        int n = sc.nextInt();
//        System.out.println(sumDigits(n));
//    }
//}

//7
//import java.util.Scanner;
//public class Main {
//    static int countDigits(int n) {
//        if (n < 10) return 1;
//        return 1 + countDigits(n / 10);
//    }
//
//    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//        int n = sc.nextInt();
//        System.out.println(countDigits(n));
//    }
//}

//8
//import java.util.Scanner;
//public class Main {
//    static void reverse(int n) {
//        if (n == 0) return;
//        System.out.print(n % 10);
//        reverse(n / 10);
//    }
//
//    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//        int n = sc.nextInt();
//        reverse(n);
//    }
//}

//9
//import java.util.Scanner;
//public class Main {
//    static int fib(int n) {
//        if (n == 0) return 0;
//        if (n == 1) return 1;
//        return fib(n - 1) + fib(n - 2);
//    }
//
//    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//        int n = sc.nextInt();
//        System.out.println(fib(n));
//    }
//}

//10
//import java.util.Scanner;
//public class Main {
//    static boolean isPalindrome(String s) {
//        if (s.length() <= 1) return true;
//        if (s.charAt(0) != s.charAt(s.length() - 1)) return false;
//        return isPalindrome(s.substring(1, s.length() - 1));
//    }
//
//    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//        String s = sc.nextLine();
//
//        if (isPalindrome(s))
//            System.out.println("Palindrome");
//        else
//            System.out.println("Not palindrome");
//    }
//}

//11
//import java.util.Scanner;
//public class Main {
//    static int sumArray(int[] arr, int i) {
//        if (i == arr.length) return 0;
//        return arr[i] + sumArray(arr, i + 1);
//    }
//
//    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//
//        int n = sc.nextInt();
//        int[] arr = new int[n];
//
//        for (int i = 0; i < n; i++) {
//            arr[i] = sc.nextInt();
//        }
//
//        System.out.println(sumArray(arr, 0));
//    }
//}

//12
//import java.util.Scanner;
//public class Main {
//    static int findMax(int[] arr, int i) {
//        if (i == arr.length - 1) return arr[i];
//        return Math.max(arr[i], findMax(arr, i + 1));
//    }
//
//    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//
//        int n = sc.nextInt();
//        int[] arr = new int[n];
//
//        for (int i = 0; i < n; i++) {
//            arr[i] = sc.nextInt();
//        }
//
//        System.out.println(findMax(arr, 0));
//    }
//}

//13
//import java.util.Scanner;
//public class Main {
//    static int countOccurrences(int[] arr, int i, int target) {
//        if (i == arr.length) return 0;
//
//        if (arr[i] == target)
//            return 1 + countOccurrences(arr, i + 1, target);
//        else
//            return countOccurrences(arr, i + 1, target);
//    }
//    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//
//        int n = sc.nextInt();
//        int[] arr = new int[n];
//
//        for (int i = 0; i < n; i++) {
//            arr[i] = sc.nextInt();
//        }
//        int target = sc.nextInt();
//        System.out.println(countOccurrences(arr, 0, target));
//    }
//}

//14
//import java.util.Scanner;
//public class Main {
//    static boolean search(int[] arr, int i, int target) {
//        if (i == arr.length) return false;
//        if (arr[i] == target) return true;
//        return search(arr, i + 1, target);
//    }
//    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//        int n = sc.nextInt();
//        int[] arr = new int[n];
//        for (int i = 0; i < n; i++) {
//            arr[i] = sc.nextInt();
//        }
//        int target = sc.nextInt();
//        if (search(arr, 0, target))
//            System.out.println("Found");
//        else
//            System.out.println("Not Found");
//    }
//}

//15
//import java.util.Scanner;
//public class Main {
//    static boolean isSorted(int[] arr, int i) {
//        if (i == arr.length - 1) return true;
//        if (arr[i] > arr[i + 1]) return false;
//        return isSorted(arr, i + 1);
//    }
//    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//        int n = sc.nextInt();
//        int[] arr = new int[n];
//        for (int i = 0; i < n; i++) {
//            arr[i] = sc.nextInt();
//        }
//        if (isSorted(arr, 0))
//            System.out.println("Sorted");
//        else
//            System.out.println("Not sorted");
//    }
//}

//bonus 16
//import java.util.Scanner;
//public class Main {
//    static int binarySearch(int[] arr, int left, int right, int target) {
//        if (left > right) return -1;
//        int mid = (left + right) / 2;
//        if (arr[mid] == target) return mid;
//        else if (target < arr[mid])
//            return binarySearch(arr, left, mid - 1, target);
//        else
//            return binarySearch(arr, mid + 1, right, target);
//    }
//    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//        int n = sc.nextInt();
//        int[] arr = new int[n];
//        for (int i = 0; i < n; i++) {
//            arr[i] = sc.nextInt();
//        }
//        int target = sc.nextInt();
//        int result = binarySearch(arr, 0, n - 1, target);
//        if (result != -1)
//            System.out.println("Element found at index " + result);
//        else
//            System.out.println("Not found");
//    }
//}