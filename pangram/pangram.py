def is_pangram(sentence):
    _ = ','.join(sentence.replace(' ', ''))
    sample_list = [elem.lower() for elem in _.split(',')]
    verify_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                   'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letter in verify_list:
        if letter not in sample_list:
            return False
    return True

