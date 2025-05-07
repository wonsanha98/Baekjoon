#include<stdio.h>
#define MAX(a, b) a > b ? a : b

int main()
{
    int n, max;
    scanf("%d", &n);
    
    int arr[n+1], dp[n+1];

    for(int i = 0; i < n; i++)
    {
        int num;
        scanf("%d", &num);
        arr[i] = num;
    }

    dp[0] = arr[0];             
    max = dp[0];                        //max 초기값 설정
    for(int i = 1; i < n; i++)
    {
        dp[i] = MAX(arr[i], dp[i-1] + arr[i]);
        max = MAX(max, dp[i]);
    }

    printf("%d\n", max);

    return 0; 
}