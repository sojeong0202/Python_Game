import pygame
import time
import random
from game_objects import Spaceship, Bullet, Enemy
from datetime import datetime
from settings import FONTS_PATH, size, screen, clock, black
from utils import crash

# 우주선 생성
ss = Spaceship()  # x좌표, y좌표, 이동 속도
ss.x = round((size[0] - ss.sx)/2)
ss.y = size[1] - ss.sy - 15

left_go = False
right_go = False
up_go = False
down_go = False
space_go = False

m_list = []
a_list = []

black = (0, 0, 0)
k = 0

game_over = 0
kill = 0
loss = 0

# 4-0. 게임 시작 대기 화면
SB = 0
while SB == 0:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                SB = 1
    screen.fill(black)
    font = pygame.font.Font(FONTS_PATH['bauhaus93'], 20)
    text = font.render("PRESS SPACEBAR TO START THE GAME", True, (255, 255, 255)) # True는 Anti aliasing 옵션 켜는 것, 글자가 매끄러워짐
    screen.blit(text, (40, round(size[1]/2-50)))
    pygame.display.flip()

# 4. 메인 이벤트
start_time = datetime.now()
SB = 0
while SB == 0:
    # FPS 설정
    clock.tick(60)

    # 각종 입력 감지
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            SB = 1
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left_go = True
            elif event.key == pygame.K_RIGHT:
                right_go = True
            elif event.key == pygame.K_UP:
                up_go = True
            elif event.key == pygame.K_DOWN:
                down_go = True
            elif event.key == pygame.K_SPACE:
                space_go = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_go = False
            elif event.key == pygame.K_RIGHT:
                right_go = False
            elif event.key == pygame.K_UP:
                up_go = False
            elif event.key == pygame.K_DOWN:
                down_go = False
            elif event.key == pygame.K_SPACE:
                space_go = False

    # 시간 흐름
    now_time = datetime.now()
    delta_time = round((now_time - start_time).total_seconds())
    
    # 방향키 (연속)이동
    if left_go == True:
        ss.x -= ss.move
        if ss.x < 0:
            ss.x = 0
    elif right_go == True:
        ss.x += ss.move
        if ss.x >= size[0] - ss.sx:
            ss.x = size[0] - ss.sx
    elif up_go == True:
        ss.y -= ss.move
        if ss.y < 0:
            ss.y = 0
    elif down_go == True:
        ss.y += ss.move
        if ss.y >= size[1] - ss.sy:
            ss.y = size[1] - ss.sy

    # 총알 발사
    if space_go == True and k % 6 == 0:
        mm = Bullet()
        mm.x = round(ss.x + (ss.sx-mm.sx)/2)
        mm.y = ss.y - mm.sy/2
        m_list.append(mm)
    k += 1
    
    # 총알 이동 및 화면 이탈 총알 삭제
    d_list = []
    for i in range(len(m_list)):
        m = m_list[i]
        m.y -= m.move
        if m.y <= -m.sy:
            d_list.append(i)
    d_list.reverse()
    for d in d_list:
        del m_list[d]

    # 적 생성 및 이동, 화면 이탈 적 삭제
    if random.random() > 0.98:
        aa = Enemy()
        aa.x = random.randrange(0, size[0]-aa.sx-round(ss.sx/2))
        aa.y = 10
        a_list.append(aa)
    d_list = []
    for i in range(len(a_list)):
        a = a_list[i]
        a.y += a.move
        if a.y >= size[1]:
            d_list.append(i)
    d_list.reverse()
    for d in d_list:
        del a_list[d]
        loss += 1

    # 총알과 적의 충돌 처리
    dm_list = []
    da_list = []
    for i in range(len(m_list)):
        for j in range(len(a_list)):
            m = m_list[i]
            a = a_list[j]
            if crash(a, m) == True:
                dm_list.append(i)
                da_list.append(j)
    dm_list = list(set(dm_list)) # 중복 제거
    da_list = list(set(da_list)) # 중복 제거
    dm_list.reverse()
    da_list.reverse()
    try:
        for dm in dm_list:
            del m_list[dm]
        for da in da_list:
            del a_list[da]
            kill += 1
    except:
        pass

    # 우주선과 적의 충돌 처리
    for i in range(len(a_list)):
        a = a_list[i]
        if crash(ss, a) == True:
            SB = 1
            game_over = 1

    # 그리기
    screen.fill(black)
    ss.show()
    for m in m_list:
        m.show()
    for a in a_list:
        a.show()

    # 점수 및 시간 표시
    font = pygame.font.Font(FONTS_PATH['bauhaus93'], 20)
    text_kill = font.render("killed : {}   loss : {}".format(kill, loss), True, (255, 255, 0))
    screen.blit(text_kill, (10, 5))
    text_time = font.render("time : {}".format(delta_time), True, (255, 255, 255))
    screen.blit(text_time, (size[0]-100, 5))

    # 화면 업데이트
    pygame.display.flip()

# 게임 종료 처리
while game_over == 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = 0
    font = pygame.font.Font(FONTS_PATH['bauhaus93'], 48)
    text = font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(text, (80, round(size[1]/2-50)))
    pygame.display.flip()
pygame.quit()