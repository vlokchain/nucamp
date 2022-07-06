# HOW QUICK SORT ALGORITHMS WORK:

"""
NOTE:

1. Implements a divide and conquer technique by dividing the list into two subsections repeatedly
2. Quicksort can use any item in the list as its pivot unlike binary search
3. Once a pivot is chosen values that are less than the pivot are moved to the left side of the list which we'll call being below the pivot
4. Values that are greater than or equal to the pivot are moved to the right side which we'll call being above the pivot
5. Then each side is treated as a separate list and a pivot is chosen for each of these sides
6. Each side is divided again into sub-lists of items that are less than or greater than or equal to the pivot
7. We continue this process recursively until the list is fully sorted
"""
# THE PROCESS (TRANSCRIPT FROM COURSE VIDEO):
"""
Let's look at an example:
1. The first step with this algorithm is to pick a pivot by convention the pivot is usually the first or the last index we will use the last index as our pivot
2. Now we can start sorting beginning with the first item since 65 is greater than 9 we must put 65 above 9. we call quick
3. So in order to put 65 above 9  3 different shifts must happen: the index of 65 must change from 0 to 4 > the index of 9 must change from 4 to 3 but there's already an item at index 3 with a value of 10.
4 So the index of 10 must change from 3 to 0 where 65 used to be just for now
5. Next we repeat the process of comparing
the item at index 0 with the pivot 9.
the pivot stays the same even though it
has moved positions in the list
since 10 is bigger than 9 we move 10
above the pivot and move the pivot down
one index the same way we did before
9 goes from index 3 to 2.
10 takes index 3 and the item at index 2
100 goes to index 0.
we're not done so repeat again
100 is also bigger than the pivot so 9
goes to index 1 100 to index 2 and 3
into index 0.
we're almost done sorting
finally 3 is less than 9 so it can stay
where it is below 9.
now since all items below the pivot are
smaller in value and all items above the
pivot are larger or equal in value we
can conclude that the pivot 9 has the
correct index
we have figured out exactly where it
needs to be
now we must handle the subsections
recursively with the same quick sort
algorithm we will divide and conquer
if a subsection has one or less items no
further sorting is needed it's already
sorted
now we can focus on the other side the
subsection of values that are greater
than or equal to the pivot value
here we have more than one item so we
must run the quick sort algorithm on
this side
we must pick a new pivot we'll use the
item in the last index for this
subsection which is 65.
we compare it with the item at the first
index for this subsection which is index
two with a value of one hundred
we know one hundred is greater than
sixty-five so 100 moves to index 4 65
moves to index 3 and the item that was
at index 3 10 moves to index 2.
we are yet left again with two more
subsections since these subsections each
only contain one item we can conclude
that these items have their correct
index
so we have divided and conquered and the
combined result is that the entire list
is sorted thus quicksort is finished in

"""