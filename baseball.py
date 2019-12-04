import random
import re


# 경기 결과 값을 무작위로 선택
def making_random_result():
    baseball_options = ['스트라이크', '볼', '안타', '아웃']
    randomResult = random.choice(baseball_options)
#    print(randomResult)
    return randomResult



# '다음 타자가 타석에 입장했습니다' 문구를 각 상황에 맞게 출력하는 함수
def next_hitter(hasItNewline, isThisOut, n_out):

    # 아웃 카운트 3개가 되면 게임이 끝나기 때문에 다음 타자가 입장했습니다 출력 않고 아웃만 출력하고 끝내기
    if n_out == 3:
        print('\n' + '아웃!', end='', flush = True)
        return

    # 줄바꿈 있음
    if hasItNewline == 1:
        if isThisOut == 1:    # 3 스트라이크 아웃
            print('\n' + '아웃! 다음 타자가 타석에 입장했습니다.', end='', flush = True)

        elif isThisOut == 0:  # 볼 넷 출루
            print('\n' + '다음 타자가 타석에 입장했습니다.', end='', flush = True)

    # 줄바꿈 없음
    elif hasItNewline == 0:
        if isThisOut == 1:    # 파울볼, 뜬 공 등 바로 아웃 된 것
            print('다음 타자가 타석에 입장했습니다.', end='', flush = True)

        elif isThisOut == 0:  # 타자가 안타 친 것
            print('다음 타자가 타석에 입장했습니다.', end='', flush = True)

    return



# 실제 게임이 진행되는 함수
def playing_the_baseball_game():

    # 에러 방지를 위한 변수값 초기화
    n_strike = 0
    n_ball = 0
    n_hit = 0
    n_out = 0


    while(1):

        
        # 아웃 카운트 3개가 되면 게임 끝내기
        # 2아웃 상태에서 3스트라이크로 공수 교대할 때 이 조건문에 의해 게임 종료
        if n_out == 3:
            print('\n' + "최종 안타수: %d" % n_hit)
            print('Game Over')
            return
        


        # 무작위 결과 얻기
        randomResult = making_random_result()

#        randomResult = input("값 입력: ")     # 테스트를 위해 값 직접 입력

        # 경기 결과 출력
        print(randomResult + '! ', end='', flush = True)

        # randomResult 값에 따라 각 변수에 값 할당하기
        if randomResult == '스트라이크': n_strike+=1
        elif randomResult == '볼': n_ball+=1
        elif randomResult == '안타': n_hit+=1
        elif randomResult == '아웃': n_out+=1


        # 아웃 카운트 3개가 되면 게임 끝내기
        # 2아웃 상태에서 곧바로 randomResult 값에 아웃이 하나 더 나와서 공수 교대할 때 이 조건문에 의해 게임 종료
        if n_out == 3:
            print('\n' + "최종 안타수: %d" % n_hit)
            print('Game Over')
            return


        # 스트라이크 3개면 아웃 카운트 하나 올리고 다음 타자로 교체
        if n_strike == 3:
            hasItNewline = 1    # print 찍어줄 때 줄 바꿈 있음
            isThisOut = 1         # print 찍어줄 때 아웃임을 알림
            n_out+=1            # 아웃 카운트 올리기

            next_hitter(hasItNewline, isThisOut, n_out)  # 다음 타자 print 찍어주는 함수 호출

            n_strike = 0        # 다음 타자로 바뀌니까 스트라이크 갯수 초기화
            n_ball = 0          # 다음 타자로 바뀌니까 볼 갯수 초기화

            


        # 경기 결과가 곧바로 아웃일 때
        elif randomResult == '아웃':
            hasItNewline = 0    # print 찍어줄 때 줄 바꿈 없음
            isThisOut = 1         # print 찍어줄 때 아웃임을 알림
            next_hitter(hasItNewline, isThisOut, n_out)  # 다음 타자 print 찍어주는 함수 호출

            n_strike = 0        # 다음 타자로 바뀌니까 스트라이크 갯수 초기화
            n_ball = 0          # 다음 타자로 바뀌니까 볼 갯수 초기화

            
        # 볼 넷이 되었을 때
        elif n_ball == 4:
            hasItNewline = 1    # print 찍어줄 때 줄 바꿈 있음
            isThisOut = 0         # print 찍어줄 때 아웃이 아님을 알림
            next_hitter(hasItNewline, isThisOut, n_out)  # 다음 타자 print 찍어주는 함수 호출

            n_strike = 0        # 다음 타자로 바뀌니까 스트라이크 갯수 초기화
            n_ball = 0          # 다음 타자로 바뀌니까 볼 갯수 초기화

            n_hit+=1            # 안타 갯수 올리기



        # 경기 결과가 곧바로 안타가 나왔을 때
        elif randomResult == '안타':
            hasItNewline = 0    # print 찍어줄 때 줄 바꿈 없음
            isThisOut = 0         # print 찍어줄 때 아웃이 아님을 알림
            next_hitter(hasItNewline, isThisOut, n_out)  # 다음 타자 print 찍어주는 함수 호출

            n_strike = 0        # 다음 타자로 바뀌니까 스트라이크 갯수 초기화
            n_ball = 0          # 다음 타자로 바뀌니까 볼 갯수 초기화


        print('\n' + "%sS  %sB  %sO" % (n_strike, n_ball, n_out))
#        print("안타 갯수: %s" % n_hit + '\n')
        












# 값을 받아서 숫자라면 True 문자라면 False 반환
def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False



# 받은 변수에 무엇이든 들어있으면 True 반환. 값이 들어있지 않은 빈 리스트이면 False 반환
def isEmpty(s):
    if s:        
        return True
    elif not s:
        # print('아무런 값도 입력되지 않았습니다.\n')
        return False



# 팀 이름 저장 함수
def input_team_name(i):

    while(1):

        teamName = input("%d팀의 이름을 입력하세요> " % i)   # 팀 이름 입력받기

        if not isEmpty(teamName): continue  # 아무런 값이 입력되지 않았다면 정보 입력 다시 받기
        else: break                         # 값이 입력됐다면 루프 빠져나가기
            

    return teamName     # 팀 이름 리턴



# 입력된 선수 정보가 제대로 들어왔는지 확인. 잘못된 값이면 False 리턴
def playerInfo_error_check(infoPlayer):

    if isNumber(infoPlayer[0]) == True: return False        # 선수 이름이 잘못 입력됨
    elif isNumber(infoPlayer[1]) == False: return False     # 타율에 숫자가 아닌 문자가 잘못 입력됨

    else:
        typeChangedBAValue = float(infoPlayer[1])               # 타율 값이 들어있는 infoPlayer[1] 에서 값을 읽어서 float으로 형 변환 후 typeChangedBAValue 변수에 저장

        if (0.1 <= typeChangedBAValue <= 0.5): return True      # 타율이 제대로 된 범위 안에 있음   
        else: return False                                      # 타율이 제대로 된 범위 값을 넘어갔음
            


# 선수 정보 받기
def input_hitter_info(howManyHittersSoFar):

    while(1):
        infoPlayer = input("%d번 타자 정보 입력> " % howManyHittersSoFar)

        p = re.compile('.*,\s.*')           # 정규 표현식을 사용하여 ', ' 형태가 없는 모든 입력을 다시 입력받음
        if not p.search(infoPlayer): continue

        infoPlayer = infoPlayer.split(', ') # 콤마다음에 공백한칸이 나올때마다 문자열 값을 나눠서 변수에 저장. 리스트 형식으로 저장됨.
        errorChecked = playerInfo_error_check(infoPlayer)   # 입력받은 타자 정보가 올바른지 체크

        if not errorChecked: continue       # 입력받은 타자 정보가 올바르지 않다면 입력 다시 받기

        else:
            infoPlayer[1] = "%0.3f" % float(infoPlayer[1])  # 타율을 소수점 셋째 자리까지만 받기
            return infoPlayer



# 메뉴 선택한 뒤 선택한 값 리턴하기
def choose_Menu():

    while(1):        
        selectedMenu = input("메뉴선택 (1 - 3) ")   # 메뉴 선택값 받기

        if not isEmpty(selectedMenu): continue          # 아무런 값이 입력되지 않았다면 입력 다시 받기
        elif isNumber(selectedMenu) == False: continue  # 숫자 대신 문자가 입력됐다면 입력 다시 받기
        else: break                                     # 메뉴가 골라졌다면 루프 탈출

    return selectedMenu



# 팀이름, 선수이름, 선수타율을 저장하기 위한 2중 리스트 선언
def define_List_dimensions():
    
    namePlayer = [0,0,0,0,0,0,0,0,0,0]
    battingAveragePlayer = [0,0,0,0,0,0,0,0,0,0]
    temaInfoList = [namePlayer, battingAveragePlayer]

    return temaInfoList




# 팀이름, 선수이름 입력받아서 배열에 넣기
def input_all_info_team(teamNumber):

    temaInfoList = define_List_dimensions() # 팀이름, 선수이름, 선수타율을 저장하기 위한 2중 리스트 선언
    
    teamName = input_team_name(teamNumber)  # 팀 이름 입력받은 함수 호출. 받은 이름을 변수에 넣기
    temaInfoList[0][0] = teamName           # 팀 이름을 리스트[0][0] 에 넣기
    
    i = 1
    while i <= 9:                           # 팀의 9명의 선수 정보 입력받기

        infoPlayer = input_hitter_info(i)   # 선수 정보 입력
        temaInfoList[0][i] = infoPlayer[0]  # 선수 이름을 배열에 입력
        temaInfoList[1][i] = infoPlayer[1]  # 선수 타율을 배열에 입력
        i+=1

    return temaInfoList



# 옵션에서 2번을 선택했을 때 팀 정보 표시하기
def print_out_teams_info(temaInfo):

    print(temaInfo[0][0], "팀 정보\n")
    i = 1
    while i <= 9:
        print(i,"번 ",temaInfo[0][i], ", ",temaInfo[1][i])
        i+=1

    return




if __name__== "__main__":

    while(1):
        print('신나는 야구 게임!' + '\n1. 데이터 입력' + '\n2. 데이터 출력' + '\n3. 시합 시작\n')

        # 메뉴 선택하기
        selectedMenu = choose_Menu()
        
        # 메뉴에서 1번을 선택했다면 팀 정보를 입력받기
        if selectedMenu == '1':

            teamInfo_1st = input_all_info_team(1)     # 첫 번째 팀 정보 입력 받아서 배열에 저장
            print()
            teamInfo_2nd = input_all_info_team(2)     # 두 번째 팀 정보 입력 받아서 배열에 저장
            print('팀 데이터 입력이 완료되었습니다.\n')
            continue

        # 메뉴에서 2번을 선택했다면 팀 정보 표시하기
        elif selectedMenu == '2':
            print_out_teams_info(teamInfo_1st)
            print()
            print_out_teams_info(teamInfo_2nd)
            print()
            continue

            # if not isEmpty(teamInfo_1st): continue          # 아무런 값이 입력되지 않았다면 입력 다시 받기

        
            '''
            print("팀이름: ", teamInfo_1st[0][0])
            i = 1
            while i <= 9:
                print(i,"번 선수", "\n이름: ",teamInfo_1st[0][i], "\n타율:",teamInfo_1st[1][i])
                i+=1
            '''

        elif selectedMenu == '3': break

