import requests

# using requests, API calls will be made to get a random word and find its definition
#
#
# random word API: http://random-word-api.herokuapp.com/home
# word definition API: https://dictionaryapi.dev/


def randomWord():
    """Makes an API call to retrieve a random word"""

    # Make an API call to get a random word
    word = str(requests.get('https://random-word-api.herokuapp.com/word').text)[2:]

    # Find the end of the word
    word = word[:word.index('"')]
    
    return word

def definition(word):
    """Makes an API call to retrieve the definition of a given word"""

    # Make an API call to get the definition of the word
    defin = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}').text
    
    # Find the beginning of the definition in the response
    index1 = defin.index('"definition"') + 14
    defin = defin[index1:]
    
    # Find the end of the definition
    index2 = defin.index('"')
    defin = defin[:index2]

    # Return the definition
    return defin


def createMessage():
    """Generates a message containing a random word and its definition"""

    success = False

    # If a certain word does not have a definition,
    # keep running until a word is generated that has a definition
    while not success: 
        try:
            # Get a random word
            word = randomWord()
            # Generate the message with the word and its definition
            message = word + " - " + definition(word)
            success = True
        except:
            pass
    
    return message
