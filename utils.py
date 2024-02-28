# 충돌 판정
def crash(a, b):
    if (a.x-b.sx <= b.x) and (b.x <= a.x+a.sx):
        if(a.y-b.sy <= b.y) and (b.y <= a.y+a.sy):
            return True # 충돌함
        else:
            False # 충돌 X
    else: False # 충돌 X