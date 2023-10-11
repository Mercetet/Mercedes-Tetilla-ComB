import pytest
import funciones

#TP5
#1
# @pytest.mark.parametrize("dni, exp",[
#     ("1234567", True),
#     ("123", False),
#     ("432", False),
#     ("46547529", True),
# ])

# def test_comprobation(dni, exp):
#     assert funciones.comprobation(dni)==exp

#2
# @pytest.mark.parametrize("word, exp",[
#     ("Mercedes Tetilla", 7),
#     ("Hola mundo", 5),
#     ("Harry Potter", 6),
#     ("Chau", 4),
# ])

# def test_word_lenght(word, exp):
#     assert funciones.word_lenght(word)==exp

#3
# @pytest.mark.parametrize("info, pos, dni, exp, exp2",[
#     ("Mercedes Tetilla", 0, "12345678", "Mercedes", "123"),
#     ("Scott McCall", 0, "8765432", "Scott", "876"),
#     ("Stiles Stilinski", 0, "4758234", "Stiles", "475"),
#     ("Lydia Martin", 0, "09384934", "Lydia", "093"),
# ])

# def test_wordselector(info, pos, dni, exp, exp2):
#     assert funciones.wordselector(info, pos)==exp
#     assert funciones.three_first_dni(dni)==exp2

#4 NO TIENE RETURN, NO SE COMO PONER EL EXP

#5
# @pytest.mark.parametrize("min, max, exp",[
#     (3, 6, 4.5),
#     (6, 10, 8),
#     (8, 32, 20),
#     (-13, 0, -6.5),
# ])

# def test_temperature(min, max, exp):
#     assert funciones.temperature(min, max)==exp

#6
# @pytest.mark.parametrize("phrase, exp",[
#     ("Teen Wolf", "T e e n   W o l f "),
#     ("Miraculous", "M i r a c u l o u s "),
#     ("Cat noir", "C a t   n o i r "),
#     ("Void", "V o i d "),
# ])

# def test_spaces(phrase, exp):
#     assert funciones.spaces(phrase)==exp

#7
# @pytest.mark.parametrize("nums, min, max",[
#     ([1,2,3,4,5], 1, 5),
#     ([10,9,3,4,5], 3, 10),
#     ([34, 54,2,123,5,1], 1, 123),
#     ([4,3,2,1], 1, 4),
# ])

# def test_min_max(nums, max, min):
#     assert funciones.min_max(nums)==(min,max)

#8
# @pytest.mark.parametrize("radio, area, peri",[
#     (9, 799, 56),
#     (122, 146899, 766),
#     (3, 88, 18),
#     (4, 157, 25),
# ])

# def test_area_per_circle(radio, area, peri):
#     assert funciones.area_per_circle(radio)==(area, peri)

#9
# @pytest.mark.parametrize("user, password, exp",[
#     ("usuario1", "asdasd", True),
#     ("usuario1", "pepe", False),
#     ("pepe", "asdasd", False),
#     ("pepe", "void", False),
# ])

# def test_login(user, password, exp):
#     assert funciones.login(user, password, 0)== exp

#10!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#11
# @pytest.mark.parametrize("list1, fc, ans", [
#     ([1, 2, 3, 4, 5], funciones.multi, [2, 4, 6, 8, 10]),
#     ([10, 20, 30, 40, 50], funciones.multi, [20, 40, 60, 80, 100]),
#     ([14, 5, 11, 23, 12], funciones.multi, [28, 10, 22, 46, 24]),
#     ([64, 93, 24], funciones.multi, [128, 186, 48]),
# ])

# def test_list_func(list1, fc, ans):
#     assert funciones.list_func(list1, fc) == ans

#12
# @pytest.mark.parametrize("phrase, exp",[
#     ("Hola mundo", ({"Hola": 4, "mundo": 5})),
#     ("Chau", ({"Chau": 4})),
#     ("Me llamo mercedes", ({"Me": 2, "llamo": 5, "mercedes":8})),
#     ("La materia es programacion", ({"La": 2, "materia": 7, "es": 2, "programacion":12})),
# ])

# def test_long_phrase(phrase, exp):
#     assert funciones.long_phrase(phrase)== exp

#13
# @pytest.mark.parametrize("A, B, H",[
#     (9, 3, 9),
#     (122, 12, 122),
#     (3, 88, 88),
#     (4, 157, 157),
# ])

# def test_hypo(A, B, H):
#     assert funciones.hypo(A,B)==H

#14
# @pytest.mark.parametrize("num, exp",[
#     (9, False),
#     (122, False),
#     (3, True),
#     (2, True),
# ])

# def test_prime(num, exp):
#     assert funciones.prime(num)== exp

#15
# @pytest.mark.parametrize("num, exp",[
#     (5, 120),
#     (9, 362880),
#     (3, 6),
#     (2, 2),
# ])

# def test_factorial(num, exp):
#     assert funciones.factorial(num)== exp

#16
# @pytest.mark.parametrize("num, dig, exp",[
#     (98984, 9, 2),
#     (111111, 1, 6),
#     (21345, 4, 1),
#     (352423, 2, 2),
# ])

# def test_serch_dig(num, dig, exp):
#     assert funciones.serch_dig(num, dig) == exp

#17
@pytest.mark.parametrize("num, exp",[
    (98, 17),
    (111111, 6),
    (21345, 15),
    (35, 8),
])

def test_sum_dig(num, exp):
    assert funciones.sum_dig(num) == exp