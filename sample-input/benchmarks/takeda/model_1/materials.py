import h5py
import numpy as np

"""
This file writes all of the materials data (multi-group nuclear
cross-sections) for the Takeda
benchmark problem to an HDF5 file. The script uses the h5py Python package
to interact with the HDF5 file format. This may be a good example for those
wishing to write their nuclear data to an HDF5 file to import using the
OpenMOC 'materialize' Python module.
"""

# Create the file to store Takeda multi-groups cross-sections
f = h5py.File('takeda-mgxs.h5')
f.attrs["# groups"] = 2

# Create a group to specify that MGXS are split by material (vs. cell)
material_group = f.create_group('material')


###############################################################################
##################################   core   ###################################
###############################################################################

# Create a subgroup for core materials data
core = material_group.create_group('Core')

# Create a subdictionary for region 1 material data
sigma_t = np.array([0.223775, 1.03864])
sigma_s = np.array([0.192423, 0.0228253, 0.00, 0.880439])
sigma_f = np.array([0.0004, 0.1])
nu_sigma_f = np.array([0.00909319, 0.290183])
chi = np.array([1.0, 0.0])
# takeda_materials['Core']['Absorption XS'] = [0.00852709, 0.158196]

# Create datasets for each cross-section type
core.create_dataset('total', data=sigma_t)
core.create_dataset('scatter matrix', data=sigma_s)
core.create_dataset('fission', data=sigma_f)
core.create_dataset('nu-fission', data=nu_sigma_f)
core.create_dataset('chi', data=chi)


###############################################################################
##################################   reflector  ###############################
###############################################################################

# Create a subgroup for reflector materials data
reflector = material_group.create_group('Reflector')

#takeda_materials['Reflector']['Absorption XS'] = [0.000416392, 0.0202999]
simga_t = np.array([0.250367, 1.64482])
sigma_s = np.array([0.193446, 0.0565042, 0.00, 1.62452])
sigma_f = np.array([0.0, 0.0])
nu_sigma_f = np.array([0.0, 0.0])
chi = np.array([1.0, 0.0])

# Create datasets for each cross-section type
reflector.create_dataset('total', data=sigma_t)
reflector.create_dataset('scatter matrix', data=sigma_s)
reflector.create_dataset('fission', data=sigma_f)
reflector.create_dataset('nu-fission', data=nu_sigma_f)
reflector.create_dataset('chi', data=chi)

###############################################################################
################################   control rod    #############################
###############################################################################

# Create a subgroup for control rod materials data
control_rod = material_group.create_group('Control Rod')

#takeda_materials['Control Rod']['Absorption XS'] = [0.0174439, 0.182224]
sigma_t = np.array([0.0852325, 0.217460])
sigma_s = np.array([0.0677241, 0.0000645461, 0.00, 0.0352358])
sigma_f = np.array([0.0, 0.0])
nu_sigma_f = np.array([0.0, 0.0])
chi = np.array([1.0, 0.0])

# Create datasets for each cross-section type
control_rod.create_dataset('total', data=sigma_t)
control_rod.create_dataset('scatter matrix', data=sigma_s)
control_rod.create_dataset('fission', data=sigma_f)
control_rod.create_dataset('nu-fission', data=nu_sigma_f)
control_rod.create_dataset('chi', data=chi)

###############################################################################
################################       Void       #############################
###############################################################################

# Create a subgroup for control rod materials data
void = material_group.create_group('Void')

#takeda_materials['Void']['Absorption XS'] = [0.0000465132, 0.00132890]
sigma_t = np.array([0.0128407, 0.0120676])
sigma_s = np.array([0.01277, 0.0000240997, 0.00, 0.0107387])
sigma_f = np.array([0.0, 0.0])
nu_sigma_f = np.array([0.0, 0.0])
chi = np.array([1.0, 0.0])

# Create datasets for each cross-section type
void.create_dataset('total', data=sigma_t)
void.create_dataset('scatter matrix', data=sigma_s)
void.create_dataset('fission', data=sigma_f)
void.create_dataset('nu-fission', data=nu_sigma_f)
void.create_dataset('chi', data=chi)

# Close the hdf5 data file
f.close()
