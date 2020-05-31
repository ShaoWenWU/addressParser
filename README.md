# Address Parser

Python script to parse address with concatenated street names and numbers.

Provide built docker image on Docker Hub also a Dockerfile that can build docker image from source code. 

## Examples of parsing

**Input:** string of address

**Output:** string of street and string of street-number as JSON object

1. `"Winterallee 3"` -> `{"street": "Winterallee", "housenumber": "3"}`
2. `"Musterstrasse 45"` -> `{"street": "Musterstrasse", "housenumber": "45"}`
3. `"Blaufeldweg 123B"` -> `{"street": "Blaufeldweg", "housenumber": "123B"}`
4. `"Am Bächle 23"` -> `{"street": "Am Bächle", "housenumber": "23"}`
5. `"Auf der Vogelwiese 23 b"` -> `{"street": "Auf der Vogelwiese", "housenumber": "23 b"}`
6. `"4, rue de la revolution"` -> `{"street": "rue de la revolution", "housenumber": "4"}`
7. `"200 Broadway Av"` -> `{"street": "Broadway Av", "housenumber": "200"}`

8. `"Calle Aduana, 29"` -> `{"street": "Calle Aduana", "housenumber": "29"}`

9. `"Calle 39 No 1540"` -> `{"street": "Calle 39", "housenumber": "No 1540"}`

## Dependency

1. python 3
2. [libpostal](https://github.com/openvenues/libpostal) library with Python binding

## Getting Started and Running

You can use docker container as a little virtual machine and only focus on the the functionality and correctness of address parsing. To eliminate the environment setting and dependencies as much as possible. Here provide different ways that you can choose either pull the image from Docker Hub or build the image from source code. Then run script in docker container.

### 1. Pull and run built image from Docker Hub 

1. Pull the image from Docker Hub

   ```
   docker pull wu8149/address_parser
   ```

2. Run the image

   ```
   docker run -ti wu8149/address_parser
   ```



### 2. Build and run image from source code

1. Build the **addressParser** docker image.
   This process will take a couple of minutes.

   ```
   docker build -t address_parser .
   ```

2. Run the image

   ```
   docker run -ti address_parser
   ```

