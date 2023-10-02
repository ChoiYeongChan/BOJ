#include <iostream>
#include <cmath>
using namespace std;

int solution(int n, int a, int b)
{
    int answer = 1;

    int i;
    for(i = 1; i < n; i++){
        if( a % 2 == 1 ) a++;
        if( b % 2 == 1 ) b++;
        a /= 2;
        b /= 2;

        if(a == b)
            break;
    }
    
    return i;
}