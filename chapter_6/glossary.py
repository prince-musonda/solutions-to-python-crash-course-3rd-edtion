word_glossary = {
        'a list' : 'an ordered collection of values',
        'boolean expression' : 'an expression that evaluates to either true or false',
        'method' : 'an action performed by a programming language on a data type',
        'if statement' :'a block of code that is excuted only if a given condition is true.',
        'string concatenation' : 'the joining of two or more strings together',
        'dictionary' : 'a collection of key and value pairs',
}

for word, word_meaning in word_glossary.items():
        print(f'{word}:\n\t"{word_meaning}"\n')
