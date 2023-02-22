from to_do import TODO


def task8(sentence, character):
 new_sentence = sentence.lower()
 count = 0
 for i in new_sentence:
    if i == 'p':
        count = count + 1
 result = count
 return result


if __name__ == "__main__":

 print(task8("I CODE IN PYTHON","P"))