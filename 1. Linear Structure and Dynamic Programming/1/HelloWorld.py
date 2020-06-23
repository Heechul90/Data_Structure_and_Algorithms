

class HelloWorld():
    def __init__ (self) :
        print("Hello World! Just one more time")

    def __del__ (self) :
        print("Good Bye")

    def performAverage(self, val1, val2):
        average = (val1 + val2) / 2
        print(average)





def main():
    world = HelloWorld()
    score1 = int(input("score1 = "))
    score2 = int(input("score2 = "))
    world.performAverage(score1, score2)


main()