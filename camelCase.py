


def main():

    # get the sentence from the user, split
    sentence = input("Please enter a sentence to convert to camelCase (letters only!)")

    sentenceList = sentence.split(' ')
    camelCase = ""

    # change to camel case
    for i in range(len(sentenceList)):
        # for the first word - lowercase
        if i == 0:
            camelCase = camelCase + sentenceList[i].lower()

        else:
            # for each additional word - capitalize first letter, lowercase for the rest
            buildWord = sentenceList[i][0].upper()
            buildWord = buildWord + sentenceList[i][1:].lower()
            camelCase = camelCase + buildWord

    # print
    print(camelCase)

main()