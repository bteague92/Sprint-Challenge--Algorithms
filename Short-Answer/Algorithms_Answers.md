#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) This is O(n) because the while loop relies on 'a', and 'a' scales up with n. Doing the math here, you will see that any number you put in n, the while loop will still run 'n' amount of times, making it O(n)

b) O(nlogn). This is because the while loop only runs logn times of n, mainly because the while loops relies on j, and in the body, j \*= 2 which means it only runs a fraction of the amount of length of n.

After that, we just have a for loop that runs through n, so O(n) there. so Now we just multiply the while loop with the foor loop time complexity and we get O(nlogn)

c) This is O(n), as it's a recursive function that only calls itself once in the body.
Since recursive functions repeat itself based on an input, it's O(n).
Since there are also no other loops in the body, everything else is O(1), leaving with the biggest time complexity being O(n)

## Exercise II

I would use binary search to find the highest floor an egg can be thrown off of while minimizing the breaking of eggs. Using this technique, I would determine the mid floor of the n-story building and drop the egg from that height. If it didn't break, I would continue up the building, halving the distance to the top until the egg broke, then using the same technique down to find the minimum height that the egg breaks. It would be O(log n) runtime since the function will continue calling itself cutting off half the list and reducing runtime complexity.

<!-- def find_breaking_floor(building_floors):
    for floor_index in range(0, len(building)):
         if throw_egg(floor_index) == "broken":
             return floor_index

simple solution. linear search to find the first floor that the egg breaks at.
runtime complexity of O(n) because the for loop runs n amount of times dependent on the length of the building_floors -->