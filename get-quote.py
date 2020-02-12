import random

def main():

    last = 13
    rnd = random.randint(0, last)
    print("Keep it logically awesome.")

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()
    
    last = len(quotes) - 1
    print(quotes[rnd])

if __name__== "__main__":
    main()
