{% include navbar.html %}

# Practice MCQ Test Corrections

## Test 1, 45/50
Q01 : A programmer is writing a program that is intended to be able to process large amounts of data.  Which of the following considerations is LEAST likely to affect the ability of the program to process larger data sets?
I chose D (How much storage space the program requires as it runs) but the answer is B (How many programming statements the program contains).  Considering that the program processes "large amounts of data" as in the size of data is largely irrelevant, the processing time would depend on the process itself. 

Q20 : Two lists, list1 and list2, contain the names of books found in two different collections. A librarian wants to create newList, which will contain the names of all books found in either list, in alphabetical order, with duplicate entries removed.   Which of the following code segments will correctly create newList?
<img src="/tri3CSPPortfolio/assets/t1q20.png">
I chose B but the answer is A, it was because the lists should be sorted before they are combined.

Q37 : The following code segment is intended to set max equal to the maximum value among the integer variables x, y, and z.  The code segment does not work as intended in all cases.  Which of the following initial values for x, y, and z can be used to show that the code segment does not work as intended?
<img src="/tri3CSPPortfolio/assets/t1q37.png">
I chose D but the answer is B, plugging in x=3, y=2, and z=1 returns an incorrect output.

Q38 : When a cellular telephone user places a call, the carrier transmits the caller’s voice as well as the voice of the person who is called. The encoded voices are the data of the call. In addition to transmitting the data, the carrier also stores metadata. The metadata of the call include information such as the time the call is placed and the phone numbers of both participants. For which of the following goals would it be more useful to computationally analyze the metadata instead of the data?
```
I. To determine if a caller frequently uses a specific word

II. To estimate the number of phone calls that will be placed next Monday between 10:30 A.M. and noon.

III. To generate a list of criminal suspects when given the telephone number of a known criminal
```
The ethics of this question is arguable, but Big Acorn says that C (II and III only) is the correct answer rather than A (II only).  This position is understandable, looking at metadata for phone numbers is a reasonable step to take in an investigation.

Q39 : A certain computer has two identical processors that are able to run in parallel.  Each processor can run only one process at a time, and each process must be executed on a single processor.  The following table indicates the amount of time it takes to execute each of three processes on a single processor.  Assume that none of the processes are dependent on any of the other processes.  Which of the following best approximates the minimum possible time to execute all three processes when the two processors are run in parallel?

| Process |	Execution Time on Either Processor |
| -- | -- |
| X | 60 seconds |
| Y | 30 seconds |
| Z | 50 seconds |

There are *two*, processors.  It would take 

## Test 2, 47/50

<!-- Q8 -->
<!-- ... -->
<!-- ... -->
<!-- ... -->
<!-- ... -->
<!-- Wow, -->

Q01 : Which of the following best describes the ability of parallel computing solutions to improve efficiency?
I chose B (Any solution can be broken down into smaller and smaller parallel portions, making the improvement in efficiency theoretically limitless as long as there are enough processors available.) when the answer is D (The efficiency of a solution that can be broken down into parallel portions is still limited by a sequential portion.).

Q03 : Which of the following actions is most likely to raise legal or ethical concerns?
What's the correct answer, D (A public interest group alerts people to a scam that involves charging them for a program that is available for free under a Creative Commons license) or C (A musician creates a song using samples of a copyrighted work and then uses a Creative Commons license to publish the song)?  Wow, I am so good at reading.

Q19 : In the following procedure, assume that the parameter x is an integer.  Which of the following best describes the behavior of the procedure?
<img src="/tri3CSPPortfolio/assets/mystery.png">
What's the correct answer, D (It displays true if x is negative and displays nothing otherwise) or C (It displays true if x is negative and displays nothing otherwise).  It displays true if x is negative and displays nothing otherwise.  Wow, I am so good at plugging in numbers.

## Test 3, 47/50

Q06 : Which of the following algorithms display all integers between 1 and 20, inclusive, that are not divisible by 3 ?
The answer should be A and D instead of A and C.  C won't display 20 while D will.

Q31 : A student is creating an algorithm to display the distance between the numbers num1 and num2 on a number line.  The following table shows the distance for several different values.  Which of the following algorithms displays the correct distance for all possible values of num1 and num2?

| Value of num1 | Value of num2 | Distance Between num1 and num2 |
| -- | -- | -- |
| 5 | 2 | 3 |
| 1 | 8 | 7 |
| -3 | 4 | 7 |

B, not D, is the correct answer because the difference between two numbers is the absolute value of subtracting one from the other, not subtracting the absolute values.

Q34 : For which of the following situations would it be best to use a heuristic in order to find a solution that runs in a reasonable amount of time?

Heuristic means that the dumb solution would take too much time, not the other way around.  Therefore the answer should be B instead of A.
