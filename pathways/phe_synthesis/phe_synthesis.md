```python
import pandas as pd
pd.set_option('display.max_columns', None)
```


```python
reaction = pd.DataFrame({
    "Reaction Id": ["R-1", "R-2", "R-3", "R-4", "R-5", "R-6", "R-7", "R-8", "R-9", "R-10", "R-11", "R-12", "R-13",
                    "R-14", "R-15", "R-16", "R-17", "R-18", "R-19", "R-20", "R-21"],

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
                 "Phenylpyruvate + CO2 + H2O -> L-Phenylalanine"
                 ],

    "Enzyme": ["Hexokinase", "Phosphohexose isomerase", "Phosphofructokinase-1", "Aldolase", "Enolase",
               "Phosphoglycerate mutase", "Phosphoglycerate kinase", "Glyceraldehyde 3-phosphate dehydrognase ",
               "Triose phosphate isomerase", "Transketolase", "Transaldolase",
               "2-keto-3-deohy-D-arabinoheptulosonate 7-phosphate synthase", "Dehydroquinate synthase",
               "3-dehydroquinate dehydratase", "Shikomate dehydrogenase", "Shikimate kinase",
               "5-Enolpyruvylshikomate 3-phosphate synthase", "Chorismate synthase", "chorismate mutase",
               "prephenate dehydratase", "Aromatic aminotransferase"],

    "Energy Consumption": ["1 ATP (ATP -> ADP)", None, "1 ATP (ATP -> ADP)", None, None, None, "1 ATP", "1 NADH",
                           None, None, None, None, "NADH", None, "NADPH", "ATP", None, None, None, None, None],

    "Pathway": ["Glycolysis (preparatory phase)", "Glycolysis (preparatory phase)",
                "Glycolysis (preparatory phase)", "Glycolysis (preparatory phase)",
                "Gluconeogenesis", "Gluconeogenesis", "Gluconeogenesis", "Gluconeogenesis", "Gluconeogenesis",
                "Pentose phosphate", "Pentose phosphate", "Shikimate", "Shikimate", "Shikimate", "Shikimate",
                "Shikimate", "Shikimate", "Shikimate", "Shikimate", "Shikimate", "Shikimate"],

    "Description": ["Phosphorylation of Glucose on carbon 6", "Isomerization moves the carbonyl-group to C-2",
                    "Phosphorylation of Fructose 6-phosphate on C-1",
                    "Cleavage of 6-carbon phosphate sugar to two 3-carbon phosphate carbon",
                    "Hydration", None, None, None, None, None, None, None, None, None, None,
                    None, None, None, None, None, None]
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
    <tr>
      <th>9</th>
      <td>R-10</td>
      <td>Xylulose 5-phosphate -&gt; Glyceraldehyde 3-phosp...</td>
      <td>Transketolase</td>
      <td>None</td>
      <td>Pentose phosphate</td>
      <td>None</td>
    </tr>
    <tr>
      <th>10</th>
      <td>R-11</td>
      <td>Glyceraldehyde 3-phosphate -&gt; Erythrose 4-phos...</td>
      <td>Transaldolase</td>
      <td>None</td>
      <td>Pentose phosphate</td>
      <td>None</td>
    </tr>
    <tr>
      <th>11</th>
      <td>R-12</td>
      <td>Erythrose 4-phosphate + Phosphoenolpiruvate + ...</td>
      <td>2-keto-3-deohy-D-arabinoheptulosonate 7-phosph...</td>
      <td>None</td>
      <td>Shikimate</td>
      <td>None</td>
    </tr>
    <tr>
      <th>12</th>
      <td>R-13</td>
      <td>2-keto-3-deohy-D-arabinoheptulosonate 7-phosph...</td>
      <td>Dehydroquinate synthase</td>
      <td>NADH</td>
      <td>Shikimate</td>
      <td>None</td>
    </tr>
    <tr>
      <th>13</th>
      <td>R-14</td>
      <td>3-Dehydroquinate -&gt; 3-Dehxdroshikimate + H2O</td>
      <td>3-dehydroquinate dehydratase</td>
      <td>None</td>
      <td>Shikimate</td>
      <td>None</td>
    </tr>
    <tr>
      <th>14</th>
      <td>R-15</td>
      <td>3-Dehxdroshikimate + NAHPH + H⁺ -&gt; Shikimate +...</td>
      <td>Shikomate dehydrogenase</td>
      <td>NADPH</td>
      <td>Shikimate</td>
      <td>None</td>
    </tr>
    <tr>
      <th>15</th>
      <td>R-16</td>
      <td>Shikimate + ATP -&gt; Shikimate 3-phosphate + ADP</td>
      <td>Shikimate kinase</td>
      <td>ATP</td>
      <td>Shikimate</td>
      <td>None</td>
    </tr>
    <tr>
      <th>16</th>
      <td>R-17</td>
      <td>Shikimate 3-phosphate + Phosphoenolpiruvate -&gt;...</td>
      <td>5-Enolpyruvylshikomate 3-phosphate synthase</td>
      <td>None</td>
      <td>Shikimate</td>
      <td>None</td>
    </tr>
    <tr>
      <th>17</th>
      <td>R-18</td>
      <td>5-Enolpyruvylshikomate 3-phosphate -&gt; Chorisma...</td>
      <td>Chorismate synthase</td>
      <td>None</td>
      <td>Shikimate</td>
      <td>None</td>
    </tr>
    <tr>
      <th>18</th>
      <td>R-19</td>
      <td>Chorismate -&gt; Prephenate</td>
      <td>chorismate mutase</td>
      <td>None</td>
      <td>Shikimate</td>
      <td>None</td>
    </tr>
    <tr>
      <th>19</th>
      <td>R-20</td>
      <td>Prephenate -&gt; Phenylpyruvate</td>
      <td>prephenate dehydratase</td>
      <td>None</td>
      <td>Shikimate</td>
      <td>None</td>
    </tr>
    <tr>
      <th>20</th>
      <td>R-21</td>
      <td>Phenylpyruvate + CO2 + H2O -&gt; L-Phenylalanine</td>
      <td>Aromatic aminotransferase</td>
      <td>None</td>
      <td>Shikimate</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>


