from string import maketrans   


s = "mohamed"
old = s[0]
new = '$' 


print  s[0] + s[1:].translate(maketrans(s[0] , new))