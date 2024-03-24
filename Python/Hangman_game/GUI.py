#!/usr/bin/python
# -*- coding: utf-8 -*-


import pygame, sys
from copy import deepcopy
from main import make_result


pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Wisielec")
FPS_menu = 30



class Object:
    def __init__(self, x_cord, y_cord, file_name):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.button_immage = pygame.image.load(f"{file_name[:-4]}.png")

    def draw_object(self, window):
        window.blit(self.button_immage, (self.x_cord, self.y_cord))

class ObjectX:
    def __init__(self, file_name):
        self.button_immage = pygame.image.load(f"{file_name[:-4]}.png")

    def draw_object(self, window, x_cord, y_cord ):
        window.blit(self.button_immage, [x_cord, y_cord])

class Button:
    def __init__(self, x_cord, y_cord, file_name):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.button_immage = pygame.image.load(f"{file_name[:-4]}.png")
        self.hovered_button_immage = pygame.image.load(f"{file_name[:-4]}_hovered.png")
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.button_immage.get_width(), self.button_immage.get_height())

    def tick(self):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                return True
    def draw(self, window):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            window.blit(self.hovered_button_immage, (self.x_cord, self.y_cord))
        else:
            window.blit(self.button_immage, (self.x_cord, self.y_cord))


class ButtonWrite:
    def __init__(self, x_cord, y_cord, name):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.button_write = name
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, 200, 35)

    def tick(self):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                return True
class ButtonGuess:
    def __init__(self, x_cord, y_cord):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, 40, 40)

    def tick(self):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                return True

class Blank:
    def __init__(self, file_name_menu):
        self.x = 0
        self.y = 0
        self.file_name_menu = pygame.image.load(f"{file_name_menu[:-4]}.png")

    def draw_menu(self, window):
        window.blit(self.file_name_menu, (self.x, self.y))




def start_gui() -> int:
    pygame.time.delay(100)
    pygame.display.update()
    tlo_1 = Blank('zdjecia_interfejs/menu.png')
    rozpocznij_gre_button = Button(275, 250, "zdjecia_interfejs/przycisk_rozpocznij.png")
    zobacz_ranking_buton = Button(275, 250 + 75, "zdjecia_interfejs/przycisk_ranking.png")
    wyjdz_buton = Button(275, 250 + 75+75, "zdjecia_interfejs/wyjdz.png")

    while True:
        pygame.time.Clock().tick(FPS_menu)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        tlo_1.draw_menu(window)
        rozpocznij_gre_button.draw(window)
        zobacz_ranking_buton.draw(window)
        wyjdz_buton.draw(window)
        if rozpocznij_gre_button.tick() == 1:
            return 1
        elif zobacz_ranking_buton.tick() == 1:
            return 2
        elif wyjdz_buton.tick() == 1:
            return 3

        pygame.display.update()


def account():
    pygame.time.delay(100)
    pygame.display.update()
    tlo_2 = Blank('zdjecia_interfejs/masz_konto.png')
    tak_button = Button(275, 250, "zdjecia_interfejs/tak.png")
    nie_buton = Button(275, 250 + 75, "zdjecia_interfejs/nie.png")
    while True:
        pygame.time.Clock().tick(FPS_menu)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        tlo_2.draw_menu(window)
        tak_button.draw(window)
        nie_buton.draw(window)
        if tak_button.tick():
            return 2
        elif nie_buton.tick():
            return 1


        pygame.display.update()


def ranking(lista_zapisanych_graczy) -> int:
    pygame.time.delay(100)
    pygame.display.update()
    tlo = Blank('zdjecia_interfejs/Ranking.png')
    wyjdz_ranking_button = Button(520, 520, "zdjecia_interfejs/wyjdz.png")
    font = pygame.font.SysFont("Comic Sans MS", 24)

    while True:
        miejsce = 1
        max_key = ""
        y_pos = 125
        pygame.time.Clock().tick(FPS_menu)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        tlo.draw_menu(window)
        wyjdz_ranking_button.draw(window)

        lista_zapisanych_graczy_pomocnicza = deepcopy(lista_zapisanych_graczy)

        while lista_zapisanych_graczy_pomocnicza != {}:
            aktualny_wartosc = 0
            for key in lista_zapisanych_graczy_pomocnicza.keys():
                if lista_zapisanych_graczy_pomocnicza[key][2] > aktualny_wartosc:
                    aktualny_wartosc = lista_zapisanych_graczy_pomocnicza[key][2]
                    max_key = key
            text = font.render('{0:4d}. {1:40s}'.format(miejsce, lista_zapisanych_graczy[str(max_key)][0] +" "+ lista_zapisanych_graczy[str(max_key)][1]), False, [128, 64, 255])
            wynik = font.render('{0:>5}'.format(aktualny_wartosc), False, [128, 64, 255])
            miejsce += 1
            window.blit(text, [215, y_pos])
            window.blit(wynik, [500, y_pos])
            del lista_zapisanych_graczy_pomocnicza[str(max_key)]
            y_pos += 29

        wyjdz_ranking_button.draw(window)

        if wyjdz_ranking_button.tick():
            return 1
        pygame.display.update()



def creat_account_gui() -> list:
    pygame.time.delay(100)
    pygame.display.update()
    tlo_tworzenie_konta = Blank('zdjecia_interfejs/tworzenie_konta.png')
    dalej_button = Button(520, 520, "zdjecia_interfejs/dalej.png")
    base_font = pygame.font.Font(None, 50)
    font = pygame.font.Font(None, 32)
    user_text = ''
    input_rect = pygame.Rect(220,320,140,50)
    color = pygame.Color('grey')
    tlo_tworzenie_konta.draw_menu(window)
    dalej_button.draw(window)
    pygame.display.flip()



    while True:
        pygame.time.Clock().tick(FPS_menu)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER:
                    return user_text

        tlo_tworzenie_konta.draw_menu(window)
        pygame.draw.rect(window, color, input_rect, 2)
        text = base_font.render(user_text, True, [0, 0, 0])
        window.blit(text, (input_rect.x+5, input_rect.y +10))
        input_rect.w = max(350,text.get_width()+10)
        window.blit(font.render("Imię i Nazwisko: ", True, [0, 0, 0]) ,(input_rect.x - 190, input_rect.y +15))
        dalej_button.draw(window)
        pygame.display.flip()

        if dalej_button.tick():
            return user_text


def choose_own_profil_gui() -> int:
    pygame.time.delay(100)
    tlo = Blank('zdjecia_interfejs/wybierz.png')

    tlo.draw_menu(window)



    font = pygame.font.Font(None, 40)

    while True:
        button = {}
        save_dict = {}
        pygame.time.Clock().tick(FPS_menu)
        nie_ma_konta_button = Button(500, 500,'zdjecia_interfejs/nie_ma_konta.png')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        with open("Zapis i Odczyt") as file:
            for line in file:
                if ":" in line:
                    save = line.split(" ")
                    save_dict[int(save[0][0])] = save[1] + " " + save[2]
        d = 135
        for key, value in save_dict.items():
            text = font.render( '{key}: {value}'.format(key= key, value = value), True, [16, 71, 8])
            window.blit(text, [300,  d])
            button[key] = ButtonWrite(300,  d, value)
            d += 40
        nie_ma_konta_button.draw(window)
        pygame.display.update()

        for key in button.keys():
            if button[key].tick():
                pygame.display.update()
                return key
            elif nie_ma_konta_button.tick():
                return 0

        tlo.draw_menu(window)




def choose_level_gui() -> int:
    pygame.time.delay(100)
    tlo = Blank('zdjecia_interfejs/poziom_trudnosci.png')
    x = 154
    latwy_button = Button(275, x, "zdjecia_interfejs/przycisk_latwy.png")
    sredni_buton = Button(275, x + 75, "zdjecia_interfejs/przycisk_sredni.png")
    trudny_buton = Button(275, x + 75 + 75, "zdjecia_interfejs/przycisk_trudny.png")
    losowy_buton = Button(275, x + 75 + 75 + 75, "zdjecia_interfejs/przycisk_losowo.png")
    tlo.draw_menu(window)
    pygame.display.update()


    while True:
        pygame.time.Clock().tick(FPS_menu)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        tlo.draw_menu(window)
        latwy_button.draw(window)
        sredni_buton.draw(window)
        trudny_buton.draw(window)
        losowy_buton.draw(window)
        pygame.display.update()
        if latwy_button.tick():
            return 1
        elif sredni_buton.tick():
            return 2
        elif trudny_buton.tick():
            return 3
        elif losowy_buton.tick():
            return 4

        pygame.display.update()

def choose_category_gui() -> int:
    pygame.time.delay(100)
    tlo = Blank('zdjecia_interfejs/kategoria.png')
    x = 150
    zwierzeta_button = Button(275, x, "zdjecia_interfejs/przycisk_zwierzeta.png")
    rzeczy_buton = Button(275, x + 75, "zdjecia_interfejs/przycisk_rzeczy.png")
    owoce_buton = Button(275, x + 75 + 75, "zdjecia_interfejs/przycisk_owoce.png")
    panstwa_buton = Button(275, x + 75 + 75 + 75, "zdjecia_interfejs/przycisk_panstwa.png")
    losowy_buton = Button(275, x + 75 + 75 + 75 + 75, "zdjecia_interfejs/przycisk_losowo.png")
    tlo.draw_menu(window)
    pygame.display.update()


    while True:
        pygame.time.Clock().tick(FPS_menu)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        tlo.draw_menu(window)
        zwierzeta_button.draw(window)
        rzeczy_buton.draw(window)
        owoce_buton.draw(window)
        panstwa_buton.draw(window)
        losowy_buton.draw(window)

        if zwierzeta_button.tick():
            return 1
        elif rzeczy_buton.tick():
            return 2
        elif owoce_buton.tick():
            return 3
        elif panstwa_buton.tick():
            return 4
        elif losowy_buton.tick():
            return 5
        pygame.display.update()


def zasady_gry() -> int:
    pygame.time.delay(100)
    tlo = Blank('zdjecia_interfejs/tlo.png')
    rozpocznij_gre_button = Button(275, 400, "zdjecia_interfejs/przycisk_rozpocznij.png")
    tlo.draw_menu(window)
    pygame.display.update()


    while True:
        pygame.time.Clock().tick(FPS_menu)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        y = 70
        tlo.draw_menu(window)
        rozpocznij_gre_button.draw(window)
        font = pygame.font.Font(None, 50)
        text = 'Masz 6 żyć i nieograniczony czas, a'
        goto_text = font.render(text, True, [131,73, 29])
        window.blit(goto_text, [110,y])
        text = 'wraz z błędną odpowiedzią tracisz jedno'
        goto_text = font.render(text, True, [131,73, 29])
        window.blit(goto_text, [55, y+50])
        text = 'Status życia reprezentuje ilość'
        goto_text = font.render(text, True, [131,73, 29])
        window.blit(goto_text, [132, y+100])
        text = 'elementów ciała bohatera na szubienicy'
        goto_text = font.render(text, True, [131,73, 29])
        window.blit(goto_text, [55, y+150])
        text = 'Ilość kresek na ekranie gry'
        goto_text = font.render(text, True, [131,73, 29])
        window.blit(goto_text, [178, y+200])
        text = 'oznacza liczbę liter w haśle'
        goto_text = font.render(text, True, [131,73, 29])
        window.blit(goto_text, [165, y+250])
        if rozpocznij_gre_button.tick():
            return 1



        pygame.display.update()


def zgadywanie_gui(password, gracz, *args):
    tak_button = Button(20, 530, 'zdjecia_interfejs/tak.png')
    nie_button = Button(360,530, 'zdjecia_interfejs/nie.png')
    font = pygame.font.Font(None, 50)
    font_game = pygame.font.Font(None, 30)
    font_result = pygame.font.Font(None, 90)
    l_zyc = 6
    text = ""
    dlugosc_slowa_na_poczatku = len(password)
    password = password.lower()
    wynik = []
    slowo = {}
    zgadywane = []
    d_slowa = len(password)
    dict_przekreslnia = {}
    przekrelsnie = ObjectX('zdjecia_interfejs/przekreslenie.png')
    pygame.time.delay(100)
    tlo={ 6: Blank('zdjecia_interfejs/pocz_gry.png'),5: Blank('zdjecia_interfejs/1_zycie.png'),4: Blank('zdjecia_interfejs/2_zycia.png'),3: Blank('zdjecia_interfejs/3_zycia.png'),
           2: Blank('zdjecia_interfejs/4_zycia.png'),1: Blank('zdjecia_interfejs/5_zyc.png'),0: Blank('zdjecia_interfejs/6_zyc.png')}
    tlo[l_zyc].draw_menu(window)
    l_zyc = 6


    for i in range(0, d_slowa):
        slowo[i] = password[i]
        wynik.extend("_")

    for char in wynik:
        text +=  "  "+char
    goto_text = font.render(text, True, [0, 0, 0])
    window.blit(goto_text, [400, 100])

    text_gamer_1 = 'Gracz: {0}'.format(gracz[0] + " "+ gracz[1])
    text_gamer_2 = 'Poziom: {0}'.format(args[0])
    text_gamer_3 = 'Kategoria: {0}'.format(args[1])
    goto_text_gamer_1 = font_game.render(text_gamer_1, True, [79, 79, 79])
    goto_text_gamer_2 = font_game.render(text_gamer_2, True, [79, 79, 79])
    goto_text_gamer_3 = font_game.render(text_gamer_3, True, [79, 79, 79])
    window.blit(goto_text_gamer_1, [100, 20])
    window.blit(goto_text_gamer_2, [100, 40])
    window.blit(goto_text_gamer_3, [100, 60])



    slownik_liter = {1:"a", 2:"b", 3:"c",4:"d", 5:"e",6:"f", 7:"g", 8:"h",9:"i", 10:"j",
                     11:"k", 12:"l",13:"m", 14:"n", 15:"o",16:"p", 17:"r", 18:"s",
                     19:"t", 20:"u",21:"q", 22:"w", 23:"y", 24: "z"}


    while l_zyc > 0 and d_slowa > 0:
        pygame.time.Clock().tick(FPS_menu)
        traf = 0
        ilosc_trafionych_liter = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        x = 40
        y = 107
        key = 1
        literka={}
        wpisany_znak =""
        for i in range(0,5):
            for j in range(0, 5):
                if i == 4 and j == 3:
                    continue
                literka[key] = ButtonGuess(x,y)
                if literka[key].tick():
                    pygame.time.delay(300)
                    wpisany_znak = slownik_liter[key]
                    if wpisany_znak in zgadywane:
                        continue
                    else:
                        zgadywane.extend(wpisany_znak)
                    for key, value in slowo.items():
                        if value == wpisany_znak:
                            wynik[key] = value
                            traf = 1
                            ilosc_trafionych_liter += 1
                    if traf == 1:
                        d_slowa = d_slowa - ilosc_trafionych_liter
                    else:
                        l_zyc = l_zyc - 1
                    tlo[l_zyc].draw_menu(window)
                    if l_zyc > 0 and d_slowa > 0:
                        window.blit(goto_text_gamer_1, [100, 20])
                        window.blit(goto_text_gamer_2, [100, 40])
                        window.blit(goto_text_gamer_3, [100, 60])
                    pygame.display.update()


                    text = ""
                    goto_text = font.render(text, True, [0, 0, 0])
                    window.blit(goto_text, [400, 100])
                    if l_zyc > 0 :
                        for char in wynik:
                            text += "  " + char
                        goto_text = font.render(text, True, [0, 0, 0])
                        window.blit(goto_text, [400, 100])
                        pygame.display.update()

                    ilosc = len(dict_przekreslnia)
                    dict_przekreslnia[ilosc] = [x, y]


                    for el in dict_przekreslnia.values():
                        przekrelsnie.draw_object(window, el[0] , el[1])
                    pygame.display.update()


                key += 1

                x+=62
            y += 58+i
            x = 40

        pygame.display.update()

    if l_zyc > 0:
        text_result = "!!!WYGRAŁEŚ!!!"
        goto_result = font_result.render(text_result, True, [37, 26, 7])
        window.blit(goto_result, [170, 10])
        pygame.display.update()
    else:
        text_result = "PRZEGRAŁEŚ :( "
        goto_result = font_result.render(text_result, True, [37, 26, 7])
        window.blit(goto_result, [170, 10])
        password_1 = ''
        for el in password:
            password_1 += el + "  "
        goto_wynik = font.render(password_1, True, [0, 0, 0])
        window.blit(goto_wynik, [410, 100])

    pygame.display.update()
    uzyskany_wynik = make_result(l_zyc, d_slowa, dlugosc_slowa_na_poczatku)
    text_uzyskany_wynik = 'Zdobyte punkty: {0}'.format(uzyskany_wynik)
    goto_uzyskany_wynik = font.render(text_uzyskany_wynik, True, [37, 26, 7])
    window.blit(goto_uzyskany_wynik, [50, 450])
    pygame.display.update()


    pyatnie = "Czy chcesz zagrać jeszcze raz?"
    goto_pytanie = font_game.render(pyatnie, True, [0, 0, 0])
    window.blit(goto_pytanie, [160, 500])
    tak_button.draw(window)
    nie_button.draw(window)
    pygame.display.update()

    tak_button.draw(window)
    nie_button.draw(window)
    pygame.display.update()




    while True:
        pygame.time.Clock().tick(FPS_menu)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        if tak_button.tick():
            result = [uzyskany_wynik, 0]
            return result
        elif nie_button.tick():
            result = [uzyskany_wynik, 1]
            return result
        pygame.display.update()











