# APP2-AA3-Qui-perd-gagne-



**Project Lowbid** 

We are currently launching our startup which wants to disrupt online auctions . 
In order to do so, we want to make a platform that turns the sell of a premium item into a viral event. 
Our project is quite simple in theory , it is called **"Lowest Unique Bid Wins"**

**Description of the programm**


**Functionalities of the platform : Comprehension of the problem : Determine the rules set**

We are going to define different rules for our game to work properly.

**Why the the 0 price is not a dominant strategy with the risque bonus**

With a relatively high value of the intensity of the risk premium alpha(α) ,rushing directly toward zero is not a predomiant strategy:
bid_cost(price) = base_cost + α/(price+1)

If the players were all ties (for example 0)  : they all pay (base_cost + α), the players wins nothing, so this strategy is not really worth it

**The kind of informations necessary to determine the winner** 

The informations necessary to determine the winner is the minimum score of each punters during an aunction 

**Determine the winner with filtering the prices**

The prices need to be filtered in order to allow for each different round of auction a unique price for a unique object for a player to choose accordingly


**Avoid degeneration**

A binary search tree can become inefficiant if it becomes degenerate. 
In order to avoid degeneration, we need to use a perfect or full binary search tree
Help algorithmic compexity : O(log(n)) instead of O(n)


**Is there structures that allows to maintain the ordonnated prices dynamically ?**

**What difference is there between sorting at the end or maintain a permanent order ?**

**If updates arrive in a continuous stream, which solution is the most suitable?**




