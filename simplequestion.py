from collections import namedtuple


Fact = namedtuple('Fact', ['sentence'])
Query = namedtuple('Query', ['sentence', 'answer', 'support'])


def load(filename):
    stories = [[]]

    with open(filename) as f:
        for line in f:
            idx, parsed = parse_line(line)
            if idx < len(stories[-1]):
                stories.append([])
            stories[-1].append(parsed)

    return stories


def parse_line(line):
    idx, sentence = line.split(' ', 1)
    idx = int(idx)
    if '?' in sentence:
        parsed = parse_query(sentence)
    else:
        parsed = parse_fact(sentence)
    return idx, parsed


def parse_fact(fact):
    return Fact(fact.strip())


def parse_query(sentence):
    query, answer, support = sentence.split('\t')
    return Query(query.strip(), answer.strip(), int(support))
