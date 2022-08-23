#키보드에 따라 캐릭터가 움직임을 코딩하기.

import pygame

pygame.init()  # 초기화 반드시 해야함

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("나도 게임")  # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\dlatn\\PycharmProjects\\파이썬 활용1\\파이썬 활용1\\back_ground.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\Users\\dlatn\\PycharmProjects\\파이썬 활용1\\파이썬 활용1\\character.png")
character_size = character.get_rect().size  # 이미지의 크기를 구해온다.
character_width = character_size[0]  # 캐릭터의 가로 크기
character_height = character_size[1]  # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2)  # 화면 가로의 절반 크기에 해당하는 곳에 위치한다. (가로)
character_y_pos = screen_height - character_height  # 화면 세로 크기 가장 아래에 해당하는 곳에 위치한다. (세로) // 좌표인 부분에서 그려지니까 빼주는 것 이다.

#이동할 좌표
to_x = 0
to_y = 0


# 이벤트 루프
running = True  # 게임이 진행중인가?
while running:
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?

        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
            running = False  # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= 1 #to_x = to_x - 1
            elif event.key == pygame.K_RIGHT:  # 캐릭터를 오른쪽으로
                to_x += 1
            elif event.key == pygame.K_UP:  # 캐릭터를 위쪽으로
                to_y -= 1 # 윈도우창 기준이다
            elif event.key == pygame.K_DOWN:  # 캐릭터를 아래로
                to_y += 1

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춘다.
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    #현재 character 포지션에다가 값을 더해준다.
    character_x_pos += to_x
    character_y_pos += to_y

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



    screen.blit(background, (0, 0))  # 배경 그리기를 가져와서 게임화면 채우기

    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터를 실제로 추가하기

    pygame.display.update()  # 게임화면을 다시 그르기! 계속적으로 그려져야한다.

# pygame 종료
pygame.quit()