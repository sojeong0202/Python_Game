import sys
import pygame
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

black = (0, 0, 0)

# 4. 메인 이벤트
SB = 0
while SB == 0:

    # 4-1. FPS 설정
    clock.tick(60) # 1초에 60번 while 문이 반복

    # 4-2. 각종 입력 감지
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            SB = 1

    # 4-3. 입력, 시간에 따른 변화


    # 4-4. 그리기
    screen.fill(black)
    ss.show()
    
    # 4-5. 업데이트
    pygame.display.flip()

# 5. 게임종료
pygame.quit()