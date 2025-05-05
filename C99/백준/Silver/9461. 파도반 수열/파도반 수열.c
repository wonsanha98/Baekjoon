#include<stdio.h>

int main()
{
    int t;
    scanf("%d", &t);
    for(int i = 0; i < t; i++)
    {
        long long dp[101] = {0};        
        dp[1] = dp[2] = dp[3] = 1;
        dp[4] = dp[5] = 2;
        
        int n;

        scanf("%d", &n);
        if(n <= 5)
        {
            printf("%d\n", dp[n]);
            continue;
        }
        else
        {
            for(int j = 6; j <= n; j++)
            {
                dp[j] = dp[j-1] + dp[j-5];
            }
        
            printf("%lld\n", dp[n]);
        }

    }
    
    return 0;
}