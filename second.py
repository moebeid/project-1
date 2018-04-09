from random import randint

def random_verb():
    random_num = randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"
        
def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

def word_transformer(word):
    if word == "NOUN":
        return random_noun()
    elif word == "VERB":
        return random_verb()
    else:
        return word[0]
        
def process_madlib(mad_lib):
    processed = ""
    s = mad_lib.find ("NOUN")
    f = ""
    f = mad_lib[s:s+5]
    word_transformer(f)
    h = mad_lib.replace("NOUN",random_noun())
    s = h.find ("VERB")
    f = h[s:s+5]
    processed = h.replace("VERB",random_verb())
    return processed


    



   
print process_madlib("I'm going to VERB to the store and pick up a NOUN or two.")