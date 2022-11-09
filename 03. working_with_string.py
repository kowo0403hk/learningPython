phrase = "Giraffe\nAcademy"
print(phrase + "\nis cool")

# using string methods
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())

# chaining methods together
print(phrase.upper().isupper())
print(len(phrase))

# working with string index like an array
print(phrase[1])

# more
# the index function returns the first index of the character we are searching for. Or, it can return
# the starting position of the phrase we are looking for
print(phrase.index("G"))
print(phrase.index("Acad"))

print(phrase.replace("Giraffe", "Elephant"))
