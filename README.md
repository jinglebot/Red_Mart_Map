# Red_Mart_Map

1. The first line indicates the dimensions of the map.
2. The values given represent the altitude for that area of the map.
3. From each area in the grid, there are only 4 directions to go: N, S, E, W.
4. You can only go to the direction whose value is less than the one you are in.
5. You are given the choice of starting point, the one you think that can give you the longest path.
6. The path is measured by the number of areas visited.
7. If there are several paths down of the same length, you want to take the one with 
    the steepest vertical drop as measured from the difference between start point and the end point.
8. Therefore, find the longest (and then steepest) path on this map specified in the format above.

## This was a question given in a job application. I had a difficult time solving it in C++ then. So, I'm trying to solve it in Python now. No purpose really. Like the problem said, it was just a diversion.

Pseudo code:
- open/read file, find highest/lowest value/values, find neighbors
- search to get next highest from neighbors in 4 directions(N, E, S, W)
- do recursion until the lowest value/values is reached

