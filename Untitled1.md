```python
import pandas as pd
pd.set_option('display.max_columns', None)
```


```python
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

reaction
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Reaction Id</th>
      <th>Reaction</th>
      <th>Enzyme</th>
      <th>Energy Consumption</th>
      <th>Pathway</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>R-1</td>
      <td>Glucose + ATP -&gt; Glucose 6-phosphate + ADP</td>
      <td>Hexokinase</td>
      <td>1 ATP (ATP -&gt; ADP)</td>
      <td>Glycolysis (preparatory phase)</td>
      <td>Phosphorylation of Glucose on carbon 6</td>
    </tr>
    <tr>
      <th>1</th>
      <td>R-2</td>
      <td>Glucose 6-phosphate &lt;-&gt; Fructose 6-phosphate</td>
      <td>Phosphohexose isomerase</td>
      <td>None</td>
      <td>Glycolysis (preparatory phase)</td>
      <td>Isomerization moves the carbonyl-group to C-2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>R-3</td>
      <td>Fructose 6-phosphate + ATP -&gt; Fructose 1,6-bis...</td>
      <td>Phosphofructokinase-1</td>
      <td>1 ATP (ATP -&gt; ADP)</td>
      <td>Glycolysis (preparatory phase)</td>
      <td>Phosphorylation of Fructose 6-phosphate on C-1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>R-4</td>
      <td>Fructose 6-phosphate &lt;-&gt; Glyseraldehhyde 3-pho...</td>
      <td>Aldolase</td>
      <td>None</td>
      <td>Glycolysis (preparatory phase)</td>
      <td>Cleavage of 6-carbon phosphate sugar to two 3-...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>R-5</td>
      <td>Phosphoenolpiruvate + H2O &lt;-&gt; 2-Phosphoglycerate</td>
      <td>Enolase</td>
      <td>None</td>
      <td>Gluconeogenesis</td>
      <td>Hydration</td>
    </tr>
    <tr>
      <th>5</th>
      <td>R-6</td>
      <td>2-Phosphoglycerate &lt;-&gt; 3-Phosphoglycerate</td>
      <td>Phosphoglycerate mutase</td>
      <td>None</td>
      <td>Gluconeogenesis</td>
      <td>None</td>
    </tr>
    <tr>
      <th>6</th>
      <td>R-7</td>
      <td>3-Phosphoglycerate + ATP &lt;-&gt; 1,3-Phosphoglycer...</td>
      <td>Phosphoglycerate kinase</td>
      <td>1 ATP</td>
      <td>Gluconeogenesis</td>
      <td>None</td>
    </tr>
    <tr>
      <th>7</th>
      <td>R-8</td>
      <td>1,3-Phosphoglycerate + NADH + H⁺ &lt;-&gt; Glyserald...</td>
      <td>Glyceraldehyde 3-phosphate dehydrognase</td>
      <td>1 NADH</td>
      <td>Gluconeogenesis</td>
      <td>None</td>
    </tr>
    <tr>
      <th>8</th>
      <td>R-9</td>
      <td>Glyseraldehhyde 3-phosphate  &lt;-&gt; Dehydroxyacet...</td>
      <td>Triose phosphate isomerase</td>
      <td>None</td>
      <td>Gluconeogenesis</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>


