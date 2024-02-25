import sys
import pygame
import random

from pygame.locals import QUIT

# 1. 게임 초기화
pygame.init()

# 2. 게임창 옵션 설정
size = [400, 900]
screen = pygame.display.set_mode(size) # 게임창 크기 설정

pygame.display.set_caption("My Game") # 제목 설정

# 3. 게임 내 필요한 설정
clock = pygame.time.Clock()

class obj:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.move = 0
    
    def put_img(self, address):
        if address[-3:] == "png":
            self.img = pygame.image.load(address).convert_alpha()
        else:
            self.img = pygame.image.load(address)
        self.sx, self.sy = self.img.get_size()

    def change_size(self, sx, sy):
        self.img = pygame.transform.scale(self.img, (sx, sy))
        self.sx, self.sy = self.img.get_size()
        
    def show(self):
        screen.blit(self.img, (self.x, self.y))

ss = obj()
ss.put_img("C:/python_game/img/ss.png")
ss.change_size(50, 80)
ss.x = round((size[0] - ss.sx)/2)
ss.y = size[1] - ss.sy - 15
ss.move = 5

left_go = False
right_go = False
up_go = False
down_go = False
space_go = False

m_list = []
a_list = []

black = (0, 0, 0)
k = 0

# 4. 메인 이벤트
SB = 0
while SB == 0:

    # 4-1. FPS 설정
    clock.tick(60) # 1초에 60번 while 문이 반복

    # 4-2. 각종 입력 감지
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            SB = 1

        # 키를 눌렀을 때   
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
                k = 0

        # 키를 뗐을 때
        elif event.type == pygame.KEYUP:
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

    # 4-3. 입력, 시간에 따른 변화
    
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
        
    # 총알 생성
    if space_go == True and k % 6 == 0:
        mm = obj()
        mm.put_img("C:/python_game/img/mm.png")
        mm.change_size(40, 30)
        mm.x = round(ss.x + (ss.sx-mm.sx)/2)
        mm.y = ss.y - mm.sy/2
        mm.move = 15
        m_list.append(mm)
    
    k += 1

    # 총알 이동 및 지우기
    d_list = []
    for i in range(len(m_list)):
        m = m_list[i]
        m.y -= m.move
        if m.y <= -m.sy:
            d_list.append(i)
    # 실질적으로 지우는 부분
    d_list.reverse()
    for d in d_list:
        del m_list[d]

    # 적 생성
    if random.random() > 0.98:
        aa = obj()
        aa.put_img("C:/python_game/img/aa.png")
        aa.change_size(40, 40)
        aa.x = random.randrange(0, size[0]-aa.sx-round(ss.sx/2))
        aa.y = 10
        aa.move = 1
        a_list.append(aa)

    # 적 이동 및 지우기
    d_list = []
    for i in range(len(a_list)):
        a = a_list[i]
        a.y += a.move
        if a.y >= size[1]:
            d_list.append(i)
    # 실질적으로 지우는 부분
    d_list.reverse()
    for d in d_list:
        del a_list[d]
        

    # 4-4. 그리기
    screen.fill(black)
    ss.show()
    for m in m_list:
        m.show()
    for a in a_list:
        a.show()
    
    # 4-5. 업데이트
    pygame.display.flip()

# 5. 게임종료
pygame.quit()