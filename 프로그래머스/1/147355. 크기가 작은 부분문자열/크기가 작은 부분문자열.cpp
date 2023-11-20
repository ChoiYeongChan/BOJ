#include <string>
#include <vector>
#include <iostream>
using namespace std;

int solution(string t, string p) {
    int answer = 0;
    int n=p.length();
    int m=t.length();
    long numB=stol(p);
    for (int i=0;i<m-n+1;i++) {
        string a=t.substr(i,n);
        long numA=stol(a);
        if (numA<=numB) answer+=1;
    }
    return answer;
}