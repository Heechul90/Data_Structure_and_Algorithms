### Chapter 01-02. Hello World in Python



# Procedure-oriented program
def main():
    print('hello, world')
    print('this program computes the average of two exam sc')

    score1, score2 = input('Enter two scores separated by a')
    average = (score1 + score2 ) / 2.0;

    print('The average of the scores is :', average)

main()



# Object-oriented program
class HelloWorld:
    def __init__(self):
        print('Hello World, Just one more time')

    def __del__(self):
        print('Good bye!')

    def performAverage(self, val1, val2):
        average = (val1 + val2) / 2.0
        print('The average of the scores is : ', average)


def main():
    world = HelloWorld()
    score1, score2 = input('Enter two scores separated by a comma: ')
    world.performAverage(score1, score2)

main()