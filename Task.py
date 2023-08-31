sentence = input()

if sentence.upper() in sentence:
    
    print(sentence.lower()+"!")

elif sentence.lower() in sentence:
    
    print(sentence.capitalize())