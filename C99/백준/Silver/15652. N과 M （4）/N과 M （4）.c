#include<stdio.h>

int n, m;
int result[8];

void dfs(int depth, int start)
{
    if(depth == m)
    {
        for(int i = 0; i < m; i++)
        {
            printf("%d ", result[i]);
        }
        printf("\n");
        return;
    }
    
    for(int i = start; i <= n; i++)
    {
        result[depth] = i;
        dfs(depth + 1, i);
    }
}

int main()
{
    scanf("%d %d", &n, &m);
    dfs(0, 1);
    return 0;
}