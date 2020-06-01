# Address Parser

Python script to parse address with concatenated street names and numbers.

Provide (1) built Docker image on Docker Hub and (2) a Dockerfile that can build a Docker image from source code. 



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



## Environment

1. Python 3
2. [libpostal](https://github.com/openvenues/libpostal) : A C library for parsing/normalizing street addresses around the world. Powered by statistical NLP and open geo data.
3. [pypostal](https://github.com/openvenues/pypostal) : Python bindings to libpostal for fast international address parsing/normalization



## Getting Started and Running

### Option 1: Run docker container

You can use the Docker container as a little virtual machine and only focus on the functionality and correctness of address parsing. To eliminate the environment setting and dependencies as much as possible. Here provide different ways that you can choose either pull the image from Docker Hub or build the image from source code. Then run the script in a Docker container.

#### 1. Pull and run the built image from [Docker Hub](https://hub.docker.com/repository/docker/wu8149/address_parser) 

1. Pull the image from Docker Hub

   ```
   docker pull wu8149/address_parser
   ```

2. Run the image in interactive mode

   ```
   docker run -ti wu8149/address_parser
   ```



#### 2. Build and run the image from source code

1. Build the **addressParser** Docker image.
   This process will take a couple of minutes.

   ```
   docker build -t address_parser .
   ```

2. Run the image in interactive mode

   ```
   docker run -ti address_parser
   ```

---



### Option 2: Run source code locally

1. Install [libpostal](https://github.com/openvenues/libpostal), a C library for parsing. For more detailed installing instruction please refer to the original repository.

   - **On Ubuntu/Debian**

     ```
     sudo apt-get install curl autoconf automake libtool python-dev pkg-config
     ```

   - **Installing libpostal**

     ```
     git clone https://github.com/openvenues/libpostal
     cd libpostal
     ./bootstrap.sh
     ./configure --datadir=[...some dir with a few GB of space...]
     make
     sudo make install
     
     # On Linux it's probably a good idea to run
     sudo ldconfig
     ```

2. Install [pypostal](https://github.com/openvenues/pypostal),  Python bindings to libpostal

   ```
   pip install postal
   ```

3. Install dependencies

   ```
   pip install -r requirements.txt
   ```

4. Run Python script 

   ```
   python3 addressParser.py
   ```

   

## Tests

Run the testing script. The testing script imports the testing dataset from`testCase.csv`.

```
python3 test_addressParser.py 
```

