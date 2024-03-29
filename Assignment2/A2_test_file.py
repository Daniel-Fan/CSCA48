from formula_game_functions import *

def bu(formula):
    '''(str) -> Leaf or NotTree or AndTree or OrTree
    abbr. of build_tree, help to spend less time while writing test file,
    I just don't write a lot 'build_tree' header itself
    REQ: same as build_tree
    '''
    return build_tree(formula)
print('______build_tree______')
print('--0--')
print('a suit of test cases provided by code mangler inventor, prof Nick')
print('vailid case')
print(build_tree('x'))
print(build_tree('-y'))
print(build_tree('(x*y)'))
print(build_tree('((-x+y)*-(-y+x))'))
print('invalid case')
print(not build_tree('X'))
print(not build_tree('x*y'))
print(not build_tree('-(x)'))
print(not build_tree('(x+(y)*z)'))
print('a suit of test cases provided by a friendly person on Piazza')
print('all copyrights reserved to all editors at piazza @1219--validity')
print('valid case')
print(build_tree('(x+-y)'))
print(build_tree('(((x*y)*z)*w)'))
print(build_tree('--x'))
print(build_tree('----------------x'))
print(build_tree('(-x*(y+z))'))
print(build_tree('((x+y)*(x+z))'))
print(build_tree('((x+y)*((y+z)*(-y+-z)))'))
print(build_tree('(---x*y)'))
a = '(a+(((((c*v)*(t+u))+-((o+-z)+((p+(r*s))*-q)))'
b = '+(d*e))*((f+-(y+z))+-((x+j)*((k+(l+w))+(m*-n))))))'
print(build_tree(a + b))
print('invalid case')
print(not build_tree('(x+y*z)'))
print(not build_tree('(x*y*z)'))
print(not build_tree('((x+y)*(x-y)*(x+z))'))
print(not build_tree('(x+(u*v*w*z)+y)'))
print(not build_tree('-x-y '))
print(not build_tree('(x+y*x+y)'))
print(not build_tree('x)'))
print(not build_tree('++++x'))
print(not build_tree('-(-a)'))
print(not build_tree('(x+y)*(x+z)'))
print(not build_tree('-(ab)'))
print(not build_tree('(a+(B*-c))'))
print(not build_tree('(x * c)'))
print(not build_tree('-+x'))
print(not build_tree('!a'))
print(not build_tree('(x+x(()'))
print(not build_tree('((x+y))'))
print(not build_tree(')x+y('))
print(not build_tree('(x+y))'))
print(not build_tree('((x*y)'))
print(not build_tree(''))
print(not build_tree(' '))
print(not build_tree('((x+y)*((y&z)*(-y+-z)))'))
print(not build_tree('(a+*)'))
print(not build_tree('(((((x*y)))))'))
print('--1--')
print('some tedious and tricky cases for build_tree')
print('valid')
print(build_tree('-(x+y)'))
print(build_tree('-(-x*-y)'))
print(build_tree('-(-x+y)'))
print(build_tree('-(x*-y)'))
print(build_tree('(x+y)'))
print(build_tree('-(a+(--b*---(-c+-(d*(e+-(f*-g))))))'))
print(build_tree('-(-(-a+(b*-(r+(-e*(z*f)))))+--(c*(d+(y*-(z+(s*-m))))))'))
print(build_tree('(-(-----------x+(y+(-z*q)))*(a*(b+(c*(d+-x)))))'))
print(build_tree('-(-(-----------x+(y+(-z*q)))*(a*(b+(c*(d+-x)))))'))
print(build_tree('-----------------------------------------------a'))
print(build_tree('--------------------------------------------(a+(b*-c))'))
print(build_tree('((a+b)*-c)'))
print(build_tree('(-((-x*y)*z)*-w)'))
print('invalid')
print(not build_tree('(-x)'))
print(not build_tree('@'))
print(not build_tree('+'))
print(not build_tree('1+1'))
print(not build_tree('(1*1)'))
print(not build_tree('(a+1)'))
print(not build_tree('-(a+1)'))
print(not build_tree('-1'))
print(not build_tree('-(-(-a+(b*-(r+(-e*(z*f)))))+--(c*(d)))'))
print(not build_tree('-(-(-a+(b*-(r+(-e*(z*f)))))+--(c*(d+(y*=z))))'))
print(not build_tree('-(-(-a+(b*-(r!(-e*(z*f)))))+--(c*(d+-(y*-z))))'))
print(not build_tree('-(-(-----------x+(y+(-z*q)))*(a*(b+(A*(d+-x)))))'))
print(not build_tree('-(-(-----------x+(y+(-Z*q)))*(a*(b+(r*(d+-x)))))'))
print(not build_tree('-----------------------------------------------A'))
print(not build_tree('--------------------------------------------(a+(b*-C))'))
print(not build_tree('--------------------------------------------(a+(B*-C))'))
print(not build_tree('--------------------------------------------(A+(b*-C))'))
print(not build_tree('(-(-----------x+(y+(-z*q)))&(a*(b+(c*(d+-x)))))'))
print(not build_tree('(-(-----------x+(y+(-z*q)))*(a*(b-(c*(d+-x)))))'))
print(not build_tree('(-(-----------x+(y+(-z*q)))*(a*(b+(+*(d+-x)))))'))
print(not build_tree('(-(-----------x+(y&(-z*q)))*(a*(b+(c*(d+-x)))))'))
print(not build_tree('-(-(-a+(b*-(r+(-e*(z*f)))))+--(c*(d+(y*-(z+(s*-m)))))'))
print(not build_tree('-(-(-a+(b*-(r+(-e*(z*f))())+--(c*(d+(y*-(z+(s*-m))))))'))
print(not build_tree('(-(-a+(b*-(-e*(z*f))))(+--)(c*(d+(y*-(z+(s*-m))))))'))
print(not build_tree('-(-(-a+(b*-(r+(-e*(#*f)))))+--(c*(d+(y*-(z+(s*-m))))))'))
print(not build_tree('-(-(-a+(b*-(r+(-e*(z*f)))))+--(c*(d+(y*-(z+(s*-m)))))'))
print(not build_tree('-(-(-a+(b*-(r+(-e*(z*f)))))+--(c*(d+(y*-(z+(s*-m))()))'))
print(not build_tree('-(-(-a+(b*-(r+(-e*(z*f)))))+--(c*(d+(y*-)z+(s*-m))))))'))
print(not build_tree('((a+a)+(2b))'))
print(not build_tree('(a+b)-c'))
print(not build_tree('((a+b)*(-c))'))
print('______draw_formula_tree______')
print('--2--')
print('draw trees from root valid root given by Nick')
print(draw_formula_tree(build_tree('x')), end = '\n' * 2)
print(draw_formula_tree(build_tree('-y')), end = '\n' * 2)
print(draw_formula_tree(build_tree('(x*y)')), end = '\n' * 2)
print(draw_formula_tree(build_tree('((-x+y)*-(-y+x))')), end = '\n' * 2)
print('--3--')
print('draw trees from root valid root given by editors on piazza')
print(draw_formula_tree(build_tree('(x+-y)')), end = '\n' * 2)
print(draw_formula_tree(build_tree('(((x*y)*z)*w)')), end = '\n' * 2)
print(draw_formula_tree(build_tree('--x')))
print(draw_formula_tree(build_tree('----------------x')), end = '\n' * 2)
print(draw_formula_tree(build_tree('(-x*(y+z))')), end = '\n' * 2)
print(draw_formula_tree(build_tree('((x+y)*(x+z))')), end = '\n' * 2)
a = '((x+y)*((y+z)*(-y+-z)))'
print(draw_formula_tree(build_tree(a)), end = '\n' * 2)
print(draw_formula_tree(build_tree('(---x*y)')), end = '\n' * 2)
a = '(a+(((((c*v)*(t+u))+-((o+-z)+((p+(r*s))*-q)))'
b = '+(d*e))*((f+-(y+z))+-((x+j)*((k+(l+w))+(m*-n))))))'
print(draw_formula_tree(build_tree(a + b)), end = '\n' * 2)
print('tedious cases for drawing trees')
print(draw_formula_tree(build_tree('-(x+y)')), end = '\n' * 2)
print(draw_formula_tree(build_tree('-(-x*-y)')), end = '\n' * 2)
print(draw_formula_tree(build_tree('-(-x+y)')), end = '\n' * 2)
print(draw_formula_tree(build_tree('-(x*-y)')), end = '\n' * 2)
print(draw_formula_tree(build_tree('(x+y)')), end = '\n' * 2)
a = '-(a+(--b*---(-c+-(d*(e+-(f*-g))))))'
b = '-(-(-a+(b*-(r+(-e*(z*f)))))+--(c*(d+(y*-(z+(s*-m))))))'
c = '(-(-----------x+(y+(-z*q)))*(a*(b+(c*(d+-x)))))'
d = '-(-(-----------x+(y+(-z*q)))*(a*(b+(c*(d+-x)))))'
e = '-----------------------------------------------a'
f = '--------------------------------------------(a+(b*-c))'
g = '((a+b)*-c)'
h = '(-((-x*y)*z)*-w)'
print(draw_formula_tree(build_tree(a)), end = '\n' * 2)
print(draw_formula_tree(build_tree(b)), end = '\n' * 2)
print(draw_formula_tree(build_tree(c)), end = '\n' * 2)
print(draw_formula_tree(build_tree(d)), end = '\n' * 2)
print(draw_formula_tree(build_tree(e)), end = '\n' * 2)
print(draw_formula_tree(build_tree(f)), end = '\n' * 2)
print(draw_formula_tree(build_tree(g)), end = '\n' * 2)
print(draw_formula_tree(build_tree(h)), end = '\n' * 2)
print('______evaluation______')
print('--4--')
for i in range(2):
    print(evaluate(bu('a'), 'a', str(i)) ==  i)
    print(evaluate(bu('-a'), 'a', str(i)) == 1 - i)
    print(evaluate(bu('(a+b)'), 'ab', str(i) + str(1 - i)) == 1)
    print(evaluate(bu('(a+b)'), 'ab', str(i) + str(i)) ==  i)
    print(evaluate(bu('(-a+b)'), 'ab', str(i) + str(i)) ==  1)
    print(evaluate(bu('(a+-b)'), 'ab', str(i) + str(i)) ==  1)
    print(evaluate(bu('(-a+-b)'), 'ab', str(i) + str(i)) ==  1 - i)
    print(evaluate(bu('(a*b)'), 'ab', str(i) + str(1 - i)) == 0)
    print(evaluate(bu('(a*b)'), 'ab', str(i) + str(i)) == i)
    print(evaluate(bu('(-a*b)'), 'ab', str(i) + str(i)) == 0)
    print(evaluate(bu('(a*-b)'), 'ab', str(i) + str(i)) == 0)
    print(evaluate(bu('(-a*-b)'), 'ab', str(i) + str(i)) == 1 - i)
    print(evaluate(bu('-(a+b)'), 'ab', str(i) + str(1 - i)) == 0)
    print(evaluate(bu('-(a+b)'), 'ab', str(i) + str(i)) == 1 - i)
    print(evaluate(bu('-(a*b)'), 'ab', str(i) + str(1 - i)) == 1)
    print(evaluate(bu('-(a*b)'), 'ab', str(i) + str(i)) == 1 - i)
print('______play2win______')
print('--5--')
print('basic things')
print(play2win(bu('a'), 'E', 'a', '') == 1)
print(play2win(bu('a'), 'A', 'a', '') == 0)
print(play2win(bu('-a'), 'A', 'a', '') == 1)
print(play2win(bu('-a'), 'E', 'a', '') == 0)
print('logic or')
print(play2win(bu('(a+b)'), 'AA', 'ab', '') == 0)
print(play2win(bu('(a+b)'), 'AA', 'ab', '0') == 0)
print(play2win(bu('(a+b)'), 'EE', 'ab', '') == 1)
print(play2win(bu('(a+b)'), 'EE', 'ab', '1') == 1)
print(play2win(bu('(a+b)'), 'AE', 'ab', '') == 0)
print(play2win(bu('(a+b)'), 'AE', 'ab', '0') == 1)
print(play2win(bu('(a+b)'), 'EA', 'ab', '') == 1)
print(play2win(bu('(a+b)'), 'EA', 'ab', '1') == 0)
print('logic or with negation')
print(play2win(bu('-(a+b)'), 'AA', 'ab', '') == 0)
print(play2win(bu('-(a+b)'), 'AA', 'ab', '0') == 1)
print(play2win(bu('-(a+b)'), 'EE', 'ab', '') == 0)
print(play2win(bu('-(a+b)'), 'EE', 'ab', '0') == 0)
print(play2win(bu('-(a+b)'), 'AE', 'ab', '') == 1)
print(play2win(bu('-(a+b)'), 'AE', 'ab', '1') == 1)
print(play2win(bu('-(a+b)'), 'EA', 'ab', '') == 1)
print(play2win(bu('-(a+b)'), 'EA', 'ab', '1') == 0)
print('logic or with one side negation')
print(play2win(bu('(-a+b)'), 'AA', 'ab', '') == 1)
print(play2win(bu('(-a+b)'), 'AA', 'ab', '1') == 0)
print(play2win(bu('(-a+b)'), 'EE', 'ab', '') == 1)
print(play2win(bu('(-a+b)'), 'EE', 'ab', '1') == 1)
print(play2win(bu('(-a+b)'), 'AE', 'ab', '') == 0)
print(play2win(bu('(-a+b)'), 'AE', 'ab', '0') == 1)
print(play2win(bu('(-a+b)'), 'EA', 'ab', '') == 0)
print(play2win(bu('(-a+b)'), 'EA', 'ab', '0') == 0)
print('logic and')
print(play2win(bu('(a*b)'), 'AA', 'ab', '') == 0)
print(play2win(bu('(a*b)'), 'AA', 'ab', '0') == 0)
print(play2win(bu('(a*b)'), 'EE', 'ab', '') == 1)
print(play2win(bu('(a*b)'), 'EE', 'ab', '1') == 1)
print(play2win(bu('(a*b)'), 'AE', 'ab', '') == 0)
print(play2win(bu('(a*b)'), 'AE', 'ab', '0') == 1)
print(play2win(bu('(a*b)'), 'EA', 'ab', '') == 1)
print(play2win(bu('(a*b)'), 'EA', 'ab', '1') == 0)
print('logic and with negation')
print(play2win(bu('-(a*b)'), 'AA', 'ab', '') == 1)
print(play2win(bu('-(a*b)'), 'AA', 'ab', '1') == 1)
print(play2win(bu('-(a*b)'), 'EE', 'ab', '') == 1)
print(play2win(bu('-(a*b)'), 'EE', 'ab', '1') == 0)
print(play2win(bu('-(a*b)'), 'AE', 'ab', '') == 0)
print(play2win(bu('-(a*b)'), 'AE', 'ab', '0') == 1)
print(play2win(bu('-(a*b)'), 'EA', 'ab', '') == 0)
print(play2win(bu('-(a*b)'), 'EA', 'ab', '0') == 0)
print('logic and with one side negation')
print(play2win(bu('(-a*b)'), 'AA', 'ab', '') == 0)
print(play2win(bu('(-a*b)'), 'AA', 'ab', '0') == 0)
print(play2win(bu('(-a*b)'), 'EE', 'ab', '') == 0)
print(play2win(bu('(-a*b)'), 'EE', 'ab', '0') == 1)
print(play2win(bu('(-a*b)'), 'AE', 'ab', '') == 1)
print(play2win(bu('(-a*b)'), 'AE', 'ab', '1') == 1)
print(play2win(bu('(-a*b)'), 'EA', 'ab', '') == 1)
print(play2win(bu('(-a*b)'), 'EA', 'ab', '1') == 0)
print('some tricky cases')
print('--6--')
print('no way to win')
print(play2win(bu('(x*y)'), 'EE', 'xy', '0') == 1)
print('opposite way to win')
print(play2win(bu('((x*-y)+z)'), 'EAA', 'xyz', '1') == 1)
print(play2win(bu('((x*-y)+z)'), 'EAA', 'xyz', '11') == 0)
print(play2win(bu('((x*-y)+-z)'), 'EAA', 'xyz', '1') == 1)
print(play2win(bu('((x*-y)+-z)'), 'EAA', 'xyz', '11') == 1)
print(play2win(build_tree('((-x+y)*z)'), 'EAE', 'xyz', '') == 0)
print(play2win(build_tree('((-x+y)*z)'), 'EAE', 'xyz', '0') == 0)
print(play2win(build_tree('((-x+y)*z)'), 'EAE', 'xyz', '00') == 1)
print(play2win(build_tree('((x*-y)+z)'), 'AEA', 'xyz', '') == 0)
print(play2win(build_tree('((x*-y)+z)'), 'AEA', 'xyz', '0') == 1)
print(play2win(build_tree('((x*-y)+z)'), 'AEA', 'xyz', '01') == 0)
print(play2win(build_tree('((-x*y)+z)'), 'AEA', 'xyz', '') == 1)
print(play2win(build_tree('((-x*y)+z)'), 'AEA', 'xyz', '1') == 1)
print(play2win(build_tree('((-x*y)+z)'), 'AEA', 'xyz', '11') == 0)