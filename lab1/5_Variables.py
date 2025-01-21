#VARIABLES CREATING VAR
x = 7
y = "Che tam"
print(x)
print(y)

x = 5 #type int
x = "Nichego" #type str
print(x)

#CASTING
x = str(3) #budet '3'
y = int(3) #budet 3
z = float(3) #budet 3.0
print(x,y,z)

#GET THE TYPE
x = 5
y = "Assan"
print(type(x))
print(type(y))

#SINGLE = DOUBLE QUOTES
x = "Erasil"
# tozhe samoe
x = 'Erasil'

#CASE-SENSITIVE
s = 4
S = "MEME"
#S will not overwrite s




#VARIABLE NAMES
myaida = "kek"
my_aida = "kek"
_my_aida = "kek"
myAida = "kek"
MYAIDA = "kek"
myaida2 = "kek"

#CAMEL CASE
myAidaAmatov = "mem"

#PASCAL CASE
MyAidaAmatov = "mem"

#SNAKE CASE
my_aida_amatov = "mem"




#ASSIGN MULTIPLE VALUES MANY VALUES TO MULTIPLE VALUES
x,y,z = "reyna", "jett", "brim"
print(x)
print(y)
print(z)

#ONE VALUE TO MULTIPLE VALUES
x = y = z = "kekus"
print(x)
print(y)
print(z)

#UNPACK A COLLECTION
heros = ["tejo", "omen", "clove"]
x,y,z = heros
print(x)
print(y)
print(z)




#OUTPUT VARIABLES
x = "PP2 is awesome"
print(x)

x = "PP2"
y = "is"
z = "awesome"
print(x,y,z)

x = "PP2"
y = "is"
z = "awesome"
print(x + y + z)

x = 2
y = 3
print(x + y)

x = 1
y = "height"
print(x,y)




#GLOBAL VARIABLES
x = "GG"

def myhehe():
    print("ETO" + " " + x)

myhehe()

#THE GLOBAL KEYWORD
x = "GG"

def myhehe():
    x = "Tochno"
    print("ETO" + " " + x)

myhehe()

print("ETO" + " " + x)


def myhehe():
    global x
    x = "GEGE"

myhehe()
print("ETO" + " " + x)


x = "GEEGEE"

def myhehe():
    global x
    x = "TOCHNO"

myhehe()
print("ETO" + " " + x)

