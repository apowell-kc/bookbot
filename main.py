def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    word_count = count_words(text)
    character_counts = count_characters(text)
    #print(character_counts)
    
    #print (dict_list)
    
    sorted_list = dict_to_sorted_list(character_counts)
    
    
    


    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item["char"]}' character was found {item["num"]}' times")

    print("--- End report ---")






def get_text(path):
    with open(path) as f:
        text = f.read()
    return text


#This is a less efficient way better option
# words = text.split
# length = len(words)
def count_words(text):
    words = text.split()
    counter = 0
    for word in words:
        counter += 1
    return counter

def count_characters(string):
    string = string.lower()
    character_counts = {}
    for char in string:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    return character_counts



# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries

def sort_on(dict):
    return dict["num"]

def dict_to_sorted_list(dict):
    sorted_list = []

    for char in dict:
        sorted_list.append({"char": char, "num": dict[char]})
    sorted_list.sort(reverse=True, key= sort_on)
    return sorted_list

main()