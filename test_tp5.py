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

# def test_comprobation(word, exp):
#     assert funciones.word_lenght(word)==exp

#3
# @pytest.mark.parametrize("info, pos, dni, exp, exp2",[
#     ("Mercedes Tetilla", 0, "12345678", "Mercedes", "123"),
#     ("Scott McCall", 0, "8765432", "Scott", "876"),
#     ("Stiles Stilinski", 0, "4758234", "Stiles", "475"),
#     ("Lydia Martin", 0, "09384934", "Lydia", "093"),
# ])

# def test_comprobation(info, pos, dni, exp, exp2):
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

# def test_comprobation(min, max, exp):
#     assert funciones.temperature(min, max)==exp

#6
# @pytest.mark.parametrize("phrase, exp",[
#     ("Teen Wolf", "T e e n   W o l f "),
#     ("Miraculous", "M i r a c u l o u s "),
#     ("Cat noir", "C a t   n o i r "),
#     ("Void", "V o i d "),
# ])

# def test_comprobation(phrase, exp):
#     assert funciones.spaces(phrase)==exp

#7
# @pytest.mark.parametrize("nums, min, max",[
#     ([1,2,3,4,5], 1, 5),
#     ([10,9,3,4,5], 3, 10),
#     ([34, 54,2,123,5,1], 1, 123),
#     ([4,3,2,1], 1, 4),
# ])

# def test_comprobation(nums, max, min):
#     assert funciones.min_max(nums)==(min,max)

#8
# @pytest.mark.parametrize("radio, area, peri",[
#     (9, 799, 56),
#     (122, 146899, 766),
#     (3, 88, 18),
#     (4, 157, 25),
# ])

# def test_comprobation(radio, area, peri):
#     assert funciones.area_per_circle(radio)==(area, peri)

#9
# @pytest.mark.parametrize("user, password, exp",[
#     ("usuario1", "asdasd", True),
#     ("usuario1", "pepe", False),
#     ("pepe", "asdasd", False),
#     ("pepe", "void", False),
# ])

# def test_comprobation(user, password, exp):
#     assert funciones.login(user, password, 0)== exp

#10!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#11
@pytest.mark.parametrize("num, list1, ans, ans2", [
    (2, [1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [2, 4, 6, 8, 10]),
])
def test_comprobation(num, list1, ans, ans2):
    resultado = funciones.list_func(list1, funciones.multi(num))
    assert resultado == ans
