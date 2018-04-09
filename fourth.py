parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]

test_string = """This is PLACE, no NOUN named PERSON, We have so many PLURALNOUN around here."""

def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None
        
def play_game(ml_string, parts_of_speech):    
	sliced= ml_string.split()
	for pos in sliced :
		index = 0
		while index < len(parts_of_speech):
			if parts_of_speech[index] in pos:
				s = pos.replace(pos , "corgi")
		
			
	return s


    #replaced = []
    # your code here
    






print play_game(test_string, parts_of_speech)       
