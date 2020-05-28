# Address Parser

Python script to parse address using libpostal library with Python binding.

Provide Dockerfile can build docker image for using.

## Examples of parsing



## Getting Started

To eliminate the environment setting and dependencies as much as possible. Here provide different ways that you can choose to run script in docker container you prefer.

### Pull from Docker Hub



### Build docker image

1. Build the **addressParser** docker image.
   This process will take a couple of minutes.

   ```
   docker build -t address_paser .
   ```

   

2. Run the image

   ```
   docker run -ti address_paser
   ```

   

3. 



## Running

In this challenge, I use docker container as a little virtual machine and only focus on the the functionality and correctness of address parsing. Once you start the container. 



## Strategy to solve the task

1. Easy case - simple address
   assumption:
2. Medium case - variant address
   assumption:
3. Complex case - different countries
   assumption:

From the first and second cases, it is possible to parse the address by splitting input string according to the assumption. However, when it comes to the complex case, the input address would be written in different languages,  from different countries and irregular, which means it is not possible to parse it based on small group of rules of assumption. It needs a large data to help us to solve the task. Thus, use the trained machine learning model would be possible approach.



## TO-DO

