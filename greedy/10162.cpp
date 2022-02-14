#include <iostream>

using namespace std;

// 버튼 개수 초기화
int a_count, b_count, c_count = 0;

// 버튼 별 지정 시간
int a=300, b=60, c=10;

// 최소 버튼 계산 함수
int greedy(int t){

    // 더 이상 남은 시간을 처리할 수 없을때까지
    while(t!=0){
        if (t >= a){
            a_count += t/a;
            t = t%a;
        }else if (t >= b){
            b_count += t/b;
            t = t%b;
        }else if (t >= c){
            c_count += t/c;
            t = t%c;
        }else{
            return -1;
        }
    }
    return 0;
}

int main(){

    // 입력 초
    int t;
    cin >> t;

    // 최소 버튼 계산 실행
    int result = greedy(t);
    
    // 시간을 정확히 나눌 수 있다면
    if (result == 0){
        cout << a_count << " " << b_count << " " << c_count << endl;
    }
    // 시간을 정확히 나눌 수 없다면
    else{
        cout << -1 << endl;
    }
}