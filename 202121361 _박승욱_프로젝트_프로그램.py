import random

def Q1():
    print('탈출 할 문을 정하라고만 했지, 탈출할 수 있다고는 안했습니다. 퀴즈를 맞추세요^^\n')
    print('불이 켜진 양초 10개가 있었다. 근데 바람이 불어서 2개가 꺼지고 말았다.')
    print('그리고 잠시 후에 보니 또 1개가 꺼져있었다.')
    print('그로부터 바람이 닿지 않도록 하고 그 후 1개도 꺼지지 않았다면')
    print('끝까지 남아 있었던 양초는 몇 개 일까?\n')
    count1 = 1
    anser1 = 0 # 정답 : 3
    while (anser1 != 3):
        anser1 = int(input('정답 입력 : '))
        if anser1 == 3:
            print('정답, 7개의 양초는 타면 없어진다. 그러므로 남은 양초는 불이 꺼진 3개!\n')
            print('시도 횟수 : %d\n' %count1)
            print('[탈출 성공]')
            print('게임을 진행하시려면 game()을 입력하세요.')
        else:
            print('다시 생각해봐...\n')
            count1 += 1

def Q2():
    print('탈출 할 문을 정하라고만 했지, 탈출할 수 있다고는 안했습니다. 퀴즈를 맞추세요^^\n')
    print('20분 후면 가라앉게 되는 여객선에 15명의 사람이 타고 있다.')
    print('정원이 5명인 보트 1척을 이용해 가까운 섬으로 피난하려고 하나')
    print('바다에는 식인 상어가 있으므로 헤엄을 쳐서 이동할 수 없다.')
    print('여객선과 섬을 왕복하는 데에 9분이 걸린다고 할 때 몇 명을 구할 수 있을까?\n')
    count2 = 1
    anser2 = 0 # 정답 : 13
    while (anser2 != 13):
        anser2 = int(input('정답 입력 : '))
        if anser2 == 13:
            print('정답, 배를 몰아야하는 사람은 제외하고 4명씩 섬으로 이동할 수 있다.')
            print('총 8명을 구하는데 걸린 시간은 18분이고, 마지막 한 팀은 5명이 이동하므로 13명!\n')
            print('시도 횟수 : %d\n' %count2)
            print('[탈출 성공]')
            print('게임을 진행하시려면 game()을 입력하세요.')
        else:
            print('다시 생각해봐...\n')
            count2 += 1
            
def Q3():
    print('탈출 할 문을 정하라고만 했지, 탈출할 수 있다고는 안했습니다. 퀴즈를 맞추세요^^\n')
    print('고양이 5마리가 5분 동안 쥐를 5마리 잡을 수 있다고 한다.')
    print('같은 비율로 쥐를 잡을 때,')
    print('100마리의 쥐를 100분만에 잡기 위해서는 몇 마리의 고양이가 있어야 할까?\n')
    count3 = 1
    anser3 = 0 # 정답 : 5
    while (anser3 != 5):
        anser3 = int(input('정답 입력 : '))
        if anser3 == 5:
            print('정답, 5마리의 고양이가 5분 동안 5마리의 쥐를 잡는다. 5분 뒤에는 10마리가 잡히게 된다.')
            print('즉, 10분 동안 10마리를 잡고, 20분 동안 20마리를 잡기 때문에, 100분 동안 100마리를 잡는다!\n')
            print('시도 횟수 : %d\n' %count3)
            print('[탈출 성공]')
            print('게임을 진행하시려면 game()을 입력하세요.')
        else:
            print('다시 생각해봐...\n')
            count3 += 1


def game():
    print('당신은 어딘지 모를 방 안에 갖혔습니다. 지금부터 탈출을 위해 게임을 진행합니다.')
    print('업 다운 게임을 시작합니다.')
    while True :
        num1 = int(input('게임에서의 최소값을 설정합니다. 원하는 값을 입력하세요: '))
        num2 = int(input('게임에서의 최대값을 설정합니다. 원하는 값을 입력하세요: '))
        if num2 > num1:
            x=random.randint(num1,num2)
            break
        else:
            print('\n최대값이 최소값보다 커야합니다.\n')

    while True:
        guess = int(input('\n설정한 범위 내의 숫자를 맞혀주세요.\n숫자 입력: '))
    
        if guess == x:
            print('\n정답!\n\n이제',x,'값으로 베스킨라빈스 게임을 시작합니다.' )
            break
        elif guess > x:
            print('\n[ Down ]')
        else:
            print('\n[  Up  ]')

    print('1부터',x,'까지의 숫자를 번갈아 불러', x,'을(를) 부르는 사람이 지는 게임 입니다.\n')
    while True :
        turn = int(input('선공을 원하시면 0, 후공을 원하시면 1 을 입력해주세요: '))
        if turn == 0 or turn == 1:
            print('\n순서가 정해졌습니다.\n\n==============================[ GAMESTART ]==============================\n')
            break
        else:
            print('\n숫자 0또는 1만을 입력해주세요.\n')

    number = 0
    while True:
        if turn == 0:
            p1 = int(input('사용자가 부를 숫자의 개수 입력 (1 ~ 3): '))
            if p1 == 1 or p1 == 2 or p1 == 3:
                for _ in range(p1):
                    number += 1
                    print('사용자: ', number)
                    turn = 1
            else:
                print('\n숫자 1에서 3까지만을 입력해주세요.\n')
                continue
            
        elif turn == 1:   
            p2 = random.randint(1, 3)
            print('컴퓨터가 숫자를 입력중...')
            for _ in range(p2):
                number += 1
                print('컴퓨터: ', number)
                turn = 0

        if number >= x:
             break

    if turn == 0:
        print('\n★★★★★★★★★★[ 당신이 승리하였습니다. ]★★★★★★★★★★\n')
        while (True):
            door = int(input('탈출하기 위해 사용 할 수 있는 문이 3개 있습니다. 탈출 할 문의 숫자를 입력하세요. [1,2,3]'))
            if (door == 1):
                Q1()
                break
            if (door == 2):
                Q2()
                break
            if (door == 3):
                Q3()
                break
    else:
        print('\n☠☠☠☠☠☠☠☠☠☠[ 탈출 실패 ]☠☠☠☠☠☠☠☠☠☠\n')
        print('게임을 진행하시려면 game()을 입력하세요.')
        
print('게임을 진행하시려면 game()을 입력하세요.')
