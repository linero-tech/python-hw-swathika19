from to_do import TODO


def task8(sentence, character):
    new_sentence = sentence.upper()
    new_character = character.upper()
    result = 0
    for character in new_sentence:
      if character == 'new_character':
        result = result + 1


    return result


if __name__ == "__main__":

   print(task8("I CODE IN PYTHON", "i"))