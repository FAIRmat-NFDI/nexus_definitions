# Application Definition for SPM Domain

# Plan for General SPM App Def


```mermaid
graph TD;
  subgraph SPM
    %%hh%%
    id1["ENTRY"]
    id0["SPM Common App Def"]
    id2["Common NXinstrument"]
    id3["Common NXdata"]
    id4["Reproducibility Indicators"]
    id5["Resolution Indicators"]

  end

  subgraph NXinstrument
        %%NXinstrument Part%%
    id6["hardware(NXfabrication)"]
    id7["software(NXfabrication)"]
    id8["current_amplifier(NXamplicon)"]
    id9["lock_in(NXlockin)"]
    id10["sample_bias(NXiv_bias)"]
    id11["output_cabling(NXciruit)"]
    id12["piezo_config(NXcollection)"]
    id13["environment(NXenvironment)"]
  end

  id0 --> id1
  id1 --> id2
  id1 --> id3
  id1 --> id4
  id1 --> id5

  id2 --> id6
  id2 --> id7
  id2 --> id8
  id2 --> id9
  id2 --> id10
  id2 --> id11
  id2 --> id12
  id2 --> id13


```

<div>
<h1>Graphical View</h1>
<table>
  <!-- Row -->
  <tr class=0>
    <!-- coloum -->
    <td style="background:red; color:black;">(00)</td>
    <td style="background:green;  color:black;">(01)</td>
    <td style="background:white;  color:black;">(02)</td>
    <td style="background:yellow;  color:black;">(03)</td>
  </tr>
  <tr class=1>
    <!-- coloum -->
    <td style="background:red; color:black;">(10)</td>
    <td style="background:green;  color:black;">(11)</td>
    <td style="background:white;  color:black;">(12)</td>
    <td style="background:yellow;  color:black;">(13)</td>
  </tr  <tr class=2>
    <!-- coloum -->
    <td style="background:red; color:black;">(20)</td>
    <td style="background:green;  color:black;">(21)</td>
    <td style="background:white;  color:black;">(22)</td>
    <td style="background:yellow;  color:black;">(23)</td>
  </tr>
  <tr class=3>
    <!-- coloum -->
    <td style="background:red; color:black;">(30)</td>
    <td style="background:green;  color:black;">(31)</td>
    <td style="background:white;  color:black;">(32)</td>
    <td style="background:yellow;  color:black;">(33)</td>
  </tr>
</table>
</div>