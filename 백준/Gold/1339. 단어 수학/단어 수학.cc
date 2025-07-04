#include <iostream>
using namespace std;

int main(){
    int res = 0;
    int N = 0;
    char dangos[10][10] = {{}};
    int alphabet[26] = {};
    cin>> N;
    for (int i = 0; i < N; i ++){
        cin>> dangos[i];
    }
    for (int j = 0; j < N; j ++){
        int cnt = 1;
        for (int i = 9; i >= 0; i --){
            if(dangos[j][i]){
                alphabet[dangos[j][i] - 65] += cnt;
                cnt *= 10;
            }
        }
    }
    for (int i = 9; i >= 0; i --){
        int M = 0;
        for (int j = 0; j < 26; j ++){
            if (alphabet[M] < alphabet[j]){
                M = j;
            }
        }
        res += alphabet[M]*i;
        alphabet[M] = 0;
    }
    
    cout<< res;
}
