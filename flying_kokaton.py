import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #練習1
    kk_img = pg.image.load("fig/3.png") #練習3
    kk_img = pg.transform.flip(kk_img,True,False) #練習3
    bg_img2 = pg.transform.flip(bg_img, True, False)  #練習8
    kk_rct = kk_img.get_rect() #10-1
    kk_rct.center = 300, 200 # 10-2

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr % 3200 #練習9
        mv = [-1, 0] #演習2
        key_lst = pg.key.get_pressed() #10-3
        # kk_rct.move_ip((-1, 0))          #演習1
        if key_lst[pg.K_UP]:     #練習10-4
            mv[1] = -1 #演習2
        if key_lst[pg.K_DOWN]:
            mv[1] = 1 #演習2
        if key_lst[pg.K_LEFT]: 
            mv[0] = -1  #演習2
        if key_lst[pg.K_RIGHT]:
            mv[0] = 1 #演習2
        kk_rct.move_ip(mv) #演習2

        
        screen.blit(bg_img, [-x,0]) #練習2 #練習5
        screen.blit(bg_img, [-x+3200,0]) #練習9
        screen.blit(bg_img2, [-x+1600, 0]) #練習7 #練習8
        screen.blit(kk_img, kk_rct) #練習4 #練習10
        pg.display.update()
        tmr += 1        
        clock.tick(200)#練習6


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()