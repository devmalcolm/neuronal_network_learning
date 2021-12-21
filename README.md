# Zaqo's Machine Learning Training

<img src="http://ForTheBadge.com/images/badges/made-with-python.svg">

This project is not finished.

Here is my neuronal network script, still in progress.

First of all im using numpy as Array and Matplotlib for graphic
All explained in my script in details (in french).

- What does it do ?
This script tht im working on is a AI working with neuronal network system.
I create an array with values 2 variables: "input_dimension" & "input_type", here a photo of my representation.

<img width="1020" alt="Screenshot 2021-12-17 at 6 58 56 PM" src="https://user-images.githubusercontent.com/96392276/146874888-41b16170-4be0-46a6-b7e4-842016dc1683.png">

This array has the lenght, and the width as values.
I also have a variable with only 0 & 1 as value that because it define if its a car or a truck (0 = car & 1 = truck)
so with these values i create an array to put all my different values in that and i let the last columns of type of vehicle empty (?)

- Why ?

Because i want my AI to find if its a car or a truck.
For that my AI need a lot a things, im not very experienced in that domain but im trying to learn by myself.

So i got my activation function, so my Sigmoid function:

![An-illustration-of-the-signal-processing-in-a-sigmoid-function](https://user-images.githubusercontent.com/96392276/146875419-a29bc746-17c1-451c-be00-ab22b46d8a45.png)

And with that function (once applied on my values) it turn all my values between 0 - 1 so more easy to calculate.

Here a representation of my neuronal system with Input Layer, Hidden 

<img width="1346" alt="Screenshot 2021-12-17 at 6 21 17 PM" src="https://user-images.githubusercontent.com/96392276/146875600-38bb4795-fb36-4569-a313-fb65589df115.png">
Layer, and Output Layer.

So in blue is the weights, when we start our AI we need to attribute random weights to our synapse. 
weights = W1
Once our W1 has a random values when can train our program to get some results (real result).

Backpropagation coming soon...
