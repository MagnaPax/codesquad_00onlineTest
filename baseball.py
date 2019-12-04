import random
import re



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


##############################################################################################################
###                                         팀 정보 출력                                                    ###
##############################################################################################################



# 옵션에서 2번을 선택했을 때 팀 정보 표시하기
def print_out_teams_info(temaInfo):

    print(temaInfo[0][0], "팀 정보\n")
    i = 1
    while i <= 9:
        print(i,"번 ",temaInfo[0][i], ", ",temaInfo[1][i])
        i+=1

    return


##############################################################################################################
###                                             경기시작                                                    ###
##############################################################################################################

# 경기 결과 값을 무작위로 선택
def making_random_result():
    baseball_options = ['스트라이크', '볼', '안타', '아웃']
    randomResult = random.choice(baseball_options)
#    print(randomResult)
    return randomResult


# 게임 시작 함수
def startGame(teamInfo_1st, teamInfo_2nd):
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


        # 메뉴에서 3번을 선택했다면 옵션 선택받는 루프 빠져나가서 게임 시작
        elif selectedMenu == '3': break

    # 게임 시작하는 함수
    startGame(teamInfo_1st, teamInfo_2nd)


