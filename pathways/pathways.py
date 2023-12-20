import matplotlib.pyplot as plt
import pandas as pd

# Table to store pathways information
paths = pd.DataFrame({
    "ID": ["CA 1", "CA 2", "CA 3", "CA 4", "CA 5", "CIN-ALD"],
    "Reaction": ["Molanic Acid + Benzaldehyde --> Cinnamic Acid ",
                  "Bromobenzene + Acrilic Acid --> Cinnamic Acid",
                  "Iodobenzene + Acrilic Acid  --> Cinnamic Acid",
                  "Cinnamon Alcohol --> Cinnamic Acid",
                  "L-Phenylalanine --> Cinnamic Acid",
                  "Cinnamic Acid --> Cinnamaldehyde"],

    "Reagent": ["Piperidine",
                " Tributylamine, "
                "Tetrabutylammonium bromide",
                " Tributylamine",
                None,
                " Potassium carbonate, Oxygen", "ATP, NADPH"],

    "Catalyst": [None,
                 " Palladium",
                 " Troxerutin, Palladium",
                 " Benzoic acid, Platinum, 1H-Imidazolium, 1,3-bis[3-(trimethoxysilyl)propyl]-, chloride",
                 "Phenylalanine Ammonia Lyase",
                 "carboxylic acid reductase (CAR) and phosphoubiquitin transferase(PPTase)"]
})


font_size = 6
pdf_filename = 'reaction_table.pdf'
fig, ax = plt.subplots(figsize=(20, 15))
ax.axis('off')
table = ax.table(cellText=paths.values, colLabels=paths.columns, cellLoc='center', loc='center', fontsize=font_size)
table.auto_set_font_size(False)
table.set_fontsize(font_size)
plt.savefig(pdf_filename, format='pdf', bbox_inches='tight')
plt.close()


# Table to store molecule information
mol = pd.DataFrame({"ID": ["Mol 1", "Mol 2", "Mol 3", "Mol 4", "Mol 5", "Mol 6", "Mol 7", "Mol 8"],

                    "Name": ["Benzaldehyde", "Cinnamic Acid",
                             "Molanic Acid", "Acrilic Acid",
                             "Brombenzene", "Iodobenzene",
                             "Cinnamon Alcohol", "L-Phenylalanine"],

                    "Price (per Kg or Liter)": ["48 € l", "134 € kg",
                                                "128 € kg", "2 € kg",
                                                "76 € kg", "547 € kg",
                                                "85 € kg", "503 € kg"]
                    })


font_size = 6
pdf_filename = 'molecule_table.pdf'
fig, ax = plt.subplots(figsize=(4, 8))
ax.axis('off')
table = ax.table(cellText=mol.values, colLabels=mol.columns, cellLoc='center', loc='center', fontsize=font_size)
table.auto_set_font_size(False)
table.set_fontsize(font_size)
plt.savefig(pdf_filename, format='pdf', bbox_inches='tight')
plt.close()

