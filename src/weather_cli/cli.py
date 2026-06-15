from .errors import (
    check_invalid_lat,
    check_invalid_long,
    LatitudeValidationError,
    LongitudeValidationError,
)

import argparse


parser = argparse.ArgumentParser(
    description="Weather CLI that reads latitude and longitude"
)

parser.add_argument(
    "--lat",
    type=float,
    required=True,
    help="Latitude value"
)

parser.add_argument(
    "--lon",
    type=float,
    required=True,
    help="Longitude value"
)

args = parser.parse_args()

print("**Welcome to the CLI Weather Project!**")
print("Where would you like to find the weather for?")

print(f"Latitude entered: {args.lat}")
print(f"Longitude entered: {args.lon}")

try:
    check_invalid_lat(args.lat)
    check_invalid_long(args.lon)

    print("Coordinates accepted")

except (LatitudeValidationError, LongitudeValidationError) as e:
    print("Coordinates invalid")
    print(e)