#include<stdio.h>
#include<stdlib.h>
#include<limits.h>

int n;            
int team[20];       
int graph[20][20];  
int min = INT_MAX;   

int abs(int x)
{
    return x < 0 ? -x : x;
}


int team_score(int flag){
    int sum = 0;
    for(int i = 0; i < n; i++)
    {
        for(int j = i+1; j < n; j++)
        {
            if(team[i] == flag && team[j] == flag)
            {
                sum += graph[i][j] + graph[j][i];
            }
        }
    }
    return sum;
}

void dfs(int idx, int count)
{
    if(count == n/2)
    {
        int s_score = team_score(1);
        int l_score = team_score(0);
        int d = abs(s_score - l_score);

        if(d < min)
        {
            min = d;
        }
        return; 
    }
    
    for(int i = idx; i < n; i++)
    {
        team[i] = 1;
        dfs(i + 1, count + 1);
        team[i] = 0;
    }
}

int main(void)
{

    scanf("%d", &n);

    for(int i = 0; i < n; i++)        
    {
        for(int j = 0; j < n; j++)
        {
            scanf("%d", &graph[i][j]);
        }
    }

    dfs(0, 0);
    printf("%d\n", min);

    return 0;
}