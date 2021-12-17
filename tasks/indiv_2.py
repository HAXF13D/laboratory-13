#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Олимпиадная задача

Задача: Кенни учится в Начальной школе
Саус-парка в четвёртом классе под руководством мистера Гаррисона.
У Кенни есть старший брат по имени Кевин.
Друзьями Кенни являются Стэн и Кайл,
он называл их «лучшими друзьями, которых можно представить»
и также он поддерживает дружбу с Эриком Картманом,
правда, исключительно из жалости.
Во время празднования дня рождения Эрика Картмана
(На который Кенни кстати не хотел идти)
на них напала банда террористов,
ваша задача, по заданным параметрам окружающей среды,
а также по наличию оружия у друзей Кенни сказать
умрёт ли Кенни.
Входные данные:

Строка, содержащая в себе полное описание месности

Выходные данные:

Ответ на задачу: "YES" или "NO"

"""


def individual_func_2(**kwargs):
    print("YES")


if __name__ == "__main__":
    print(individual_func_2(amount_of_weapons={"Gunner": 1, "Killer": 2}))
    print(individual_func_2(season="winter"))
    print(individual_func_2(home="building", weather="rain"))
