# open todos for duck ecosystem

The application simulates a lake, where birds, predators and humans visit

It has the following features:
- the eco system get prepopulated with all creatures
- all creatures have an atrtibute danger which provides the total danger at lake side
- each creature has a certain limit and can float into lake szenario or out
- birds can be duck types, gull or swans, they can fly, swim or duck
- predators can be wolf and lynx, they can walk or hide
- humans can be hunter or ranger, they can walk, sit or hide. They can have a gun, binocular or backsack, or all of which.
- different creatures are attracted by different eco system states: humans are attracted by wheather condition and number of birds and predators. birds are attracted by other birds and absence of predators or humans. predators are attracted by birds and absence of humans.
- eco system knows all creatures at lake side, wheather conditions, number of birds, humans and predators and total danger index.

- ecosystem needs to be Subject as well and have all objects which cannot be in Lake
- ideally all the different animals/humans at the lake should be from the same class and provide decorator options, e.g. ranger, hunter, duck, wolf
- all these observers should provide an danger factor back to the lake and all animals at the lake should respond to the danger potential at the lake. this then has to be part of the abstract class as getDanger() method

