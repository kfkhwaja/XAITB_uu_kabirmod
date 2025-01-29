# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 10:06:28 2024

@author:  Andres Cremades Botella

Data for the training of the model:
    - field_ini    : Initial field of the training
    - field_fin    : Final field of the training
    - field_delta  : Separation between files
    - nsamples     : number of samples used for the calculation of the SHAP values in the Expected Gradients
    - nsamples_max : maximum number of samples loaded in memory for calculating the SHAPs
"""
# ----------------------------------------------------------------------------------------------------------------------
# Fields used in the training
#     - field_ini   : Initial field of the training
#     - field_fin   : Final field of the training
#     - field_delta : Separation between files
# ----------------------------------------------------------------------------------------------------------------------
field_ini   = 7000
field_fin   = 9998
field_delta = 1

# ----------------------------------------------------------------------------------------------------------------------
# Select the number of samples for calculating the SHAP values
#     - nsamples     : number of samples used for the calculation of the SHAP values in the Expected Gradients
#     - nsamples_max : maximum number of samples loaded in memory for calculating the SHAPs
# ----------------------------------------------------------------------------------------------------------------------
nsamples     = 200
nsamples_max = 100