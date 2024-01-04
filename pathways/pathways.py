import matplotlib.pyplot as plt
import pandas as pd

# Table to store pathways information
paths = pd.DataFrame({
    "ID": ["CA 1", "CA 2", "CA 3", "CA 4", "CA 5", "CIN-ALD"],
    "Reaction": ["Malanic Acid + Benzaldehyde --> Cinnamic Acid ",
                  "Bromobenzene + Acrylic Acid --> Cinnamic Acid",
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
mol = pd.DataFrame({
    "ID": ["Mol 1", "Mol 2", "Mol 3", "Mol 4", "Mol 5", "Mol 6", "Mol 7", "Mol 8"],

    "Name": ["Benzaldehyde", "Cinnamic Acid",
             "Malanic Acid", "Acrylic Acid",
             "Brombenzene", "Iodobenzene",
             "Cinnamon Alcohol", "L-Phenylalanine",
             "Acetic anhydride"],

    "Price (per Kg or Liter)": ["45.60 € l", "152.00 € kg",
                                "120.00 € kg", "111.00 € kg",
                                "115.00 € kg", "269.00 € 0.25 l",
                                "61.90 € 0.5 kg", "717.00 € kg",
                                "47.20 € l"]
})


font_size1 = 6
pdf_filename1 = 'molecule_table.pdf'
fig, ax = plt.subplots(figsize=(4, 8))
ax.axis('off')
table1 = ax.table(cellText=mol.values, colLabels=mol.columns, cellLoc='center', loc='center', fontsize=font_size2)
table1.auto_set_font_size(False)
table1.set_fontsize(font_size1)
plt.savefig(pdf_filename1, format='pdf', bbox_inches='tight')
plt.close()




reaction = pd.DataFrame({

    "Reaction": ["Benzaldehyde + Acetic anhydride -> Cinnamic acid",
                  "Benzaldehyde + Malonic Acid --> Cinnamic Acid ",
                  "Bromobenzene + Acrylic Acid --> Cinnamic Acid",
                  "Iodobenzene + Acrylic Acid  --> Cinnamic Acid",
                  "Cinnamon Alcohol --> Cinnamic Acid",
                  "L-Phenylalanine --> Cinnamic Acid",
                  "Cinnamic Acid --> Cinnamaldehyde"],

    "Price": ["45.60 + 47.20 = 92.8", "45.60 + 120 = 165.60", "115 + 111 = 226",
              "(269*4) + 111 = 1187", "123.8", "717", "152"]

})


font_size2 = 6
pdf_filename2 = 'rprice.pdf'
fig, ax = plt.subplots(figsize=(4, 8))
ax.axis('off')
table2 = ax.table(cellText=reaction.values, colLabels=reaction.columns, cellLoc='center', loc='center', fontsize=font_size2)
table2.auto_set_font_size(False)
table2.set_fontsize(font_size2)
plt.savefig(pdf_filename2, format='pdf', bbox_inches='tight')
plt.close()


