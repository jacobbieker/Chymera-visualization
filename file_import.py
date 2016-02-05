__author__ = 'jacob'
import os
import csv
import numpy as np
from glob import glob

# get files of various types
data_loc = os.path.abspath("data")

center_of_mass_files = glob(os.path.join(data_loc, "c_o_m.*"))

coefs_files = glob(os.path.join(data_loc, "coefs.*"))

coolheat_files = glob(os.path.join(data_loc, "coolheat.*"))

massflow_files = glob(os.path.join(data_loc, "massflow.*"))

tcoef_files = glob(os.path.join(data_loc, "tcoef.*"))

tctot_files = glob(os.path.join(data_loc, "tctot.*"))

# Combine the files into one larger file to make it easier on reading in

with open(os.path.join(data_loc, "c_o_m_all"), 'w') as outfile:
    for fname in center_of_mass_files:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)

with open(os.path.join(data_loc, "coefs_all"), 'w') as outfile:
    for fname in coefs_files:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)

with open(os.path.join(data_loc, "coolheat_all"), 'w') as outfile:
    for fname in coolheat_files:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)

with open(os.path.join(data_loc, "massflow_all"), 'w') as outfile:
    for fname in massflow_files:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)

with open(os.path.join(data_loc, "tcoef_all"), 'w') as outfile:
    for fname in tcoef_files:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)

with open(os.path.join(data_loc, "tctot_all"), 'w') as outfile:
    for fname in tctot_files:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)