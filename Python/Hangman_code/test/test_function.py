#!/usr/bin/python
# -*- coding: utf-8 -*-


import unittest
from main import *

lista_zapisanych_graczy = {}
aktualny_gracz = 0


class MakeResultTestCase(unittest.TestCase):
    def test_make_result(self):
        result = make_result(1, 5, 3)
        self.assertEqual(result, 50)
    def test_choose_level(self):
        dostepne_poziomy = {1: "Łatwy poziom trudności", 2: "Średni poziom trudnośći", 3: "Wysoki poziom trudności"}
        result = choose_level(dostepne_poziomy)
        self.assertEqual(result, 1)
    def test_choose_category(self):
        dostepne_kategorie = {1: "Zwierzeta", 2: "Rzeczy", 3: "Owoce i Warzywa", 4: "Panstwa"}
        result = choose_category(dostepne_kategorie)
        self.assertEqual(result, 1)
    def test_save_result(self):
        aktualny_gracz = 1
        lista_zapisanych_graczy = {'1': ['kamil', 'maj', 4]}
        to_test(aktualny_gracz, lista_zapisanych_graczy)
        save_result(50)
        self.assertEqual(lista_zapisanych_graczy, {'1': ['kamil', 'maj', 54]})




if __name__ == '__main__':
    unittest.main()
