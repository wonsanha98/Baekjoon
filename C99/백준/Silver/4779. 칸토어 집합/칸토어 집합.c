#include<stdio.h>
#include<string.h>

int pow_int(int a)   //3의 제곱을 구하는 함수
{
    int result = 1;
    for(int i = 0; i < a; i++)
        result *= 3;
    return result;
}

void cantor_set(char str[], int start, int end)
{
    int f, s; 
    int size = end - start;     //end는 배열의 사이즈, 마지막 인덱스를 구하기 위해서는 -1을 한다.
    f = (size / 3);           //첫 경계 시작
    s = f + f;              //두번째 경계 시작
    if(size == 1)
        return;

    cantor_set(str, start, start + f);
    for(int i = start + f ; i < start + s; i++)
    {
        str[i] = ' ';
    }
    cantor_set(str, start + s, end);
}


int main()
{
    int n;
    while(scanf("%d", &n) == 1) //scanf는 읽어들여 저장에 성공한 데이터 개수를 반환한다.
    {
        int n_n = pow_int(n);
        char str[n_n + 1];      //NULL 문자 공간을 위해 +1
        for(int i = 0; i < n_n; i++)
        {
            str[i] = '-';
        }
        str[n_n] = '\0';        //마지막에 NULL문자 추가

        cantor_set(str, 0, n_n);
        printf("%s\n", str);
    }    

    return 0;
}