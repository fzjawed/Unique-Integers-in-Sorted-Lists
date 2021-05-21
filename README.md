# Unique-Integers-in-Sorted-Lists
>20th May 2021 09:56 PM

Okay this one's gonna be my last for the day. I've run into the same "Time Limit Exceeded" problem again but I'm sure I'll figure out a way.

***Question: Given a list of sorted integers nums return the number of unique integers in the list.***


The question also mentions that O(n) is accepted but O(k log n) is encouraged. Dunno what that means lolll.

Anywho as of now I'll be uploading my solution that works for smaller lists.

>21st May 2021 02:44 PM

So I think I overworked my brain yesterday and chose an approach that was way too complicated. The solution I found is simple and similar to other questions I did. Compare the value with the next value - if it's not the same increase the counter; return the counter. 

I've uploaded that piece of code but the hint I checked asked to use binary search so I want to understand the binary search method too! Looking into that now.


Another thing I'm seeing which is a very common solution to this problem is to convert the list "nums" into a set and returning the length of that set. To convert the list into a set they're doing set(nums) and then len() of that set. Set stores only unique values from a list.

Still can't find the binary search one???
