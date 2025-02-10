# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------------------------------------------------
norm_tb.py
-------------------------------------------------------------------------------------------------------------------------
Created on Fri Mar 22 11:59:50 2024

@author:  Andres Cremades Botella

File to normalize the turbulent budgets fields. The normalization generates values between 0 and 1 using the 
minimum and the maximum of the velocity values. The file contains the following functions:
    Functions:
        - norm_tb : function for normalize the turbulent budget
        - dim_tb  : function for dimensionalize the turbulent budget
"""

# -----------------------------------------------------------------------------------------------------------------------
# Import packages for all the functions
# -----------------------------------------------------------------------------------------------------------------------
import sys
import numpy as np

# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# Define the functions
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

def norm_tb(data_in={"prod_uu":[],"folder_data":"Data","norm_file":"norm.txt","data_type":"float32",
                     "mean_norm":False}):
    """
    .....................................................................................................................
    # norm_tb: function for normalize the velocity
    .....................................................................................................................
    Parameters
    ----------
    data_in : dict, optional
        Data for the normalization of the velocity.
        The default is {"prod_uu":[],"folder_data":"Data","norm_file":"norm.txt","data_type":"float32"}.
        Data:
            - prod_uu     : streamwise velocity stress (uu) production budget
            - folder_data : path to the folder containing the normalization
            - norm_file   : file with the normalization values
            - data_type   : type of the data (float32,float16...)
            - mean_norm   : choose normalizing with the mean

    Returns
    -------
    data_out : dict
        Normalized velocity. The velocity is configured in float16 to save memory during the training
        Data:
            - prod_uunorm : normalized streamwise velocity stress (uu) production budget

    """    
    # -------------------------------------------------------------------------------------------------------------------
    # The normalization of the turbulent budget is generated in float format
    # -------------------------------------------------------------------------------------------------------------------
    prod_uu   = np.array(data_in["prod_uu"],dtype="float")
    mean_norm = bool(data_in["mean_norm"])
    
    # -------------------------------------------------------------------------------------------------------------------
    # import packages
    # -------------------------------------------------------------------------------------------------------------------
    if mean_norm:
        print("Standarization not implemented. Set mean_norm to False",flush=True)
        sys.exit()
    else:
        from py_bin.py_functions.normalization_tb import read_norm
        
    # -------------------------------------------------------------------------------------------------------------------
    # Check datatype
    # -------------------------------------------------------------------------------------------------------------------
    if "data_type" in data_in.keys():
        data_type = str(data_in["data_type"])                       # definition of the data type.
        if not (data_type=="float32" or data_type=="float16"):
            data_type = "float32"
    else:
        print("[trainvali_data.py:data_traintest_tf] Data type needs to be selected.")
        sys.exit()
    
    # -------------------------------------------------------------------------------------------------------------------
    # Read the normalization parameters
    # -------------------------------------------------------------------------------------------------------------------
    folder_data    = str(data_in["folder_data"])               # folder of the generated data
    norm_file      = str(data_in["norm_file"])                 # file of the normalization data
    norm_data      = {"folder":folder_data,"file":norm_file}
    try:
        norm_param = read_norm(norm_data)
    except:
        print('Normalization file could not be located. Calculation is stopped...',flush=True)
        sys.exit()
    
    if mean_norm:
        print("Standarization not implemented. Set mean_norm to False",flush=True)
        sys.exit()
    else:
        prod_uumax = float(norm_param["prod_uumax"])
        prod_uumin = float(norm_param["prod_uumin"])
        
        # ---------------------------------------------------------------------------------------------------------------
        # Define the normalized fields using float 16 format
        # ---------------------------------------------------------------------------------------------------------------
        prod_uunorm = np.array((prod_uu-prod_uumin)/(prod_uumax-prod_uumin),dtype=data_type)
    data_out = {"prod_uunorm":prod_uunorm}
    return data_out

def dim_tb(data_in={"prod_uunorm":[],"folder_data":"Data","norm_file":"norm.txt",
                    "data_type":"float32","mean_norm":False}):
    """
    .....................................................................................................................
    # dim_tb: function for dimensionalize the turbulent budget
    .....................................................................................................................
    Parameters
    ----------
    data_in : dict, optional
        Data for the non-normalization of the velocity.
        The default is {"prod_uunorm":[],"folder_data":"Data","norm_file":"norm.txt",
                        "data_type":"float32","mean_norm":False}.
        Data:
            - prod_uunorm : normalized streamwise velocity stress (uu) production budget
            - folder_data : path to the folder containing the normalization
            - norm_file   : file with the normalization values
            - data_type   : type of the data (float32,float16...)
            - mean_norm   : choose normalizing with the mean

    Returns
    -------
    data_out : dict
        Normalized velocity. The turbulent budget is configured in float16 to save memory during the training
        Data:
            - prod_uu : streamwise velocity stress (uu) production budget

    """
    # -------------------------------------------------------------------------------------------------------------------
    # Calculate the dimensional turbulent budget
    # -------------------------------------------------------------------------------------------------------------------
    if "data_type" in data_in.keys():
        data_type = str(data_in["data_type"])                   # definition of the data type.
        if not (data_type=="float32" or data_type=="float16"):
            data_type = "float32"
    else:
        print("[trainvali_data.py:data_traintest_tf] Data type needs to be selected.")
        sys.exit()
    prod_uunorm = np.array(data_in["prod_uunorm"],dtype=data_type)
    mean_norm   = bool(data_in["mean_norm"])
    
    # -------------------------------------------------------------------------------------------------------------------
    # import packages
    # -------------------------------------------------------------------------------------------------------------------
    if mean_norm:
        print("Standarization not implemented. Set mean_norm to False",flush=True)
        sys.exit()
    else:
        from py_bin.py_functions.normalization_tb import read_norm
    
    # -------------------------------------------------------------------------------------------------------------------
    # Read the normalization parameters, use the float 16 format
    # -------------------------------------------------------------------------------------------------------------------
    folder_data    = str(data_in["folder_data"])                # folder of the generated data
    norm_file      = str(data_in["norm_file"])                  # file of the normalization data
    norm_data      = {"folder":folder_data,"file":norm_file}
    try:
        norm_param = read_norm(norm_data)
    except:
        print('Normalization file could not be located. Calculation is stopped...',flush=True)
        sys.exit()
    
    if mean_norm:
        print("Standarization not implemented. Set mean_norm to False",flush=True)
        sys.exit()
    else:
        prod_uumax = float(norm_param["prod_uumax"])
        prod_uumin = float(norm_param["prod_uumin"])
        
        # ---------------------------------------------------------------------------------------------------------------
        # Define the normalized fields using float 16 format
        # ---------------------------------------------------------------------------------------------------------------
        prod_uu = np.array(prod_uunorm*(prod_uumax-prod_uumin)+prod_uumin,dtype=data_type)
    data_out = {"prod_uu":prod_uu}
    return data_out
