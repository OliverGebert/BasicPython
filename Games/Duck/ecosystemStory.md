# The Ecosystem
it provides a system of elements like landscape, plants and animals, which require certain frame conditions to prosper and also provide constraints or attrractors to animals in the same ecosystem.

## Landscape
A Landscape has a size (lxw), e.g. 5x5 and each tile is of one type
- water
- beach
- wood

Every tile can be entered by muiltiple habitants. In case more than one habitant enters the tile, following options exist:
- a carnivor kills the other habitant
- the strongest habitant pushes the othe habitants to one of the connected tiles.
- later: birds might fly away from earth predator

## Tiles
- Every tile has a fixed position (x/y coordinate)
- every tile owns a certain type of landscape
- every tile can have max one habitant at the end of the progression

## Landscape
- every landscape has a type (water, beach, wood)
- every landscape has a vision indicator (0-10)
 
## Habitant
- Every habitant is of a type (seagull, fox, human)
- later: every habitant has a current hydration level
- every habitant has a current food level
- every habitant has preferred landscapes for motion
- every habitant has preferred landscape for food

## Progression
The Ecosystem has a live in descrete rounds/progressions. In each round the folllowing happens:
- for each habitant the current food level is recalculated based on landscape offerings
- For each tile potential habitants analyse their most attractive next tile
- Each habitant moves to its most attractive tile
- If there are multiple habitants on one tile they either push others away or kill them.
- repeat with previous step until there are no more clashes on tiles

## Animals
- bird
- predator

### Attributes
- Fear
- Vision
- pace

### Position
- moves alwys in direction of highest attraction
- attraction is defined by existing prey, water, food and absence of other predators

## human
- ranger
- hunter

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

