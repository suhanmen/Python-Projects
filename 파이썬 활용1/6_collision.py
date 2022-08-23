#충돌 처리

import pygame

pygame.init()  # 초기화 반드시 해야함

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("나도 게임")  # 게임 이름

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\dlatn\\PycharmProjects\\파이썬 활용1\\파이썬 활용1\\back_ground.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\Users\\dlatn\\PycharmProjects\\파이썬 활용1\\파이썬 활용1\\character.png")
character_size = character.get_rect().size  # 이미지의 크기를 구해온다.
character_width = character_size[0]  # 캐릭터의 가로 크기
character_height = character_size[1]  # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2)  # 화면 가로의 절반 크기에 해당하는 곳에 위치한다. (가로)
character_y_pos = screen_height - character_height  # 화면 세로 크기 가장 아래에 해당하는 곳에 위치한다. (세로) // 좌표인 부분에서 그려지니까 빼주는 것 이다.

#캐릭터 이동할 좌표
to_x = 0
to_y = 0

#캐릭터 이동 속도
character_speed = 0.6


# 적 enemy 캐릭터 만들어주기
enemy = pygame.image.load("C:\\Users\\dlatn\\PycharmProjects\\파이썬 활용1\\파이썬 활용1\\enemy.png")
enemy_size = enemy.get_rect().size  # 이미지의 크기를 구해온다.
enemy_width = enemy_size[0]  # 캐릭터의 가로 크기
enemy_height = enemy_size[1]  # 캐릭터의 세로 크기
enemy_x_pos = (screen_width / 2) - (enemy_width / 2)  # 화면 가로의 절반 크기에 해당하는 곳에 위치한다. (가로)
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)  # 화면 세로 크기 가장 아래에 해당하는 곳에 위치한다. (세로) // 좌표인 부분에서 그려지니까 빼주는 것 이다.



# 이벤트 루프
running = True  # 게임이 진행중인가?
while running:

    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정
    print("fps : " + str(clock.get_fps())) # 현재 프레임 수를 run화면에 보여준다.


    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?

        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
            running = False  # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= character_speed #to_x = to_x - 1
            elif event.key == pygame.K_RIGHT:  # 캐릭터를 오른쪽으로
                to_x += character_speed
            elif event.key == pygame.K_UP:  # 캐릭터를 위쪽으로
                to_y -= character_speed # 윈도우창 기준이다
            elif event.key == pygame.K_DOWN:  # 캐릭터를 아래로
                to_y += character_speed

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춘다.
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    '''캐릭터가 100 만큼 이동을 해야함
    10 fps : 1초 동안에 10번 동작 -> 1번에 몇 만큼 이동? 10만큼 10 * 10 = 100
    20 fps : 1초 동안에 20번 동작 -> 1번에 5만큼 5 * 20 = 100
    즉 프레임이 달라진다고 게임 속도가 달라지면 안된다. 이동이 부드럽거나 그런건 가능해도. 따라서 dt를 곱해서 보정한다.'''
    #현재 character 포지션에다가 값을 더해준다.
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    #캐릭터가 화면에 나가지않게 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    #캐릭터가 화면에 나가지않게 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height


    #충돌 처리를 위한 rect정보 업데이트
#일단 캐릭터의 rect에 주소정보를 넣어준다.
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
#enemy의 rect에 주소정보를 넣어준다.
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    #충돌 체크
    if character_rect.colliderect(enemy_rect): # 사각형기준으로 충돌하는지의 검사
        print("충돌했어요")
        running = False


    screen.blit(background, (0, 0))  # 배경 그리기를 가져와서 게임화면 채우기

    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터를 실제로 추가하기

    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적을 실제로 추가하기

    pygame.display.update()  # 게임화면을 다시 그르기! 계속적으로 그려져야한다.

# pygame 종료
pygame.quit()