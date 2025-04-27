#include<stdio.h>

int hanoi(int n)
{   
    if(n == 0)
        return 0;
    if(n == 1)
    {
        return 1;
    }
    return (2 * hanoi(n-1)) + 1;
}

void hanoi_move(int n, int a, int b)
{
    if(n == 1)
    {
        printf("%d %d\n", a, b);
        return;
    }

    hanoi_move(n-1, a, 6 - a - b);
    printf("%d %d\n", a, b);
    hanoi_move(n-1, 6 - a - b, b);
}

int main()
{
    int n;
    scanf("%d", &n);
    printf("%d\n", hanoi(n));
    hanoi_move(n, 1, 3);

    return 0;
}