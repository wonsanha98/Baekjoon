#include<stdio.h>

int cnt = 0;
int dp[41]; 

int fib(int n)
{
    dp[1] = 1;
    dp[2] = 1;
    for(int i = 3; i <= n; i++)
    {
        dp[i] = dp[i-1] + dp[i-2];
        cnt++;
    }
    return dp[n];
}

int main()
{
    int n, recursion; 
    scanf("%d", &n);

    recursion = fib(n);
    printf("%d %d\n", recursion, cnt);
    
    return 0;
}