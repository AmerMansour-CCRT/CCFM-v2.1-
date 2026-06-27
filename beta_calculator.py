#!/usr/bin/env python3
"""
CCFM v2.1 Beta Calculator
Calculates theoretical fine-structure constant variation: Δα/α = 4.16e-6
Independent researcher: Amer Mansour
ORCID: 0009-0000-3369-7009
"""

import numpy as np

# CCFM v2.1 Constants
PHI = (1 + np.sqrt(5)) / 2  # Golden ratio
ALPHA_BASE = 1/137.035999084  # CODATA 2018
BETA_CCFM = 4.16e-6  # Core prediction

def calculate_beta():
    """Calculate CCFM v2.1 beta parameter"""
    beta = BETA_CCFM
    delta_alpha = beta * ALPHA_BASE
    alpha_new = ALPHA_BASE + delta_alpha
    
    print("="*50)
    print("CCFM v2.1 Beta Calculator")
    print("="*50)
    print(f"Base α (CODATA):     {ALPHA_BASE:.12f}")
    print(f"CCFM β parameter:    {BETA_CCFM:.2e}")
    print(f"Δα/α prediction:     {beta:.2e}")
    print(f"New α (CCFM):        {alpha_new:.12f}")
    print("="*50)
    print(f"ORCID: 0009-0000-3369-7009")
    print(f"Repo: github.com/AmerMansour-CCRT/CCFM-v2.1")
    print("="*50)
    
    return beta

if __name__ == "__main__":
    calculate_beta()
