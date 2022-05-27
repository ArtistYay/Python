#To print on another line use triple quotes
letter = """Dear Terry,
You must cut down the mightiest tree in the forest with... 
a herring!""" 
print(letter)

#You can join a sentence without a catenate
name = 'Artist'
color = 'PURPLE'

msg = '[' + name + '] loves the color ' + color + '!' #Before
msg1 = f'[{name}] loves the color {color.lower()}!' #After
#When using the f strings or f' it means all the variables inside the curly brackets are read and replaced by there value.

print(msg)
print(msg1)

