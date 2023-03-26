"""address.py - generate postal addresses"""

import string
import random
import requests

from generic import MUGProduct
from get_resource import get_items


class Address(MUGProduct):
    """Generate an address.
    
    Gets a real, randomly chosen street address,
    with the exception of the addressee.
	Limited to the US for now, or occasionally 
    points close to the US.
    Uses Openstreetmap API, so if the connection 
    fails then it just generates a simple address.
    """

    def __init__(self):
        """Init"""
        super().__init__()
        street_and_locality = self.make_street_and_locality()
        self.number = self.make_address_number()
        self.street = street_and_locality["street"]
        self.locality = street_and_locality["locality"]
        

    def make_address_number(self) -> str:
        """Make address number.
        
        This may be multiline, to account
        for more complicated locations beyond
        the street level (e.g.,
        Room 581
        Floor 24
        235)"""
        
        if random.randint(0,9) == 0:
            mod = get_items("address modifier", 1)[0]["id"]
            if mod in ["Dept","Department"]:
                modnum = get_items("corporate department", 1)[0]["id"]
                modnum = f"of {modnum}"
            else:
                modnum = str(random.randint(1,50))
                if random.randint(0,14) == 0:
                    modnum = modnum + random.choice(string.ascii_uppercase)

            stnum = random.randint(1,9999)
            address_number = f"{mod} {modnum}\n{stnum}"
        else:
            address_number = str(random.randint(1,9999))

        return address_number


    def make_street_and_locality(self) -> dict:

        startcode = get_items("zip code", 1)[0]["id"]

        try:
            # Determine where the center of the given zip code is,
            # in terms of lat/lon
            payload = {"postalcode":startcode,
                       "countrycodes":"us",
                       "limit":"1",
                       "addressdetails":"1",
                       "format":"json"
                       }
            
            req = requests.get("https://nominatim.openstreetmap.org/search/",
                                params = payload)
                                
            result = req.json()
            
            try: # Some locations don't exit
                lat = result[0]["lat"]
                lon = result[0]["lon"]
            except IndexError: 
                lat = "32.435860"
                lon = "-96.964169"
            
            # Add some jitter to the lat/lon
            lat = str(float(lat) + random.uniform(-0.4,0.4))
            lon = str(float(lon) + random.uniform(-0.4,0.4))
                
            # Then get the new location
            payload2 = {"lat":lat,
                        "lon":lon,
                        "zoom":"18",
                        "addressdetails":"1",
                        "format":"json"}
                                    
            req2 = requests.get("https://nominatim.openstreetmap.org/reverse",
                                params = payload2)
                                                    
            result = req2.json()
            
            try:	# The most specific local area name may vary by type 
                road = result["address"]["road"]
                if "locality" in result["address"]:
                    area = result["address"]["locality"]
                elif "city" in result["address"]:
                    area = result["address"]["city"]
                elif "town" in result["address"]:
                    area = result["address"]["town"]
                elif "village" in result["address"]:
                    area = result["address"]["village"]
                elif "hamlet" in result["address"]:
                    area = result["address"]["hamlet"]
                elif "county" in result["address"]:
                    area = result["address"]["county"]
                state = result["address"]["state"]
                postcode = result["address"]["postcode"] #May have changed due to jitter
                
                street = f"{road}"
                locality = f"{area}, {state} {postcode}"

            except KeyError: # Many addresses lack the values above

                # TODO: fix for instances where display_name includes a street

                street_name = get_items(random.choice(["forename","surname"]), 1)[0]["id"]
                street_postfix = get_items("street postfix", 1)[0]["id"]
                street = f"{street_name} {street_postfix}"
                try:
                    locality = result["display_name"]
                except KeyError:
                    locality = startcode # If we still don't have a display_name

                if locality.endswith("United States"):
                    locality = locality.replace(", United States", "", 1)
                    if not ((locality.split())[-1]).isnumeric():
                        locality = f"{locality} {startcode}"
            
        except requests.exceptions.ConnectionError:

            # TODO: improve

            street = "unreadable"
            locality = "unreadable"

        address_locality = {"street":street,
                            "locality":locality
                            }

        return address_locality
