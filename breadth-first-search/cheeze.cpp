#include <iostream>
#include <queue>
#include <string.h>

#define MAX 100
using namespace std;

// 사각형 보드 크기
int r,c;

// 치즈, 공기 칸 표시
int board[MAX][MAX];

// BFS 로 방문한 위치 기억
int visited[MAX][MAX] = {-1};

// 치즈가 모두 녹기까지 걸린 시간
int hour = 0;

// 칸
int space;

// 전체 치즈 개수
int total_cheeze_count = 0;

// 뺄셈 전 치즈 개수
int melting_cheeze_count = 0;

// 상하좌우 확인 시 사용
int row_element[4] = {-1, 1, 0, 0};
int col_element[4] = {0, 0, -1, 1};

// 치즈, 공기 칸 보드 확인
void check_board(int x, int y){

    // 본인의 위치를 방문한것으로 저장
    visited[x][y] = 0;

    // 시작 위치 상하좌우에 존재하는 칸 탐색
    for (int i=0; i<4; ++i){
        
        // 상하좌우로 확인할 칸
        int new_row = x + row_element[i];
        int new_col = y + col_element[i];

        // 상하좌우로 인접한 칸이, 보드 내에 존재하는지 확인
        if (0 <= new_row && new_row < r && 0 <= new_col && new_col < c){

            // 해당 칸이 이전에 방문하지 않았을 경우
            if (visited[new_row][new_col] == -1 ){
                // 치즈, 공기 칸 보드 상에서, 중심 칸의 상하좌우에 치즈 칸이 존재한다면
                if (board[new_row][new_col] == 1){
                    // 해당 치즈 칸을 방문했다고 기록
                    visited[new_row][new_col] = 1;
                    // 치즈, 공기 칸 보드 상에서, 해당 치즈 칸 녹이기
                    board[new_row][new_col] = 0;
                    // 치즈 개수 뺄셈
                    total_cheeze_count--;
                }
                else{
                    // 인접한 칸 탐색
                    check_board(new_row, new_col);
                }
            }
        }
    }
    return;
}


int main(){

    // 사각형 보드 크기 입력
    cin >> r >> c;

    // 치즈, 공기 칸 입력
    for (int i=0; i<r; ++i){
        for (int j=0; j<c; ++j){
            cin >> space;
            // 보드에 치즈, 공기 칸 표시
            board[i][j] = space;
            // 치즈 개수 계산
            if (space == 1){
                total_cheeze_count++;
            }
        }
    }    

    // 치즈가 없어지기 전까지
    while (total_cheeze_count!=0){
        // 남은 치즈 개수
        melting_cheeze_count = total_cheeze_count;
        // 방문한 위치 초기화
        memset(visited, -1, sizeof(visited));
        // 치즈, 공기 칸 보드 확인
        check_board(0,0);
        // 치즈 녹이는 시간 추가
        hour++;
    }

    cout << hour << endl;
    cout << melting_cheeze_count << endl;
    
    return 0;

}