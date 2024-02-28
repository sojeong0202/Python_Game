import pygame

# 이미지 파일 경로
IMAGES_PATH = {
    'spaceship': "C:/python_game/img/ss.png",
    'bullet': "C:/python_game/img/mm.png",
    'enemy': "C:/python_game/img/aa.png",
    # 필요한 만큼 추가
}

FONTS_PATH = {
    'bauhaus93' : "C:/Windows/Fonts/BAUHS93.TTF"
}

# 1. 게임 초기화
pygame.init()

# 2. 게임창 옵션 설정
size = [400, 900]
screen = pygame.display.set_mode(size) # 게임창 크기 설정

pygame.display.set_caption("My Game") # 제목 설정

# 3. 게임 내 필요한 설정
clock = pygame.time.Clock()
black = (0, 0, 0)