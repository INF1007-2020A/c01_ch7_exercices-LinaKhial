def histogram(string: str) -> dict:
    
    histogram = dict() 

    for letter in string :
        if letter != " " :
            histogram[letter] = string.count(letter)

    return histogram
