#################################################
# hw1.py
# name: Ritam
#################################################

import cs112_f22_week1_linter
import math

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7): #helper-fn
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d): #helper-fn
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Functions for you to write
#################################################

def distance(x1, y1, x2, y2):
    del_x = abs(x1 - x2)
    del_y = abs(y1 - y2)
    return math.sqrt(del_x**2 + del_y**2)

def circlesIntersect(x1, y1, r1, x2, y2, r2):  
    return distance(x1,y1,x2,y2) <= (r1+r2)

def getInRange(x, bound1, bound2):
    minimum = min(bound1,bound2)
    maximum = max(bound1,bound2)
    if x < minimum:
        return minimum
    if x > maximum:
        return maximum
    return x

def eggCartons(eggs):
    return math.ceil(eggs/12)

def pascalsTriangleValue(row, col):
    #pascal triangle element can be found with nCr = C(row-1,col-1)
    # but since the row, col is 0 indexed we wont subtract 1
   
    #wrote this check based on  test cases
    if row < 0 or col < 0 or col > row:
        return None
    return math.factorial(row) / (math.factorial(row-col) * math.factorial(col))

def getKthDigit(n, k):
    n = abs(n)
    n = n // (10**k)

    return n%10

def setKthDigit(n, k, d):
    sign = -1 if n < 0 else +1
    n = abs(n)
    last_digits = n % 10**k
    first_digits = n // (10**(k+1))

    result = first_digits* (10**(k+1)) + last_digits  + d* (10**k)
    return result*sign 
        
def nearestOdd(n):
    int_n = int
    d = n - int(n)
    #if the difference is greater
    if d > 0:
        if int(n)%2 == 0:
            return int(n) + 1
    #if the difference is smaller or equal
    else:
        if int(n)%2 == 0:
            return int(n) - 1
    #no change if the number is already odd
    return int(n)

def numberOfPoolBalls(rows):
    # 4 - 1 + 2 + 3 + 4
    # it just sums from 1 to n
    if rows == 0:
        return 0
    return (rows * (rows + 1)) //2

def numberOfPoolBallRows(balls):
    # row * (row+1) // 2 = total number of balls
    # row**2 + row = 2 * balls
    # row^2 + row - 2*balls = 0
    # solving for the roots of the quadratic equation
    # roots = (-b +(-) sqrt(b^2 - 4ac) ) / (2a)
    #D = b^2 - 4ac
    D = 1**2 - 4 * (1)*(-2*balls) #15

    # we should not do integer division here 
    # as the ceil function would not have a fraction part
    root1 = math.ceil((-1 + math.sqrt(D))/(2*1))
    root2 = math.ceil((-1 - math.sqrt(D))/(2*1))

    #discard the negative root

    positive_root = root1 if root1 >= 0 else root2

    return positive_root
    

def colorBlender(rgb1, rgb2, midpoints, n):
    # n cant be negative or greater than the midpoints + 1
    if n < 0 or n>(midpoints+1):
        return None 

    color_s_r =100*getKthDigit(rgb1,8) +  \
        10* getKthDigit(rgb1,7) + 1*getKthDigit(rgb1,6)
    color_s_g =100*getKthDigit(rgb1,5) +  \
        10* getKthDigit(rgb1,4) + 1*getKthDigit(rgb1,3)
    color_s_b =100*getKthDigit(rgb1,2) + \
        10* getKthDigit(rgb1,1) + 1*getKthDigit(rgb1,0)


    color_e_r =100*getKthDigit(rgb2,8) + \
        10* getKthDigit(rgb2,7) + 1*getKthDigit(rgb2,6)
    color_e_g =100*getKthDigit(rgb2,5) + \
        10* getKthDigit(rgb2,4) + 1*getKthDigit(rgb2,3)
    color_e_b =100*getKthDigit(rgb2,2) + \
        10* getKthDigit(rgb2,1) + 1*getKthDigit(rgb2,0)

    delta_r = ( color_e_r - color_s_r )/(midpoints+1)
    delta_g = ( color_e_g - color_s_g)/(midpoints+1)
    delta_b = ( color_e_b - color_s_b)/(midpoints+1)

    result = roundHalfUp((color_s_r  + delta_r*n))*(10**6) + \
            roundHalfUp((color_s_g  + delta_g*n))*(10**3) + \
            roundHalfUp((color_s_b  + delta_b*n))*(10**0)
    return result

#################################################
# Bonus/Optional
#################################################
def handToDice(n):
    return getKthDigit(n,2), getKthDigit(n,1),getKthDigit(n,0)

def diceToOrderedHand(n1,n2,n3):
    max2 = max(n1,n2,n3)
    
    if max2 == n1:
        max1 = max(n2,n3)
    elif max2 == n2:
        max1 = max(n1,n3)
    else:
        max1 = max(n1,n2)

    max0 = n1+n2+n3 - max1  - max2

    return max2*100 + max1*10 + max0

def playStep2(hand, dice):
    d1,d2,d3 = handToDice(hand)
    if d1 != d2 or d2 != d3:
        if d1 == d2:
            d3 =dice%10
            dice = dice //10
        elif d2 == d3:
            d1 =dice%10
            dice = dice //10
        elif d1 == d3:
            d2= dice%10
            dice=dice//10
        else :
            d1 = max(d1,d2,d3)
            d2 = dice%10
            dice = dice //10
            d3 = dice %10
            dice = dice//10

    hand_output = diceToOrderedHand(d1,d2,d3)

    return hand_output, dice

def score(hand):
    d1,d2,d3 = handToDice(hand)
    if d1 == d2 and d2 == d3:
        score = 20 + d1*3
    elif d1 == d2:
        score = 10 + d1*2
    elif d2 == d3:
        score = 10 + d2*2
    elif d1 == d3:
        score = 10 + d1*2
    else :
        score = max (d1,d2,d3)
    return score

def bonusPlayThreeDiceYahtzee(dice):
    
    hand1_outcome,out_dice  = playStep2(dice % 1000, dice // 1000)
    hand2_outcome,out_dice = playStep2(hand1_outcome, out_dice)

    return hand2_outcome,score(hand2_outcome)

#################################################
# Test Functions
#################################################

def testDistance():
    print('Testing distance()... ', end='')
    assert(almostEqual(distance(0, 0, 3, 4), 5))
    assert(almostEqual(distance(-1, -2, 3, 1), 5))
    assert(almostEqual(distance(-.5, .5, .5, -.5), 2**0.5))
    print('Passed!')

def testCirclesIntersect():
    print('Testing circlesIntersect()... ', end='')
    assert(circlesIntersect(0, 0, 2, 3, 0, 2) == True)
    assert(circlesIntersect(0, 0, 2, 4, 0, 2) == True)
    assert(circlesIntersect(0, 0, 2, 5, 0, 2) == False)
    assert(circlesIntersect(3, 3, 3, 3, -3, 3) == True)
    assert(circlesIntersect(3, 3, 3, 3,- 3, 2.99) == False)
    print('Passed!')

def testGetInRange():
    print('Testing getInRange()... ', end='')
    assert(getInRange(5, 1, 10) == 5)
    assert(getInRange(5, 5, 10) == 5)
    assert(getInRange(5, 9, 10) == 9)
    assert(getInRange(5, 10, 10) == 10)
    assert(getInRange(5, 10, 1) == 5)
    assert(getInRange(5, 10, 5) == 5)
    assert(getInRange(5, 10, 9) == 9)
    assert(getInRange(0, -20, -30) == -20)
    assert(almostEqual(getInRange(0, -20.25, -30.33), -20.25))
    print('Passed!')

def testEggCartons():
    print('Testing eggCartons()... ', end='')
    assert(eggCartons(0) == 0)
    assert(eggCartons(1) == 1)
    assert(eggCartons(12) == 1)
    assert(eggCartons(13) == 2)
    assert(eggCartons(24) == 2)
    assert(eggCartons(25) == 3)
    print('Passed!')

def testPascalsTriangleValue():
    print('Testing pascalsTriangleValue()... ', end='')
    assert(pascalsTriangleValue(3,0) == 1)
    assert(pascalsTriangleValue(3,1) == 3)
    assert(pascalsTriangleValue(3,2) == 3)
    assert(pascalsTriangleValue(3,3) == 1)
    assert(pascalsTriangleValue(1234,0) == 1)
    assert(pascalsTriangleValue(1234,1) == 1234)
    assert(pascalsTriangleValue(1234,2) == 760761)
    assert(pascalsTriangleValue(3,-1) == None)
    assert(pascalsTriangleValue(3,4) == None)
    assert(pascalsTriangleValue(-3,2) == None)
    print('Passed!')

def testGetKthDigit():
    print('Testing getKthDigit()... ', end='')
    assert(getKthDigit(809, 0) == 9)
    assert(getKthDigit(809, 1) == 0)
    assert(getKthDigit(809, 2) == 8)
    assert(getKthDigit(809, 3) == 0)
    assert(getKthDigit(0, 100) == 0)
    assert(getKthDigit(-809, 0) == 9)
    print('Passed!')

def testSetKthDigit():
    print('Testing setKthDigit()... ', end='')
    assert(setKthDigit(809, 0, 7) == 807)
    assert(setKthDigit(809, 1, 7) == 879)
    assert(setKthDigit(809, 2, 7) == 709)
    assert(setKthDigit(809, 3, 7) == 7809)
    assert(setKthDigit(0, 4, 7) == 70000)
    assert(setKthDigit(-809, 0, 7) == -807)
    print('Passed!')

def testNearestOdd():
    print('Testing nearestOdd()... ', end='')
    assert(nearestOdd(13) == 13)
    assert(nearestOdd(12.001) == 13)
    assert(nearestOdd(12) == 11)
    assert(nearestOdd(11.999) == 11)
    assert(nearestOdd(-13) == -13)
    assert(nearestOdd(-12.001) == -13)
    assert(nearestOdd(-12) == -13)
    assert(nearestOdd(-11.999) == -11)
    # results must be int's not floats
    assert(isinstance(nearestOdd(13.0), int))
    assert(isinstance(nearestOdd(11.999), int))
    print('Passed!')

def testNumberOfPoolBalls():
    print('Testing numberOfPoolBalls()... ', end='')
    assert(numberOfPoolBalls(0) == 0)
    assert(numberOfPoolBalls(1) == 1)
    assert(numberOfPoolBalls(2) == 3)   # 1+2 == 3
    assert(numberOfPoolBalls(3) == 6)   # 1+2+3 == 6
    assert(numberOfPoolBalls(10) == 55) # 1+2+...+10 == 55
    print('Passed!')

def testNumberOfPoolBallRows():
    print('Testing numberOfPoolBallRows()... ', end='')
    assert(numberOfPoolBallRows(0) == 0)
    assert(numberOfPoolBallRows(1) == 1)
    assert(numberOfPoolBallRows(2) == 2)
    assert(numberOfPoolBallRows(3) == 2)
    assert(numberOfPoolBallRows(4) == 3)
    assert(numberOfPoolBallRows(6) == 3)
    assert(numberOfPoolBallRows(7) == 4)
    assert(numberOfPoolBallRows(10) == 4)
    assert(numberOfPoolBallRows(11) == 5)
    assert(numberOfPoolBallRows(55) == 10)
    assert(numberOfPoolBallRows(56) == 11)
    print('Passed!')

def testColorBlender():
    print('Testing colorBlender()... ', end='')
    # http://meyerweb.com/eric/tools/color-blend/#DC143C:BDFCC9:3:rgbd
    assert(colorBlender(220020060, 189252201, 3, -1) == None)
    assert(colorBlender(220020060, 189252201, 3, 0) == 220020060)
    assert(colorBlender(220020060, 189252201, 3, 1) == 212078095)
    assert(colorBlender(220020060, 189252201, 3, 2) == 205136131)
    assert(colorBlender(220020060, 189252201, 3, 3) == 197194166)
    assert(colorBlender(220020060, 189252201, 3, 4) == 189252201)
    assert(colorBlender(220020060, 189252201, 3, 5) == None)
    # http://meyerweb.com/eric/tools/color-blend/#0100FF:FF0280:2:rgbd
    assert(colorBlender(1000255, 255002128, 2, -1) == None)
    assert(colorBlender(1000255, 255002128, 2, 0) == 1000255)
    assert(colorBlender(1000255, 255002128, 2, 1) == 86001213)
    assert(colorBlender(1000255, 255002128, 2, 2) == 170001170)
    assert(colorBlender(1000255, 255002128, 2, 3) == 255002128)
    print('Passed!')

def testBonusPlayThreeDiceYahtzee():
    print('Testing bonusPlayThreeDiceYahtzee()...', end='')
    assert(handToDice(123) == (1,2,3))
    assert(handToDice(214) == (2,1,4))
    assert(handToDice(422) == (4,2,2))
    assert(diceToOrderedHand(1,2,3) == 321)
    assert(diceToOrderedHand(6,5,4) == 654)
    assert(diceToOrderedHand(1,4,2) == 421)
    assert(diceToOrderedHand(6,5,6) == 665)
    assert(diceToOrderedHand(2,2,2) == 222)
    assert(playStep2(413, 2312) == (421, 23))
    assert(playStep2(421, 23) == (432, 0))
    assert(playStep2(413, 2345) == (544, 23))
    assert(playStep2(544, 23) == (443, 2))
    assert(playStep2(544, 456) == (644, 45))
    assert(score(432) == 4)
    assert(score(532) == 5)
    assert(score(443) == 10+4+4)
    assert(score(633) == 10+3+3)
    assert(score(333) == 20+3+3+3)
    assert(score(555) == 20+5+5+5)
    assert(bonusPlayThreeDiceYahtzee(2312413) == (432, 4))
    assert(bonusPlayThreeDiceYahtzee(2315413) == (532, 5))
    assert(bonusPlayThreeDiceYahtzee(2345413) == (443, 18))
    assert(bonusPlayThreeDiceYahtzee(2633413) == (633, 16))
    assert(bonusPlayThreeDiceYahtzee(2333413) == (333, 29))
    assert(bonusPlayThreeDiceYahtzee(2333555) == (555, 35))
    print('Passed!')


#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    testDistance()
    testCirclesIntersect()
    testGetInRange()
    testEggCartons()
    testPascalsTriangleValue()
    testGetKthDigit()
    testSetKthDigit()
    testNearestOdd()
    testNumberOfPoolBalls()
    testNumberOfPoolBallRows()
    testColorBlender()
    # Bonus:
    testBonusPlayThreeDiceYahtzee()

def main():
    cs112_f22_week1_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
