#include<stdio.h>

int n, m;
int result[9];
int used[9] = {0};

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
            if(used[i] == 0)
            {
                used[i] = 1;

                if(depth == 0)
                {
                    result[depth] = i;
                }

                if(result[depth - 1] < i)
                {
                    result[depth] = i;
                    dfs(depth + 1);
                }
                used[i] = 0;
            }
        }
    }
}

int main(void)
{
    scanf("%d %d", &n, &m);
    dfs(0);
    return 0;
}