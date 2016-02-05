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

