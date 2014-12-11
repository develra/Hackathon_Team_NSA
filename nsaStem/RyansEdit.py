from porter2 import stem
import difflib
import requests
import json

stopList = []

#######################################

# Open stopWords and put into list

def setStops():
    with open('stopWords.txt') as f:
        lines = f.read().splitlines()
    f.close()
    return lines

#######################################

# Open wav2text output and put words in list

def openWav2Text():
    with open('out.txt', 'r') as f:
        readWords = f.read()
    f.close()

    return readWords.split()

#######################################

# Readwords not in stoplist are stemmed, return all root + suffix to json

def stemWords(data):

    jstuff = []

    for word in data:
        suffix = ''
        root = ''
        if word.lower() not in stopList:
            if '*' not in word:
                root = stem(word)
                print root

                for i,s in enumerate(difflib.ndiff(root, word)):
                    if s[0]==' ': continue
                    #elif s[0]=='-':
                    #    print(u'Delete "{}" from position {}'.format(s[-1],i))
                    elif s[0]=='+':
                        print(u'Add "{}" to position {}'.format(s[-1],i))
                        suffix += s[-1]
                jstuff.append({'word':root, 'variance':suffix})
    return jstuff
#######################################

#######################################

# Post jstuff to the interwebs
# Install the Python Requests library:
# `pip install requests`


def send_request(data):
    # My API (POST https://teamnsa.herokuapp.com/words)

    try:
        r = requests.post(
            url="https://teamnsa.herokuapp.com/words",
            headers = {
                "Content-Type":"application/json",
            },
            data = json.dumps(data)
        )
        print('Response HTTP Status Code : {status_code}'.format(status_code=r.status_code))
        print('Response HTTP Response Body : {content}'.format(content=r.content))
    except requests.exceptions.RequestException as e:
        print('HTTP Request failed')


#######################################

if __name__ == "__main__":
    
    stopList = setStops()
    
    readWords = openWav2Text() 

    jstuff = stemWords(readWords)

    send_request(jstuff)
