# ANSC6100_Project

### Introduction
Researchers have found that rates of cancer death in the US have decreased by 21% between 1991 and 2020, however, cancer remains one of the leading causes of death in the US and Canada (Kopec et al., 2024; Viale, 2020). The decrease in cancer death rates can partially be attributed to decreased smoking rates, but improvements in treatments and therapies have had profound impacts (Viale, 2020). Due to their role in cell proliferation, differentiation and survival, receptors from the ErbB family have been studied as potential targets in cancer treatments (Appert-Collin et al., 2015). Numerous studies have found that epidermal growth factor receptor (EGFR), of the ErbB family, is overexpressed in tumours such as lung cancer, breast cancer, kidney, and colon cancer tissues (Herbst 2004). Since it is overly abundant in cancerous tissues compared to normal tissues, inhibitory treatments targeting this receptor are able to selectively focus on affected cells and reduce the cell proliferation effects seen with excess EGFR (Herbst 2004). Recently, there have been fourteen EGFR inhibitors approved globally for the use of cancer treatment (Abourehab et al., 2021). With the use of experimental data, including from these approved treatments and other clinical trials, it is anticipated that machine learning models can be trained on this existing data and subsequently predict the effectiveness of new drugs in their EGFR-reducing capabilities based on each compound’s structural characteristics.

### Problem statement
Test edit to make sure directory is connected to Github. Test edit to make sure I can pull changes to local directory.


### Objectives
The project's main objective will be to build a regression-based quantitative structure-activity relationship model. The goals of this project are the following:

    1. Evaluate the most impactful features for inhibitory strength prediction;
    2. Quantitatively assess the inhibitory strength of a compound against EGFR based upon its chemical structure.

By building this model and achieving these goals, it gives scientists insight into which specific features are important for creating effective inhibitors of EGFR, and in turn, increases the efficiency in which novel therapeutics are produced. This can also potentially reduce the costs for producing a novel therapeutic as the model can be used as a filter for different potential therapeutics for EGFR and thus cut the time needed in the initial stages of drug development.

### Materials and Methods

#### Data

For this project, we will be using data from the CHEMBL database. CHEMBL is a manually curated database that contains data on the bioactivity of small molecules with potential drug-like properties (Zdrazil et al., 2023). A data set will be acquired from CHEMBL containing compounds that have been experimentally shown to be bioactive against the EGFR protein. The value used to measure the bioactivity of the molecules is IC50. IC50 is a quantitative measurement that tests the concentration at which a target's biological activity is reduced by half (Aykul & Martinez-Hackert, 2016). This will be the ground truth of the data set and therefore the value we are building the model to predict. The Simplified Molecular Input Line Entry System (SMILES) notation for each compound in the data set will be used to generate physicochemical features for the compounds. SMILES are used to map a compound's molecular connectivity in a way readable by a machine learning algorithm (Weininger, 1988). The RDkit python library will be used to create new features from these SMILES notations consisting of various physicochemical properties for each of the compounds. These physicochemical properties will be used as the features that the machine learning algorithm will use to model the relationships with IC50. After cleaning the data and filtering, 5,542 compounds will be used to train the machine learning algorithms. 

#### Methods
The first step in our workflow will be to acquire the necessary data from CHEMBL. This will be done using the “chembl_webresource_client” library in python. Utilizing a search function from chembl_webresource_client, all data corresponding to single protein targets of EGFR will be used to construct a data frame of raw data. This raw data frame will be made up of many feature columns including a unique id for each molecule, and the canonical SMILES notation for each compound. Any missing IC50 values and/or canonical SMILES will be filtered out. Each compound is associated with a specific type of biological assay, which refers to the specific experimental setup used to determine the bioactivity of that compound. Based on initial data exploration, a compound's IC50 value can be dramatically influenced by the specific biological assay used to test the bioactivity of the compound. This is particularly true amongst compounds tested in vitro vs. in vivo. Therefore, we will use data only pertaining to an ‘in vitro’ assay type as this is the most abundant data type compared with the ‘in vivo’ cell-based approaches. To account for different scales used for IC50, we will normalize the IC50 across all the compounds. This normalization will also help account for variations in experimental conditions. Once the data has been filtered and standardized, we will create new features of the physiochemical properties using the RDkit module. RDkit contains functions to calculate over 200 different molecular descriptors from SMILES notation. These molecular descriptors will give insight into the physicochemical properties of each of the compounds. A final data set will then be created with physicochemical properties as the predictors and IC50 values as the response. 

The data set will be split into training and testing sets and cross-fold validation will be used for training on various regression models. Each model will be assessed for its learning and generalization ability by generating a learning curve to plot error and training time for the training and validation dataset. This can give insight into whether the models are overfitting or underfitting the data. Several different error metrics will also be used to assess and visualize the performance of the models on the training data. These error metrics include mean square error, mean absolute error, mean absolute percentage error, and mean root error. After the first training step, hyperparameter tuning will be conducted for the models that show promising initial results. Once optimal parameters are found, the models will be trained once again using the optimal hyperparameters and the errors for each model will be compared. Further investigation will be conducted on the optimized model corresponding to the lowest errors to evaluate which features are most important in predicting the IC50 of a compound. Once training is complete, the models will be tested using the testing data to assess the final performance of the models using the various error metrics. 

### References

1. Abourehab MAS, Alqahtani AM, Youssif BGM, Gouda AM. Globally Approved EGFR Inhibitors: Insights into Their Syntheses, Target Kinases, Biological Activities, Receptor Interactions, and Metabolism. Molecules. 2021 Nov 4;26(21):6677. doi: 10.3390/molecules26216677. PMID: 34771085; PMCID: PMC8587155.  
 
2. Appert-Collin A, Hubert P, Crémel G, Bennasroune A. Role of ErbB Receptors in Cancer Cell Migration and Invasion. Front Pharmacol. 2015 Nov 24;6:283. doi: 10.3389/fphar.2015.00283. PMID: 26635612; PMCID: PMC4657385. 
 
3. Aykul, S., & Martinez-Hackert, E. (2016). Determination of half-maximal inhibitory concentration using biosensor-based protein interaction analysis. Analytical Biochemistry, 508, 97–103. https://doi.org/10.1016/j.ab.2016.06.025 
 
4. Bhushan A, Gonsalves A, Menon JU. Current State of Breast Cancer Diagnosis, Treatment, and Theranostics. Pharmaceutics. 2021 May 14;13(5):723. doi: 10.3390/pharmaceutics13050723. PMID: 34069059; PMCID: PMC8156889. 

5. Dietterich TG. Ensemble methods in machine learning In: Goos G, Hartmanis J, Van Leeuwen JP, editors. International Workshop on Multiple Classifier Systems. Springer: 2000. p. 1–15. 

6. Herbst RS. Review of epidermal growth factor receptor biology. Int J Radiat Oncol Biol Phys. 2004;59(2 Suppl):21-6. doi: 10.1016/j.ijrobp.2003.11.041. PMID: 15142631. 

7. Kwon, S., Bae, H., Jo, J. et al. Comprehensive ensemble in QSAR prediction for drug discovery. BMC Bioinformatics 20, 521 (2019). https://doi.org/10.1186/s12859-019-31354 
 
8. Niu B, Li J, Li G, Poon S, Harrington PB. Analysis and Modeling for Big Data in Cancer Research. Biomed Res Int. 2017;2017:1972097. doi: 10.1155/2017/1972097. Epub 2017 Jun 12. PMID: 28691016; PMCID: PMC5485265. 
 
9. Polyak K. Heterogeneity in breast cancer. J Clin Invest. 2011 Oct;121(10):3786-8. doi: 10.1172/JCI60534. Epub 2011 Oct 3. PMID: 21965334; PMCID: PMC3195489. 
13. Speck-Planche A, Kleandrova VV, Luan F, Cordeiro MN. Chemoinformatics in anti-cancer chemotherapy: multi-target QSAR model for the in silico discovery of anti-breast cancer agents. Eur J Pharm Sci. 2012 Aug 30;47(1):273-9. doi: 10.1016/j.ejps.2012.04.012. Epub 2012 Apr 17. PMID: 22538055. 
 
10. Wei L, Wan S, Guo J, Wong KK. A novel hierarchical selective ensemble classifier with bioinformatics application. Artif Intell Med. 2017; 83:82–90. https://doi.org/10.1016/j.artmed.2017.02.005
 
11. Weininger, D. (1988). Smiles, a chemical language and information system. 1. introduction to methodology and encoding rules. Journal of Chemical Information and Computer Sciences, 28(1), 31–36. https://doi.org/10.1021/ci00057a005 
 
12. Xiao Y, Wu J, Lin Z, Zhao X. A deep learning-based multi-model ensemble method for cancer prediction. Comput Methods Prog Biomed. 2018; 153:1–9. https://doi.org/10.1016/j.cmpb.2017.09.005
 
13.  Zhao M, Wang L, Zheng L, Zhang M, Qiu C, Zhang Y, Du D, Niu B. 2D-QSAR and 3D-QSAR Analyses for EGFR Inhibitors. Biomed Res Int. 2017;2017:4649191. doi: 10.1155/2017/4649191. Epub 2017 May 29. PMID: 28630865; PMCID: PMC5467385. 
 
14. Zdrazil, B., Felix, E., Hunter, F., Manners, E. J., Blackshaw, J., Corbett, S., de Veij, M., Ioannidis, H., Lopez, D. M., Mosquera, J. F., Magarinos, M. P., Bosc, N., Arcila, R., Kizilören, T., Gaulton, A., Bento, A. P., Adasme, M. F., Monecke, P., Landrum, G. A., & Leach, A. R. (2023). The CHEMBL database in 2023: A drug discovery platform spanning multiple bioactivity data types and time periods. Nucleic Acids Research, 52(D1):D1180-D1192. 
. https://doi.org/10.1093/nar/gkad1004

