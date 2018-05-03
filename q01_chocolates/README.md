# Chocolates are favourite
Complete the calculate function in the editor
so that for each day Ni (where 1 ≤ x ≤ N ≤ Y) in array arr, the number of chocolates 
Sam purchased (during days 1 through N) is printed on a new line. 
This is a function-only challenge, so input is handled for you by the locked stub code in the editor.

## Write a function `q01_chocolates` that:

- Takes an array of integers as a parameter.


The locked code in the editor handles reading the following input from stdin, assembling it into an array of integers (arr), and calling calculate(arr).
The first line of input contains an integer, T (the number of test cases). Each line i of the T subsequent lines describes the ith test case as an integer, Ni (the number of days).


### Output Format
For each test case, Ti in arr, your calculate method should print the total number of chocolates Sam purchased by day Ni on a new line.

### Explanation
Test Case 0: N = 1
Sam buys 1 chocolate on day 1, giving us a total of 1 chocolate. Thus, we print 1 on a new line.
 
Test Case 1: N = 2
Sam buys 1 chocolate on day 1 and 0 on day 2. This gives us a total of 1 chocolate. Thus, we print 1 on a new line.
 
Test Case 2: N = 3
Sam buys 1 chocolate on day 1, 0 on day 2, and 3 on day 3. This gives us a total of 4 chocolates. Thus, we print 4 on a new line.
