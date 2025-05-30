#include<stdio.h>

int n, m;
int result[9];  
int check[9];    

void dfs(int depth)     
{
    int i;

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
        for(i = 1; i <= n; i++)
        {
            if(check[i] == 0)
            {
                result[depth] = i;
                check[i] = 1;
                dfs(depth + 1);
                check[i] = 0;
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