# import necessary libraries
import pandas
import argparse

# read filename from command line
ap = argparse.ArgumentParser(description='Convert dta file to csv')
ap.add_argument("-f", "--file", required=True, help="dta file to convert")
args = vars(ap.parse_args())

print(args['file'][:-4])

# read data from given dta file
data = pandas.io.stata.read_stata(args['file'])

# save data in csv format
data.to_csv(f"{args['file'][:-4]}.csv")
