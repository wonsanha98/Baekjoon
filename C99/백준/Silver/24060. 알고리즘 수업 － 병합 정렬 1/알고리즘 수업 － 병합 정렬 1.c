#include<stdio.h>

int cnt = 0;
int cnt_num = 0;
int k = 0;
int reselt = 0;

void merge(int A[], int p, int q, int r)
{
    int i = p, j = q + 1, t = 0;
    int tmp[r - p + 1]; 

    while(i <= q && j <= r)
    {
        if(A[i] <= A[j])
        {
            tmp[t++] = A[i++];  
        }
        else
        {
            tmp[t++] = A[j++];  
        }
    }

    while(i <= q)
    {
        tmp[t++] = A[i++];
    }

    while(j <= r)
    {
        tmp[t++] = A[j++];
    }

    for(i = p, t = 0; i <= r; i++, t++)
    {
        cnt++;
        if(cnt == k)
        {
            reselt = tmp[t];
        }
        A[i] = tmp[t];
    }   
}

void merge_sort(int A[], int p, int r)
{
    if(p < r)
    {
        int q = (p + r) / 2;        
        merge_sort(A, p, q);        
        merge_sort(A, q + 1, r);    
        merge(A, p, q, r);          
    }
}
int main()
{
    int n;
    scanf("%d %d", &n, &k);
    int arr[n];

    for(int i = 0; i < n; i++)
    {
        int num;
        scanf("%d", &num);
        arr[i] = num;
    }

    merge_sort(arr, 0, n-1);

    if(cnt < k)
    {
        printf("%d", -1);
    }
    else
    {
        printf("%d", reselt);
    }
    
    return 0; 
}