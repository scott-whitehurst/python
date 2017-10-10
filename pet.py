#!/usr/local/bin/python3.4

def snake(type, noise, age=5, colour='black'):
    print("My snake is a", age, "year old", colour, type, "and he says", noise)

def dog(breed, call, age=7, colour='brown', state='good'):
    print("My dog is a", age, "year old", colour, breed, "and he says", call, "- He is a", state, "boy!")

snek = "cobra"
doggo = "husky"
dragon = "night fury"

snake(snek, 'venom strike', 5, 'green')

dog(doggo, 'borf', 6, 'white', 'bad')

print("I love my %s and I love my %s, but most of all I love my %s!" % (snek, doggo, dragon))
