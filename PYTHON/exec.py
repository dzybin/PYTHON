import os

chemin = "/mnt/nfs/homes/dzybin/Documents/PYTHON"
dossier = os.path.join(chemin, "new_dir", "branch_dir")
os.makedirs(dossier)