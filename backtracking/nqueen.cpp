#include <stdio.h>
#include <stdlib.h>
#define MAX 14
using namespace std;

// 입력
int n;

// 찾은 경우의 수 
int cnt = 0;

// queen의 위치를 저장할 배열의 길이를 maximum 으로 정적 할당
int queen_loc[MAX];

// 해당 행, 열 위치가 퀸의 위치로 가능한지 확인
int possible_loc(int row){

    // 입력 받은 행까지 탐색하며
    // 이전에 찾은 퀸들의 열 위치와 같은 열에 위치해 있거나, 대각선에 위치해 있다면 불가능하다고 판단
    for(int i=0; i<row; ++i){
        if ((queen_loc[i] == queen_loc[row]) || ( row - i == (abs(queen_loc[row] - queen_loc[i])))){
            return 0;
        }
    }
    return 1;
}

// nqueen 알고리즘 수행하며, 찾은 경우의 수 덧셈
void nqueen(int row){

    // n번째 행까지 n개의 퀸을 놓는 하나의 경우의 수를 찾았다면, 함수 종료
    if (row == n){
        cnt++;
        return;
    }
    // 모든 경우의 수를 찾지 못한 경우
    else{
        
        // 현재 행에서 모든 열 검사
        for (int col=0; col<n; ++col){       
            
            // 행 위치에 열 값을 할당
            queen_loc[row] = col;
            
            // 현재 행, 열 위치가 퀸의 위치로 문제 없다면, 다음 행 검사
            if (possible_loc(row)){
                nqueen(row + 1);
            }
            // 현재 행, 열 위치가 퀸의 위치로 문제가 있다면, 이어서 반복문 진행
        }
    }
}

int main(void){

    // 입력
    scanf("%d", &n);

    // nqueen 알고리즘 수행 (0번째 행부터 탐색)
    nqueen(0);

    // nqueen 알고리즘 수행 후, 찾은 경우의 수 반환
    printf("%d", cnt);
    
    return 0;

}


