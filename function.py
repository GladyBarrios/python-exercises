def calculate_tip(tip_percentage, bill):
    amount_to_tip = bill * tip_percentage
    return amount_to_tip
# for the diffrent excersises 
def get_letter_grade(grade):
    if type(grade) == int or type(grade) == float:
        if grade >= 90:
            return "A"
        elif grade >= 80:
            return "B"
        elif grade >= 70:
            return "C"
        elif grade >= 60:
            return "D"
        else:
            return "F"
    else:
        return "Input must be a number"

# for the diffrent excersises 
def remove_vowels(string):
    output = ''
    for char in string:
        if is_consonant(char):
            output += char
    return output         




def is_vowel(string):
    return len(string) == 1 and string.lower() in 'aeiou'
    