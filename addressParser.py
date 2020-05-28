print("Starting address parser...")
from postal.parser import parse_address
import json
import re
from collections import OrderedDict

def addressParser():
	while(1):
		inputAddress =  input("Enter one-line address: \n")

		if(inputAddress == "exit()"):
			break;
		else:
			parsedAddress = parse_address(inputAddress)
			try :
			    parsedHouseNumber = [element for element in parsedAddress if 'house_number' in element[1]][0][0]
			    houseNumber = re.search(parsedHouseNumber, inputAddress, flags=re.IGNORECASE).group(0)

			    streetArray = [element for element in parsedAddress if 'house_number' not in element[1]]

			    parsedStreet = ' '.join([str(x[0]) for x in streetArray]) 

			    # print("parsedStreet: ", parsedStreet)
			    street = re.search(parsedStreet, inputAddress, flags=re.IGNORECASE).group(0)

			    addressDict = OrderedDict( [("street",street), ("housenumber",houseNumber)] )
			    print(json.dumps(addressDict, ensure_ascii=False)) # output json object with orderedDict
			except Exception as e:
			    print(e)

   


def main():
	print("Enter \"exit()\" to exit the script.")
	addressParser()

if __name__ == "__main__":
    main()