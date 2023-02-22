from to_do import TODO


def task9(sentence, character):

    count = 0
    for character in sentence:
        if character == 'P':
            count = count + 1
        result = True

    else:

         result = False


    return result


if __name__ == "__main__":

 print(task9("I CODE IN PYTHON","P"))