import pickle
from rich import print as pprint

smile = '[C]1[C]CN=CN[CH][N]C1'
smile = 'C[C@@]12[C@H](O)[C@H]3CCN1[C@H]32'
# Specify the path to the pickle file
file_path = '/home/sehmimul/torsional-diffusion/QM9/qm9/' + smile + '.pickle'

# Open and load the pickle file
with open(file_path, 'rb') as file:  # 'rb' mode is for reading binary files
    data = pickle.load(file)

# Display the content
pprint(data)
molecule = data['conformers'][2]['rd_mol']
pprint("molecule is {}".format(molecule))
pprint("molecule conformer is {}".format(molecule.GetConformers()))
for i, conf in enumerate(molecule.GetConformers()):
    pprint("i is {} and conformer position is \n{}\n".format(i, conf.GetPositions()))
    # if i == 2:
    #     molecule.RemoveConformer(conf.GetId())


# Iterate over bonds in the molecule
for bond in molecule.GetBonds():
    # Get bond features
    bond_type = bond.GetBondType()  # Bond type (e.g., SINGLE, DOUBLE, etc.)
    begin_atom_idx = bond.GetBeginAtomIdx()  # Index of the first atom in the bond
    end_atom_idx = bond.GetEndAtomIdx()      # Index of the second atom in the bond
    is_aromatic = bond.GetIsAromatic()       # Check if the bond is aromatic

    # Print bond information
    pprint(f"Bond between atom {begin_atom_idx} and {end_atom_idx}")
    pprint(f"  Bond type: {bond_type}")
    pprint(f"  Is aromatic: {is_aromatic}\n")


for atom in molecule.GetAtoms():
    atom_idx = atom.GetIdx()  # Index of the atom
    atom_symbol = atom.GetSymbol()  # Element symbol (e.g., C, O, H)
    atom_mass = atom.GetMass()  # Atomic mass
    atom_degree = atom.GetDegree()  # Number of directly bonded neighbors
    atom_hybridization = atom.GetHybridization()  # Hybridization state
    is_aromatic = atom.GetIsAromatic()  # Whether the atom is aromatic

    # Print atom information
    pprint(f"Atom Index: {atom_idx}, Symbol: {atom_symbol}, Mass: {atom_mass}, "
            f"Degree: {atom_degree}, Hybridization: {atom_hybridization}, Aromatic: {is_aromatic}")
