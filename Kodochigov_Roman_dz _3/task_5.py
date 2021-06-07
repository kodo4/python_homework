from random import randrange, choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n, repeat=False):
    """
    function return random jokes from three lists
    :param n: count of jokes
    :param repeat: True if the jokes are unique
    :return: list oj jokes
    """
    result = []
    noun, adverb, adjective = nouns.copy(), adverbs.copy(), adjectives.copy()
    min_list = min(noun, adverb, adjective)
    while n != 0 and len(min_list) != 0:
        num = randrange(0, len(min_list))
        if repeat:
            result.append(f'{noun.pop(num)} {adverb.pop(num)} {adjective.pop(num)}')
        else:
            result.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
        n -= 1
    return result


print(get_jokes(10))
