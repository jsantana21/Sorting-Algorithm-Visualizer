# Sorting Algorithm Visualizer

### Project Duraiton: September 30, 2020 - November 8, 2020 

### Project Task
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The aim of this project is to create an generated user interface (GUI) using Python's Tkinter module to generate random arrays of data values in the form of a bargraph and implement sorting algorithms such as Bubble Sort, Insertion Sort, Quick Sort and Merge Sort to sort the data values and show an animation of how the array is sorted at each step.  

### Background
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; In preparation for my techincal interviews when applying for jobs, I decided to make a project that demonstrates what I've learned from studying for these interviews. So I made this project and in the process of making this I've came to a deeper understanding of these sorting alogrithms. 

### Algorithm & Implementation Outline
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; When it came to creating the GUI, I had to first configure the background and size of the window using the Tkinter module. The white canvas background would be where the bargraph would be generated while the gray box above would be where the user can manipulate certain variables to their liking. The user can change the sorting algorithm, the sorting speed of the algorithm (ranging from 0.1 to 5.0 seconds), the array size (ranging from 3 to 100), the min value (ranging from 0 to 10), and the max value (ranging from 10 to 100). There is a button to generate a new random array based off of the variables mentioned beofre that the user can change and obviously there is also a button to start the sorting algorithm. For more details on the creation of GUI, refer to the comments in the sortingAlgorithmVisualizer.py file. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; I'm going to assume that you know how the sorting algorithms work but if not then refer to these links to understand: [Bubble Sort](https://www.geeksforgeeks.org/bubble-sort/) , [Quick Sort](https://www.geeksforgeeks.org/quick-sort/) , [Merge Sort](https://www.geeksforgeeks.org/merge-sort/) , and [Insertion Sort](https://www.geeksforgeeks.org/insertion-sort/). That aside, when it came to coding out how the sorting would be animated on the GUI the easier of the four would be the Bubble Sort and Insertion Sort probably due to their time complexity of O(n<sup>2</sup>) making them not so efficient in sorting in comparsion to Quick Sort's and Merge Sort's time complexity of O(n log n). Coding out Quick Sort's and Merge Sort's animations were more difficult as both algorithms are Divide and Conquer algorithm where the array is recursively broken down into smaller parts and solved with the base case. I also had to use different colors on certains to denote a variable on each iteration which I will go over in the next section. Once again for more details, refer to the comments in each of the sorting algorithm py files.  

### Results
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; In 


### What Could be Improved?
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; I 
