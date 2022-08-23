#게임에 캐릭터 추가해주기

import pygame

pygame.init() #초기화 반드시 해야함

# 화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("나도 게임") #게임 이름

#배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\dlatn\\PycharmProjects\\파이썬 활용1\\파이썬 활용1\\back_ground.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\Users\\dlatn\\PycharmProjects\\파이썬 활용1\\파이썬 활용1\\character.png")
character_size = character.get_rect().size #이미지의 크기를 구해온다.
character_width = character_size[0] #캐릭터의 가로 크기
character_height = character_size[1] #캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2)# 화면 가로의 절반 크기에 해당하는 곳에 위치한다. (가로)
character_y_pos = screen_height - character_height# 화면 세로 크기 가장 아래에 해당하는 곳에 위치한다. (세로) // 좌표인 부분에서 그려지니까 빼주는 것 이다.

# 이벤트 루프
running = True #게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?

        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님


    screen.blit(background, (0,0)) # 배경 그리기를 가져와서 게임화면 채우기

    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터를 실제로 추가하기

    pygame.display.update() # 게임화면을 다시 그르기! 계속적으로 그려져야한다.
    
    
# pygame 종료
pygame.quit()