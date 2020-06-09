from postal.parser import parse_address
import json
import re
from collections import OrderedDict


def addressParser(inputAddress):

    parsedAddress = parse_address(inputAddress)
    print(parsedAddress)
    try:
        try:
            # extract the first house_number value
            parsedHouseNumber = [element for element in parsedAddress
                                 if 'house_number' in element[1]][0][0]

        except IndexError:
            parsedHouseNumber = ''

        houseNumber = re.search(
            parsedHouseNumber, inputAddress, flags=re.IGNORECASE).group(0)

        streetArray = [element for element in parsedAddress
                       if 'house_number' not in element[1]]

        parsedStreet = ' '.join([str(x[0]) for x in streetArray])

        # substitute houseNumber with empty in the input string,
        # igore leading and trailing space and specific chracter
        street = re.sub(
                        houseNumber, '',
                        inputAddress,
                        flags=re.IGNORECASE
                        ).rstrip(
                                    '}{[]()?@$%^*<>/\\\"\'~;:-_, '
                        ).lstrip(
                                    '}{[]()?@$%^*<>/\\\"\'~;:-_,. '
                        ).replace(
                                    '  ', ' '
                        ).replace(
                                    ' ,', ','
                        )

        addressDict = OrderedDict([("street", street),
                                  ("housenumber", houseNumber)])
        # retnrn json object with orderedDict
        return json.dumps(addressDict, ensure_ascii=False)
    except Exception as e:
        print(e)


def main():
    print("Enter \"exit()\" to exit the script.")

    while(1):
        inputAddress = input("\nEnter one-line address: \n")

        if(inputAddress == "exit()"):
            break
        else:
            print(addressParser(inputAddress))


if __name__ == "__main__":
    main()
