import pygame
import os
from random import randint


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    return image, image.get_rect()

def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    fullname = os.path.join('data', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error:
        print ('Cannot load sound: %s' % fullname)
        raise SystemExit(str(pygame.geterror()))
    return sound

class Mlotek(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.off, self.rect1 = load_image('hammerpix_off.png', -1)
        self.on = load_image('hammerpix_on.png', -1)[0]
        self.image, self.rect = self.off, self.rect1
    def update(self):
        self.pos = pygame.mouse.get_pos()
        self.rect.center = self.pos
    def cymbal(self, target):
        self.image = self.on
        hitbox = self.rect.inflate(-870, -720)
        hitbox = hitbox.move(-50, 75)
        return hitbox.colliderect(target.rect)
    def cymbal_button(self, target):
        self.image = self.on
        hitbox = self.rect.inflate(-100, -120)
        hitbox = hitbox.move(-45, 30)
        return hitbox.colliderect(target.rect)
        
    def uncymbal(self):
        self.image = self.off
        
class Play(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('play.png', -1)
        self.rect.center = (250,460)

class Play_ll(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('play_ll.png', -1)
        self.rect.center = (470,625)

class Exit(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('exit1.png', -1)
        self.rect.center = (690,460)

class Exit_ss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('exit2.png', -1)
        self.rect.center = (690,500)
class Again_ss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('again.png')
        self.rect.center = (250,500)
class level1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('wambg_mini.png')
        self.rect.center = (290,210)
class level2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('wambg2_mini.png')
        self.rect.center = (640,210)
class diff1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('1.png')
        self.rect.center = (360, 470)
class diff2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('2.png')
        self.rect.center = (470, 470)
class diff3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('3.png')
        self.rect.center = (580, 470)
class check1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('check1.png')
        self.check1_pos = [(360, 470), (470, 470), (580, 470)]
        self.rect.center = self.check1_pos[0]
class check2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('check2.png')
        self.check2_pos = [(290, 210), (640, 210)]
        self.rect.center = self.check2_pos[0]

class Krecik(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.dziurki1 = [(-274, 20), (-4, 20), (266, 20), (-274, 200), (-4, 200), (266, 200)]
        self.dziurki2 = [(-262, -66), (78, -53), (301, -164), (-188, 85), (223, 139), (-33, 268)]
        self.image, self.rect = load_image('krecik.png', -1)
        self.spr = -1
        self.uciekej1()
        self.ucieczka = 0
        self.speed = [150, 145, 140, 135, 130, 125, 120, 115, 110, 100, 90, 80, 70, 60, 50, 45, 40, 35, 30, 25]
        self.level_back = 0
        self.difficulty = 0
        self.level = 0
    def uciekej1(self):
        self.wsp = randint(0,5)
        if (self.wsp == self.spr):
            self.uciekej1()
        self.spr = self.wsp
        self.rect.topleft = self.dziurki1[self.wsp]
    def uciekej2(self):
        self.wsp = randint(0,5)
        if (self.wsp == self.spr):
            self.uciekej2()
        self.spr = self.wsp
        self.rect.topleft = self.dziurki2[self.wsp]
    def czekanko(self):
        self.ucieczka += 1

class Hit(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('data', 'hit.png'))
        self.rect = self.image.get_rect()
        self.rect.center = (470, 160)
        self.show = -1
    def hit(self, screen):
        screen.blit(self.image, self.rect)
    def check(self, screen):
        if(self.show >= 0):
            self.hit(screen)
            self.show += 1
            if(self.show > 40):
                self.show = -1

class Gierka():
    def __init__(self):
        pygame.init()
        size = (940, 780)
        self.black = (0, 0, 0)
        self.screen = pygame.display.set_mode(size)
        pygame.mouse.set_visible(0)
        pygame.display.set_caption('nie')
        self.background1 = load_image('wambg.png')[0]
        self.background2 = load_image('wambg2.png')[0]
        self.background_menu = load_image('wambg_menu.png')[0]
        self.menu_music = load_sound('house.flac')
        self.level_choice_music = load_sound('market.flac')
        self.level1_music = load_sound('horse_race.flac')
        self.level2_music = load_sound('lostwoods.flac')
        self.results_music = load_sound('results.ogg')
        self.click_snd = load_sound('hit1.ogg')
        self.wmorde_snd = load_sound('hurt.ogg')
        self.clock = pygame.time.Clock()
        self.time = Time()
        self.play = Play()
        self.play_ll = Play_ll()
        self.exit = Exit()
        self.exit_ss = Exit_ss()
        self.again_ss = Again_ss()
        self.level1 = level1()
        self.level2 = level2()
        self.diff1 = diff1()
        self.diff2 = diff2()
        self.diff3 = diff3()
        self.check1 = check1()
        self.check2 = check2()
        self.krecik = Krecik()
        self.mlotek = Mlotek()
        self.hit = Hit()
        self.tekst = Tekst()
        self.level_choice = 1
        self.wmorde = 0
        self.allsprites = pygame.sprite.RenderPlain(self.krecik, self.mlotek)
        self.menu_sprites = pygame.sprite.RenderPlain(self.play, self.exit, self.mlotek)
        self.ss_sprites = pygame.sprite.RenderPlain(self.again_ss, self.exit_ss, self.mlotek)
        self.ll_sprites = pygame.sprite.RenderPlain(self.check1, self.check2, self.diff1, self.diff2, self.diff3, self.level1, self.level2, self.play_ll, self.mlotek)
        self.graj = True
        self.jechanka = 0
    
    def menu(self):
        self.menu_music.play(-1)
        self.menu_jazda = True
        while self.menu_jazda:
            if(self.jechanka > 0):
                if(self.jechanka > 60):
                    self.menu_jazda = False
                    self.jechanka = 0
                else:
                    self.jechanka += 1
            self.screen.blit(self.background_menu, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.graj = False
                    self.menu_jazda = False
                elif (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.graj = False
                    self.menu_jazda = False
                elif (event.type == pygame.MOUSEBUTTONDOWN):
                    if(self.mlotek.cymbal_button(self.play)):
                        self.click_snd.play()
                        #self.wmorde_snd.play()
                        self.jechanka = 1
                    elif(self.mlotek.cymbal_button(self.exit)):
                        self.click_snd.play()
                        #self.wmorde_snd.play()
                        self.graj = False
                        self.menu_jazda = False
                    else:
                        self.click_snd.play()
                elif(event.type == pygame.MOUSEBUTTONUP):
                    self.mlotek.uncymbal()
            self.mlotek.update()
            self.tekst.title(self.screen)
            self.menu_sprites.draw(self.screen)
            self.clock.tick(120)
            pygame.display.flip()
        self.menu_music.stop()
            
    def level(self):
        self.level_choice_music.play(-1)
        self.jechanka = 0
        self.ll_jazda = True
        while self.ll_jazda:
            if(self.jechanka > 0):
                if(self.jechanka > 180):
                    self.ll_jazda = False
                else:
                    self.jechanka += 1
            self.screen.fill(self.black)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.graj = False
                    self.ll_jazda = False
                elif (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.graj = False
                    self.ll_jazda = False
                elif(event.type == pygame.MOUSEBUTTONDOWN):
                    if(self.mlotek.cymbal_button(self.play_ll)):
                        self.click_snd.play()
                        #self.wmorde_snd.play()
                        self.jechanka = 1
                    if(self.mlotek.cymbal_button(self.level1)):
                        self.click_snd.play()
                        self.check2.rect.center = self.check2.check2_pos[0]
                        self.level_choice = 1
                    if(self.mlotek.cymbal_button(self.level2)):
                        self.click_snd.play()
                        self.check2.rect.center = self.check2.check2_pos[1]
                        self.level_choice = 2
                    if(self.mlotek.cymbal_button(self.diff1)):
                        self.click_snd.play()
                        self.check1.rect.center = self.check1.check1_pos[0]
                        self.krecik.level = 0
                        self.krecik.difficulty = 8
                    if(self.mlotek.cymbal_button(self.diff2)):
                        self.click_snd.play()
                        self.check1.rect.center = self.check1.check1_pos[1]
                        self.krecik.level = 7
                        self.krecik.difficulty = 13
                    if(self.mlotek.cymbal_button(self.diff3)):
                        self.click_snd.play()
                        self.check1.rect.center = self.check1.check1_pos[2]
                        self.krecik.level = 12
                        self.krecik.difficulty = 19
                    else:
                        self.click_snd.play()
                elif(event.type == pygame.MOUSEBUTTONUP):
                    self.mlotek.uncymbal()
            self.tekst.choose_level(self.screen)
            self.mlotek.update()
            self.ll_sprites.draw(self.screen)
            self.clock.tick(120)
            pygame.display.flip()
        self.level_choice_music.stop()
    
    def wam_ll1(self):
        self.level1_music.play()
        self.jazda = True
        self.krecik.level_back = self.krecik.level
        while self.jazda:
            self.screen.blit(self.background1, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.jazda = False
                elif (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.jazda = False
                elif(event.type == pygame.MOUSEBUTTONDOWN):
                    if(self.mlotek.cymbal(self.krecik)):
                        self.click_snd.play()
                        self.wmorde_snd.play()
                        self.hit.show = 0
                        self.krecik.uciekej1()
                        self.krecik.ucieczka = 0
                        self.wmorde += 1
                        if(self.wmorde > 1 and self.krecik.level < self.krecik.difficulty and self.wmorde % 5 == 0):
                            self.krecik.level += 1
                    else:
                        self.click_snd.play()
                elif(event.type == pygame.MOUSEBUTTONUP):
                    self.mlotek.uncymbal()
            if(self.time.odliczanko >0):
                self.time.czas()
            else:
                self.jazda = False
                break
            self.tekst.licznik(self.screen, self.time.odliczanko, self.jazda)
            self.krecik.czekanko()
            self.mlotek.update()
            self.tekst.punkty(self.screen, self.wmorde)
            self.hit.check(self.screen)
            if (self.krecik.ucieczka > self.krecik.speed[self.krecik.level]):
                self.krecik.uciekej1()
                self.krecik.ucieczka = 0
                continue
            self.allsprites.draw(self.screen)
            self.clock.tick(120)
            pygame.display.flip()
        self.krecik.level = self.krecik.level_back
        self.level1_music.stop()
        
    def wam_ll2(self):
        self.level2_music.play()
        self.krecik.level_back = self.krecik.level
        self.jazda = True
        self.krecik.uciekej2()
        while self.jazda:
            self.screen.blit(self.background2, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.jazda = False
                elif (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.jazda = False
                elif(event.type == pygame.MOUSEBUTTONDOWN):
                    if(self.mlotek.cymbal(self.krecik)):
                        self.click_snd.play()
                        self.wmorde_snd.play()
                        self.hit.show = 0
                        self.krecik.uciekej2()
                        self.krecik.ucieczka = 0
                        self.wmorde += 1
                        if(self.wmorde > 1 and self.krecik.level < self.krecik.difficulty and self.wmorde % 5 == 0):
                            self.krecik.level += 1
                    else:
                        self.click_snd.play()
                elif(event.type == pygame.MOUSEBUTTONUP):
                    self.mlotek.uncymbal()
            if(self.time.odliczanko >0):
                self.time.czas()
            else:
                self.jazda = False
                break
            self.tekst.licznik(self.screen, self.time.odliczanko, self.jazda)
            self.krecik.czekanko()
            self.mlotek.update()
            self.tekst.punkty(self.screen, self.wmorde)
            self.hit.check(self.screen)
            if (self.krecik.ucieczka > self.krecik.speed[self.krecik.level]):
                self.krecik.uciekej2()
                self.krecik.ucieczka = 0
                continue
            self.allsprites.draw(self.screen)
            self.clock.tick(120)
            pygame.display.flip()
        self.krecik.level = self.krecik.level_back
        self.level2_music.stop()
    def scorescreen(self):
        self.results_music.play(-1)
        self.jazda_scorescreen = True
        self.jechanka = 0
        while self.jazda_scorescreen:
            if(self.jechanka > 0):
                if(self.jechanka > 180):
                    self.wmorde = 0
                    self.time.odliczanko = 37
                    self.jazda_scorescreen = False
                else:
                    self.jechanka += 1
            self.screen.fill(self.black)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.graj = False
                    self.jazda_scorescreen = False
                elif (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.graj = False
                    self.jazda_scorescreen = False
                elif(event.type == pygame.MOUSEBUTTONDOWN):
                    if(self.mlotek.cymbal_button(self.again_ss)):
                        self.click_snd.play()
                        #self.wmorde_snd.play()
                        self.jechanka = 1
                        
                    if(self.mlotek.cymbal_button(self.exit_ss)):
                        self.click_snd.play()
                        #self.wmorde_snd.play()
                        self.graj = False
                        self.jazda_scorescreen = False
                      
                    else:
                        self.click_snd.play()
                elif(event.type == pygame.MOUSEBUTTONUP):
                    self.mlotek.uncymbal()
            self.mlotek.update()
            self.tekst.punkty_ss(self.screen, self.wmorde)
            self.ss_sprites.draw(self.screen)
            self.clock.tick(120)
            pygame.display.flip()
        self.results_music.stop()
            
class Tekst():
    def __init__(self):
        self.font = pygame.font.Font(os.path.join('data', 'HelveticaNeue-Heavy.otf'), 40)
        self.title_font = pygame.font.Font(os.path.join('data', 'INVASION2000.TTF'), 110)
        self.ss_font = pygame.font.Font(os.path.join('data', 'INVASION2000.TTF'), 90)
    def punkty(self, screen, wmorde):
        self.pts = self.font.render("Score: " + str(wmorde), True, (0, 0, 0))
        screen.blit(self.pts, (705, 30))
    def punkty_ss(self, screen, wmorde):
        self.pts_ss = self.ss_font.render("YOUR SCORE: " + str(wmorde), True, (255, 255, 255))
        screen.blit(self.pts_ss,(60, 200))
    def licznik(self, screen, odliczanko, jazda):
        if(odliczanko >= 1):
            if(odliczanko > 10):
                kolorek = (0, 0, 0)
            elif(odliczanko > 3):
                kolorek = (255, 239, 0)
            else:
                kolorek = (255, 0, 0)
            self.timeleft = self.font.render("Time left: ", True, (0, 0, 0))
            self.zegar = self.font.render(str(odliczanko), True, kolorek)
            screen.blit(self.timeleft, (45, 30))
            screen.blit(self.zegar, (247, 30))
    def title(self, screen):
        self.nazwa = self.title_font.render("whack-a-mole", True, (0, 0, 0))
        screen.blit(self.nazwa,(60, 60))
    def choose_level(self, screen):
        self.choose = self.font.render("Choose level:", True, (255, 255, 255))
        self.diff = self.font.render("Choose difficulty:", True, (255, 255, 255))
        screen.blit(self.choose, (330, 30))
        screen.blit(self.diff, (290, 350))
        
class Time():
    def __init__(self):
        self.odliczanko = 37
        self.klateczki = 1
        self.font = pygame.font.Font(os.path.join('data', 'HelveticaNeue-Heavy.otf'), 40)        
    def czas(self):
        self.klateczki += 1
        if(self.klateczki % 120 == 0):
            self.odliczanko -= 1
        
def main():
    gierka = Gierka()
    gierka.menu()
    while gierka.graj:
        gierka.level()
        if gierka.graj:
            if (gierka.level_choice == 1):
                gierka.wam_ll1()
                gierka.scorescreen()
            else:
                gierka.wam_ll2()
                gierka.scorescreen()
    pygame.quit()
    
if __name__ == '__main__':
    main()
