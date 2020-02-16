import random

def main():

    print("Keep it logically awesome.")

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()
    
    rnd = random.randint(0, len(quotes))
    quote = quotes[rnd].strip()
    print(quote)

    output = open("quote.txt", "w")
    output.write(quote)
    output.close()


if __name__== "__main__":
    main()
