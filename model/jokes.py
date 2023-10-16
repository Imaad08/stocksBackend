import random

jokes_data = []
joke_list = [
    "If you give someone a program... you will frustrate them for a day; if you teach them how to program... you will "
    "frustrate them for a lifetime.",
    "Q: Why did I divide sin by tan? A: Just cos.",
    "UNIX is basically a simple operating system... but you have to be a genius to understand the simplicity.",
    "Enter any 11-digit prime number to continue.",
    "If at first you don't succeed; call it version 1.0.",
    "Java programmers are some of the most materialistic people I know, very object-oriented",
    "The oldest computer can be traced back to Adam and Eve. It was an apple but with extremely limited memory. Just "
    "1 byte. And then everything crashed.",
    "Q: Why did Wi-Fi and the computer get married? A: Because they had a connection",
    "Bill Gates teaches a kindergarten class to count to ten. 1, 2, 3, 3.1, 95, 98, ME, 2000, XP, Vista, 7, 8, 10.",
    "Q: What’s a aliens favorite computer key? A: the space bar!",
    "There are 10 types of people in the world: those who understand binary, and those who don’t.",
    "If it wasn't for C, we’d all be programming in BASI and OBOL.",
    "Computers make very fast, very accurate mistakes.",
    "Q: Why is it that programmers always confuse Halloween with Christmas? A: Because 31 OCT = 25 DEC.",
    "Q: How many programmers does it take to change a light bulb? A: None. It’s a hardware problem.",
    "The programmer got stuck in the shower because the instructions on the shampoo bottle said: Lather, Rinse, Repeat.",
    "Q: What is the biggest lie in the entire universe? A: I have read and agree to the Terms and Conditions.",
    'An SQL statement walks into a bar and sees two tables. It approaches, and asks may I join you?'
]

# Initialize jokes
def initJokes():
    # setup jokes into a dictionary with id, joke, haha, boohoo
    item_id = 0
    for item in joke_list:
        jokes_data.append({"id": item_id, "joke": item, "haha": 0, "boohoo": 0})
        item_id += 1
    # prime some haha responses
    for i in range(10):
        id = getRandomJoke()['id']
        addJokeHaHa(id)
    # prime some haha responses
    for i in range(5):
        id = getRandomJoke()['id']
        addJokeBooHoo(id)
        
# Return all jokes from jokes_data
def getJokes():
    return(jokes_data)

# Joke getter
def getJoke(id):
    return(jokes_data[id])

# Return random joke from jokes_data
def getRandomJoke():
    return(random.choice(jokes_data))

# Liked joke
def favoriteJoke():
    best = 0
    bestID = -1
    for joke in getJokes():
        if joke['haha'] > best:
            best = joke['haha']
            bestID = joke['id']
    return jokes_data[bestID]
    
# Jeered joke
def jeeredJoke():
    worst = 0
    worstID = -1
    for joke in getJokes():
        if joke['boohoo'] > worst:
            worst = joke['boohoo']
            worstID = joke['id']
    return jokes_data[worstID]

# Add to haha for requested id
def addJokeHaHa(id):
    jokes_data[id]['haha'] = jokes_data[id]['haha'] + 1
    return jokes_data[id]['haha']

# Add to boohoo for requested id
def addJokeBooHoo(id):
    jokes_data[id]['boohoo'] = jokes_data[id]['boohoo'] + 1
    return jokes_data[id]['boohoo']

# Pretty Print joke
def printJoke(joke):
    print(joke['id'], joke['joke'], "\n", "haha:", joke['haha'], "\n", "boohoo:", joke['boohoo'], "\n")

# Number of jokes
def countJokes():
    return len(jokes_data)

# Test Joke Model
if __name__ == "__main__": 
    initJokes()  # initialize jokes
    
    # Most likes and most jeered
    best = favoriteJoke()
    print("Most liked", best['haha'])
    printJoke(best)
    worst = jeeredJoke()
    print("Most jeered", worst['boohoo'])
    printJoke(worst)
    
    # Random joke
    print("Random joke")
    printJoke(getRandomJoke())
    
    # Count of Jokes
    print("Jokes Count: " + str(countJokes()))