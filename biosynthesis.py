import pandas as pd

pd.set_option('display.max_columns', None)

reaction = pd.DataFrame({
    "Reaction Id": ["R-1",
                    "R-2",
                    "R-3",
                    "R-4",
                    "R-5",
                    "R-6",
                    "R-7",
                    "R-8",
                    "R-9"],

    "Reaction": ["Glucose + ATP -> Glucose 6-phosphate + ADP",
                 "Glucose 6-phosphate <-> Fructose 6-phosphate",
                 "Fructose 6-phosphate + ATP -> Fructose 1,6-bisphosphate + ADP",
                 "Fructose 6-phosphate <-> Glyseraldehhyde 3-phosphate + Dehydroxyacetone phosphate",
                 "Phosphoenolpiruvate + H2O <-> 2-Phosphoglycerate",
                 "2-Phosphoglycerate <-> 3-Phosphoglycerate",
                 "3-Phosphoglycerate + ATP <-> 1,3-Phosphoglycerate + ADP",
                 "1,3-Phosphoglycerate + NADH + H⁺ <-> Glyseraldehhyde 3-phosphate + Pi",
                 "Glyseraldehhyde 3-phosphate  <-> Dehydroxyacetone phosphate"
                 ],

    "Enzyme": ["Hexokinase",
               "Phosphohexose isomerase",
               "Phosphofructokinase-1",
               "Aldolase",
               "Enolase",
               "Phosphoglycerate mutase",
               "Phosphoglycerate kinase",
               "Glyceraldehyde 3-phosphate dehydrognase ",
               "Triose phosphate isomerase"
               ],

    "Energy Consumption": ["1 ATP (ATP -> ADP)",
                           None,
                           "1 ATP (ATP -> ADP)",
                           None,
                           None,
                           None,
                           "1 ATP",
                           "1 NADH",
                           None
                           ],

    "Pathway": ["Glycolysis (preparatory phase)",
                "Glycolysis (preparatory phase)",
                "Glycolysis (preparatory phase)",
                "Glycolysis (preparatory phase)",
                "Gluconeogenesis",
                "Gluconeogenesis",
                "Gluconeogenesis",
                "Gluconeogenesis",
                "Gluconeogenesis"
                ],

    "Description": ["Phosphorylation of Glucose on carbon 6",
                    "Isomerization moves the carbonyl-group to C-2",
                    "Phosphorylation of Fructose 6-phosphate on C-1",
                    "Cleavage of 6-carbon phosphate sugar to two 3-carbon phosphate carbon",
                    "Hydration",
                    None,
                    None,
                    None,
                    None
                    ]
})


print(reaction)