# Address Parser

Python script to parse address using [libpostal](https://github.com/openvenues/libpostal) library with Python binding.

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

You can use docker container as a little virtual machine and only focus on the the functionality and correctness of address parsing. 


