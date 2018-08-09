# Chocolates are favourite
Complete the function 
so that for each day N in array arr, the number of chocolates 
Sam purchased (during days 1 through N) is stored in a list.

## Write a function `q01_chocolates` that:

- Takes an array of integers as a input parameter.
- Each element i of the the array describes the Nth day on which Sam has purchased chocolates
- The function returns a list of chcolates Sam would have purchased till Nth day


### Explanation
For eg if input list is [1,2,5,8]

N = 1, Sam buys 1 chocolate on day 1, giving us a total of 1 chocolate. Hence we append 1 to the output list.

N = 2, Sam buys 1 chocolate on day 1 and 0 on day 2. This gives us a total of 1 chocolate. Thus, we appemd 1 to the output list.

N = 5, Sam buys 1 chocolate on day 1, 0 on day 2, and 5 on day 5. This gives us a total of 6 chocolates. Thus, we append 6 to th output list.

N = 8, Sam buys 1 chocolate on day 1, 0 on day 2, 5 on day 5 and 0 on day 8. This gives us a total of 6 chocolates. Thus, we append 6 to the output list.

Hence the function should return the list [1,1,6,6]
