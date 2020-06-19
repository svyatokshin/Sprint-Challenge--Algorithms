#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n) - even though there is an n*n*n within the while loop, this increases in a linear fashion. the while loop continues until n^3 but increases by n^2. This seems to be a trick question where they want you to think it is n^3 based on the amount of n's even though it is a linear relationship.

b) O(nlog(n)) - we have a while loop nested inside of a for loop. O(n) represents the outside for loop as you will be moving through this loop n times, and log(n) represents the while loop, as the j is being multiplied by 2 every loop through, meaning that we will be moving way faster than n amount of times through this loop.

c) O(n) - This one seems to be a linear relationship as well. You will have a result of 2 for 1 bunny, 4 for 2 bunnies, 6 for 3 bunnies, 8 for 4 bunnies, 10 for 5 bunnies and so on. This is linear as it does not exponentially or logrithmically go up.

## Exercise II

n story building
plenty of eggs
if egg is dropped from f floor or higher, it breaks, lower it doesnt

strategy:
Since we have n floors and a main floor that is the last one to break eggs, this can be achieved using a Binary Search.

We will start by finding the middle floor by using (n//2).
We then drop the egg from this floor and using a boolean we will return true (breaks) and false (does not break).

If it returns true, we will use this middle floor as our new end value and divide it by 2 again (mid//2) and run again to find out if it breaks.

if it returns false, we will use (n-mid)//2 in order to find a new middle and run it again to see if it breaks. We will repeat the process until it breaks.

This would be O(log(n)) runtime complexity

A simpler approach that wouldnt be as efficient would be to drop the egg from the top floor, then decrease n by 1 until we reach a floor that is does not break the egg. That would have a runtime complexity of O(n).
