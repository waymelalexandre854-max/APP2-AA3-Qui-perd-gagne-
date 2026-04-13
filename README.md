# APP2-AA3-Qui-perd-gagne-



**Project Lowbid** 

We are currently launching our startup which wants to disrupt online auctions . 
In order to do so, we want to make a platform that turns the sell of a premium item into a viral event. 
Our project is quite simple in theory , it is called **"Lowest Unique Bid Wins"**

**Description of the programm**

.....

**Functionalities of the platform : Comprehension of the problem : Determine the rules set**

We are going to define different rules for our game to work properly.


**The aunction system**
Our lowbid platform regroups different items to sell with a corresponding price to each :
A different item for a different round of aunction 
Examples : 
Round 1 : A De Vince painting , Value: 2 000 000 €
Round 2 : An hellenistic greec helmet , Value : 12 000 €

Strategy : The players can choose to change their play style depending on the initial cost of the object in aunction: skip an item for a more intersting one 


**Opponents strategy for the game**
Our Lowbid aunction system included different IA types for each opponent , which that every opponent have a unique in game strategy.
Each player can choose different paths depending on a current situation 




**The kind of informations necessary to determine the winner** 

The informations necessary to determine the winner is the minimum score of each punters during an aunction, the minimum being 0 . 
Winner takes all: The winner obtains the object of the auction of the round, the other players get nothing .

**Why the the 0 price is not a dominant strategy with the risque bonus**

With a relatively high value of the intensity of the risk premium alpha(α) ,rushing directly toward zero is not a predomiant strategy:
bid_cost(price) = base_cost + α/(price+1)
α is determined in the menu of the game . For a specific aunction , the jury can impose a certain value of α
If the players were all ties (for example 0)  : they all pay (base_cost + α), the players wins nothing, so this strategy is not really worth it

**Determine the winner with filtering the prices**

The prices need to be filtered in order to allow for each different round of auction a unique price for a unique object for a player to choose accordingly


**Avoid degeneration**

A binary search tree can become inefficiant if it becomes degenerate. 
In order to avoid degeneration, we need to use a perfect or full binary search tree
Help algorithmic compexity : O(log(n)) instead of O(n)



Lowbid is unique and revolutionnary project that will change the future of online aunction in a more fun and strategic aspect. It is no longer about just paying money: intelligent moves are rewarded and rushed moves are punished. 
That is why we ask you to invest in our project !  

**download requierment :** the programm need the python library random and sys to work propely
