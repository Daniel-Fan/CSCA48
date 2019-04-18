"""
# Copyright Yuchen Fan, 2016, 2018
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 2, CSCA48, Winter 2018
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file. If not, see <http://www.gnu.org/licenses/>.
"""

# Do not change this import statement, or add any of your own!
from formula_tree import FormulaTree, Leaf, NotTree, AndTree, OrTree

# Do not change any of the class declarations above this comment.

# Add your functions here.


def build_tree(formula):
    '''(str) -> FormulaTree or None
    take a string which represents the formula and return the FormulaTree when
    the formula is valid or None when the formula is invalid
    REQ: formula should be the right combinations of lower case
    latter, '-', '+', '*', '(' and ')'
    >>> build_tree("(x*y+z*x)")

    >>> build_tree('(x*y)')
    AndTree(Leaf('x'), Leaf('y'))
    '''
    # create two list:
    # one is the list which stores the operators
    # the other is the list which stores the lower case letters
    operator = list()
    letter = list()
    # go through the formula and the formula need to be valid
    index = 0
    is_valid = True
    while(index < len(formula) and is_valid is True):
        # the first element in formula[index:] is '(', '-', '+' or '*'
        if(formula[index] in ('(', '+', '-', '*')):
            # put this element into the operator list
            operator.append(formula[index])
        # the first element in formula[index:] is lower case letter
        elif(formula[index].islower() is True):
            # the previous str is also a letter
            if(index > 0 and formula[index - 1].islower() is True):
                is_valid = False
            # the last element in operator list is '-'
            # that means '-' is the parent of the current leaf
            elif(len(operator) > 0 and operator[-1] == '-'):
                # pop the last element in the operator list
                # build a NotTree whose child is the current leaf
                # push this subtree to letter list
                operator.pop()
                letter.append(NotTree(Leaf(formula[index])))
                # there is still symbol '-' exists in operator list
                while(len(operator) > 0 and operator[-1] == '-'):
                    operator.pop()
                    current_formula = letter.pop()
                    letter.append(NotTree(current_formula))
            # the last element in operator is not '-'
            else:
                # push this letter to letter list
                letter.append(Leaf(formula[index]))
        # the first element in formula[index:] is ')'
        elif(formula[index] == ')'):
            # the operator list is empty
            # or the letter list does not have two element
            if(len(operator) <= 1 or len(letter) < 2):
                is_valid = False
            else:
                # pop the last element in the operator list
                symbol = operator.pop()
                # pop two element from letter list
                # the last one is right child
                # and the second last one is left child
                right_child = letter.pop()
                left_child = letter.pop()
                # the symbol is '+'
                if(symbol == '+'):
                    # build a OrTree for this subtree
                    subtree = OrTree(left_child, right_child)
                # the symbol is '+'
                elif(symbol == '*'):
                    # build a AndTree for this subtree
                    subtree = AndTree(left_child, right_child)
                # the other symbol should be a invalid formula
                else:
                    is_valid = False
                if(is_valid is True):
                    # pop the last element in operator, it should be '('
                    # otherwise, it should be invalid
                    previous_symbol = operator.pop()
                    if(previous_symbol != '('):
                        is_valid = False
                    else:
                        # the last element in operator is '-'
                        # pop '-' and it is the parent of the subtree
                        if(len(operator) > 0 and operator[-1] == '-'):
                            operator.pop()
                            # push this subtree to letter list
                            letter.append(NotTree(subtree))
                            while(len(operator) > 0 and operator[-1] == '-'):
                                operator.pop()
                                current_formula = letter.pop()
                                letter.append(NotTree(current_formula))
                        # the last element in operator is not '-'
                        # push subtree to letter list straightly
                        else:
                            letter.append(subtree)
        # there are other symbol in the formula
        else:
            is_valid = False
        # increase the index
        index += 1
    # the is_valid is True, the operator list is empty
    # and there is only one element in the letter list
    # the last element in the letter list is the FormulaTree
    if(is_valid is True and len(operator) == 0 and len(letter) == 1):
        result = letter.pop()
    else:
        result = None
    return result


def draw_formula_tree_helper(root, depth):
    '''(FormulaTree, int) -> str
    the helper function of draw_formula_tree
    return the string which is the tree that is like the description in handout
    there are the spaces acoording to the depth of the node
    '''
    # the root is the Leaf
    if isinstance(root, Leaf):
        result = root.get_symbol() + '\n'
    # the root has the children
    # there is one space between symbol and child
    # there is depth * two spaces for the left child
    # from the beginning of the line
    # the root is NotTree
    elif isinstance(root, NotTree):
        # get the child
        child = root.get_children()[0]
        result = root.get_symbol() + ' '\
            + draw_formula_tree_helper(child, depth + 1)
    # the root is AndTree or OrTree
    else:
        # get the right_child
        right_child = root.get_children()[1]
        # get the left child
        left_child = root.get_children()[0]
        result = root.get_symbol() + ' '\
            + draw_formula_tree_helper(right_child, depth + 1)\
            + depth * '  ' + draw_formula_tree_helper(left_child, depth + 1)
    return result


def draw_formula_tree(root):
    '''(FormulaTree) -> str
    return the string which is the tree that is like the description in handout
    '''
    # the depth of child of root is 1
    depth = 1
    result = draw_formula_tree_helper(root, depth)
    # remove the last \n
    return result[:-1]


def evaluate_helper(root, dict_of_value):
    '''(FormulaTree, dict) -> int
    get the value of the dictionnary and calculate truth value of FormulaTree
    REQ: all the letters in the formulatree should be found as the key of dict
    '''
    # the root is the letter
    # find the truth value in the dict according to the key(letters)
    if isinstance(root, Leaf):
        result = dict_of_value[root.get_symbol()]
    # the root is the operator
    else:
        # the root is '-', the value will be one minus the truth value
        if(root.get_symbol() == '-'):
            result = not evaluate_helper(root.get_children()[0], dict_of_value)
        # the root is '+', the value will be max of two truth values
        elif(root.get_symbol() == '+'):
            result = evaluate_helper(root.get_children()[0], dict_of_value)\
                or evaluate_helper(root.get_children()[1], dict_of_value)
        # the root is '*', the value will be min of two truth values
        elif(root.get_symbol() == '*'):
            result = evaluate_helper(root.get_children()[0], dict_of_value)\
                and evaluate_helper(root.get_children()[1], dict_of_value)
    return result


def evaluate(root, variables, values):
    '''(FormulaTree, str, str) -> int
    get the value of variables from values and calculate the truth value
    of formulatree by the corresponding value, return it
    REQ: all the letters in the fromulatree should be found in the variables
    REQ: the length of the strings of varibles and values should be same
    >>> evaluate(build_tree('(a*-b)'), 'ab', '10')
    1
    >>> evaluate(build_tree('-(a*b)'), 'ab', '11')
    0
    '''
    # create a dictionnary whose keys are variables and values are the values
    index = 0
    dict_of_value = {}
    # go through the whole strings of variables and values
    while(index < len(variables)):
        dict_of_value[variables[index]] = int(values[index])
        index += 1
    # use the helper function to find the truth value
    result = int(evaluate_helper(root, dict_of_value))
    return result


def play2win(root, turns, variables, values):
    '''(FormulaTree, str, str, str) -> int
    When the player whose trun is next will win the game,
    return the best next move
    When there is no chance to win the game or either 1 or 0 can win the game,
    return 1 if it is E's turn, return 0 if it is A's turn
    REQ: turns should be the string of A's and E's
    REQ: variable should be the string of variables in the fromula
    REQ: values should be the string of 0 and 1
    REQ: length of turns should be longer than the length of values
    >>> play2win(build_tree('-(a+b)'), 'AE', 'ab', '0')
    0
    >>> play2win(build_tree('-(a+b)'), 'AE', 'ab', '1')
    1
    >>> play2win(build_tree('-(a*b)'), 'AE', 'ab', '0')
    1
    >>> play2win(build_tree('-(a*b)'), 'AE', 'ab', '1')
    0
    '''
    # correspongd each player and variable
    index = 0
    letter_to_player = {}
    while(index < len(turns)):
        letter_to_player[variables[index]] = turns[index]
        index += 1
    # find the best move
    result = all_possibility(root, variables, values, letter_to_player,
                             turns[len(values):], turns[len(values)], values)
    # there is no way to win or either 1 or 0 can win
    if(result is False):
        if(turns[len(values)] == 'E'):
            result = 1
        elif(turns[len(values)] == 'A'):
            result = 0
    return result


def all_possibility(root, variables, values, letter_to_player,
                    turns, player, original_value):
    '''(FormulaTree, str, str, dict, str, str, str) -> int or bool
    find all the possibility for the value of variables
    return the best move or default value
    '''
    # the value of variable is all assigned
    if(len(variables) == len(values)):
        # evaluate the FormulaTree
        result = evaluate(root, variables, values)
    # all the values have not been assigned
    # do the recursion to add the value repeated
    else:
        # assign the next value by '0'
        value0 = values + '0'
        result0 = all_possibility(root, variables, value0, letter_to_player,
                                  turns[1:], player, original_value)
        # assign the next value by '1'
        value1 = values + '1'
        result1 = all_possibility(root, variables, value1, letter_to_player,
                                  turns[1:], player, original_value)
        # it is the last time to add value
        if(len(value0) == len(variables)):
            # this is the player's turn
            if(turns[0] == player):
                # it is player 'E'
                if(player == 'E'):
                    # one of the result is the default value that would be fine
                    if(result0 == 1 or result1 == 1):
                        result = True
                    # both value cannot get the default value
                    else:
                        result = False
                    # this is the next move what we need to find
                    if(len(original_value) == len(values)):
                        # we can find the best move
                        if(result is True and result0 != result1):
                            if(result0 == 1):
                                result = 0
                            else:
                                result = 1
                        else:
                            result = False
                # it is player 'A'
                elif(player == 'A'):
                    # one of the result is the default value that would be fine
                    if(result0 == 0 or result1 == 0):
                        result = True
                    else:
                        result = False
                    # this is the next move what we need to find
                    if(len(original_value) == len(values)):
                        if(result is True and result0 != result1):
                            if(result0 == 0):
                                result = 0
                            else:
                                result = 1
                        else:
                            result = False
            # it is not the player's turn
            # both results should be default value
            else:
                # it is player 'E'
                if(player == 'E'):
                    if(result0 == 1 and result1 == 1):
                        result = True
                    else:
                        result = False
                # it is player 'A'
                elif(player == 'A'):
                    if(result0 == 0 and result1 == 0):
                        result = True
                    else:
                        result = False
        # the recursion before the last one
        else:
            # this is the player's turn
            if(turns[0] == player):
                result = result0 or result1
            # it is not the player's turn
            else:
                result = result0 and result1
            # it is the first time in this function
            if(len(original_value) == len(values)):
                # we can find the best move
                if(result is True and result0 != result1):
                    if(result0 is True):
                        result = 0
                    else:
                        result = 1
                else:
                    result = False
    return result
