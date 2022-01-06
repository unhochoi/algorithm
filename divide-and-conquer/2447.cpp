#include <iostream>

using namespace std;

// 좌표에 대한 공백 여부 탐색
void check_blank(int i, int j, int n){

    // 현재 탐색하고 있는 N X N 정사각형의 크기가 1 이라면, 
    // 더 이상 탐색할 수 있는 공백이 없으므로 * 출력
    if (n == 1){
        cout << "*";
    }
    // 현재 탐색하고 있는 N X N 정사각형의 크기가 3 이상이고,
    // i,j 좌표가 해당 정사각형의 중간에 위치하고 있다면, 공백 출력
    else if ((i / (n/3)) % 3 == 1 && (j / (n/3)) % 3 == 1){
        cout << " ";
    }
    // 현재 탐색하고 있는 N X N 정사각형의 크기가 3 이상이고, 위 과정에서 공백을 찾지 못했다면
    // 탐색하고자하는 정사각형의 크기를 N/3 으로 줄인 뒤, 해당 정사각형 기준으로 중간에 위치한 공백인지 재탐색
    else{
        check_blank(i, j, n/3);
    }
}

int main(){
    // 정사각형 크기 입력
    int n;
    cin >> n;

    // 정사각형이므로 이중 포문 탐색
    for (int i=0; i<n; ++i){
        for (int j=0; j<n; ++j){
            check_blank(i, j, n);
        }
        cout << endl;
    }

    return 0;

}