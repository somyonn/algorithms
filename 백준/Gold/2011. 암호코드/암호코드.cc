#include <iostream>
#include <cstring>
using namespace std;

long long times = 1;
int stk = 0;
int top = 7;
long long ignite[5001] = {1,2,3,5,8,13,21,};
void aniak(){
    if (stk < 0){
        stk = 0;
    }
    if (top < stk){
        for (int i = top; i < stk+1; i ++){
            ignite[i] = (ignite[i-1] + ignite[i-2]) % 1000000;
        }
        top = stk;
    }
    times = (times * ignite[stk]) % 1000000;
    stk = 0;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    char ango[5001] = {'0'};
    cin>>ango;
    int flag = 0;
    for (int i = 0; i <int(strlen(ango)); i++){
        switch(ango[i]){
            case '0':
                if (flag == 1 or flag == 2){
                    if (stk > 1){
                        stk -=2;
                    }
                    else{
                        stk --;
                    }
                    aniak();
                    flag = 0;
                }
                else{
                    cout<<"0";
                    exit(0);
                }
                break;
            case '1':
                stk ++;
                flag = 1;
                break;
            case '2':
                stk ++;
                flag = 2;
                break;
            default:
                if (int(ango[i]) < '7'){
                    aniak();
                    flag = 3;
                }
                else if (int(ango[i]) > '6'){
                    if (flag == 2){
                        stk --;
                    }
                    aniak();
                    flag = 3;
                }
        }
    }
    if (stk > 0) {
        stk --;
    }
    aniak();
    cout<<times;
}