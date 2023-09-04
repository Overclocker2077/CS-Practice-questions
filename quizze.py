import random
import os

questions_dict = {   # The first answer choice is the correct answer (it will get randomized when displayed to the user)
    """What is the output of the following code?\n
int x = 5;
x += 3;
System.out.println(x);""": "8:5:3:2",

"Which of the following data structures is a Last-In-First-Out (LIFO) structure?": "Stack:Set:List:Queue",

"""What is the output of the following code?\n
String s1 = "hello";
String s2 = "world";
System.out.println(s1 + s2);
""": "helloworld:hello world:hello+world:None of the above",

"Which of the following is not a primitive data type in Java?": "string:double:float:int",

"""What is the output of the following code?\n
int i = 0;
while (i < 5) {
  System.out.print(i + " ");
  i++;
}
""": "01234:12345:012345:None of the above",

"Which of the following is true about recursion?": "It is a technique that involves calling a function from within itself:It is a form of parallel computing:It can only be used with certain data structures:It is always more efficient than using a loop",

"""What is the output of the following code?\n
int[] arr = {1, 2, 3, 4, 5};
for (int i = 0; i < arr.length; i++) {
  System.out.print(arr[i] + " ");
}
""": "12345:54321:01234:None of the above",

"Which of the following is not a sorting algorithm": "Search sort:Merge sort:Quick sort:Bubble sort",

"""What is the output of the following code?\n
int x = 7;
if (x > 5 && x < 10) {
  System.out.println("x is between 5 and 10");
} else {
  System.out.println("x is not between 5 and 10");
}
""":"x is between 5 and 10:x is not between 5 and 10:7:None of the above",

"Which of the following is a valid way to declare a two-dimensional array in Java?": "Both A and B are valid:Neither A nor B is valid:int[][] arr = new int[3][2];:int[][] arr = { {1, 2}, {3, 4}, {5, 6} };",

"Which of the following is true about object-oriented programming?": "It allows for encapsulation and inheritance:It does not allow for code reuse:It focuses on functions rather than data:It is only used in web development",

"""What is the output of the following code?\n
int x = 5;
int y = 10;
System.out.println(x + y);""": "15:510:5 + 10:None of the above",

"Which of the following is not a primitive data type in Java?": "string:double:char:boolean",

"""What is the output of the following code?\n
int[] arr = {2, 4, 6, 8, 10};
for (int i = 0; i < arr.length; i += 2) {
  System.out.print(arr[i] + " ");
}
""": "2 6 10:4 8:2 4 6 8 10:None of the above",

"Which of the following is a valid way to declare and instantiate an ArrayList of Strings in Java?"
: "ArrayList<String> arr = new ArrayList<String>();:Both A and B are valid:ArrayList<String> arr = new ArrayList<String>() {};:ArrayList<String> arr = new ArrayList<String>{};",

"""What is the output of the following code?\n
String s = "hello";
System.out.println(s.length());""":"5:4:6:None of the above",

"Which of the following is a valid way to declare a constant variable in Java?"
: "final int x = 5;:const int x = 5;:int final x = 5;:None of the above",

"""What is the output of the following code?\n
int[] arr = {1, 2, 3};
System.out.println(arr[3]);

""": "ArrayIndexOutOfBoundsException:3:2:1",

"Which of the following is true about abstract classes in Java?": "They can have both abstract and non-abstract methods:They cannot have any constructors:They cannot be extended by other classes:They cannot have any abstract methods",

"""What is the output of the following code?\n
int x = 5;
if (x == 5 || x == 6) {
  System.out.println("x is either 5 or 6");
} else {
  System.out.println("x is neither 5 nor 6");
}

""": "x is either 5 or 6:x is neither 5 nor 6:5 6:None of the above",

"""What is the output of the following code?\n 
String s = "hello";
System.out.println(s.substring(1, 3));
""": "el:he:llo:None of the above",

"Which of the following is the maximum data transfer rate of USB 3.0?": "5 Gbps:5 Mbps:480 Mbps:10 Gbps",

"Which of the following is a characteristic of a solid-state drive (SSD)?": "It is less prone to physical damage than a HDD:It has a larger storage capacity than a HDD:It is slower than a hard disk drive (HDD):It has moving parts"
,

"What type of power connector is commonly used to provide power to a hard disk drive (HDD)?":
"Molex Power Connector:SATA Power Connector:PCIe Power Connector:USB Power Connector",

"Which of the following is a type of port used to connect an external hard drive to a computer?":
"USB:HDMI:VGA:DVI",

"Which of the following is a characteristic of a local area network (LAN)?":
"It is used to connect devices within a building or campus:It uses satellite communication for data transfer:It is typically owned by a telecommunications company:It covers a large geographic area"
,
"What is the purpose of a router in a network?"
:"To connect the network to the internet:To provide power to devices on the network:To convert analog signals to digital signals:To store data on the network",

"Which of the following is a type of computer memory that is non-volatile and retains data even when the computer is turned off?":
"ROM:RAM:Cache:Virtual Memory",

"Which of the following is a type of software that is designed to prevent or remove malware from a computer?":
"Antivirus:Firewall:Encryption:Intrusion Detection System",

"Which of the following is a type of printer that uses ink cartridges to print documents?":
"Inkjet Printer:Dot Matrix Printer:Thermal Printer:Laser Printer",

"What is the purpose of a domain name system (DNS)?":
"To translate domain names into IP addresses:To provide internet connectivity to a network:To encrypt network traffic:To store website data on a server",

"Which of the following can be represented by a single binary digit?":"The remainder when dividing a whole number by 2:The volume of a car radio:The position of the minute hand of a clock:The value of a Boolean variable",

"Digital images are often represented by the red, green, and blue values (an RGB triplet) of each individual pixel in the image. A photographer is manipulating a digital image and overwriting the original image. Which of the following describes a lossless transformation of the digital image?"
:"Creating the negative of an image by creating a new RGB triplet for each pixel in which each value is calculated by subtracting the original value from 255. The negative of an image is reversed from the original; light areas appear dark, and colors are reversed.:Creating the gray scale of an image by averaging the amounts of red, green, and blue in each pixel and assigning this new value to the corresponding pixel in the new image. The new value of each pixel represents a shade of gray, ranging from white to black.:Compressing the image in a way that may lose information but will suffer only a small loss of image quality.:Modifying part of the image by taking the pixels in one part of the picture and copying them to the pixels in another part of the picture.",

"Consider the 4-bit binary numbers 0011, 0110, and 1111. Which of the following decimal values is NOT equal to one of these binary numbers?":"9:15:6:3",

"Three students in different locations are collaborating on the development of an application. Which of the following strategies is LEAST likely to facilitate collaboration among the students?"
:"Having all three students write code independently and then having one student combine the code into a program:Having all three students work in a shared document that each can edit to provide comments on the work in progress:Having all three students use an online shared folder to contribute and discuss components to be considered for use in the application:Having all three students participate in frequent video chat sessions to discuss ideas about the project and to provide feedback on work done so far",

"""A programmer completes the user manual for a video game she has developed and realizes she has reversed the roles of goats and sheep throughout the text.
 Consider the programmer’s goal of changing all occurrences of “goats” to “sheep” and all occurrences of “sheep” to “goats.” The programmer will use the fact that the word “foxes” does not appear anywhere in the original text.

Which of the following algorithms can be used to accomplish the programmer’s goal?""":"""First, change all occurrences of “goats” to “foxes.”
Then, change all occurrences of “sheep” to “goats.”
Last, change all occurrences of “foxes” to “sheep.:
First, change all occurrences of “goats” to “sheep.”
Then, change all occurrences of “sheep” to “goats.”:
First, change all occurrences of “goats” to “sheep.”
Then, change all occurrences of “sheep” to “goats.”
Last, change all occurrences of “foxes” to “sheep.:
First, change all occurrences of “goats” to “foxes.”
Then, change all occurrences of “foxes” to “sheep.”
Last, change all occurrences of “sheep” to “goats.”""",

"""A student wrote the following code segment, which displays true if the list myList contains any duplicate values and displays false otherwise.
The code segment compares pairs of list elements, setting containsDuplicates to true if any two elements are found to be equal in value. 
Which of the following best describes the behavior of how pairs of elements are compared?

ContainsDuplicates = false
j = 1
REPEAT UNTIL j > LENGTH myList -1
    k = j + 1 
    REPEAT UNTIL k > Length myList
        IF myList j = myList j
            containsDuplicates = true
        k = k + 1
    j = j + 1
DISPLAY containsDuplicates
""":"The code segment iterates through myList, comparing each element to all subsequent elements in the list.:The code segment iterates through myList, comparing each element to all other elements in the list.:The code segment iterates through myList, comparing each element to the element that immediately follows it in the list.:The code segment iterates through myList, comparing each element to the element that immediately precedes it in the list.",

"""A homework assignment consists of 10 questions. The assignment is graded as follows. 9-10 = check plus, 7-8 = check, Under 7 = check minus
Let numCorrect represent the number of correct answers for a particular student. The following code segment is intended to display the appropriate grade based on numCorrect. The code segment does not work as intended in all cases.

IF numCorrect > 7
    IF numCorrect >= 9
        DISPLAY "check plus"
    ELSE
        DISPLAY "check minus"
ELSE
    DISPLAY "check"

For which of the following values of numCorrect does the code segment NOT display the intended grade?
"""
:"8:9:7:10",

"""Consider the following code segment.\n
a = 10
b = 20
c = 30
d = 40
x = 20
b = x + b
a = x + 1
d = c + d / 2 
DISPLAY a
DISPLAY b 
DISPLAY c
DISPLAY d

What is the result of the code segment?
""":"21 40 30 50:21 40 30 40:21 30 40 50:10 20 30 40",

"""A programmer is creating an algorithm that will be used to turn on the motor to open the gate in a parking garage. The specifications for the algorithm are as follows.

The gate should not open when the time is outside of business hours.
The motor should not turn on unless the gate sensor is activated.
The motor should not turn on if the gate is already open.
Which of the following algorithms can be used to open the gate under the appropriate conditions?"""
: "Check if the time is during business hours. If it is, check if the gate sensor is activated. If it is, check if the gate is open. If it is not, turn on the motor.:Check if the time is during business hours. If it is, check if the gate sensor is activated. If it is not, check if the gate is open. If it is not, turn on the motor.:Check if the time is during business hours. If it is, check if the gate sensor is activated. If it is, check if the gate is open. If it is, turn on the motor.:Check if the time is outside of business hours. If it is, check if the gate sensor is activated. If it is, check if the gate is closed. If it is, turn on the motor.",

"""In a certain game, the integer variable bonus is assigned a value based on the value of the integer variable score.

If score is greater than 100, bonus is assigned a value that is 10 times score.
If score is between 50 and 100 inclusive, bonus is assigned the value of score.
If score is less than 50, bonus is assigned a value of 0.
Which of the following code segments assigns bonus correctly for all possible integer values of score ?""":
"""
IF(score > 100){
    bonus = score * 10
}
ELSE{
    IF(score >= 50){
        bonus = score
    }
    ELSE{
        bonus = 0
    }
}:
IF(score >= 50){
    IF(score > 100){
        bonus = score * 10
    }
    ELSE{
        bonus = 0
    }
}
ELSE{
    bonus = score
}:
IF(score < 50){
    bonus = 0
}
ELSE{
    IF(score >= 50){
        bonus = score
    }
    ELSE{
        bonus = score * 10
    }
}:
IF(score >= 50){
    IF(score > 100){
        bonus = score * 10
    }
    ELSE{
        bonus = 0
    }
}
ELSE{
    bonus = score
}

""",
"Three different numbers need to be placed in order from least to greatest. For example, if the numbers are ordered 9, 16, 4, they should be reordered as 4, 9, 16. Which of the following algorithms can be used to place any three numbers in the correct order?"
: "If the first number is greater than the middle number, swap them. Then, if the middle number is greater than the last number, swap them. Then, if the first number is greater than the middle number, swap them.:If the first number is greater than the middle number, swap them. Then, if the middle number is greater than the last number, swap them. Then, if the first number is greater than the last number, swap them.:If the first number is greater than the middle number, swap them. Then, if the middle number is greater than the last number, swap them.:If the first number is greater than the last number, swap them. Then, if the first number is greater than the middle number, swap them."
,
"A sorted list of numbers contains 200 elements. Which of the following is closest to the maximum number of list elements that will need to be examined when performing a binary search for a particular value in the list?"
:"8:5:100:200",

"""
In the following code segment, assume that x and y have been assigned integer values.

sum = 0 
REPEAT x TIMES{
    REPEAT y TIMES{
        sum = sum + 1 
    }
}
At the end of which of the following code segments is the value of sum the same as the value of sum at the end of the preceding code segment?
"""
:"""
sum = 0 
z = x*y
REPEAT z TIMES{
    sum = sum + 1
}:
sum = 0
z = x+y 
REPEAT x TIMES{
    sum=sum+1
}:
sum = 0 
REPEAT x TIMES{
    sum = sum + 1
}
REPEAT y TIMES{
    sum = sum + 1
}:
sum = 0
z = x/y 
REPEAT x TIMES{
    sum=sum+1
}
""",
"""Consider the following code segment. Assume that index1 is a number between 1 and LENGTH(theList), inclusive, and index2 is a number between 2 and LENGTH(theList) - 1, inclusive.

theList ← [9, -1, 5, 2, 4, 8]
x ← theList[index1] + theList[index2]

What is the largest possible value that the variable x can have after the code segment executes?""":
"14:17:11:4",

"""
Line 1: count ← 0
Line 2: REPEAT n TIMES
Line 3: {
Line 4:    REPEAT 2 TIMES
Line 5:    {
Line 6:       MOVE_FORWARD()
Line 7:    }
Line 8:    ROTATE_RIGHT()
Line 9: }
Consider the goal of modifying the code segment to count the number of squares the robot visits before execution terminates. Which of the following modifications can be made to the code segment to correctly count the number of squares the robot moves to?""":
"Inserting the statement count  ← count + 1 between line 6 and line 7:Inserting the statement count  ← count + 2 between line 6 and line 7:Inserting the statement count  ← count + 1 between line 8 and line 9:Inserting the statement count ← count + n between line 8 and line 9",

"In which of the following scenarios would a simulation be the LEAST beneficial?":"A retail company wants to determine the most popular item that was sold on the company’s Web site last month.:A manufacturing company wants to determine whether using robots in its facility will increase productivity:An insurance company wants to study the effect of cold weather patterns on health-care costs.:An engineering company wants to test whether a change to a car design will negatively affect fuel efficiency."
,
"The transportation department plans to build a new high-speed train route between two cities. The transportation department wants to implement a simulation of the train before any construction begins on this project. Which of the following statements is true about the use of a simulation for this project?":
"Using a simulation may expose potential safety issues that can be corrected before construction begins.:Other high-speed train routes have been constructed in other locations, so a simulation is not needed.:Implementing a simulation is likely to increase the overall costs associated with the project.:A simulation cannot be used to test the train under varying weather conditions."
,
"A large number of genetic codes are stored as binary values in a list. Which one of the following conditions must be true in order for a researcher to obtain the correct result when using a binary search algorithm to determine if a given genetic code is in the list?":
"The list must be sorted based on the genetic code values.:The genetic codes must be converted from binary to decimal numbers.:The number of genetic code values in the list must be a power of 2.:The number of genetic code values in the list must be even."
,
"A city planner is using simulation software to study crowd flow out of a large arena after an event has ended. The arena is located in an urban city. Which of the following best describes a limitation of using a simulation for this purpose?":
"The model used by the simulation software often omits details so that it is easier to implement:The model used by the simulation software cannot be modified once the simulation has been used.:Running a simulation requires more time to generate data from trials than observing the crowd exiting the arena at various events:Running a simulation requires a large number of observations to be collected before it can be used to explore a problem."
,



# Questions rang up to Prep homework 5 
}

def correct_anwser(answers):
    return answers.split(":")[0]

questions = list(questions_dict.keys())

questions = random.sample(questions, len(questions))

for x in range(20):
    os.system("cls")
    answer_list = random.sample(questions_dict[questions[x]].split(":"), len(questions_dict[questions[x]].split(":")))
    print(questions[x])
    answer = correct_anwser(questions_dict[questions[x]])
    users_answer = input(f""" \n    A) {answer_list[0]}\n
    B) {answer_list[1]}\n
    C) {answer_list[2]}\n
    D) {answer_list[3]}
    """).lower()
    answer_dict = {"a":0,"b":1,"c":2,"d":3}
    try:
        if answer_list[answer_dict[users_answer]] == answer:
            print("Correct!")
        else:
            print(f"The answer is {answer}")
    except KeyError:
        print(f"The answer is {answer}")
    print()
    input("Press enter to continue")
