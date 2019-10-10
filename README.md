# Informed Search
Assignment #2 AI

## Requirements
You need python to run the program. 

## The Pancake Problem
### Define The problem
The problem can be defined as a search problem if we define the sequence of cake as nodes 
and the path between nodes means there's a way to flip the cakes once to change the sequence of cakes from one states to another.

All we need is to find a path from the original sequence to the goal sequence.

### Cost Function
The cost of a node is the times of flips from the root node. That means it will cost `1` for a node to reach it's child node.

###  Heuristic Function
A heuristic function will calculate the occurrence times of two adjacent number without adjacent value.

Take `[3, 1, 4, 5, 2, 6]` for example, the heuristic value is `4` ( `[3, 1]`, `[1, 4]`, `[5, 2]`, `[2, 6]`don't have adjacent value)

It is consistent because when we move closer to the goal, the heuristic value will be smaller.

It is admissible because the heuristic value is less than the real cost to flip the cakes to a correct order.
###
## Implementation Details
All the cakes are randomly sequenced, like `[3, 2, 1, 4, 5, 6]` in which `6` represents the plate. 

Cakes are also assigned a number which represents the size of the cake.(`1` is the smallest cake and `5` is the biggest one)

Our goal is to flip cakes on top of the stack until the sequence is `[1, 2, 3, 4, 5, 6]`

## Authors

Alvaro Mendez ([alvaro.mendez@tufts.edu](mailto:alvaro.mendez@tufts.edu))

Yuqiao Zhao ([yuqiao.zhao@tufts.edu](mailto:yuqiao.zhao@tufts.edu))