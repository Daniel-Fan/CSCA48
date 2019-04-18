# beta-2
'''
DISCLAIMER:
Passing this test suite does NOT imply that your code will fully pass the auto marker.
However, if your code fails any of the test cases, chances are there is a bug in your code.
'''


import unittest
import itertools
from formula_game_functions import *
from random import randint


NOT, AND, OR = '-', '*', '+'
OPS = {0: NOT, 1: AND, 2: OR}
VARS = {0: 'x', 1: 'y', 2: 'z'}


# Retrieved from https://piazza.com/class/ixgonr8vwig5f5?cid=854
def generate_formula(layers, var='x'):
    """(int[, str]) -> str

    Builds and returns a random formula of with a given number of layers,
    such that a formula with a layer of zero is simply the variable itself.

    NOTE: formulas with layers > 6 will get VERY LARGE!

    REQ: layers >= 0
    REQ: var == var.lower() and len(var) == 1
    """
    # Base case: 0th layer is simply the var itself (leaf).
    if layers == 0:
        formula = var
    # Recursive decomposition: n-1 approach.
    else:
        # Get a random operator.
        operator = OPS[randint(0, 2)]
        # Case 1: create an unary layer.
        if operator == NOT:
            formula = generate_formula(layers - 1, var)
            # Check if sub-formula is already negated.
            if formula[0] != NOT:
                formula = NOT + formula
        # Case 2: create a binary layer.
        else:
            # Recursively generate sub-formulas.
            sub_formula = generate_formula(layers - 1, var)
            # Generate another random variable.
            other_var = VARS[randint(0, 2)]
            other_formula = generate_formula(randint(0, layers), other_var)
            # Swap sub-formulas for random balance.
            if randint(0, 1) == 0:
                sub_formula, other_formula = other_formula, sub_formula
            # Concatenate the binary formula.
            formula = '(' + sub_formula + operator + other_formula + ')'
    # Return formula at current recursive call.
    return formula


def evaluate_formula(formula, variables, values):
    for i in range(len(variables)):
        formula = formula.replace(variables[i], "True" if values[i] == "1" else "False")
    formula = formula.replace("-", " not ").replace("*", " and ").replace("+", " or ")
    result = eval(formula)
    return 1 if result else 0


class TestA2(unittest.TestCase):
    def test_not_valid_00(self):
        formula = "x+(-y)"
        actual = build_tree(formula)
        expected = None
        self.assertEqual(actual, expected)

    def test_not_valid_01(self):
        formula = "(((x+y)*(x-y) + ((a-b)*(a+b)))"
        actual = build_tree(formula)
        expected = None
        self.assertEqual(actual, expected)

    def test_not_valid_02(self):
        formula = "(((x+y)*(x-y)+((a-b)*(a+b)))"
        actual = build_tree(formula)
        expected = None
        self.assertEqual(actual, expected)

    def test_not_valid_03(self):
        formula = "(u*v*w*z)"
        actual = build_tree(formula)
        expected = None
        self.assertEqual(actual, expected)

    def test_not_valid_04(self):
        formula = "-((x+y))"
        actual = build_tree(formula)
        expected = None
        self.assertEqual(actual, expected)

    def test_not_valid_05(self):
        formula = "((x+y*z+d*e) * (z+e*y))"
        actual = build_tree(formula)
        expected = None
        self.assertEqual(actual, expected)

    def test_not_valid_06(self):
        formula = "((-x+y)*-(-y+X))"
        actual = build_tree(formula)
        expected = None
        self.assertEqual(actual, expected)

    def test_not_valid_07(self):
        formula = "((A*B)+E+D+F)"
        actual = build_tree(formula)
        expected = None
        self.assertEqual(actual, expected)

    def test_not_valid_08(self):
        formula = "(x+(y)*z)"
        actual = build_tree(formula)
        expected = None
        self.assertEqual(actual, expected)

    def test_not_valid_09(self):
        formula = "(x+(y+a)*z)"
        actual = build_tree(formula)
        expected = None
        self.assertEqual(actual, expected)

    def test_not_valid_10(self):
        formula = "(((((x+y)"
        actual = build_tree(formula)
        expected = None
        self.assertEqual(actual, expected)

    def test_not_valid_11(self):
        formula = "(xyz+*)"
        actual = build_tree(formula)
        expected = None
        self.assertEqual(actual, expected)

    def test_not_valid_12(self):
        formula = "(+x*+-z)"
        actual = build_tree(formula)
        expected = None
        self.assertEqual(actual, expected)

    def test_not_valid_13(self):
        formula = "()(((((((a"
        actual = build_tree(formula)
        expected = None
        self.assertEqual(actual, expected)

    def test_not_valid_14(self):
        formula = "-(-x*-y)*-(x+y)"
        actual = build_tree(formula)
        expected = None
        self.assertEqual(actual, expected)

    def test_not_valid_15(self):
        formula = "(-y)"
        actual = build_tree(formula)
        expected = None
        self.assertEqual(actual, expected)

    def test_not_valid_16(self):
        formula = "(x*y+z*x)"
        actual = build_tree(formula)
        expected = None
        self.assertEqual(actual, expected)

    def test_not_valid_17(self):
        formula = "(((x+y)*(x-y))+((a-b)*(a+b)))"
        actual = build_tree(formula)
        expected = None
        self.assertEqual(actual, expected)

    def test_is_valid_random_00(self):
        for i in range(10):
            formula = generate_formula(1)
            actual = build_tree(formula)
            expected = actual != None
            self.assertTrue(expected, formula + " should be valid")

    def test_is_valid_random_01(self):
        for i in range(10):
            formula = generate_formula(2)
            actual = build_tree(formula)
            expected = actual != None
            self.assertTrue(expected, formula + " should be valid")

    def test_is_valid_random_02(self):
        for i in range(10):
            formula = generate_formula(3)
            actual = build_tree(formula)
            expected = actual != None
            self.assertTrue(expected, formula + " should be valid")

    def test_is_valid_random_03(self):
        for i in range(10):
            formula = generate_formula(4)
            actual = build_tree(formula)
            expected = actual != None
            self.assertTrue(expected, formula + " should be valid")

    def test_is_valid_random_04(self):
        for i in range(10):
            formula = generate_formula(5)
            actual = build_tree(formula)
            expected = actual != None
            self.assertTrue(expected, formula + " should be valid")

    def test_is_valid_random_05(self):
        for i in range(10):
            formula = generate_formula(6)
            actual = build_tree(formula)
            expected = actual != None
            self.assertTrue(expected, formula + " should be valid")


            
if __name__ == "__main__":
    unittest.main(exit=False)
