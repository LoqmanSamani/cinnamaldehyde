```python
import matplotlib.pyplot as plt
import pandas as pd
%matplotlib inline
```


```python
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
      <td>Molanic Acid + Benzaldehyde --&gt; Cinnamic Acid</td>
      <td>Piperidine</td>
      <td>None</td>
    </tr>
    <tr>
      <th>1</th>
      <td>CA 2</td>
      <td>Bromobenzene + Acrilic Acid --&gt; Cinnamic Acid</td>
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
      <td>48 € l</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Mol 2</td>
      <td>Cinnamic Acid</td>
      <td>134 € kg</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Mol 3</td>
      <td>Molanic Acid</td>
      <td>128 € kg</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Mol 4</td>
      <td>Acrilic Acid</td>
      <td>2 € kg</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Mol 5</td>
      <td>Brombenzene</td>
      <td>76 € kg</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Mol 6</td>
      <td>Iodobenzene</td>
      <td>547 € kg</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Mol 7</td>
      <td>Cinnamon Alcohol</td>
      <td>85 € kg</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Mol 8</td>
      <td>L-Phenylalanine</td>
      <td>503 € kg</td>
    </tr>
  </tbody>
</table>
</div>


