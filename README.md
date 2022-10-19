# Mindbox test tasks
Test tasks for Mindbox company vacancy.

## Assignment conditions
A company needs to group clients for AB-tests. Grouping algorithm is quiet simple: take client ID (consists of 5-7 digits, e.g. 7412567) and find sum of these digits.
Result number shall be group number, in which client belong. 

To find out how good is this algorithm you need to write these diagnostic functions:
1. A function that counts the number of customers that get into each group, if ID has end-to-end numbering and begins from 0.
Function input is an integer number `n_customers` (number of client).
2. A function similar to the first function, if ID begins from arbitrary number. Function input are integer numbers: `n_customers` (number of clients) and `n_first_id` (first ID in a sequence).