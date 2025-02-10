# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------------------------------------------------
read_velocity.py
-------------------------------------------------------------------------------------------------------------------------
Created on Thu Mar 21 15:18:38 2024

@author: Andres Cremades Botella

File to read the data of the velocity fields. The file contains the following functions:
    Functions:
        - read_velocity : file to read the velocity
"""
# -----------------------------------------------------------------------------------------------------------------------
# Read the packages for all the functions
# -----------------------------------------------------------------------------------------------------------------------
import sys
import numpy as np

# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# Define the functions
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

def read_tb(data_in={"folder":"../../P125_21pi_vu","file":"P125_21pi_vu.$INDEX$.h5.uvw","index":1000,
                     "dx":1,"dy":1,"dz":1,"shpx":196,"shpy":201,"shpz":96,"padding":15,
                     "data_folder":"Data"}):
    """
    .....................................................................................................................
    # read_tb: Function to read the turbulent budget for uu, the function generates seven arrays containing the 
               production (prod_uu), turbulent transport (turb_uu), viscous transport (visc_uu), pressure strain 
               (pstr_uu), pressure dissipation (pdis_uu), diffussion (diff_uu) and convection (conv_uu)
    .....................................................................................................................
    Parameters
    ----------
    data_in : TYPE, optional
        DESCRIPTION. The default is {"folder":"../P125_21pi_vu","file":"P125_21pi_vu.$INDEX$.h5.uvw","index":1000,
                                     "dx":1,"dy":1,"dz":1,"shpx":196,"shpy":201,"shpz":96,"padding":15
                                     "data_folder":"Data"}.
        Data:
            - folder      : folder of the velocity data
            - file        : file of the velocity data without the index
            - index       : index of the velocity data file
            - dx          : downsampling in x
            - dy          : downsampling in y
            - dz          : downsampling in z
            - shpx        : shape in x of the tensors
            - shpy        : shape in y of the tensors
            - shpz        : shape in z of the tensors
            - padding     : padding of the fields
            - data_folder : folder to store generated data
    Returns
    -------
    dict
        Turbulent budget fluctuation in the streamwise, wall-normal and spanwise directions.
        Data:
            - prod_uu : production of uu
            - turb_uu : turbulent transport of uu
            - visc_uu : viscous transport of uu
            - pstr_uu : pressure strain of uu
            - pdis_uu : pressure dissipation of uu
            - diff_uu : diffussion of uu
            - conv_uu : convection of uu

    """
    # -------------------------------------------------------------------------------------------------------------------
    # Import packages
    # -------------------------------------------------------------------------------------------------------------------
    import h5py
    from py_bin.py_functions.padding_field import padding_field
    
    # -------------------------------------------------------------------------------------------------------------------
    # Read the data
    # -------------------------------------------------------------------------------------------------------------------
    folder        = str(data_in["folder"])      # folder of the data
    file          = str(data_in["file"])        # file of the data
    index         = str(int(data_in["index"]))  # index of the file
    dx            = int(data_in["dx"])          # downsampling in x
    dy            = int(data_in["dy"])          # downsampling in y
    dz            = int(data_in["dz"])          # downsampling in z
    shpx          = int(data_in["shpx"])        # shape of the tensors in the x direction
    shpy          = int(data_in["shpy"])        # shape of the tensors in the y direction
    shpz          = int(data_in["shpz"])        # shape of the tensors in the z direction
    padding       = int(data_in["padding"])     # padding of the fields
    data_folder   = str(data_in["data_folder"]) # folder to store generated data
    file_complete = folder+'/'+file
    file_ii       = file_complete.replace("$INDEX$",index) 
        
    print('Reading field:' + str(file_ii),flush=True)
    
    # -------------------------------------------------------------------------------------------------------------------
    # Read the information from the files. The information requires the mean values in the wall-normal directions
    # This values should be stored in the data folder, in the case of missing the file, the software will calculate it.
    # -------------------------------------------------------------------------------------------------------------------
    file = h5py.File(file_ii,'r')    
    prod_uu = np.array(file['prod'])[::dy,::dz,::dx]
    # turb_uu = np.array(file['turb_uu'])[::dy,::dz,::dx]
    # visc_uu = np.array(file['visc_uu'])[::dy,::dz,::dx]
    # pstr_uu = np.array(file['pstr_uu'])[::dy,::dz,::dx]
    # pdis_uu = np.array(file['pdis_uu'])[::dy,::dz,::dx]
    # diff_uu = np.array(file['diff_uu'])[::dy,::dz,::dx]
    # conv_uu = np.array(file['conv_uu'])[::dy,::dz,::dx]
    
    # -------------------------------------------------------------------------------------------------------------------
    # Apply the padding if necessary. The padding takes the variable padding to add that number of nodes in both sizes
    # of the channel in the streamwise and the spanwise directions. The idea is to preserve the periodicity of the 
    # channel
    # -------------------------------------------------------------------------------------------------------------------
    if padding > 0:
        prod_uu = padding_field(data_in={"field":prod_uu,"shpx":shpx,"shpy":shpy,"shpz":shpz,"padding":padding})["field"]
        # turb_uu = padding_field(data_in={"field":turb_uu,"shpx":shpx,"shpy":shpy,"shpz":shpz,"padding":padding})["field"]
        # visc_uu = padding_field(data_in={"field":visc_uu,"shpx":shpx,"shpy":shpy,"shpz":shpz,"padding":padding})["field"]
        # pstr_uu = padding_field(data_in={"field":pstr_uu,"shpx":shpx,"shpy":shpy,"shpz":shpz,"padding":padding})["field"]
        # pdis_uu = padding_field(data_in={"field":pdis_uu,"shpx":shpx,"shpy":shpy,"shpz":shpz,"padding":padding})["field"]
        # diff_uu = padding_field(data_in={"field":diff_uu,"shpx":shpx,"shpy":shpy,"shpz":shpz,"padding":padding})["field"]
        # conv_uu = padding_field(data_in={"field":conv_uu,"shpx":shpx,"shpy":shpy,"shpz":shpz,"padding":padding})["field"]
    data_output = {"prod_uu":prod_uu}#,"turb_uu":turb_uu,"visc_uu":visc_uu,"pstr_uu":pstr_uu,"pdis_uu":pdis_uu,
                   # "diff_uu":diff_uu,"conv_uu":conv_uu}
    return data_output