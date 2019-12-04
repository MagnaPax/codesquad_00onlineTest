# 코드스쿼드 온라인 테스트 제출용


## 1단계: 간단 야구 게임 구현하기

## 대부분 손코딩으로 작성

- making_random_result: 
  * 경기 결과 값을 무작위로 선택 함수
			랜덤 모듈을 이용해서 네 개의 옵션 중에서 무작위로 경기 결과 값을 선택

- next_hitter(hasItNewline, isThisOut, n_out): '다음 타자가 타석에 입장했습니다' 문구를 각 상황에 맞게 출력 함수
			문구가 나타나야 되는 형식이 각 상화별로 다름. 각 상황에 맞는 형식으로 문구 출력

- playing_the_baseball_game(): 실제 게임이 진행되는 함수
			making_random_result 함수에서 무작위로 경기 결과 값을 얻은 뒤
			각 경기 결과 값에 따라 경기 결과에 해당되는 변수값을 1씩 증가시킴
			아웃 변수의 누적값이 3이 되면 게임 끝냄
			스트라이크 변수의 누적값이 3이 되면 아웃 변수를 1증가시킨 뒤 다음 타자로 교체
			볼 변수의 누적값이 4가 되면 안타 변수 1증가 시키고 스트라이크,볼 값을 초기화. 다음 타자로 교체
			경기 결과가 아웃이면 스트라이크, 볼 갯수를 초기화. 다음 타자로 교체
			경기 결과가 안타면 스트라이크, 볼 갯수를 초기화. 다음 타자로 교체
			



## 2단계: 팀데이터 입력 및 시합 기능 구현

- isNumber(s): 매개변수가 숫자라면 True 문자라면 False 반환

- isEmpty(s): 매개변수에 무슨 값이든 값이 들어있으면 True 반환. 값이 없으면 False 반환

- input_team_name(i): 팀 이름을 매개변수가 제대로 된 값이 아니면 재입력 요청

- playerInfo_error_check(infoPlayer): 매개변수 선수 정보가 제대로 들어왔는지 오류 체크 잘못된 값이면 False 리턴

- input_hitter_info(howManyHittersSoFar): 선수 정보 콘솔 입력 받은 뒤 오류 검사 후 받은 값 리턴
			정규표현식과 playerInfo_error_check 함수 사용하여 잘못된 값이면 재입력 받음

- choose_Menu(): 메뉴 선택한 뒤 값 리턴
			
        		isEmpty 함수와 isNumber 함수 이용하여 오류 체크 후 잘못된 값이면 재입력 받음


- define_List_dimensions(): 팀의 모든 정보를 저장하기 위한 2중 배열 선언 후 리턴

- input_all_info_team(teamNumber): 팀이름, 선수이름 입력 받아서 배열에 넣은 뒤 리턴
			define_List_dimensions 로 선언된 배열 받아서
			input_team_name 함수 사용하여 팀이름 받고
			9명의 선수 정보를 배열에 저장하여 리턴


- print_out_teams_info(temaInfo): 옵션 선택 2를 했을 때 팀 정보 표시하는 함수
