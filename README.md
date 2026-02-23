# CSCI-415 Project 1 - Weka
## Program Author: Sameer Ramkissoon
## Instructor: H. Gu

### Table Of Contents
<ol>
    <li>Describing the Dataset</li>
    <li>Cleaning & Preprocessing</li>
    <li>Converting to ARFF Weka Format</li>
</ol>

### Describing the Dataset
**Dataset Name:** Algerian Forest Fires

**Dataset Link:** https://archive.ics.uci.edu/dataset/547/algerian+forest+fires+dataset

**Dataset Authors:** Faroudja Abid, Nouma Izeboudjen

The original dataset, located at the following path **data/Algerian_forest_fires_dataset_UPDATE.csv**, was developed for the
purpose of predicting forest fires in Algeria. The two authors listed above created it to perform a case study on the decision
tree algorithm. There are **244 instances of data and 14 features/attributes**. Additionally, the original data is
**SPLIT** between two regions: Bejaia and Sidi-Bel Abbes. Below is a look at how the original data is formatted.

![bejaia-og.png](imgs/bejaia-og.png)
**Figure 1:** The head of the Bejaia region data

![sidi-og.png](imgs/sidi-og.png)
**Figure 2:** The head of the Sidi-Bel Abbes region data. Note that the dataset contained **BOTH** separated by a blank row