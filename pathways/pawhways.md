```python
import matplotlib.pyplot as plt
import pandas as pd
%matplotlib inline
```


```python
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
paths
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
      <th>ID</th>
      <th>Reaction</th>
      <th>Reagent</th>
      <th>Catalyst</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>CA 1</td>
      <td>Malanic Acid + Benzaldehyde --&gt; Cinnamic Acid</td>
      <td>Piperidine</td>
      <td>None</td>
    </tr>
    <tr>
      <th>1</th>
      <td>CA 2</td>
      <td>Bromobenzene + Acrylic Acid --&gt; Cinnamic Acid</td>
      <td>Tributylamine, Tetrabutylammonium bromide</td>
      <td>Palladium</td>
    </tr>
    <tr>
      <th>2</th>
      <td>CA 3</td>
      <td>Iodobenzene + Acrilic Acid  --&gt; Cinnamic Acid</td>
      <td>Tributylamine</td>
      <td>Troxerutin, Palladium</td>
    </tr>
    <tr>
      <th>3</th>
      <td>CA 4</td>
      <td>Cinnamon Alcohol --&gt; Cinnamic Acid</td>
      <td>None</td>
      <td>Benzoic acid, Platinum, 1H-Imidazolium, 1,3-b...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>CA 5</td>
      <td>L-Phenylalanine --&gt; Cinnamic Acid</td>
      <td>Potassium carbonate, Oxygen</td>
      <td>Phenylalanine Ammonia Lyase</td>
    </tr>
    <tr>
      <th>5</th>
      <td>CIN-ALD</td>
      <td>Cinnamic Acid --&gt; Cinnamaldehyde</td>
      <td>ATP, NADPH</td>
      <td>carboxylic acid reductase (CAR) and phosphoubi...</td>
    </tr>
  </tbody>
</table>
</div>




```python
mol = pd.DataFrame({
    "ID": ["Mol 1", "Mol 2", "Mol 3", "Mol 4", "Mol 5", "Mol 6", "Mol 7", "Mol 8", "Mol 9"],

    "Name": ["Benzaldehyde", "Cinnamic Acid", "Malanic Acid", "Acrylic Acid",
             "Brombenzene", "Iodobenzene", "Cinnamon Alcohol", "L-Phenylalanine",
                             "Acetic anhydride"],

    "Price (per Kg or Liter)": ["45.60 € l", "152.00 € kg", "120.00 € kg", "111.00 € kg",
                                "115.00 € kg", "269.00 € 0.25 l", "61.90 € 0.5 kg", "717.00 € kg",
                                "47.20 € l"]
})

mol
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
      <th>ID</th>
      <th>Name</th>
      <th>Price (per Kg or Liter)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Mol 1</td>
      <td>Benzaldehyde</td>
      <td>45.60 € l</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Mol 2</td>
      <td>Cinnamic Acid</td>
      <td>152.00 € kg</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Mol 3</td>
      <td>Malanic Acid</td>
      <td>120.00 € kg</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Mol 4</td>
      <td>Acrylic Acid</td>
      <td>111.00 € kg</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Mol 5</td>
      <td>Brombenzene</td>
      <td>115.00 € kg</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Mol 6</td>
      <td>Iodobenzene</td>
      <td>269.00 € 0.25 l</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Mol 7</td>
      <td>Cinnamon Alcohol</td>
      <td>61.90 € 0.5 kg</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Mol 8</td>
      <td>L-Phenylalanine</td>
      <td>717.00 € kg</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Mol 9</td>
      <td>Acetic anhydride</td>
      <td>47.20 € l</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
      <th>Reaction</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Benzaldehyde + Acetic anhydride -&gt; Cinnamic acid</td>
      <td>45.60 + 47.20 = 92.8</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Benzaldehyde + Malonic Acid --&gt; Cinnamic Acid</td>
      <td>45.60 + 120 = 165.60</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Bromobenzene + Acrylic Acid --&gt; Cinnamic Acid</td>
      <td>115 + 111 = 226</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Iodobenzene + Acrylic Acid  --&gt; Cinnamic Acid</td>
      <td>(269*4) + 111 = 1187</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Cinnamon Alcohol --&gt; Cinnamic Acid</td>
      <td>123.8</td>
    </tr>
    <tr>
      <th>5</th>
      <td>L-Phenylalanine --&gt; Cinnamic Acid</td>
      <td>717</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Cinnamic Acid --&gt; Cinnamaldehyde</td>
      <td>152</td>
    </tr>
  </tbody>
</table>
</div>


