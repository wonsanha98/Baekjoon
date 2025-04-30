#include<stdio.h>

int n, m;
int result[8];

void dfs(int depth)
{
    if(depth == m)
    {
        for(int i = 0; i < m; i++)
        {
            printf("%d ", result[i]);
        }
        printf("\n");
    }
    else
    {
        for(int i = 1; i <= n; i++)
        {
            {
                result[depth] = i;
                dfs(depth + 1);  
            }
        }
    }
}

int main()
{
    scanf("%d %d", &n, &m);
    dfs(0);
    return 0;
}