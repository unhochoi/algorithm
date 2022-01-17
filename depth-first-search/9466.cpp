#include <iostream>
#include <string.h>
#define MAX 100001
using namespace std;

// 전체 학생 수
int student_cnt;

// 팀원을 찾은 학생 수
int cnt = 0;

// 팀 매칭 결과를 확인하기 위한 배열
int done[MAX] = {0};

// 방문 결과
int visited[MAX] = {0};

// 각 학생들이 원하는 학생 벡터
int student_hope[MAX] = {0};

// 묶여있는 팀을 찾는 함수
void dfs(int current_student){

    // 입력 받은 현재 학생을 방문 처리
    visited[current_student] = 1;

    // 현재 학생이 원하는 학생을 저장
    int next_student = student_hope[current_student];

    // 현재 학생이 원하는 학생이, 이전에 방문한 적이 없는 학생이라면 방문
    if (visited[next_student] == 0){
        dfs(next_student);
    }
    // 현재 학생이 원하는 학생이, 이전에 방문한 적은 있지만, 아직 팀 매칭이 끝나지 않은 학생이라면
    else if (done[next_student] == 0){

        // 예를 들어, 사이클이 4 -> 7 -> 6 -> 4 로 반복된다면,
        // 6 에서 다시 6 으로 돌아올 때까지, 6 -> 4 방향으로, 사이클에 속한 인원을 확인
        // 하지만, 0 -> 2 -> 2 와 같은 경우에는, 2 -> 2 가 동일 인물이므로, 반복문을 실행하지 않음
        for (int i = next_student; i != current_student; i = student_hope[i]){
            cnt++;
        }
        // 사이클 시작 학생을 추가
        cnt++;
    }
    
    // 팀 매칭 가능 여부와 무관하게, 탐색된 학생은 팀 매칭이 끝난 것으로 저장
    done[current_student] = 1;
        
}

int main(){

    // 테스트 케이스 개수 입력
    int test_case;
    cin >> test_case;

    for (int i=0; i<test_case; ++i){

        // 배열 초기화
        memset(done, 0, sizeof(done));
        memset(visited, 0, sizeof(visited));
        memset(student_hope, 0, sizeof(student_hope));

        //  학생 수 입력
        cin >> student_cnt;

        // 각 학생별로, 원하는 학생들을 저장
        for (int j=1; j<=student_cnt; ++j){
            cin >> student_hope[j];
        }
        
        // 탐색된 팀원 수 초기화
        cnt = 0;    
        // 팀 찾기
        for (int j=1; j<=student_cnt; ++j){     
            
            // i 번째 학생을 방문 하지 않은 경우에만 탐색 시작
            if (visited[j]==0){
                dfs(j);
            }
        }

        // 전체 학생 수 - 팀 가능 학생 수
        cout << student_cnt - cnt << endl;
    }
}