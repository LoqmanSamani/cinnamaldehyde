import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', 1)

reaction = pd.DataFrame({
    "Reaction Id": ["R-1", "R-2", "R-3", "R-4", "R-5", "R-6", "R-7", "R-8", "R-9", "R-10", "R-11", "R-12", "R-13",
                    "R-14", "R-15", "R-16", "R-17", "R-18", "R-19", "R-20", "R-21", "R-22", "R-23"],

    "Reaction": ["Glucose + ATP -> Glucose 6-phosphate + ADP",
                 "Glucose 6-phosphate <-> Fructose 6-phosphate",
                 "Fructose 6-phosphate + ATP -> Fructose 1,6-bisphosphate + ADP",
                 "Fructose 6-phosphate <-> Glyseraldehhyde 3-phosphate + Dehydroxyacetone phosphate",
                 "Phosphoenolpiruvate + H2O <-> 2-Phosphoglycerate",
                 "2-Phosphoglycerate <-> 3-Phosphoglycerate",
                 "3-Phosphoglycerate + ATP <-> 1,3-Phosphoglycerate + ADP",
                 "1,3-Phosphoglycerate + NADH + H⁺ <-> Glyseraldehhyde 3-phosphate + Pi",
                 "Glyseraldehhyde 3-phosphate  <-> Dehydroxyacetone phosphate",
                 "Xylulose 5-phosphate -> Glyceraldehyde 3-phosphate",
                 "Glyceraldehyde 3-phosphate -> Erythrose 4-phosphate",
                 "Erythrose 4-phosphate + Phosphoenolpiruvate + H2O -> 2-keto-3-deohy-D-arabinoheptulosonate 7-phosphate + Pi",
                 "2-keto-3-deohy-D-arabinoheptulosonate 7-phosphate NADH + H⁺ -> 3-Dehydroquinate + Pi + NAD⁺",
                 "3-Dehydroquinate -> 3-Dehxdroshikimate + H2O",
                 "3-Dehxdroshikimate + NAHPH + H⁺ -> Shikimate + NADP⁺",
                 "Shikimate + ATP -> Shikimate 3-phosphate + ADP",
                 "Shikimate 3-phosphate + Phosphoenolpiruvate -> 5-Enolpyruvylshikomate 3-phosphate + Pi",
                 "5-Enolpyruvylshikomate 3-phosphate -> Chorismate + Pi",
                 "Chorismate -> Prephenate",
                 "Prephenate -> Phenylpyruvate",
                 "Phenylpyruvate + CO2 + H2O -> L-Phenylalanine",
                 "L-phenylalanine -> trans-cinnamic acid + NH3",
                 "trans-cinnamic acid + NADPH + H⁺ + ATP -> Cinnamaldehyde + AMP + NADP⁺"
                 ],

    "Enzyme": ["Hexokinase", "Phosphohexose isomerase", "Phosphofructokinase-1", "Aldolase", "Enolase",
               "Phosphoglycerate mutase", "Phosphoglycerate kinase", "Glyceraldehyde 3-phosphate dehydrognase ",
               "Triose phosphate isomerase", "Transketolase", "Transaldolase",
               "2-keto-3-deohy-D-arabinoheptulosonate 7-phosphate synthase", "Dehydroquinate synthase",
               "3-dehydroquinate dehydratase", "Shikomate dehydrogenase", "Shikimate kinase",
               "5-Enolpyruvylshikomate 3-phosphate synthase", "Chorismate synthase", "chorismate mutase",
               "prephenate dehydratase", "Aromatic aminotransferase", "L-phenylalanine ammonia-lyase",
               "carboxylic acid reductase (CAR), PPTase"],

    "Energy Consumption": ["1 ATP (ATP -> ADP)", None, "1 ATP (ATP -> ADP)", None, None, None, "1 ATP", "1 NADH",
                           None, None, None, None, "NADH", None, "NADPH", "ATP", None, None, None, None, None, None, "2 ATP (ATP -> AMP) & 1 NADPH"],

    "Pathway": ["Glycolysis (preparatory phase)", "Glycolysis (preparatory phase)",
                "Glycolysis (preparatory phase)", "Glycolysis (preparatory phase)",
                "Gluconeogenesis", "Gluconeogenesis", "Gluconeogenesis", "Gluconeogenesis", "Gluconeogenesis",
                "Pentose phosphate", "Pentose phosphate", "Shikimate", "Shikimate", "Shikimate", "Shikimate",
                "Shikimate", "Shikimate", "Shikimate", "Shikimate", "Shikimate", "Shikimate", None, None],

    "Description": ["Phosphorylation of Glucose on carbon 6", "Isomerization moves the carbonyl-group to C-2",
                    "Phosphorylation of Fructose 6-phosphate on C-1",
                    "Cleavage of 6-carbon phosphate sugar to two 3-carbon phosphate carbon",
                    "Hydration", None, None, None, None, None, None, None, None, None, None,
                    None, None, None, None, None, None, None, None]
})

font_size = 4
pdf_filename = 'reaction1.pdf'
fig, ax = plt.subplots(figsize=(28, 8))
ax.axis('off')
table = ax.table(cellText=reaction.values, colLabels=reaction.columns, cellLoc='center', loc='center', fontsize=font_size)
table.auto_set_font_size(False)
table.set_fontsize(font_size)
plt.savefig(pdf_filename, format='pdf', bbox_inches='tight')
plt.close()
