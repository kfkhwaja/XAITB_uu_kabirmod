# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------------------------------------------------
normalization.py
-------------------------------------------------------------------------------------------------------------------------
Created on Fri Mar 22 12:33:24 2024

@author: Andres Cremades Botella

File to create the normalization values for the velocity fields. The normalization generates 
values between 0 and 1 using the minimum and the maximum of the velocity values. The file contains
the following functions:
    Functions:
        - save_norm : function for saving the normalization to a file
        - read_norm : function for reading the normalization file
        - calc_norm : function for calculating the normalization
"""

# ---------------------------------------------------------------------------------------------------------------------
# Import packages for all the functions
# ---------------------------------------------------------------------------------------------------------------------
import numpy as np

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# Define the functions
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
    
def save_norm(data_in={"folder":"Data","file":"norm.txt","prod_uumax":0,"turb_uumax":0,"visc_uumax":0,"pstr_uumax":0,
                       "pdis_uumax":0,"diff_uumax":0,"conv_uumax":0,"prod_uumin":0,"turb_uumin":0,"visc_uumin":0,
                       "pstr_uumin":0,"pdis_uumin":0,"diff_uumin":0,"conv_uumin":0}):
    """
    .....................................................................................................................
    # save_norm: function for saving the normalization to a file. The function saves the maximum and minimum values
                 of the velocity components and stress components
    .....................................................................................................................
    Parameters
    ----------
    data_in : dict, optional
        Data for saving the normalization values. 
        The default is {"folder":data,"file":"norm.txt","uumax":0,"vvmax":0,"wwmax":0,"uumin":0,"vvmin":0,
                         "wwmin":0,"uvmax":0,"vwmax":0,"uwmax":0,"uvmin":0,"vwmin":0,"uwmin":0}.
        Data:
            - folder     : folder of the generated data
            - file       : file of the normalization data
            - prod_uumax : maximum energy production
            - turb_uumax : maximum turbulent transport
            - visc_uumax : maximum viscous dissipation
            - pstr_uumax : maximum pressure strain
            - pdis_uumax : maximum pressure dissipation
            - diff_uumax : maximum diffussion
            - conv_uumax : maximum convection
            - prod_uumin : minimum energy production
            - turb_uumin : minimum turbulent transport
            - visc_uumin : minimum viscous dissipation
            - pstr_uumin : minimum pressure strain
            - pdis_uumin : minimum pressure dissipation
            - diff_uumin : minimum diffussion
            - conv_uumin : minimum convection
    Returns
    -------
    None.
    """
    
    # -----------------------------------------------------------------------------------------------------------------
    # Read the data
    # -----------------------------------------------------------------------------------------------------------------
    folder     = str(data_in["folder"])   
    file       = str(data_in["file"])
    prod_uumax = float(data_in["prod_uumax"])
    # turb_uumax = float(data_in["turb_uumax"])
    # visc_uumax = float(data_in["visc_uumax"])
    # pstr_uumax = float(data_in["pstr_uumax"])
    # pdis_uumax = float(data_in["pdis_uumax"])
    # diff_uumax = float(data_in["diff_uumax"])
    # conv_uumax = float(data_in["conv_uumax"])
    prod_uumin = float(data_in["prod_uumin"])
    # turb_uumin = float(data_in["turb_uumin"])
    # visc_uumin = float(data_in["visc_uumin"])
    # pstr_uumin = float(data_in["pstr_uumin"])
    # pdis_uumin = float(data_in["pdis_uumin"])
    # diff_uumin = float(data_in["diff_uumin"])
    # conv_uumin = float(data_in["conv_uumin"])
    
    # -----------------------------------------------------------------------------------------------------------------
    # Save the data to a file
    # -----------------------------------------------------------------------------------------------------------------
    file_norm = folder+'/'+file
    file_save = open(file_norm, "w+")           
    content   = str(prod_uumax)+'\n'
    file_save.write(content)          
    # content   = str(turb_uumax)+'\n'
    # file_save.write(content)          
    # content   = str(visc_uumax)+'\n'
    # file_save.write(content)          
    # content   = str(pstr_uumax)+'\n'
    # file_save.write(content)          
    # content   = str(pdis_uumax)+'\n'
    # file_save.write(content)          
    # content   = str(diff_uumax)+'\n'
    # file_save.write(content)          
    # content   = str(conv_uumax)+'\n'
    # file_save.write(content)         
    content   = str(prod_uumin)+'\n'
    file_save.write(content)          
    # content   = str(turb_uumin)+'\n'
    # file_save.write(content)          
    # content   = str(visc_uumin)+'\n'
    # file_save.write(content)          
    # content   = str(pstr_uumin)+'\n'
    # file_save.write(content)          
    # content   = str(pdis_uumin)+'\n'
    # file_save.write(content)          
    # content   = str(diff_uumin)+'\n'
    # file_save.write(content)          
    # content   = str(conv_uumin)+'\n'
    # file_save.write(content) 
    

def read_norm(data_in={"folder":"Data","file":"norm.txt"}):
    """
    .....................................................................................................................
    # read_norm: function for reading the normalization file. The function reads the maximum and minimum values
                 of the velocity components and stress components
    .....................................................................................................................
    Parameters
    ----------
    data_in : dict, optional
        Data for the normalization of the velocity data. 
        The default is {folder:"Data",file:"norm.txt"}.
        Data:
            - folder : folder to read the data
            - file   : file to read the data

    Returns
    -------
    dict
        Data of the maximum and minimum values for the normalization.
        Data:
            - prod_uumax : maximum energy production
            - turb_uumax : maximum turbulent transport
            - visc_uumax : maximum viscous dissipation
            - pstr_uumax : maximum pressure strain
            - pdis_uumax : maximum pressure dissipation
            - diff_uumax : maximum diffussion
            - conv_uumax : maximum convection
            - prod_uumin : minimum energy production
            - turb_uumin : minimum turbulent transport
            - visc_uumin : minimum viscous dissipation
            - pstr_uumin : minimum pressure strain
            - pdis_uumin : minimum pressure dissipation
            - diff_uumin : minimum diffussion
            - conv_uumin : minimum convection

    """
    # -----------------------------------------------------------------------------------------------------------------
    # Read the data
    # -----------------------------------------------------------------------------------------------------------------
    folder = str(data_in["folder"]) # folder to read the normalization data
    file   = str(data_in["file"])   # file to read the normalization data
    
    # -----------------------------------------------------------------------------------------------------------------
    # Read the normalization file
    # -----------------------------------------------------------------------------------------------------------------
    file_norm = folder+'/'+file
    file_read = open(file_norm,"r")
    prod_uumax = np.array(file_read.readline().replace('[','').replace(']','').split(','),dtype='float')
    # turb_uumax = np.array(file_read.readline().replace('[','').replace(']','').split(','),dtype='float')
    # visc_uumax = np.array(file_read.readline().replace('[','').replace(']','').split(','),dtype='float')
    # pstr_uumax = np.array(file_read.readline().replace('[','').replace(']','').split(','),dtype='float')
    # pdis_uumax = np.array(file_read.readline().replace('[','').replace(']','').split(','),dtype='float')
    # diff_uumax = np.array(file_read.readline().replace('[','').replace(']','').split(','),dtype='float')
    # conv_uumax = np.array(file_read.readline().replace('[','').replace(']','').split(','),dtype='float')
    prod_uumin = np.array(file_read.readline().replace('[','').replace(']','').split(','),dtype='float')
    # turb_uumin = np.array(file_read.readline().replace('[','').replace(']','').split(','),dtype='float')
    # visc_uumin = np.array(file_read.readline().replace('[','').replace(']','').split(','),dtype='float')
    # pstr_uumin = np.array(file_read.readline().replace('[','').replace(']','').split(','),dtype='float')
    # pdis_uumin = np.array(file_read.readline().replace('[','').replace(']','').split(','),dtype='float')
    # diff_uumin = np.array(file_read.readline().replace('[','').replace(']','').split(','),dtype='float')
    # conv_uumin = np.array(file_read.readline().replace('[','').replace(']','').split(','),dtype='float')
    data_out = {"prod_uumax":prod_uumax,"prod_uumin":prod_uumin}#,"turb_uumax":turb_uumax,"visc_uumax":visc_uumax,"pstr_uumax":pstr_uumax,
                # "pdis_uumax":pdis_uumax,"diff_uumax":diff_uumax,"conv_uumax":conv_uumax,"prod_uumin":prod_uumin,
                # "turb_uumin":turb_uumin,"visc_uumin":visc_uumin,"pstr_uumin":pstr_uumin,"pdis_uumin":pdis_uumin,
                # "diff_uumin":diff_uumin,"conv_uumin":conv_uumin}
    return data_out

               
def calc_norm(data_in={"field_ini":1000,"field_fin":9999,"data_folder":"Data",
                       "dx":1,"dy":1,"dz":1,"folder":"../../P125_21pi_vu","file":"P125_21pi_vu.$INDEX$.h5.uvw",
                       "shpx":192,"shpy":201,"shpz":96,"save_file":True,"norm_file":"norm.txt"}):
    """
    .....................................................................................................................
    # calc_norm: function to calculate the normalization of the turbulent budget. The function calculates the maximum  
                 and minimum values of the turbulent budget components and stress components
    .....................................................................................................................
    Parameters
    ----------
    data_in : dict, optional
        Data for normalizing the velocity.
        The default is {"field_ini":1000,"field_fin":9999,"data_folder":"Data",
                        "dx":1,"dy":1,"dz":1,"folder":"../P125_21pi_vu","file":"P125_21pi_vu.$INDEX$.h5.uvw",
                        "shpx":192,"shpy":201,"shpz":96,"padding":15,"save_file":True,"norm_file":"norm.txt"}.
        Data:
            - field_ini   : initial field of the data to calculate the normalization
            - field_fin   : final field of the data to calculate the normalization
            - data_folder : folder to store the data calculated by the code
            - dx          : downsampling of x direction
            - dy          : downsampling of y direction
            - dz          : downsampling of z direction
            - folder      : folder of the turbulent budget data
            - file        : file of the turbulent budget data without index
            - shpx        : shape of the tensor in x
            - shpy        : shape of the tensor in y
            - shpz        : shape of the tensor in z
            - save_file   : flag to save the normalization in a file
            - norm_file   : file of the normalization data
            

    Returns
    -------
    dict
        Data for the normalization. Only returns it in case of not saving a file
        Data:
            - prod_uumax : maximum energy production
            - turb_uumax : maximum turbulent transport
            - visc_uumax : maximum viscous dissipation
            - pstr_uumax : maximum pressure strain
            - pdis_uumax : maximum pressure dissipation
            - diff_uumax : maximum diffussion
            - conv_uumax : maximum convection
            - prod_uumin : minimum energy production
            - turb_uumin : minimum turbulent transport
            - visc_uumin : minimum viscous dissipation
            - pstr_uumin : minimum pressure strain
            - pdis_uumin : minimum pressure dissipation
            - diff_uumin : minimum diffussion
            - conv_uumin : minimum convection
    """
    # -----------------------------------------------------------------------------------------------------------------
    # Import packages
    # -----------------------------------------------------------------------------------------------------------------
    from py_bin.py_functions.read_tb import read_tb
    
    # -----------------------------------------------------------------------------------------------------------------
    # Read the data
    # -----------------------------------------------------------------------------------------------------------------
    field_ini   = int(data_in["field_ini"])
    field_fin   = int(data_in["field_fin"])  
    data_folder = str(data_in["data_folder"]) 
    folder      = str(data_in["folder"])      
    file        = str(data_in["file"])      
    dx          = int(data_in["dx"])      
    dy          = int(data_in["dy"])   
    dz          = int(data_in["dz"])       
    shpx        = int(data_in["shpx"])    
    shpy        = int(data_in["shpy"])       
    shpz        = int(data_in["shpz"])       
    save_file   = bool(data_in["save_file"])  
    norm_file   = str(data_in["norm_file"])  
    
    # -----------------------------------------------------------------------------------------------------------------
    # In the loop
    #   - ii : index of the file that we are reading
    # -----------------------------------------------------------------------------------------------------------------
    for ii in range(field_ini,field_fin):
        data_tb      = {"folder":folder,"file":file,"index":ii,"dx":dx,"dy":dy,"dz":dz,"shpx":shpx,
                        "shpy":shpy,"shpz":shpz,"padding":0,"data_folder":data_folder}            
        data_read_tb = read_tb(data_tb)
        prod_uui0    = np.array(data_read_tb["prod_uu"],dtype="float")
        # turb_uui0    = np.array(data_read_tb["turb_uu"],dtype="float")
        # visc_uui0    = np.array(data_read_tb["visc_uu"],dtype="float")
        # pstr_uui0    = np.array(data_read_tb["pstr_uu"],dtype="float")
        # pdis_uui0    = np.array(data_read_tb["pdis_uu"],dtype="float")
        # diff_uui0    = np.array(data_read_tb["diff_uu"],dtype="float")
        # conv_uui0    = np.array(data_read_tb["conv_uu"],dtype="float")
        if ii == field_ini:
            prod_uumax = np.max(prod_uui0)
            # turb_uumax = np.max(turb_uui0)
            # visc_uumax = np.max(visc_uui0)
            # pstr_uumax = np.max(pstr_uui0)
            # pdis_uumax = np.max(pdis_uui0)
            # diff_uumax = np.max(diff_uui0)
            # conv_uumax = np.max(conv_uui0)
            prod_uumin = np.min(prod_uui0)
            # turb_uumin = np.min(turb_uui0)
            # visc_uumin = np.min(visc_uui0)
            # pstr_uumin = np.min(pstr_uui0)
            # pdis_uumin = np.min(pdis_uui0)
            # diff_uumin = np.min(diff_uui0)
            # conv_uumin = np.min(conv_uui0)
        else:
            prod_uumax = np.max([prod_uumax,np.max(prod_uui0)])
            # turb_uumax = np.max([turb_uumax,np.max(turb_uui0)])
            # visc_uumax = np.max([visc_uumax,np.max(visc_uui0)])
            # pstr_uumax = np.max([pstr_uumax,np.max(pstr_uui0)])
            # pdis_uumax = np.max([pdis_uumax,np.max(pdis_uui0)])
            # diff_uumax = np.max([diff_uumax,np.max(diff_uui0)])
            # conv_uumax = np.max([conv_uumax,np.max(conv_uui0)])
            prod_uumin = np.min([prod_uumin,np.min(prod_uui0)])
            # turb_uumin = np.min([turb_uumin,np.min(turb_uui0)])
            # visc_uumin = np.min([visc_uumin,np.min(visc_uui0)])
            # pstr_uumin = np.min([pstr_uumin,np.min(pstr_uui0)])
            # pdis_uumin = np.min([pdis_uumin,np.min(pdis_uui0)])
            # diff_uumin = np.min([diff_uumin,np.min(diff_uui0)])
            # conv_uumin = np.min([conv_uumin,np.min(conv_uui0)])
            
    # -----------------------------------------------------------------------------------------------------------------
    # Save the normalization in a file or return the values of the normalization
    # -----------------------------------------------------------------------------------------------------------------
    if save_file:
        data_norm_save = {"folder":data_folder,"file":norm_file,"prod_uumax":prod_uumax,"prod_uumin":prod_uumin}#,"turb_uumax":turb_uumax,
                          # "visc_uumax":visc_uumax,"pstr_uumax":pstr_uumax,"pdis_uumax":pdis_uumax,
                          # "diff_uumax":diff_uumax,"conv_uumax":conv_uumax,"prod_uumin":prod_uumin,
                          # "turb_uumin":turb_uumin,"visc_uumin":visc_uumin,"pstr_uumin":pstr_uumin,
                          # "pdis_uumin":pdis_uumin,"diff_uumin":diff_uumin,"conv_uumin":conv_uumin}
        save_norm(data_in=data_norm_save)
    else:
        data_out = {"prod_uumax":prod_uumax,"prod_uumin":prod_uumin}#,"turb_uumax":turb_uumax,"visc_uumax":visc_uumax,"pstr_uumax":pstr_uumax,
                    # "pdis_uumax":pdis_uumax,"diff_uumax":diff_uumax,"conv_uumax":conv_uumax,"prod_uumin":prod_uumin,
                    # "turb_uumin":turb_uumin,"visc_uumin":visc_uumin,"pstr_uumin":pstr_uumin,"pdis_uumin":pdis_uumin,
                    # "diff_uumin":diff_uumin,"conv_uumin":conv_uumin}
        return data_out
    
        