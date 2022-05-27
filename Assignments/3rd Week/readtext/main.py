# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 

# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    text = open(filename, "r")

    word = text.read().split()
    
    text.close()

    return word


def count_words():
    count = 0
    container = []

    text = read_file_content("./story.txt")
    
    for word in text:
        if word not in container:
            container.append(word)

    for ntotal in container:
        count = text.count(ntotal)

        print(ntotal + ": " + str(count))

count_words()













# # Count the Number of Occurrences in a Python list using .count()
# items = ['a', 'b', 'a', 'c', 'd', 'd', 'd', 'c', 'a', 'b']

# container = []
# count = 0

# for alp in items:
#     if alp not in container:
#         container.append(alp)

# for xy in container:
#     count = items.count(xy)
#     # print(xy + " occurs " + str(count) + " times")
#     # print({f'{xy + ":"} {count}'})

