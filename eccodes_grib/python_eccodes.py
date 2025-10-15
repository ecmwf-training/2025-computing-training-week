# eccodes basic demo
# this script shows how to open a grib file, read messages, and print key values

from eccodes import *

# choose one of your grib files
grib_file = "output.grib1"

print(f"Opening GRIB file: {grib_file}\n")

# open the file
with open(grib_file, "rb") as f:
    print("Reading first GRIB message...")
    gid = codes_grib_new_from_file(f)
    if gid is None:
        raise Exception("No GRIB messages found in file!")

    print("Extracting key metadata:\n")
    print("  centre:", codes_get(gid, "centre"))
    print("  dataDate:", codes_get(gid, "dataDate"))
    print("  dataTime:", codes_get(gid, "dataTime"))
    print("  shortName (parameter):", codes_get(gid, "shortName"))
    print("  level:", codes_get(gid, "level"))
    print("  grid size (Ni x Nj):", codes_get(gid, "Ni"), "x", codes_get(gid, "Nj"))

    print("\nReading data values...")
    values = codes_get_values(gid)
    print(f"  total number of values: {len(values)}")
    print("  first 5 values:", values[:5])

    # release handle
    codes_release(gid)

print("\nECCODES demo completed.")
