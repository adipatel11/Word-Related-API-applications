import requests
import random
import turtle

# requests will be used to make API calls
# the call will return a response in json
# the response will include various synonyms for the given word
# the other response will generate a random word to guess
# Random Word API: http://random-word-api.herokuapp.com/home
# Synonym API: https://words.bighugelabs.com/site/api



def randomWord():

    word = str(requests.get('https://random-word-api.herokuapp.com/word').text)[2:] #API Call

    word = word[:word.index('"')] # finds the end of the word
    
    return word


def getSynonyms(word):

    response = requests.get(f'https://words.bighugelabs.com/api/2/8d80fe04f473c60402905a1fdd32d632/{word}/json').text #API Call

    response = dict(eval(response)) # converts json to a dictionary so that retrieving information becomes easier

    synonyms = []

    # retrieves synonyms for the noun and verb version of the word
    try:
        synonyms += response['noun']['syn']
    except:
        pass    

    try:
       synonyms += response['verb']['syn'] 
    except:
        pass

    return synonyms

# a random word will be generated
# for each synonym that the user does not guess the word, a point will be added
# the point system will work similar to how it works in golf

draw = turtle.Turtle()
draw.ht()
screen = turtle.Screen()
screen.bgcolor('black')
screen.screensize(600,600)
draw.up()
draw.home()
draw.color('antique white')

def turtleWrite(text):
    draw.write(text,move=False,align = 'center', font=('arial',30,'bold'))

draw.down()
turtleWrite('Loading...')



def main():

    success = False
    while not success:
        word = randomWord() # generates random word
        try:
            synonyms = getSynonyms(word) # collects synonyms of the word
            random.shuffle(synonyms) # randomly shuffles the synonyms and the order
            numSynonyms = len(synonyms)
            if numSynonyms > 4:
                success = True
        except:
            pass
            
    
    draw.clear()
    points = 0
    distance = 600/numSynonyms 
    x = 1
    draw.up()
    draw.goto(0,280)
    draw.down()
    draw.color('green')
    turtleWrite('Synonyms:')
    draw.color('antique white')

    for synonym in synonyms:
        draw.up()
        draw.goto(0,290-distance*x)
        draw.down()
        turtleWrite(synonym)

        print(f'One word related to the word is {synonym}\n')
        guess = input("Which word could this be? Enter here: ")
        if guess == word:
            print(f'Great job! You have won with {points} points!')
            break
        else:
            points += 1
            print(f'\nThat is not correct. You now have {points} points.\n')
        x += 1

    print('The word was', word)

    while True:
        screen.exitonclick()


main()
