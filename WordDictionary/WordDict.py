import re

print "Welcome to Perry's Vocab Notebook."
wordDict = {};
word = "";
patternWord = re.compile(r'^[a-zA-Z]+$');
while (True):
    word = raw_input("Please input your word:\n");
    if(len(word)==0 or word == "q" or word == "Q"):
        #q or empty input -> exit the tool
        print("No input, exit.");
        break;
    else:
        if(patternWord.match(word)):
            if(wordDict.has_key(word)):
                print("The word exist, meaning is:  " + wordDict[word] + "");
            else:
                meaning = raw_input("New word, Please enter the meaning for this word :");
                wordDict[word] = meaning;
                print("" + word + "->" + meaning + " saved.");
        else:
            print("Sorry, please enter a vaild English Word.");


