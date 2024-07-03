# ন্ত্্ㅇ $-$ <br> TowaRDS P£RSONALISED AND  <br> HUMAN-IN-THE-LOOP DOCUMENT Sumifarisation <br>  <br> $\mathrm{PhD}$ in Computer Science 

A thesis sUBMitTED to MACQUARIE UNIVERSITY

FOR THE DEGREE OF

Doctor of Philosophy

Department of Computing

MAY 2021

MACQUARIE

University

(C) Samira Ghodratnama, 2023.

Typeset in $\mathrm{AT}_{\mathrm{E}} \mathrm{X} 2_{\varepsilon}$.

## Declaration

I certify that the work in this thesis entitled Towards Personalised and Humanin-the-Loop Document Summarisation has not previously been submitted for a degree nor has it been submitted as part of the requirements for a degree to any other university or institution other than Macquarie University. I also certify that the thesis is an original piece of research and it has been written by me. Any help and assistance that I have received in my research work and the preparation of the thesis itself have been appropriately acknowledged. In addition, I certify that all information sources and literature used are indicated in the thesis.

Samira Ghodratnama

## Dedication

I dedicate this dissertation to three beloved people who have meant and continue to mean so much to me.

The first is my father, for his endless love and support. He always trusts my abilities and respects all my decisions, giving me the confidence to follow my dreams. He taught me to believe in hard work and inspired me to be strong despite many life obstacles.

In memory of my mother, Shirin, who, though no longer in this world, continues to regulate my life. Her words of encouragement and push for commitment always remain in my mind.

Last but not least, I dedicate this to my husband, Mehrdad, who always encourages me to accept every adventure life offers, especially this one. He taught me to think big and view every challenge as an opportunity to achieve what I aspire. I am genuinely thankful for having you in my life and exploring the world with you, Mehrdad!

## Acknowledgements

I would like to take this opportunity to acknowledge those who have impacted my $\mathrm{PhD}$ accomplishment and doctorate journey.

First, I express my deep gratitude and sincere appreciation to my Principal Supervisor, Dr Amin Beheshti, for his guidance, encouragement and support he has provided throughout my PhD program. His positive outlook inspired me and gave me the confidence to explore new research directions. He gave me the academic freedom to follow my ideas, and his insightful feedback pushed me to sharpen my thinking and elevated my work to a higher level. I have been extremely lucky to have a supervisor who cared so much and enriched my growth as a student, a researcher and a scientist.

I would like to thank my associate supervisor, Dr Jia Wu, whose expertise were valuable in formulating the research questions and methodology. I would also like to thank Dr Fariborz Sobhanmanesh and Dr Hamid Reza Motahari-Nezhad for their valuable guidance and thoughtful comments throughout my studies. I extend further thanks to Dr Mohamed Sarwat at Arizona State University for being such a kind and understanding host during my research visit, especially given COVID-19.

My sincere appreciation also goes to Macquarie University and the AI-enabled Processes Research Centre for generously funding this PhD research through the Macquarie Research Excellence Scholarship and the Postgraduate Research Fund. These scholarships made it possible for me to pursue my doctoral studies.

I am thankful to every member of Data Analytics Research Lab at Macquarie University, who supported me in my research. In addition, I would like to thank the
anonymous reviewers who provided helpful feedback and suggestions on my publications.

I would also like to acknowledge Capstone Editing for providing copyediting and proofreading services, according to the guidelines laid out in the university-endorsed national 'Guidelines for Editing Research Theses'.

Finally, I am thankful to my family and my in-laws for their love and patience over the years and during my research endeavours - especially my cute and sweet niece, Kimia, for her love, patience and understanding when I was so busy doing my research and I did not have time to spend with her. They are my source of strength, and without their love and endless support this dissertation would have neither been started nor completed.

## Samira Ghodratnama

May 2021

## Dissertation Examiners

- Professor Ladjel Bellatreche, ISAE-ENSMA, France
- Professor Ismail Khalil, Johannes Kepler University Linz, Austria
- Professor Salil Kanhere, UNSW Sydney, Australia


## List of Publications

- Ghodratnama, Samira, Mehrdad Zakershahrak, and Amin Beheshti. "Summary2vec: Learning Semantic Representation of Summaries for Healthcare Analytic.", IJCNN 2021: International Joint Conference on Neural Network, 2021. (CORE Rank: A).
- Ghodratnama, Samira, Amin Beheshti, Mehrdad Zakershahrak, and Fariborz Sobhanmanesh. "Intelligent Narrative Summaries:

From Indicative to Informative Summarization", Big Data Research Journal, 2021. (Q1, IF: 3.58).

- Ghodratnama, Samira, Amin Beheshti, Mehrdad Zakershahrak, and Fariborz Sobhanmanesh. "Extractive Document Summarization based on Dynamic Feature Space Mapping.", IEEE Access, 8, pp.139084-139095, 2020. (Q1, IF: 3.74).
- Ghodratnama, Samira, Mehrdad Zakershahrak, and Fariborz Sobhanmanesh. "Am I Rare? An Intelligent Summarization Approach for Identifying Hidden Anomalies." AI-PA 2020 - 18th International Conference on Service Oriented Computing (ICSOC) Workshop, 2020. (CORE Rank: A).
- Ghodratnama, Samira, Mehrdad Zakershahrak, and Fariborz Sobhanmanesh. "Adaptive Summaries: A Personalized Concept-based Summarization Approach by Learning from Users' Feedback. AI-PA 2020 - 18th International Conference on Service Oriented Computing (ICSOC) Workshop, 2020. (CORE Rank: A).
- Ghodratnama, Samira, Amin Beheshti, and Mehrdad Zakershahrak. "A Personalized Reinforcement Learning Summarization Method for Learning Structure from Unstructured Data." submitted to Web Information Systems Engineering (WISE), 2021. (CORE Rank: A).
- Ghodratnama, Samira, Amin Beheshti, Mehrdad Zakershahrak, and Hamid Reza Motahari-Nezhad. "SumRecom: A Personalized Interactive Summary Recommendation System by Learning from Users' Feedback using Reinforcement Learning." submitted to Machine Learning Journal, 2021. (Q1, IF: 2.67).
- Beheshti, Amin, Francesco Schiliro, Samira Ghodratnama, Farhad Amouzgar, Boualem Benatallah, Jian Yang, Quan Z. Sheng, Fabio Casati, and Hamid Reza Motahari-Nezhad. iProcess: enabling IoT platforms in data-driven knowledgeintensive processes., In International Conference on Business Process Management, pp. 108-126. Springer, Cham, 2018. (CORE Rank: A).
- Amouzgar, Farhad, Amin Beheshti, Samira Ghodratnama, Boualem Benatallah, Jian Yang, and Quan Z. Sheng. "iSheets: a spreadsheet-based machine learning development platform for data-driven process analytics." In International Conference on Service-Oriented Computing, pp. 453-457. Springer, Cham, 2018. (CORE Rank: A).
- Schiliro, Francesco, Amin Beheshti, Samira Ghodratnama, Farhad Amouzgar, Boualem Benatallah, Jian Yang, Quan Z. Sheng, Fabio Casati, and Hamid Reza Motahari-Nezhad. "iCOP: IoT-enabled policing processes." In International Conference on Service-Oriented Computing, pp. 447-452. Springer, Cham, 2018. (CORE Rank: A).
- Amin Beheshti, Boualem Benatallah, Hamid Reza Motahari-Nezhad, Samira Ghodratnama, and Fred Amouzgar,. "BP-SPARQL: A Query Language for Summarizing and Analyzing Big Process Data", Springer, 2020. (Book Chapter).


## Abstract

The ubiquitous availability of computing devices and the widespread use of the internet have generated a large amount of data continuously. Therefore, the amount of available information on any given topic is far beyond humans' processing capacity to properly process, causing what is known as 'information overload'. To efficiently cope with large amounts of information and generate content with significant value to users, we require identifying, merging and summarising information. Data summaries can help gather related information and collect it into a shorter format that enables answering complicated questions, gaining new insight and discovering conceptual boundaries.

This thesis focuses on three main challenges to alleviate information overload using novel summarisation techniques. It further intends to facilitate the analysis of documents to support personalised information extraction. This thesis separates the research issues into four areas, covering (i) feature engineering in document summarisation, (ii) traditional static and inflexible summaries, (iii) traditional generic summarisation approaches, and (iv) the need for reference summaries. We propose novel approaches to tackle these challenges, by:

- enabling automatic intelligent feature engineering
- enabling flexible and interactive summarisation
- utilising intelligent and personalised summarisation approaches.

The experimental results prove the efficiency of the proposed approaches compared to other state-of-the-art models. We further propose solutions to the information overload
problem in different domains through summarisation, covering network traffic data, health data and business process data.

## Contents

Declaration ..... iii
Dedication ..... $\mathrm{v}$
Acknowledgements ..... vii
Dissertation Examiners ..... ix
List of Publications ..... xi
Abstract ..... xiii
List of Figures ..... xxi
List of Tables ..... XXV
1 Introduction ..... 1
1.1 Key Research Issue .. ..... 3
1.1.1 Feature Engineering in Document Summarisation ..... 4
1.1.2 Traditional Static and Inflexible Summaries ..... 4
1.1.3 Traditional Generic Summarisation Approaches ..... 4
1.1.4 Need for Reference Summaries ..... 5
1.2 Contribution Overview ..... 5
1.2.1 Enabling Automatic Intelligent Feature Engineering ..... 6
1.2.2 Enabling Flexible and Interactive Summarisation ..... 7
1.2.3 Enabling Intelligent and Personalised Summarisation ..... 8
1.2.4 Dissertation Organisation ..... 10
2 Background and Related Work ..... 13
2.1 Document Summarisation: Overview ..... 14
2.1.1 Definition ..... 14
2.1.2 Document Summarisation v. Document Compression ..... 15
2.2 Document Summarisation Categories ..... 16
2.2.1 Categorising Based on Input Sources' Properties ..... 17
2.2.2 Categorising Based on Summarisation Purpose ..... 19
2.2.3 Categorising Based on Output Summary Properties ..... 20
2.2.4 Language-based and Application-based Categorisation ..... 21
2.2.5 Proposed Categorisation Schema ..... 23
2.3 Feature Engineering in Document Summarisation ..... 23
2.3.1 State-of-the-art Features ..... 24
2.3.2 Learning Optimal Feature Set ..... 26
2.4 Traditional Summarisation ..... 28
2.4.1 Abstractive Approaches ..... 28
2.4.2 Extractive Approaches' Structure ..... 28
2.4.3 Extractive Approach Categorisation ..... 30
2.4.4 Hybrid Extractive and Abstractive Approaches ..... 33
2.5 Structured Summarisation ..... 34
2.5.1 Timeline Summarisation ..... 34
2.5.2 Document Thread Summarisation ..... 35
2.5.3 Hierarchical Summarisation ..... 35
2.5.4 Concept Map Summarisation ..... 36
2.6 Interactive and Personalised Summarisation ..... 36
2.7 Summary ..... 37
3 Experimental Setup ..... 39
3.1 Dataset ..... 39
3.1.1 DUC Datasets ..... 40
3.1.2 CNN/Daily Mail Datasets ..... 40
3.2 Evaluation Metric ..... 41
3.2.1 Automatic Evaluation ..... 41
3.2.2 Human Evaluation ..... 42
3.3 Baseline ..... 43
3.4 Summary ..... 44
4 Towards Intelligent Feature Engineering ..... 45
4.1 Introduction ..... 47
4.1.1 Problem Statement ..... 49
4.1.2 Feature Set ..... 49
4.1.3 Methodology ..... 51
4.1.4 Experiments and Evaluation ..... 55
4.2 Summary ..... 61
5 Towards Interactive Document Summarisation ..... 63
5.1 NARS ..... 66
5.1.1 Problem Definition ..... 68
5.1.2 Proposed Framework ..... 69
5.2 SNARS ..... 69
5.2.1 Problem Definition ..... 69
5.2.2 Hierarchical Time-aware Clustering ..... 71
5.2.3 Hierarchical Location-aware Clustering ..... 72
5.2.4 Hierarchical Topic-based and Hybrid Time-Location Clustering ..... 73
5.2.5 Summarising Over the Hierarchies ..... 74
5.3 FNARS ..... 76
5.3.1 Problem Definition ..... 76
5.3.2 Extracting Concepts and Relations ..... 76
5.3.3 Hierarchical Clustering of Concepts ..... 77
5.3.4 Summarising Over Hierarchies ..... 78
5.4 Experiments and Evaluation ..... 78
5.5 Summary ..... 85
6 Towards Personalized Document Summarisation ..... 87
6.1 Adaptive Summaries ..... 88
6.1.1 Problem Definition ..... 90
6.1.2 Methodology ..... 90
6.1.3 Experiment ..... 92
6.2 SumRecom ..... 94
6.2.1 Preference-based and Reinforcement-based Approaches ..... 96
6.2.2 Methodology ..... 97
6.2.3 Experiment ..... 108
6.3 Summation ..... 116
6.3.1 Problem Definition ..... 116
6.3.2 Organiser (Structuring Unstructured Data) ..... 117
6.3.3 Summariser ..... 120
6.3.4 Experiment ..... 123
6.4 Summary ..... 126
7 Summarisation Applications ..... 129
7.1 Detecting Anomalies Through Summarisation ..... 130
7.1.1 Related Work ..... 131
7.1.2 Proposed Approach (INSIDENT) ..... 134
7.1.3 Experiments and Evaluation ..... 137
7.2 Summarisation in Healthcare Analytics ..... 143
7.2.1 Related Work ..... 144
7.2.2 Summary2vec ..... 148
7.2.3 Personalised Summarisation ..... 152
7.2.4 Evaluation ..... 153
7.3 Summarising Business Process Data . ..... 156
7.3.1 Motivating Scenario: Missing People ..... 157
7.3.2 Process Data Lake and Process Knowledge Lake ..... 159
7.3.3 Data Summaries and Narratives Construction ..... 159
7.3.4 Process Analytics ..... 163
7.3.5 Implementation and Evaluation ..... 166
7.4 Summary ..... 168
8 Conclusion and Feature Work ..... 169
8.1 Summary of Contributions ..... 169
8.2 Open Challenges and Future Directions ..... 171
8.2.1 Personalised Feature Engineering for Summarisation . ..... 171
8.2.2 Summary Representation and Visualisation .. ..... 172
8.2.3 Real-time Summarisation and Performance Boosting ..... 172
8.2.4 Datasets and Evaluation Metrics ..... 172
8.2.5 Summarizing Business Process Data ..... 173
8.2.6 Different Domains and Applications ..... 174
References ..... 175

## List of Figures

2.1 Document summarisation categorisation. ..... 17
2.2 Proposed categorisation schema for document summarisation. ..... 24
4.1 Overview of the proposed approach (ExDoS). (A) A simple dataset with
two classes. (B) Each instance is a sentence. We combine both surface
and linguistic features (extracted from the semantic graph) to make a
unified feature set. (C) The final output is groups of similar samples in
which features are locally weighted in each group. ..... 48
4.2 (A) ExDos architecture. (A) The weights of features in each cluster are
updated iteratively to bring similar samples closer to each other in the
new feature spaces by minimising the error of classifiers in clusters. (B)
The architecture of state-of-the-art approaches. ..... 49

4.3 (A) Distribution of synthetic data (2-class). (B) The output of the ExDoS is two new feature spaces where the weights (alpha and beta) are updated in such a way that similar samples are close to each other.* *The details of this transformation are illustrated in Fig. 4.4. . ..... 50
4.4 Single iteration of ExDoS. All samples are considered in each iteration,
and weights are updated to bring the nearest same-label sample $\left(s_{=}\right)$
closer and push different-label samples $\left(s_{\neq}\right)$further. The local weights
of features are subsequently updated. ..... 51
4.5 Caption for LOF ..... 55

4.6 Both graphs show the number of iterations versus the score in both datasets.

4.7 Both graphs show the learning parameters $(\alpha, \gamma)$ and the corresponding ROUGE-1.

4.8 Both graphs show the learning parameters $(\phi, \lambda)$ and the corresponding score value.

5.1 Traditional summarisation approaches are depicted on the left. (A) Extractive approach (the most informative sentences are selected); (B) Abstractive approach (summaries are generated in the form of new sentences). (C, D) NARS process (a hierarchical summarisation approach).

5.2 NARS's hierarchical structure, where nodes correspond to sentences in SNARS and concepts in FNARS.

5.3 (A) Documents are pre-processed. (B) Hierarchical clustering is performed. (C) Created summaries are shown to users for interaction, where nodes correspond to sentences in SNARS and concepts in FNARS. .

5.4 Example of a hierarchical concept map: two levels of hierarchy are coloured, and each node's children is shown to users if they select a parent node.

5.5 Time each user took to answer predefined questions when reading different summarisation approaches.

5.6 Accuracy of users' answers when reading summaries generated using different approaches.

5.7 User preferences based on different aspects mentioned in Table 4.5(tie is allowed).

6.1 An overview of the proposed approach (Adaptive Summaries). 1) Summaries are initiated with ExDos. 2) Users integrate their preferences in making summaries by giving feedback in an iterative loop. 3) An example of user interaction.

6.2 Left graph shows the ROUGE-1 based on iteration number, and the right graph shows the ROUGE-2 based on iteration number. The green samples represent the permitted concept unit in unigrams, blue denotes bigrams and red represents sentences.

6.3 (A) Number of iterations and ROUGE-1 for DUC2002. (B) Number of iterations versus ROUGE-2 values. (C) Number of actions versus iterations for DUC2002.

6.4 Overview of the SumRecom approach. Active and preference-based learning are used to extract users' preferences. The learnt preference ranked function is used to produce the desired summary using IRL for learning the reward. An RL algorithm is proposed for learning the optimal policy.

6.5 Comparing two summaries that put significant cognitive burden on users. 97

6.6 SumRecom approach in more detail: 1) The left side is the user preference extractor using active preference learning over concepts, and 2) the right side is the summarizer including reward learning (IRL) and policy learning (RL)

6.7 Features for estimating the ranker function for preferred concepts. . . . 109

6.8 Comparing different strategies used in active learning. . . . . . . . . . . 111

6.9 effect of query budget size in the quality of summaries. . . . . . . . . . 112

6.10 Evaluating different feature sets for estimating the ranker function.

7.1 Result of comparing information loss based on different summary sizes. FIB: forwarding information base; NTS: network traffic summarisation

7.2 Summary2vec architecture. Summaries are transformed into word units to be embedded. Sequences of word vectors are encoded to build a sentence matrix. Attention to the sentence matrix is applied to make sentence embedding, which is encoded to make the summary matrix. The concatenated output of two parallel networks, corresponding to two summaries, is fed into a fully connected network to estimate the summary's similarity.

7.3 (A) Summary embeddings are produced. (B) The hierarchical summaries are made based on the proposed hierarchical clustering approach. 152

7.4 IoT-enabled process data analytics pipeline.

7.5 Process knowledge graph schema. (A) A sample OLAP dimension, and (B) an interactive graph summary (C)

7.6 Scalable summary generation.

7.7 Presenting a spreadsheet-like interface on top of the scalable summary generation framework $[1]$

7.8 Taxonomy of the machine learning algorithms used as a service to streamline the process of acquiring knowledge when interacting with the summaries.

7.9 Scalability with the size of physical memory for entity and relationship summaries. (B) Scalability with the size of physical memory for path summaries.

## List of Tables

2.1 Term-level Features ..... 25
2.2 Sentence-level Features ..... 26
2.3 Paragraph-level Features ..... 26
2.4 Corpus-based Features ..... 26
4.1 ROUGE score (\%) Comparison on DUC2002 Dataset . ..... 56
4.2 ROUGE score (\%) Comparison on CNN/Daily Mail Using F1 Variant
of ROUGE ..... 57
4.3 Estimation of Features Importance ..... 57
4.4 Effects of Dynamic Local Feature Weighting ..... 58
4.5 Human Evaluation Result ..... 60
5.1 ROUGE Score (\%) Comparison on DUC2002 Dataset . ..... 80
5.2 Score Comparison on CNN/Daily Mail Using F1 Variant of ROUGE . ..... 81
5.3 Comparing Previous Approaches Based on Different Features ..... 84
6.1 ROUGE score comparison on CNN/DailyMail using F1 variant of ROUGE. ..... 93
6.2 ROUGE score (\%) comparison on DUC-2002 dataset ..... 93
6.3 Comparing SumRecom on DUC2001 Dataset ..... 113
6.4 Comparing SumRecom on DUC2002 Dataset ..... 113
6.5 Comparing SumRecom on DUC2004 Dataset ..... 113
6.6 Overview of the Parameters Used in Simulation Experiments ..... 114
6.7 Comparing SumRecom, SumRecom-AC and SumRecom-PR on DUC2001
Dataset ..... 114
6.8 Comparing SumRecom, SumRecom-AC and SumRecom-PR on DUC2002
Dataset ..... 115
6.9 Comparing SumRecom, SumRecom-AC and SumRecom-PR on DUC2004
Dataset ..... 115
6.10 Comparing SumRecom and SumRecom-GE ..... 115
6.11 Comparing Summation with Benchmark Datasets ..... 126
7.1 Example of Network Traffic Samples ..... 135
7.2 Dataset Description ..... 139
7.3 Real SCADA Dataset (WTP) Results . ..... 140
7.4 Simulated SCADA Datasets Results (Sim1 and Sim2) ..... 141
7.5 Simulated SCADA Datasets with Injected Anomalies Results (MI and
$\mathrm{MO})$ ..... 142
7.6 Comparing the Distribution of Anomalies in Summaries and Original Data142 ..... 142
7.7 valuating Summary Size Effect According to RMSE Value ..... 155

'Its not information overload. Its filter failure.'

Clay Shirky

# Introduction 

The way information is being generated, stored, manipulated, retrieved and disseminated has changed dramatically in recent decades. The ubiquitous availability of computing devices and the widespread use of the internet have seen many data being generated continuously. Therefore, the amount of available information on any given topic is far beyond humans' processing capacity to manage, causing 'information overload'. This is commonly caused by [2]:

- multiple information sources presence, or information overabundance
- information managing challenge, or irrelevant obtained information
- users' lack of time to analyse and understand gathered data.

Although this considerable amount of data can be useful in analytic applications,
information is not valuable unless the knowledge can be derived. However, no processing technique is possible on raw data until it becomes meaningful and relevant. Indeed, there are many practical scenarios in which users need to process extensive textual documents with a specific goal. Examples include lawyers facing an extensive collection of legal documents to find and process relevant information for a case to derive arguments and conclusions. Researchers also need to read vast amounts of published scientific articles and find connections and trends across the content. Obviously, the more documents which one has to face, the more challenging the problem of finding what they need is due to information overload. In these scenarios, information-seeking processes are more beyond the searching of facts, aiming to extend one's knowledge about a topic, gain new insights and discover conceptual boundaries [3]. Therefore, new tools and techniques are required to facilitate understanding of big data.

To efficiently cope with a large amount of information and generate significant value to users, one must identify the data and merge it as a whole entity, specifically when the question comprises a distributed and complicated topic. This process commonly includes three activities, including (i) discovery, to explore new information; (ii) filtering, to summarise new information; and (iii) adapting, to make information accessible to new users [4]. Therefore, summaries are helpful when huge amounts of information need processing.

Data summaries can help gather related information and collect it into a shorter format that enables answering complicated questions, gaining new insight and discovering conceptual boundaries. A large body of research exists to address this problem, specifically regarding summaries that need to be generated in textual form, known as 'text summarisation'. Automatic document summarisation is a long-studied area covering different perspectives to articulate the effects and needs of data reduction for analysis, commercialisation, management and personalising purposes.

The goal of automatic text summarisation is to identify and highlight the critical aspects of one or multiple input document(s) within a defined size limit [5]. A good summary conveys the key ideas efficiently, allowing users to quickly gain an overview of the text without expending much effort. Despite the body of research, it is still
difficult to produce summaries that are comparable to human-generated ones [5]. The massive collection of documents (volume), the speed of generated documents (velocity), and the unstructured format (variety) in which documents appear make summarisation challenging. Various text summarization models have been studied in the natural language processing community, including extractive and abstractive approaches, single-document or multi-document summarisation (MDS), and query-focused or update summarisation. Existing MDS approaches produce a uniform summary for all users without considering individual interests. Optimising a system to produce one 'best' summary that satisfies all variants of users is also highly impractical. Therefore, a more significant challenge is the subjectivity aspect of summarization in selecting the content in summaries for different users. Besides, current approaches optimise their system based on gold-standard summaries generated by human experts, which are expensive and time consuming.

This dissertation proposes novel approaches towards intelligent, personalised and interactive human-in-the-loop summarisation. We first introduce concepts central to the work described in this dissertation, and identify significant research issues in personalising document summarisation and information-seeking processes. This is followed by a description of the critical research issues tackled in the thesis. Next, we summarise our contributions to the area and outline the thesis structure.

### 1.1 Key Research Issue

This thesis focuses on three main challenges proposing novel summarisation techniques to alleviate information overload. We intend to facilitate the analysis of documents to support personalised information extraction. Therefore, we separate the research issues into three areas covering (i) feature engineering in document summarisation, (ii) interactive summarisation and (iii) personalised summarisation.

### 1.1.1 Feature Engineering in Document Summarisation

The essential part of any text-related problem is feature engineering, (i.e., the process of creating features from raw text data). Feature engineering in machine learning is more than selecting the appropriate features and transforming them. It prepares a dataset to be compatible with an algorithm, improves a model's performance, and reveals any hidden information, highlighting what is important in summarisation. Text summarisation is an old challenge that dates back to the 1950s when such features as word and phrase frequency were used to select essential sentences. However, these factors are still required for feature engineering in summarisation tasks, due to its applicability.

### 1.1.2 Traditional Static and Inflexible Summaries

In general form, summarisation takes a topic-related document set as input and generates a summary that bears the most crucial aspect. Research on MDS, in general, ignores the usefulness of the approach for users. Instead, the literature mostly focuses on the accuracy of their produced summaries, resulting in short (3-6 sentences), single, inflexible and flat summaries for all users. Therefore, these approaches are incapable of producing more extended summaries since all the details are omitted, even if users are interested in obtaining more information. Besides, the produced summaries are unstructured and, therefore, are improperly equipped for allowing further analysis. Unfortunately, a single summary is unlikely to serve all users in a large population. Therefore, there is an urgent demand to make summaries that can be changed upon a user's request.

### 1.1.3 Traditional Generic Summarisation Approaches

Existing summarisation approaches produce a general summary in the form of a few selected sentences to serve all the users' needs. In contrast to a generic summary that is unique for all users, there is a lack of user-centric summarisation approaches in which a user can specify their desired content in making summaries. Several reports $[6,7]$
demonstrate that users prefer personalised summaries that accurately reflect their interests - hence the demand. However, the system should have background knowledge about the user to achieve this, making tailored summarisation a challenging task. Challenges include acquiring relevant information about a user, aggregating and integrating the information into a user model, and using the provided information to make a personalised summary.

### 1.1.4 Need for Reference Summaries

State-of-the-art summarisation approaches train their system towards one single summary, referred to as reference or gold-standard summaries made by a human [5]. A report by Lin [8] shows that three thousand hours of human effort were needed for summaries' evaluation for the Document Understanding Conferences (DUC)—a subjective, costly and time-consuming task.

### 1.2 Contribution Overview

Our goal is to facilitate the creation of personalised and comprehensive text summarisation. The research discussed in this dissertation aims to answer the following high-level research questions:

- How useful are the current state-of-the-art methods in automatically creating and detecting features in the context of document summarisation? How can we distinguish the efficiency of different features?
- What structures are required to help users seek their desired information? How can we use individual feedback such that summarisation approaches adapt to the users' needs?
- Can we simulate user behaviour to predict their desired summary or informationseeking path? Can we provide predictability for unseen situations in terms of application?
- How can we eliminate the need for reference summaries to reduce the cost of summarisation? How can the task of persoanlised summarization be better regulated, formulated, and comparable to contribute more to the research field?

To answer these questions, we propose novel computational methods and extensive experiments for the creation of intelligent and personalised summaries. In detail, this thesis makes the following contributions to tackle this problem, categorised as enabling:

- automatic intelligent feature engineering
- flexible and interactive summarisation
- intelligent and personalised summarisation.


### 1.2.1 Enabling Automatic Intelligent Feature Engineering

To enable automatic intelligent feature engineering in document summarisation, we propose two solutions, which are also fundamental to other contributions made by this thesis.

## Contribution 1: Dynamic Feature Space Mapping Through a Novel Traditional Summarisation Approach

We present a novel intelligent approach for summarisation, which benefits from using supervised and unsupervised algorithms simultaneously and in an interpretable manner. We combine the clustering and classification algorithm into a single objective function. Clustering aims to discover the underlying structure of data, and then feeds the processed information to the classification stage through a single objective function. The goal is to improve the performance of the summarisation algorithm. Besides, features are dynamically weighted by optimising the process in each cluster. The proposed approach is capable of measuring the role of features through the summarisation process by making various feature spaces.

### 1.2.2 Enabling Flexible and Interactive Summarisation

Compared to gold-standard summaries, previous approaches mainly optimise their system to enhance summaries' accuracy rather than users' need, resulting in short and static summaries. We present an interactive narrative framework based on the feature extracted from users' engagement to tackle these issues. Therefore, we propose to hierarchically structure the summary output to improve navigation and provide users with more information upon request. Based on the proposed structure, we present two intelligent and interactive summarisation approaches: semi-structured narrative summaries (SNARS) and fully structured narrative summaries (FNARS). The proposed approaches aim to engage users in the summarisation process to guarantee interactive speed even for extensive text collections, and to eliminate the need for reference summaries.

## Contribution 2: An Intelligent Semi-structured Narrative Summaries (SNARS) for Interactive Summarisation

We propose a new task for MDS, called narrative summaries (NARS); this technique gathers the related information and collects it into a coherent hierarchy. We called this approach 'narrative summaries' because it provides information in a logical order, ranked from the most indicative sentences to more informative sentences, to prevent users from being cognitively overwhelmed with a complete summary at once. This is important because a user might be interested in different aspects of a topic based on their background knowledge, situation and context, as well as cognitive bias. Therefore, we enable users to explore their desired information with minimal reading required. Since sentences are the representative unit in this structure, the proposed model is considered an extractive and semi-unstructured approach.

## Contribution 3: An Intelligent Fully-structured Narrative Summaries (FNARS)

 for Interactive SummarisationStudies have shown that when people are exposed to many documents, they rarely make a fully formulated summary. Instead, they attempt to extract concepts and the relationships between them [9-11]. Therefore, access to structured data is increasingly critical in every domain [12-14]. The proposed model is presented as a hierarchical concept map, as this structured presentation style is suitable for summarisation. A concept map is a labelled graph. Nodes in a concept map denote the concepts and edges are the relations between them [15]. Therefore, a summary in concept map form provides a concise overview of the contents of document collections, reveals interesting connections, can provide better navigational structure for greater exploration, and facilitates use of the summaries for further analysis. The representation unit is a sentence in SNARS and a concept in FNARS. Therefore, FNARS provides a more concise overview of information, while SNARS provides more detail. Conversely, FNARS is a fully structured model and can be used for further analysis.

### 1.2.3 Enabling Intelligent and Personalised Summarisation

Traditional summarisation approaches produce a generic summary that fits all users. Therefore, the subjectivity aspect of summarisation (i.e., what is deemed valuable for different users) is ignored, making these approaches impractical in real-world scenarios. Crafting a user-specific summary for an input document cluster is a challenging task. In a personalised approach, the system needs to know about a user's background knowledge or interests. When we do not have access to prior knowledge, including profile or background knowledge, the system requires user interaction to procure feedback for modelling individual interests. Therefore, this thesis provides human-in-the-loop approaches to generate personalised summaries that better understand the users' needs. This eliminates the need for reference summaries, which is a challenging issue for summarisation tasks.

## Contribution 4: Adaptive Summarisation: A Personalised and Interactive Concept-based Summarisation Approach

Producing a user-desired summary is a challenging task. To tackle this problem, we propose a novel optimisation algorithm that directly reflects users' interests in making extractive summaries. The proposed approach, called 'adaptive summaries', learns from the information users provide to the system gradually through interaction. Users are allowed to provide their feedback in an iterative loop, and can choose important concepts while defining their degree of importance. Moreover, they can define their confidence level in their choices and can even select which concepts not to include in the output. The proposed approach learns to select sentences that maximise the summary score according to user feedback. By doing this, we allow even novice users to interactively explore, manipulate and analyse unstructured text document collections to integrate their own notion of importance. The proposed approach can guarantee interactive speed to keep the user engaged in the process.

Contribution 5: Novel Personalised Summarisation Approach to Predict Users' Desired Unstructured Summaries Based on Feedback

The proposed approach considers the summarisation problem as a recommender system, where the goal is to suggest a personalised summary to a user based on their preferences. Therefore, we keep humans in the loop by providing feedback through interaction. We also propose a preference-based interactive summarisation model to extracts users' interests to learn and generate user-adapted results. We present the content in a condensed fashion using summarisation while interacting with the system. The proposed method, 'SumRecom', learns to predict users' preferences to generate summaries utilising their feedback by creating a behavioural model that relies on reinforcement learning (RL). We also use an inverse RL (IRL) algorithm to automatically evaluate a summary based on a domain expert's previous history evaluation. The representation unit is a sentence, meaning the model follows an extractive approach [16].

## Contribution 6: Personalised Summarisation Approach to Predict Users' Desired Structured Summaries Based on the Proposed Hierarchical Structure

Predicting users' desired structured summary is another challenge addressed in this dissertation. We examine the automatic production of personalised and structured summaries to dynamically maintain a federated summary view incrementally, resulting in a unified framework for an intelligent summary generation. We first propose a hierarchical, personalised, concept-based summarisation approach, which sums up a collection of documents in a concise hierarchical concept map based on users' feedback. Instead of providing a short and static summary, the approach engages users by querying their preferences and utilising an RL algorithm to learn how to generate useradapted content through a hierarchy. The proposed model improves the deficiency of traditional approaches in various aspects such as subjectivity aspect and finding interesting patterns and relationships in different collection parts interactively.

### 1.2.4 Dissertation Organisation

This dissertation is organised as follows. We first discuss the fundamental background and a discussion of the current state-of-the-art approaches in Ch. 2. We explain what document summarisation is in more depth, and offer a new perspective on the related work for describing different categories towards personalising summaries. The summarization task is defined formally, and the challenges are discussed in the following.

Ch. 3 discusses in depth the experimental set-up, evaluation metrics, and the required data to train and evaluate the proposed summarisation models. Ch. 4 then focuses on the central task of document summarisation and the role of feature engineering. We propose a novel approach to dynamic feature space mapping to tackle the problem. We then evaluate the proposed approaches experimentally to assess the applicability of modelling for future tasks.

Ch. 5 explores the problem of automating intelligent and interactive summarisation. We propose a hierarchical structure for this purpose. Based on the proposed structure, we provide two solutions for interactive summarisation-SNARS and FNARS - followed by human and automatic evaluation of the proposed approaches.

Ch. 6 discusses the problem of automating intelligent and personalised summarisation. We focus on alternative models for personalising summarisation and predicting desired summaries for specific users. Different solutions for a personalised and interactive concept-based summarisation approach are posited. Each predict users' desired extractive and unstructured and structured summaries based on their feedback, as well as the personalised information-seeking path. Then, a comprehensive evaluation of each approach is given.

Ch. 7 develops different applications of the technology discussed in this thesis. We discuss how our model facilitates the representation and analysis of documents in various domains and address three specific applications, including:

- the use of summarisation in detecting anomalies in network traffic data
- application of summarisation in healthcare analytic problems
- using summarisation to narrate business process data.

We also propose a novel approach called 'Summary2vec', which presents each summary by a fixed-length vector using a novel architecture. The goal is to create a numeric representation of summaries as an individual related unit of meaning conveying one or more aspects of information space. Summary2vec is remedial, in that it helps to design automatic services for various analytic purposes that require information-seeking activities.

Finally, Ch. 8 summarises the findings and outlines promising directions for future research. We close the chapter by highlighting the remaining challenges to encourage and guide possible future directions on this research topic.

## Background and Related Work

This dissertation investigates the problem of intelligent, personalised and human-inthe-loop document summarisation. This chapter discusses the fundamental concepts in the field and state-of-the-art document summarisation techniques. We start with an overview of document summarisation and the definition, followed by a comparison with document compression (Sec. 2.1). We conclude that there is no ideal summarisation approach, as summarisation is defined according to the needs of the application and individual users.

Sec. 2.2 categorises state-of-the-art approaches based on the common categorisation style, including input type, purpose type and output type. Each category and the following subcategories are also explained. We then propose a new categorisation schema including traditional summarisation, structured summarisation, and interactive and personalised summarisation. Sec. 2.3 next discusses the need for feature engineering in
document summarisation and explores the various existing features (with their respective definition), including term-level, sentence-level, paragraph-level and corpus-level features.

Sec. 2.4 presents various works in traditional automatic summarisation, especially more recent ones. We also explain the need for structured (Sec. 2.5), interactive, and personalised (Sec. 2.6) summarisation approaches. The chapter is concluded in Sec. 2.7. We present both the challenges and limitations that prevent progress in the field, and further highlight the remaining problems and gaps in personalised document summarisation. These challenges are interesting for researchers as a guide for future research.

### 2.1 Document Summarisation: Overview

Producing a summary is complicated even for a domain expert, yet it can be even more difficult for machines. The machine should have the ability for learning NLP and producing summaries and background knowledge suitable for humans. This section explains different summarisation definitions and compares the summarisation task with the compression task.

### 2.1.1 Definition

Summarisation creates the best representation of the original data, enabling efficient storage, quick browsing, and retrieval of a large collection of data without loss [17]. However, there is no unique definition for summarisation, meaning it can be understood based on application or user. For instance, summarisation can be defined as the process of reducing data size or finding the important part(s) of data while eliminating redundant or non-relevant data.

The most general definition for summarisation is the automatic mechanism of generating brief and condensed representations of the content [18]. A summary can also be defined as concise, informational, and grammatically correct text without redundancy [19]. A summary is also defined as a shorter version of a document generated by
a machine to draw the most significant information in a more concise format without human assistance $[20]$.

Radev et al. [21] provided a more recent definition, framing summarisation as 'a text that is produced from one or more texts, that conveys the important information in the original text(s) and usually significantly less than that'. According to this definition, three important issues should be considered:

- Summaries are produced from single or multiple documents.
- Summaries should preserve the important parts of the original text.
- Summaries have to reduce the original text by at least $50 \%$.

Defining what is important in this definition is a challenging task. For example, in query-based summarisation, a good summary should cover topics related to the query. Conversely, it is more challenging to decide which aspects are interesting to readers when it comes to generic summarisation systems - finding a balance between the main and other related topics $[22,23]$. Size is also an essential aspect of summarisation. However, size is the main aspect in developing compression-based approaches. Sec. 2.1.2 compares summarisation and compression approaches for clarification.

### 2.1.2 Document Summarisation v. Document Compression

While text summarisation aims to discover relevant information from multiple documents and prepare this in a concise readable format for users, document compression seeks to reduce the amount of data required to represent documents. Therefore, document compression employs filtering approaches to tackle information overload. The document compression concept derives from the idea of compressing data using encoding techniques used in information theory [24]. Text compression techniques condense sentences while keeping the important information. Text compression has a wide variety of practical applications such as compressing microblogs and generating headlines for news articles. Text compression approaches are classified into two groups, including deletion-based and abstractive procedures.

## Deletion-based Text Compression

Deletion-based text compression approaches work based on the idea of reducing without significant loss [25]. Therefore, the goal is to remove as many extraneous words from a (set of) document(s) without diminishing the text's main content or sentence transformations [26]. 'Data-intensive processing' and making data 'lean' are two main subcategories of deletion-based text compression.

Early approaches belong to the lean category since they follow an unsupervised paradigm, such as an integer linear programming-based approach [27]. Consequently, they do not require training data but rather employ a language model to extract the most compressed sentences instead of using training sentence-compression pairs. Conversely, the data-intensive approaches are supervised and require sentence-compression pairs for training. Other proposed modelling approaches include the noisy-channel model [21, 28, 29], variational auto encoders [30] and Seq2Seq models [31]. A recent approach proposed by Zhaoet al. [32] is based on a new language-model-based evaluator. They use trial-and-error deletion operations and the RL algorithm to get the most desirable target compression.

## Abstractive Text Compression

Abstractive models produce more compressed texts by inserting, reordering or deleting operations-similar to abstractive text summarisation techniques [29]. A recent abstractive compression model is a tree-to-tree transduction model using synchronous tree-adjoining grammars [33] to obtain all different formats for rewriting a sentence Other approaches include using attentive long short-term memory (LSTM) models used for caption compression [34], and a Seq2Seq model decoder [35].

### 2.2 Document Summarisation Categories

Document summarisation approaches are categorised based on the input, purpose and output type. A graphical structure of these categories is depicted in Fig. 2.1.



Figure 2.1: Document summarisation categorisation.

### 2.2.1 Categorising Based on Input Sources' Properties

We examined the input documents using three criteria: (i) input size (how many documents a system can have as input), (ii) domain specificity (domains that the model can handle), and (iii) input format (the structure of documents).

## Single-document Summarisers v. Multi-document Summarisers

Early works on summarisation focused on a single document. However, recently, due to the fast development of documents, MDS has gained more attention [5]. Singledocument summarisation approaches process just one input document, and the first
work in this category returns to 50s [36-38]. Conversely, multi-document summarisers gather many documents on the same topic as input, enabling diversification of information sources and redundancy simultaneously [39].

## Domain Specificity: General Input v. Domain-specific Input

The input documents can be general or related to the same domain, such as legal documents or biomedical documents. However, it is more suitable to develop a summarisation system specific to a domain to reduce term ambiguity, use grammar and formatting schemes, and facilitate the use of domain knowledge by enhancing relevancy detection. An example is a medical text summarisation where the authors use domainspecific cue phrases and other features to find relevant sentences [40]. Another example is LetSum, a summarisation system for legal [41] and biomedical texts [42].

## Input Format: From Textual to Multimedia Documents

Input documents are in varied forms based on their structures, mediums and scales. The structure relates to the document organisation. For example, the structure of a scientific article typically includes an introduction, related works, methods, experiments and conclusions. Focusing on the structure is the basis of some approaches to generate summaries, as this increases summarisation performance [41].

Scale is another aspect that affects performance. For example, in many known summarisation systems, term frequency is used for measuring relevancy. Consequently, the input document should be large enough to detect essential concepts. Conversely, common techniques do not work for summarising low-scale documents such as tweets and microblogs, [43]. Instead, trending phrases or a phrase specified by users, such as a hashtag, can be selected as a topic [44].

The medium is another critical aspect that carries information. While most summarisation systems focused on textual support, there exists some work on summarising images, audio and videos [45]. Recently, there has been increased interest in multimedia summarisation. Examples include interactive football summarisation [46], summarising important events in a football video [47], video summarisation using web
images [48], video summarisation using a given category [49], and video summarisation by learning $[50]$.

### 2.2.2 Categorising Based on Summarisation Purpose

According to the summarisation goal, summarisation approaches are categorised based on the audience, content and expansiveness.

## Audience: Generic v. Query-oriented Summarisation Approaches

The concept of importance is different for different users. For example, a user may need to focus on specific aspects of a document rather than the input document's main idea. In these scenarios, the interest can be defined by a query. In a queryoriented summarisation approach, a good summary is judged according to a user's query. One common technique in this category is to adapt existing summarisation approaches to answer a query. Topic signature words or graph-based approaches [51] and submodular approaches [52] are examples of common approaches in this category. Other approaches also exist, which are explicitly designed for answering queries [53]. In contrast to a query-based approach, a generic summarisation method tries to preserve important information presented by the author from an input document [54-56].

## Content: Indicative v. Informative Summarisation Approaches

'Informative summaries' include the primary information of the original documents and help users find their interests by extracting the main idea(s). Most existing summarisation approaches are informative ones. Conversely, 'indicative summaries' only include a global representation of the original document(s) and can be helpful to decide whether to refer to the original source.

## Expansiveness: Update Summarisation v. Background Summarisation Approaches

A generated summary may focus on the original document's background or compare it to past documents, referred to as the 'expansiveness' metric. A 'background summarisation' algorithm produces summaries based on the input content without eliminating information from prior related documents [57]. Conversely, 'update summarisation' should convey information beyond what is already known. The goal is to generate summaries from recent documents that do not include prior information, known as 'novelty'. Extracting novelty in addition to salience can be modelled using latent Dirichlet allocation or through incremental hierarchical clustering [58].

### 2.2.3 Categorising Based on Output Summary Properties

According to the output summary, summarisation algorithms are classified based on three measures: (i) the derivation process (the process applied to generate a summary from the primary document), (ii) partiality (how a summary handles the original document's opinions), and (iii) the summary's format.

## Derivation: Extractive Summarisation v. Abstractive Summarisation

The derivation measure refers to the process of obtaining a summary-that is, extracting important parts or producing a new summary. Abstractive summaries are generated by interpreting the main concepts of a document, and then stating those contents using clear and natural language $[59,60]$. Abstraction techniques are a substitute for the original documents rather than a part of them. Therefore, abstractive approaches require deep NLP such as semantic representation and inference. However, these are challenging to produce due to the current limitation in linguistic techniques.

Conversely, extractive methods are more popular because of their comparative simplicity. This approach usually contains three steps, involving (i) representation of the original text document, (ii) sentence scoring, and (iii) selecting high-scoring sentences
in the summary. Extractive summaries are generated by selecting units as the representative of the original documents, usually measured in sentences, whose grammatical structure is easy to maintain. These sentences are then concatenated into a shorter text to produce a meaningful and coherent summary $[61]$.

## Partiality: Opinion-based Summarisation v. Neutral Summarisation

Produced summarisation can be neutral or opinion based. Neutral summarisation algorithms produce summaries that reflect the input documents' content without judgement or evaluation, even if they are judgemental in nature. Most existing summarisa-

tion works belong to this category $[55,56]$. In contrast, opinion-based summarisation algorithms include automatic judgements either implicitly or explicitly. An explicit judgement includes some opinion statements in the summary, while the implicit one uses bias to add and/or omit material. With the growth of interest in users' opinions, this kind of summarisation is more popular. For example, one approach summarises customer opinions through Twitter by extracting the different product features and the conversation messages' polarity $[62]$.

## Format: Output Format

Produced summaries can feature in various formats, including structured in a concept map format [15] or unstructured in the form of some sentences using a different template [63]. Summaries may also focus on users' preferences or goals. For example, the OntoSum system [64] uses device profiles such as mobile phones and web browsers to adjust the summary formatting and length.

### 2.2.4 Language-based and Application-based Categorisation

This section discusses different categories of summarisation algorithms based on language and application of document summarisation.

## Language Model

Based on the input documents' language, three different categories exist for summarisation: monolingual, multilingual or cross-lingual. In a monolingual summarisation algorithm the source and the target language are the same and specific. Multilingual summarisation approaches accept documents in different languages and produce the output in the same language [65]. For example, SUMMARIST [66] is a multilingual summariser that is available in English, Japanese, Spanish, Arabic, Indonesian and Korean and FarsiSum [67] (which is a monolingual text summarisation system for Persian). In a cross-lingual summarisation system, the source text is written in one language and the user can choose the language of the output summary [68].

## Application

Document summarisation has many real-world applications, which have been studied at length. Examples include summarisation for emails, online news and social media; customer reviews; scientific articles; and both medical and legal document summarisation. The following describes email and scientific paper summarisation in more detail.

Emails have some distinct characteristics such as the interactive dialogue nature, as in verbal communications. Nenkova et al. [69] offer initial progress in this field by generating a summary of thread discussions. Newman et al. [70] further proposed a system to summarise a full inbox rather than a single thread. They clustered messages into topical groups and then obtaining summaries for individual clusters.

In scientific paper summarisation, there is a substantial amount of research to be used to identify essential sentences in an original article. One approach is to use a language model that indicates a probability to words mentioned in the citation context sentences, following by scoring the sentence importance in an original paper using the Kullback-Leibler divergence method [71].

### 2.2.5 Proposed Categorisation Schema

The problem of automatic document summarisation is an old challenge, and many approaches exist for various purposes to solve one key drawback of previous methods. The following lists different metrics to evaluate a good summary from various perspectives [15]. Based on the goal and the application, a summarisation approach should:

- contain an overview of the chosen documents
- remove redundancy
- present the various relations in documents
- generate summaries with great detail while also covering the main topics
- be user friendly
- be multidimensional and cover different aspects of documents
- produce personalised summaries based on the user's goal(s).

Based on these criteria, the existing gaps and the requirements of good document summarisation, we categorised state-of-the-art approaches as (i) traditional, (ii) structured, and (iii) interactive and personalised. The proposed hierarchy is depicted in Fig. 2.2. Before explaining each category and the leading approach in each category, we first describe feature engineering in document summarisation, required to explain state-of-the-art techniques.

### 2.3 Feature Engineering in Document Summarisation

Abstractive approaches require deep NLP such as semantic representation and inference. However, they are challenging to produce and require maturation. The goal of



Figure 2.2: Proposed categorisation schema for document summarisation.

automatic extractive summarisation is to rank the important sentences in a document set (i.e., sentences containing maximum information about the document's topics). Therefore, sentences should be represented based on certain features. This section explains state-of-the-art features and the proposed approaches to learn optimal feature sets.

### 2.3.1 State-of-the-art Features

Luhn [36] was the first to address the automatic document summarisation problem in the 1950s using the keyword frequency feature. Other features were later proposed, including cue words, title words and sentence location [38]. Church et al. [72] proposed other new features such as sentence length cut-off, fixed phrases, paragraph features, thematic word features and upper-case word features. Later, Hovy and Lin [73] verified
that the position method is not applicable and efficient for all domains. Therefore, other features such as term frequency-inverse document frequency (TF-IDF),cue words, sentence location, and longest common subsequences (LCSs) were proposed for sentence scoring $[74]$.

Many other features have been also proposed over the years to improve the performance of automatic document summarisation. We categorised existing features summarisation in four groups, covering term-level features, sentence-level features, paragraph-level features and corpus-level features [75]. Table 2.1, 2.2, 2.3.1 and 2.3.1

TABLE 2.1: Term-level Features

| Feature | Description |
| :--- | :--- |
| Term Frequency | Frequent words mentioned in the document. |
| TF-IDF | Frequent words considering other terms. |
| Cue Words | Sentences includes cue words. |
| Title Similarity | Sentences containing words from the title. |
| Uppercase word | Sentences include upper-case words. |
| Positive Keyword | Frequent keywords occurring in the summary. |
| Negative Keyword | Keywords not frequently occurring in the summary. |
| Residual IDF | The residual IDF of a word. |
| Gain | Features based on hypothesising which moderately frequent <br> words are most important in a document. |
| Term Co-occurrence | Clusters of important words are identified and weighted. |
| Query Score | Sentences are scored according to the number of query terms. |
| Synonyms | Synonyms are matched using WordNet or other tools. |
| Significant Word | Relative significance of words. |
| Title Similarity | Squares the number of common terms between a document's <br> title and each sentence. |

Table 2.2: Sentence-level Features

| Feature | Description |
| :--- | :--- |
| Sentence location | Position of sentences determine the weights. |
| Semantic structure | Using a graph structure where node are sentences, and related sentences <br> are recognised by edges between them. |
| Length Cut Off | Too short or too long sentences are eliminated. |
| Fixed Phrase | Sentences containing some fixed phrases, known as indicator <br> phrases, are given priority. |
| Concept Signature | Topic words and the associated pairs are selected (co-occurrence feature). |
| Concept Count | Counts the concepts' occurrence instead of individual verbs and nouns. |

Table 2.3: Paragraph-level Features

| Feature | Description |
| :--- | :--- |
| Paragraph Position | Sentences are weighted according to their paragraph' position. |
| Optimal Position | A sequence of most important sentences are identified. |

present some important features in each group, with brief descriptions.

### 2.3.2 Learning Optimal Feature Set

Features are applied individually or collectively according to the application and the proposed model. Typically, a different set of combinations is required to obtain optimal

Table 2.4: Corpus-based Features

| Feature | Description |
| :--- | :--- |
| Signature word | Frequency of word occurrence averaged across a large corpus is used. |
| Baseline Probability | Using baseline documents, we define a term's importance <br> such that more frequent words have higher probability. |
| Document Probability | Estimates a term's likeliness of within a document. |

results. Rafael et al. [76] tried combining different word-, sentence- and graph-level features for scoring sentence. Meena and Gopalani [77] evaluated available features and analysed the results of combining different features. As discovered, finding the optimal feature set remains a challenge. One solution is to test different combinations of features and report the best feature for each document [75]. However, as the number of features increases, the approaches become less practical. Besides, most existing approaches give equal weight to all features - a solution in which each feature is weighted based on its respective importance. To the best of our knowledge, there is no feature weighting algorithm for extractive document summarisation.

In addition to features, different models also have been suggested for recommending features. Fattah and Ren [78] proposed supervised models including genetic algorithms (GAs), probabilistic neural networks, feed-forward neural networks, mathematical regression, and a Gaussian mixture model. The authors used various features to train the summarisation model, including sentence position, relative sentence length, positive and negative keywords, sentence resemblance to the title, named entity in the sentence, sentence centrality, numerical data, and aggregate similarity. Elsewhere, Prasad and Kulakarni [79] used word similarity among paragraphs, iterative query scoring, word similarity among sentences, as well as a format-based score, term frequency, cue words, and tile similarity as features to score sentences. Abuobieda et al. [80] further used title feature, sentence position, numerical data, sentence length and thematic words. In another study, Mendoza et al. [81] used title similarity, sentence position, cohesion sentence length and coverage as the features. Optimisation techniques were used with evolutionary algorithms to generate summaries. However, the goal of weighting in these problems is to measure the importance of sentences and to select them, not to weight the features $[81,82]$.

Recent approaches use deep learning methods such as convolutional neural networks $[83,84]$, a recurrent neural network (RNN) $[85,86]$, or a combination of the two $[87,88]$. Consequently, they do not need handmade features. Although these approaches could gain outstanding results in terms of performance, they are neither efficient nor interpretable, and even require a large volume of training data - one of the
key challenges in summarisation. Besides, they cannot estimate each feature's role in the summarisation task and for each class separately.

### 2.4 Traditional Summarisation

The main categorisations in document summarisation are abstractive, extractive and hybrid approaches. Each of these categories and their subcategories is explained in this section. Since the focus of this dissertation is on extractive approaches, they are analysed in greater detail.

### 2.4.1 Abstractive Approaches

Abstractive summaries are generated by interpreting the main concepts of a document, and then stating those contents in a clear and natural manner $[59,60]$. Abstraction techniques are a substitute for the original documents rather than a part of them. Therefore, abstractive approaches require deep NLP such as semantic representation and inference. However, they are challenging to produce and need time to mature. The reason is that today's systems and computing devices cannot provide semantic representation, inference and natural language to such a level that is equivalent to humans. Abstractive summarisation approaches are mainly classified into two groups: structure-based approaches and semantic-based approaches [63, 89]. The structurebased approach aims to find a schema that can describe the document, including template-based methods, rules-based methods, and ontology- and tree-based procedures. In semantic-based strategies, a document's semantic structure is used, including linguistic data (i.e., noun and verb phrases) and semantic graph-based approaches.

### 2.4.2 Extractive Approaches' Structure

Extractive text summarisation approaches select some sentences as representative of the original document(s). These sentences are then concatenated into a shorter text format to produce a meaningful and coherent summary [61]. An extractive approach
usually contains three steps, including representation of the original text document, sentence scoring, and then selecting high-scoring sentences. These three steps are the basis of various categories of extractive approaches.

## Representation Model

Before performing any summarisation algorithm, the original text requires to be converted to an intermediate representation model. Generally, there are two main representation models: 'topic' representations and 'indicator' representations [90] which are different considering the representation model and complexity. Indicator representation approaches represent sentences in the form of features (indicators), discussed in Sec. 2.3. Topic representation approaches convert the text into an intermediate model and interpret the text.

## Sentence Scoring

When an intermediate representation is generated, each sentence is scored based on its importance. A sentence's score is computed based on the covered topic in the original documents in a topic representation approach. Conversely, indicator representation methods aggregate the evidence from different indicators using techniques such as machine learning.

## Generating Summaries

Eventually, the summariser selects the top most important sentences based on a size limit parameter to generate the final summary. Greedy algorithms such as converting the sentence selection into an optimisation problem are also used to select important sentences. In this setting, a set of sentences is chosen to maximise overall importance and minimise redundancy.

### 2.4.3 Extractive Approach Categorisation

This dissertation categorises extractive approaches as statistical approaches, graphbased approaches, knowledge-based approaches, and machine learning approaches.

## Statistical (Early) Approaches

Early approaches on document summarisation combined various features (defined in Sec. 2.3) to score the relevancy of selected text units. However, combining some features does not guarantee summary improvement. Two significant approaches in this category are Lead-3 and the phrase-based ILP model [91]. Lead-3 selects the three leading sentences as the summary, and the phrase-based ILP model [91] is based on a linear programming formulation that learns to combine phrases considering such features as coverage, length and grammar constraints. Although this category relies on shallow features, these two approaches still report promising results.

## Graph-based Approaches

Graph theory has been used in many approaches for representing the semantic structure of a document [92]; therefore, it is appropriate for document summarisation tasks. For graph-based methods, each text element (words or sentences) is treated as a node [20, 59, 93, 94]. Two nodes or specifically two sentences are connected with an edge if they share some similarities. Two types of graphs are used to represent text: these are 'lexical graphs', which use the lexical features of the text and 'semantic graphs', which use the text's semantic properties, such as the ontological relationship between words. The relationship between a set of words represents the sentences' syntactic structure (dependency tree and syntactic trees). TGRAPH [95] and URANK [96] are two significant approaches that use a graph model and ranking scores for each sentence obtained in a unified ranking process. Further, TextRank [97] and LexRank [59] use lexical features to create a graph. The difference between the two is that the similarity measure in TextRank is estimated by counting the number of similar words between two sentences, whereas LexRank utilises the cosine similarity among sentences [98].

Other approaches to find similarity measures between the nodes involve discounting, the cumulative sum method [93] and position weight [94].

## Clustering-based and Frequent Term Approaches

Clustering-based approaches group together the related information retrieved from similar documents and passages. After clustering, sentences are ranked within each cluster. Their salience scores are calculated, and high-scoring sentences from each cluster are extracted to form the summary [93].

Conversely, frequent term approaches seek the frequent and semantically similar terms in documents [99]. Semantic similarity checks the path's length linking the terms and further measures the content difference and similarity. The summariser selects sentences including the most frequent and semantically related terms.

## Knowledge-based Summarisation Approaches

The automatic text summarisation aims to create summaries similar to human-created summaries. One solution is to combine summarisation techniques with knowledge bases (semantic-based or ontology-based summarisers) such as Wikipedia, YAGO and DBpedia to consider the semantics of words. For example, Sankarasubramaniam et al. [100] employed Wikipedia along with a graph-based ranking technique. Another example is the YAGO-based summariser [100] that utilises YAGO ontology [101] to classify key concepts in a document set.

## Optimisation-based and Machine Learning Approaches

This dissertation characterises recent, state-of-the-art summarisation approaches as an optimisation problem, a fuzzy problem or a machine learning problem.

Summarisation as an optimisation problem. Optimisation algorithms have been widely used for various summarisation purposes. The most common algorithms are the GA [102] and particle swarm optimisation [103]. A GA is a search-based optimisation algorithm inspired by two concepts of evolution and population genetics. It generates random solutions and optimises population by applying natural operations
such as selection, mutations and crossover. GAs also create an initial population randomly. The algorithm evaluates each population member based on a defined fitness measure and assesses according to some preferred requirements. The algorithm then selects some individuals while favouring higher fitness (selection) and generating new samples by combining the chosen individuals' features (crossover).

Particle swarm optimisation is another commonly applied bio-inspired algorithm used to obtain an optimal solution, inspired by birds' social movement [104, 105]. It initiates with a randomly discovered population of particles with a random position and a velocity. Then, a velocity vector is calculated for each individual. Their respective position is updated using its former position and the recently renewed velocity vector before converging.

Summarisation as a fuzzy problem. Fuzzy logic has been widely used in summarisation systems. Fuzzy systems take text features as input, and the algorithm transforms them to a fuzzy linguistic values (fuzzifier). Fuzzy rules in the form of 'if-then' statements are used to generate the outputs $[106,107]$. he fuzzy evolutionary optimisation method (FEOM) [23] is another approach in this category, which clusters the documents and selects the most important sentence in each group.

Machine learning for summarisation. Machine learning algorithms are widely used for summarisation using supervised, unsupervised and semi-supervised approaches. Supervised learning algorithms require a large amount of labelled data for training. These algorithms model summarisation as a binary classification sorted either as 'in summary' or 'not in summary'. Therefore, different machine learning algorithms used for classification can also be used for this purpose. Commonly used supervised learning algorithms include regression, support vector machines, naïve Bayes classification, and decision trees $[5,20]$.

Unsupervised learning algorithms aim to discover the hidden structure of data without the need for labelled data. Commonly used techniques include clustering and the hidden Markov model (HMM). The 'query, cluster and summarise' technique [108]
is another system based on the HMM that computes the probability of each sentence as being appropriate for the summary set. Meanwhile, semi-supervised learning algorithms require both labelled and unlabelled data, whereas conditional random fields [109] consider the summarisation task a sequence-labelling problem.

Recently, the focus has shifted to neural network-based and deep RL methods, which could show promising results. Both employ word embedding [110] to represent words at the input level, and then feed this information to the network to gain the output summary. These models mainly use a convolutional neural network [83], an RNN $[85,86]$ or a combination of the two $[87,88]$. Although these approaches could gain outstanding results in terms of performance, they are not efficient and interpretable. Neural network sentence extraction (NN-SE) [85] is a neural network model composed of a hierarchical document encoder and an attention-based extractor; SummerRuNNer [86] is an RNN-based sequence model; and the hierarchical structured self-attentive model for extractive document summarisation (HSSAS) [111] is a neural network model with a hierarchical structured self-attention mechanism to create both sentence and document embedding. Last is BanditSum [112], a neural network model that considers summarisation a contextual bandit (CB) problem.

Lately, RL approaches have been proposed for both extractive and abstractive summarisation [113-115]. Most existing RL-based approaches use heuristic and greedy functions as the reward function and, therefore, do not require reference summaries [113, 116]. Other approaches use different recall-oriented understudy for gisting evaluation (ROUGE) measure variants as the reward function and, therefore, require reference summaries to reward RL $[114,115,117]$. The reward quality is a bottleneck for RLbased summarisation approaches $[118]$.

### 2.4.4 Hybrid Extractive and Abstractive Approaches

Hybrid approaches combine both abstractive and extractive techniques. A hybrid approach commonly consists of an extractive phase to extract the key sentences from the input text and an abstractive phase to generate the final abstractive summary. The two approaches are interrelated and the overall summarisation performance is
enhanced. However, the research community focuses more on extractive techniques since their abstractive counterparts are highly complex and need extensive NLP. One example is an approach that uses a graph model to obtain the key sentences in the extraction phase, and an RNN-based encoder-decoder for abstraction phase [119].

SumItUp [120] is another example that employs some statistical features and a semantic feature (emotion described by the text) to generate a summary. For removing redundant sentences, Cosine similarity is used. A language generator takes the extracted sentences to transform the extractive summary into an abstractive summary. Sentences are reordered to retain the original sequence.

### 2.5 Structured Summarisation

Traditional summarisation approaches are incapable of producing more extended summaries since all details are omitted, even if the user is interested in obtaining more information. Besides, the produced summaries are unstructured and, therefore, difficult to unpack for further analysis. This prompts the need for structured summarisation. Structured summaries are defined by generating Wikipedia articles and biographies [121]. We categorised structured summarisation approaches into four groups, covering (i) timeline summarisation approaches, (ii) document thread summarisation, (iii) hierarchical summarisation, and (iv) concept map summarisation.

### 2.5.1 Timeline Summarisation

Timeline approaches commonly produce a short summary to form a story based on dates. Using partial ordering relations [122] to link the events in a narrative and a temporal representation of events according to time intervals [123] are examples of timeline summaries.

Some approaches emphasise the summarisation aspect for generating timelines from multiple articles. One example is to formalise generating timeline problems as an optimisation problem that balances coherency, diversity and summary quality [124]. Another model is a summarisation-based approach to create timelines based on the
inter-date and intra-date sentence dependencies [125]. Other approaches identify the most important dates and the bursts of news that surround them, and then categorise events based on the burst time $[126-130]$.

### 2.5.2 Document Thread Summarisation

Discovering threads of related documents is another category of structured summaries. These mostly employ a machine algorithm to find the threads using a supervised approach. Features include the temporal sector of stories for recognising events and order of time to capture dependencies [131]. Others used a hybrid clustering and topic modelling approach to cluster news articles [132], or statistical models to detect trends and topics from document $[133]$.

Identifying coherent threads of documents is another category among structured summarisation algorithms. One proposed algorithm formulated components of an article chain and connected two specified articles [134]. In the literature, Gillenwater et al. [135] a probabilistic technique was proposed to extract a set of threads from a document set. Shahaf et al. [136] extended the work by implementing the idea of metro maps in scientific areas $[137]$.

### 2.5.3 Hierarchical Summarisation

The relationship between summarisation and hierarchies are analysed in the literature [138-140]. However, the hierarchy in these approaches is the relation between different elements of a document, such as words or phrases [138-140]. A hierarchy is also defined as a structure prioritising more general information $[141,142]$ or spreading the summary out across the hierarchy $[143,144]$. A recent hierarchical summarisation approach is SUMMA, which produces a hierarchy of relatively short summaries. The hierarchy is based on time intervals and, therefore, can also be considered a timeline approach $[145]$.

### 2.5.4 Concept Map Summarisation

Concept map MDS approaches produce structured summaries in the form of concept maps. A concept map that extends the mind map idea introduced by Novak and Gowin [146] is a labelled graph showing concepts as nodes and the relations between them as edges. Different techniques have been suggested for single documents [147-150] and multiple documents [151-154]. Different document models have also used concept maps, including in scientific papers [154], legal documents [153], student essays [148] and general webpages $[151]$.

The first step in creating a concept map is to extract the concepts and relation spans from the input documents. Extracted mentions refer to the same concept or the relations that require grouping. Concept and relation labelling and importance estimation are the final steps in creating a summarised concept map. The most recent approach in concept summarisation was proposed by Falke [15]. This approach learns to identify and merge coreferent concepts to reduce redundancy, determine their importance with a robust supervised model, and find an optimal summary through ILP.

### 2.6 Interactive and Personalised Summarisation

Interactive NLP algorithms ask users to provide certain feedback forms to refine the model and generate higher-quality outcomes tailored to the user. Multiple forms of feedback have also been studied for different applications including mouse clicks for information retrieval [155], post-edits and ratings for machine translation [156, 157], error markings for semantic parsing [158], and preferences for translation [159].

Most existing computer-assisted summarisation tools present essential parts of documents to the user using a traditional automatic summarisation algorithm, and then ask users to refine the results without further interaction. The refining process includes cutting, pasting and reorganising the essential elements to formulate a final summary [160-162]. Other works present automatically derived hierarchically ordered summaries that allow users to drill down from a general overview to detailed information $[145,163]$. Therefore, these systems are neither interactive nor consider user
feedback to update their internal summarisation models. Other interactive summarisation systems include the iNeATS [164] and IDS [165], which allow users to tune several parameters (e.g., size, redundancy and focus) for customising the produced summaries. Avinesh and Meyer [166] proposed a more recent interactive summarisation approach that asks users to label important bigrams within candidate summaries. Their system can achieve near-optimal performance in 10 rounds of interaction in simulation experiments, collecting up to 350 critical bigrams. However, labelling important bigrams is an enormous burden on users, as they have to read many potentially unimportant bigrams.

There is increasing research interest in using preference-based feedback and RL algorithms in summarisation. For example, one approach learns a sentence ranker from human preferences on sentence pairs [167]. The ranker is then used to evaluate the quality of summaries by counting the number of high-ranked sentences included in a summary. This preference-based RL algorithm has also been used in summarisation. The structured prediction from partial information (SPPI) $[168,169]$ is a policygradient RL algorithm that receives rewards from the preference-based feedback. The problem is that SPPI suffers heavily from the high sample complexity problem.

Another recent preference RL approach is APRIL [170], which has two stages. First, the user's ranking over candidate summaries is retrieved, and then a neural RL agent is used to search for the optimal summary. However, favouring one summary to another in both approaches places considerable burden on users. It is worth re-mentioning that summarisation aims to provide users with a summary that reduces the need to read multiple documents. However, asking users to prefer a summary to another in multiple rounds among a summary space that includes all randomly possible combinations of sentences only adds more cognitive load.

### 2.7 Summary

This chapter provides an overview of document summarisation (Sec. 2.1) and explores several different categories based on various parameters, including input size, purpose
type, output properties, and language and applications, with brief descriptions of each (Sec. 2.2). Also proposed was a new categorisation schema based on current gaps in state-of-the-art approaches to summarisation (Sec. 2.2.5). The proposed categorisation schema includes traditional approaches, structured approaches, and interactive and personalised summarisation approaches.

Sec. 2.3 outlined the existing methods and techniques for feature engineering in document summarisation, including the various proposed features. Traditional approaches - including extractive, abstractive, and hybrid extractive and abstractive approaches - are discussed in Sec. 2.4. Sec. 2.5 then explored the different structured summarisation approaches, including timeline and document thread summarisation, hierarchical summarisation, and concept map summarisation, followed by an explanation of various interactive and personalised approaches (Sec. 2.6). In summary, there are four main limitations facing the current summarisation approaches, addressed in the following chapters:

- There is a need for intelligent automatic feature engineering in summarisation that can capture each feature's importance based on the defined score.
- Flexible and interactive approaches are needed to facilitate improved summary navigation based on users' interests.
- There is a lack of personalised summarisation approaches that can predict the desired summary for a specific user based on their individual behaviour.


## Experimental Setup

This chapter outlines the experimental set-up, the datasets used in our experiments, and the evaluation metrics to evaluate the proposed models. These factors are considered when comparing each of the proposed approaches in this thesis.

### 3.1 Dataset

Different datasets are created for various summarisation applications. We used the same dataset to evaluate the proposed approaches in this dissertation: these are the DUC dataset and the CNN/Daily Mail dataset.

### 3.1.1 DUC Datasets

DUC datasets are the most common datasets used in text summarisation research, provided by the National Institute of Standards and Technology. DUC datasets are released online as part of the summarisation shared task hosted at the DUC each year. ${ }^{1}$ However, access to the data requires permission. Each dataset contains both documents and their corresponding summaries, which are created manually or automatically, either as baseline summaries or generated by challenge participants' systems. These datasets are in English and are sourced from the news domain. They can be used for both single-document summarisation and MDS. In this dissertation, we used DUC2001, DUC2002 and DUC2004. DUC2001 contains 60 sets of approximately 10 documents that cover various subjects. DUC2002 contains 567 document summary pairs divided into 59 clusters. DUC2004 contains 100 sets of approximately 10 documents that cover various subjects. To forge a valid comparison between the approaches, we used an experimental setting similar to the state-of-the-art approaches explained in each section.

### 3.1.2 CNN/Daily Mail Datasets

The CNN/Daily Mail dataset [171] is an English dataset created for passage-based question-answering tasks. However, a modified version of this corpus has been extensively used for evaluating summarisation systems [86]. The dataset is in English, is publicly available, and contains online news articles. ${ }^{2}$ Each dataset comprises a set of document clusters accompanied by several human-generated summaries used for training and evaluation purposes. The dataset includes news articles (781 tokens on average) matched with multi-sentence summaries ( 3.75 sentences or 56 tokens on average), 287,226 training pairs, 13,368 validation pairs and 11,490 test pairs.[^0]

### 3.2 Evaluation Metric

One approach to evaluate produced summaries is by comparing the generated summary and the reference summary. Comparing summaries to the original text helps to understand the measures, including information loss. Conversely, comparison to a reference summary will quantify the quality of summaries against humans. In both situations, the evaluation strategy is deemed 'intrinsic' in nature, since it is compared against itself as a content evaluation method or to verify linguistic aspects of the output summary, including the grammar, coherence and reference clarity. coherence [172]. To perform a comprehensive evaluation of the proposed approach, we categorised evaluation as 'automatic evaluation' and 'human evaluation' (discussed in Sec. 3.2.1 and 3.2.2). Automatic summarisation approaches are also used to perform other tasks such as information retrieval, translation, or question answering. Therefore, one strategy is to evaluate the summarisation approach towards a specific task, known as an 'extrinsic method'.

### 3.2.1 Automatic Evaluation

There are some conferences with a primary role in designing evaluation standards for automatic scoring of summaries and human evaluation [173]. ROUGE [8] is the most commonly accepted metric for evaluating summaries, which automatically determines the summary quality by comparing it to human (reference) summaries. It computes the number of common units (n-grams) in both the system's summary and the reference summary. ROUGE-N is a recall-based measure and is based on a comparison of ngrams. Eq. 3.1 describes how ROUGE-N is calculated.



where $n$ is the n-gram size, Count ${ }_{\text {match }}\left(\right.$ gram $\left._{n}\right)$ is the number of common n-grams in the candidate and the reference summaries, and Count $\left(\operatorname{gram}_{n}\right)$ is the number of n-grams in the reference summary.

ROUGE-L employs the concept of longest common sequence between the two sequences of text. Although this metric is more flexible, its drawback is that all ngrams must be consecutive [8]. Three variants of ROUGE (ROUGE-1, ROUGE-2 and ROUGE-L) are used in this dissertation. ROUGE-1 and ROUGE-2 were used to evaluate informativeness, and ROUGE-L (LCS) was used to assess fluency. We used the limited-length ROUGE recall-only evaluation ( 75 words) to compare the proposed approach and DUC dataset to avoid bias. Besides, the full-length F1 score was used to evaluate the CNN/Daily Mail dataset.

### 3.2.2 Human Evaluation

While ROUGE serves as a rough measure of coverage, it only compares the n-gram units [174]. Since our goal is to advance personalised approaches, ROUGE cannot be a useful measure. Therefore, we conducted human experiments to evaluate the proposed models based on various criteria. The details of the experiments are explained in each subsection. The general setting is explained as follows.

We hired Amazon Mechanical Turk (MTurk) ${ }^{3}$ workers to attend tasks without any specific prior background required. We designed a series of micro-tasks for each experiment. Not recently published articles were selected for the experiments to avoid any bias in understanding the topics. To ensure the human subjects understood the study's objective, we asked workers to complete a qualification task first. Participants were asked to write a summary of a news article. The results that did not have logical meaning or structure were noted as spam and, thus, removed manually from the results. For example, in the qualification tasks, we asked users to write a summary explaining the main parts of a document. Some results could not pass the qualification task. Another example is the short response time allocated for the tasks, intended to prove that the answers recorded are random or not provided in advance by the workers. Four evaluation aspects were analysed. These are (i) information coverage (how much information the summary covers), (ii) knowledge extraction (how much[^1]users can learn from summaries), (iii) effectiveness (the speed at which users learn) and (iv) user preference (the users' preference(s) compared to other approaches).

### 3.3 Baseline

We compared the proposed approaches to various previously published models known for their significant performance on the datasets. The basic state-of-the-art approaches are explained as follows.

Two early approaches with particular significance are 'Lead-3', which selects the three leading sentences as the summary, and the 'phrase-based ILP model' [91], which is based on a linear programming formulation that learns to combine phrases considering such features as coverage, length and grammar constraints. Although these approaches rely on shallow features, they still report promising results.

Next are TGRAPH [95] and URANK [96]. These two graph-based approaches use graph modelling and ranking scores for each sentence obtained in a unified ranking process. Differential evolution [175] is another approach in basic machine learning algorithms that optimises the allocation of sentences. The selection of sentences is based on a recursive scheme.

Next is FEOM [23], which clusters documents in a dataset and then selects the most important sentence of each group. Querying, clustering and summarising [108] are based on the hidden HMM, which computes the probability of each sentence's appropriateness for the summary set. Finally, the conditional random field [109] considers summarisation tasks as sequence-labelling problems.

Most prominent neural network models include the NN-SE [85], which harnesses a hierarchical document encoder and an attention-based extractor, and SummaRuNNer [86], an RNN. Further, HSSAS [111] uses a hierarchical structured self-attention mechanism to create both sentence and document embedding, and BanditSum [112] considers summarisation a CB problem. This model receives a document and chooses a sequence of sentences to include in the summary. The goal is to maximise the ROUGE score.

### 3.4 Summary

This chapter discussed the experimental set-up, the datasets used in our experiments, and the evaluation metrics to evaluate the proposed models. We explained different evaluation perspectives, including intrinsic and extrinsic approaches. Based on these two measures, we defined automatic evaluation using the ROUGE measure and human evaluation, and further presented the general setting using MTurk for the human evaluation component. Also introduced were the baselines for comparison.

## Towards Intelligent Feature Engineering

Automatic extractive summarisation approaches aim to rank sentences based on some defined features that reflect their importance. Various features have been suggested for this purpose. However, it remains a challenge to produce a summary that best represents documents in a dataset. This chapter focuses on answering the following questions about enabling automatic intelligent feature engineering for document summarisation purposes:

- How good are the state-of-the-art methods in automatically creating and detecting features in the context of document summarisation?
- How can we evaluate the efficiency of different features in making summaries?

We propose a novel approach, called ExDoS, which benefits from supervised and unsupervised algorithms simultaneously and in an interpretable manner. We combined
the clustering and classification algorithm into a single objective function. Clustering aims to discover the underlying structure of data, and then feeds the processed information to the classification stage through a single objective function. ExDoS iteratively minimises the classifier's error rate in each cluster by proposing a dynamic local feature weighting schema. Moreover, ExDoS specifies each feature's contribution in discriminating each class - a challenging task in summarisation. The unique contributions of this chapter are as follows.

We introduce and formalise a theoretically grounded method based on the idea of combining supervised and unsupervised learning, and employ this for the task of document summarisation. Since clustering aims to discover the underlying structure of data and feed this information to the classification stage through a single objective function, it improves the performance of the summarisation algorithm. This architecture allows us to develop clusters of sentences that can help in selecting summaries. Specifically, we designed a ranking measure that determines whether a document sentence matches a highlight, and should be labelled with ' 1 ' (must be in the summary) or ' 0 ' (not in the summary).

Second, ExDoS can measure the role of features in discriminating each class individually through the summarisation process by making various feature spaces. Features are dynamically weighted through the optimisation process in each cluster. These weights represent the role of each feature in discriminating each label individually while summarising documents.

Third, sentences are selected in a way that produced summaries are coherent and non-redundant. The most crucial sentence will be at the top, and then other sentences are chosen to cover all critical information without redundancy.

Finally, ExDoS has an additional advantage which is interpretability. The separated terms in the optimisation process allow us to track the output summary. Such visualisation is beneficial to explain decisions made by the system to the end user.

### 4.1 Introduction

Among the various categories for extractive summarisation approaches are machine learning approaches, which, although a recent phenomenon, have been widely used. Extractive summarisation can be either unsupervised or supervised. In unsupervised approaches, the goal is to find representative sentences. In supervised methods, the problem is a binary classification task where classes are defined as being/not being included in a summary $[176,177]$. Our proposed approach, ExDoS, benefits from using both supervised and unsupervised algorithms simultaneously and in an interpretable manner. The rationale behind this is to harvest the advantages of both classification and clustering algorithms. While classification uses the knowledge of labels, clustering extracts the hidden information based on features. Therefore, combining these two approaches can provide many advantages for different problems $[178,179]$.

ExDoS obviates the need for feature engineering in the summarisation task. Although the most critical phase in machine learning algorithms is feature extraction, prior work has mainly focused on the sentence selection process. Recently, some attempts have been made to find an optimum feature set for the summarisation process. These approaches consider each feature's relevance as a binary problem (i.e., whether a feature is included in the feature set or not) [75]. In addition to summarising a set of documents, ExDoS can measure the importance of different features with the help of local feature weighting. The local weights of features indicate how each feature contributes to making each cluster. ExDoS transforms the feature space into a new feature space by weighting features locally in each cluster. This feature weighting process aims to close up the same-label samples and push different-label samples further.

An overview of ExDoS is illustrated in Fig. 4.1, where a sample is a sentence modelled as a vector of features. The final output is groups of similar samples where features are locally weighted in each group. The weights of features illustrate the importance of each feature in subspaces (clusters). Since the algorithm performs in an iterative manner using gradient descent, the simplest clustering (k-means) and k-nearest neighbour classification (KNN) algorithms are used to support efficiency. However, k-means



Figure 4.1: Overview of the proposed approach (ExDoS). (A) A simple dataset with two classes. (B) Each instance is a sentence. We combine both surface and linguistic features (extracted from the semantic graph) to make a unified feature set. (C) The final output is groups of similar samples in which features are locally weighted in each group.

is one of the most reliable and widely used clustering algorithms. Besides, the KNN classifier has been successfully used in many pattern-recognition applications. It has been statistically proven that when $K=1$ (1NN), the probable error of $1 \mathrm{NN}$ would be less than twice the Bayes classifier error. This proof states that 1NN is capable of generating near-optimal results. Fig. 4.2 shows the architecture of ExDoS and how supervised and unsupervised approaches are combined to make new feature spaces. As shown, weights of features in each cluster are updated iteratively to bring similar samples closer to each other in the new feature spaces by minimising classifier error in clusters.

We provide a detailed technical description of the proposed summarisation system throughout this chapter and illustrate its functionality using a working example. A synthetic example of the ExDoS is illustrated in Fig. 4.3 and 4.4. In Fig. 4.3, the distribution of synthetic two-dimensional data (2-class) is depicted. The output of the ExDoS is two new feature spaces where the weights (alpha and beta) are updated such that similar samples are close to each other. The details of this transformation and how the output is derived are illustrated step by step in Fig. 4.4. We also evaluated our model both automatically (in terms of ROUGE factor) and empirically (human



Figure 4.2: (A) ExDos architecture. (A) The weights of features in each cluster are updated iteratively to bring similar samples closer to each other in the new feature spaces by minimising the error of classifiers in clusters. (B) The architecture of state-of-the-art approaches.

analysis) on two benchmark datasets (DUC2002 and the CNN/Daily Mail). The accuracy of the approach, the importance of features, the effect of local feature weighting, the method's complexity, and the parameters are all evaluated.

### 4.1.1 Problem Statement

The input is a set of documents $D=\left\{D_{1}, D_{2}, \ldots, D_{n}\right\}$, and each document consists of a sequence of sentences $S=\left[s_{1}, s_{2}, \ldots, s_{N}\right]$. Each sentence $s_{i} \in R^{d}$ is a sample vector corresponding to the $i$-th sentence, and $d$ is the number of features. $Y=\left[Y_{1}, Y_{2}\right]$ is the class labels with two possible values of ' 1 ' (being in summary) and ' 0 ' (not being in summary). $K$ is the number of clusters, and cluster centroids are denoted as $C$, where $C_{k}$ is the centre of $k$-th cluster. The sample $s_{=}$is the closest sample with the same class label, and the sample $s_{\neq}$is the closest sample with a different class label. Also, $d_{w}$ denotes the weighted Euclidean distance. Then, the goal is to learn a function $f: S \rightarrow Y$, which is defined on a given dataset $\left\{\left(s_{1}, y_{1}\right),\left(s_{2}, y_{2}\right), \ldots,\left(s_{m}, y_{m}\right)\right\}$.

### 4.1.2 Feature Set

We explored a broad range of features that are commonly used for summarisation. Two feature sets were defined to represent documents: these are surface-level sets and



(A) Feature1



(B)

Alpha1 * Feature 1



Alpha2 * Feature1

Figure 4.3: (A) Distribution of synthetic data (2-class). (B) The output of the ExDoS is two new feature spaces where the weights (alpha and beta) are updated in such a way that similar samples are close to each other.*

*The details of this transformation are illustrated in Fig. 4.4.

linguistic-level sets. The first sets were extracted directly from the document, and the document was transformed into a semantic graph for the latter.

Essentially, 'surface features' contain frequency-based features (TF-IDF, residual IDF [RIDF], gain and word co-occurrence), word-based features (upper-case words and signature words), similarity-based features (Word2Vec and Jaccard measure), sentencelevel features (position, length cut-off and length), and named entities. Conversely, 'linguistic features' are categorised based on semantic graphs. That is, for each sentence, a parse tree is constructed using the Stanford NLP tool [180]. Each sentence is then summarised as a subgraph, which is a triple form. To make the triples, we used an algorithm that extracts triples in the form of subject, predicate and object [181]. Subgraphs are connected to each other, where edges are annotated with similarity weights. Similar or synonymous verbs (using Wordnet) are merged and subjects are concatenated. Then, weights update as the average weights of two merged sentences. Thus, linguistic features are composed of the average weights of connected edges, the merge status of a sentence as a binary feature, the number of sentences merged with a sentence, and the number of sentences connected with a sentence.



Figure 4.4: Single iteration of ExDoS. All samples are considered in each iteration, and weights are updated to bring the nearest same-label sample $\left(s_{=}\right)$closer and push differentlabel samples $\left(s_{\neq}\right)$further. The local weights of features are subsequently updated.

### 4.1.3 Methodology

ExDoS aims to discover the data's underlying structure in the clustering phase and then feed this information to the classification stage in an iterative manner. Therefore, a continuous objective function is defined for analytically optimising both clustering and classification stages by incorporating a new local feature weighting technique. The nearest neighbour classifier's error rate is minimised using the weighted distance, which overcomes the deficiency of popular Euclidean distance. Moreover, the captured space for decision-making (in 1NN) by the Euclidean distance is a hyper-sphere. The overall objective function is defined in Eq. 4.1.

$$
J(\mathbf{W}, \mathbf{C})=J_{1}(\mathbf{W}, \mathbf{C})+J_{2}(\mathbf{W})
$$

where the first term $\left(J_{1}\right)$ is the estimation error of clustering, and the second term $\left(J_{2}\right)$ is the summation of the classification errors over the $K$ clusters. These equations
are expanded in Eq. 4.2, where $N_{k}$ is the number of samples in $k$-th cluster.

$$
J(\mathbf{W}, \mathbf{C})=\sum_{k=1}^{K} \sum_{i=1}^{\left|N_{k}\right|} d_{w}^{2}\left(s_{i}, C_{k}\right)+\frac{1}{N} \sum_{k=1}^{K} \sum_{i=1}^{\left|N_{k}\right|} S_{\beta}\left(\frac{d_{w}\left(s_{i}, s=\right)}{d_{w}\left(s_{i}, s_{\neq}\right)}\right)
$$

To estimate the error of $1 \mathrm{NN}$, the following approximation function is used [182]:

$$
\frac{1}{N} \sum_{s \in S} S_{\beta}\left(\frac{d_{w}\left(s, s_{=}\right)}{d_{w}\left(s, s_{\neq}\right)}\right)
$$

The sample $s_{=}$is the nearest same-class sample, and the sample $s_{\neq}$is the nearest different-class sample to the input sample $s$. Respectively, $d_{w}$ is the weighted Euclidean distance and $S_{\beta}$ is the sigmoid function. Two parameters are optimised in this objective function. The feature-dependent weights associated with the sample $s$ are trained to make the $s_{=}$closer to $s$ while making the sample $s_{\neq}$further. Then, the cluster centres update using the learnt weighted distance. Since this function is differentiable, we can analytically use gradient descent, guaranteeing convergence for estimating the matrix $W$ and the centres. The iterative optimisation of learning parameters are given in Eq. 4.4 and 4.5 , where $\alpha$ and $\gamma$ are learning parameters.

$$
\begin{aligned}
& W^{t+1}=W^{t}-\alpha\left(\frac{J(\mathbf{W}, \mathbf{C})}{\delta(W)}\right) \\
& C^{t+1}=C^{t}-\gamma\left(\frac{J(\mathbf{W}, \mathbf{C})}{\delta(C)}\right)
\end{aligned}
$$

To simplify the formula, the function $R(x)$ is defined in Eq. 4.6 [182].

$$
R\left(s_{i}\right)=\left(\frac{d_{w}\left(s_{i}, s_{i,=}\right)}{d_{w}\left(s_{i}, s_{i, \neq}\right)}\right)
$$

The partial derivative of $J(W, C)$ with respect to $W$ is calculated in Eq. 4.7.

$$
\frac{\delta J(\mathbf{W}, \mathbf{C})}{\delta W_{k}} \cong \sum_{i=1}^{\left|N_{k}\right|} 2 W_{k} \odot\left(x_{i}-C_{k}\right)^{2}+\frac{1}{N} \sum_{i=1}^{\left|N_{k}\right|} S_{\beta}^{\prime}\left(R\left(s_{i}\right)\right) \frac{\delta R\left(s_{i}\right)}{\delta W_{k}}
$$

where $\odot$ is the inner product, and $\frac{\delta R\left(x_{i}\right)}{\delta W_{k}}$ is defined in Eq. 4.8.

$$
\frac{\delta R\left(s_{i}\right)}{\delta W_{k}}=\frac{1}{d_{W_{k}}^{2}\left(s_{i}, s_{i, \neq}\right)}\left(\frac{1}{R\left(s_{i}\right)} W_{k} \odot\left(x s_{i}-s_{i,=}\right)^{2}-R\left(s_{i}\right) W_{k} \odot\left(s_{i}-s_{i, \neq}\right)^{2}\right)
$$

The derivative of $S_{\beta}(z)$ is defined in Eq. 4.9.

$$
S_{\beta}(z)^{\prime}=\frac{\delta S_{\beta}(z)}{\delta z}=\frac{\beta e^{\beta(1-z)}}{\left(1+e^{\beta(1-z)}\right)^{2}}
$$

And the partial derivative of $J(\mathbf{W}, \mathbf{C})$ with respect to $C$ is calculated using Eq. 4.10.

$$
\frac{J(\mathbf{W}, \mathbf{C})}{\delta C_{k}} \cong \sum_{i=1}^{\left|N_{k}\right|}-2 W_{k}^{2} \odot\left(x_{i}-C_{k}\right)
$$

Since we need to optimise the features' weight for cluster samples along with the centre of clusters, we first update $W$ in each cluster, and then update the centres $(C)$.

## Generating Summary

After training the model, we defined three measures, including coverage, coherence and redundancy, to generate summaries.

## Coverage

The sentences' coverage based on the proposed architecture is defined using Eq. 4.11.

$$
\operatorname{Cov}\left(s_{i}\right)=\left|d_{w}\left(c_{+}, s_{i}\right)-d_{w}\left(c_{-}, s_{i}\right)\right|
$$

For each sentence, the weighted distance to cluster centres is estimated. The coverage is defined as the difference between data points and two cluster centres. $c_{+}$is the cluster where the majority of samples belong to the positive class (being in summary), and $\left(c_{-}\right)$is the cluster where samples mostly belong to the negative class (not being in summary). The summary coverage is the sum of all sentences' coverage in that summary.

## Coherence

A critical aspect of a good summary is coherence, or the summary order. For this purpose, we used G-Flow ${ }^{1}$ [183], a graph model for selection and ordering that balances[^2]coverage and coherence. G-Flow relies on the approximate discourse graph, where each node is a sentence, and edges indicate whether a sentence coherently follows one other. The indicators include coreference, discourse cues, de-verbal nouns, and more. The coherence is defined in Eq. 4.12 as the sum of the edge weights between successive summary sentences.

$$
\operatorname{Coh}\left(s_{i}\right)=w_{G+}\left(s_{i}, s_{i+1}\right)+w_{G-}\left(s_{i}, s_{i+1}\right)
$$

where $w_{G+}$ and $w_{G-}$ represent positive and negative edges, respectively. Since this formula considers the coherence between adjacent sentences, the produced summary may lack topic coherence compared to human-generated summaries. However, the outcome of the experiments does not indicate this problem. The coherence of a summary is the sum of the coherence of all sentences in the summary.

## Redundancy

The redundancy measure is defined as the combination of a sentence's embedding similarity with the previously selected sentences. The overall score of each sentence is defined in Eq. 4.13.

$$
\operatorname{Red}\left(s_{i}\right)=\sum_{s \in \text { Summary }} \operatorname{sim}\left(s_{i}, s\right)
$$

## Objective Function

We propose our objective function to balance defined criteria by having all coverage, coherence, redundancy and the limit size $(B)$ in one objective function (Eq. 4.14).

$$
\begin{aligned}
\operatorname{maximize}: \operatorname{Score}(S) & \triangleq \operatorname{Cov}(S)+\lambda \operatorname{Coh}(S)-\phi \operatorname{Red}(S) \\
\text { s.t. } & \sum_{s \in \text { Summary }} \text { length }(s)<B
\end{aligned}
$$

To solve this objective function, we need to use a local search to approximate the optimum value. For this purpose, we used a hill-climbing algorithm with a random

| Topic: How historic California drought affects rest <br> of nation, often for the worse | Summary |
| :---: | :---: |
| It's more than just one state's internal problem. The <br> historic California drought hurts the rest of the union, <br> tod. That's because California is a breadbasket to the | A) The historic California drought hurts the <br> rest of the union, too. |
| nation. California is growing more than a third of its <br> vegetables and nearly two-thirds of its fruits and <br> nuts. Here's why we should heed the ongoing <br> drought in the most populous state. It is a slowly | B) The historic California drought hurts the <br> rest of the union, too. California is growing <br> more than a third of its vegetables and <br> nearly two-thirds of its fruits and nuts. |
| expanding natural disaster now in its fourth year that <br> this week prompted Gov. Jerry Brown to announce <br> mandatory $25 \%$ cutback in water consumption in all <br> cities. Prices rose last year for these items on your <br> kitchen table: Brocolil by 11 cents per pound to <br> $\$ 1.89$. Grapes by 64 cents a pound to $\$ 3.06$ | C) The historic California drought hurts the <br> rest of the union, too. California is growing <br> more than a third of its vegetables and <br> nearly two-thirds of its fruits and nuts. Jerry <br> Brown to announce a mandatory $25 \%$ <br> cutback in water consumption in all cities. |

Figure 4.5: Visualisation of the summarisation process for a CNN article about the California droughts. ${ }^{3}$ The left box contains the original text, and the right box is the summarisation process (three iterations). To visualise the sentence score, we divide the ranks of an iteration into four portions, each coloured differently. (The darkest colour shows the most important one.) However, it should be noticed that ranks are changed in each iteration.

start [184]. Adding, removing or replacing a sentence is permitted in each step, and the parameters are trained in the process. An example of ranking sentences is depicted in Fig. 4.5.

### 4.1.4 Experiments and Evaluation

This section presents the experimental set-up for assessing the performance of our summarisation model. The three variants of ROUGE (ROUGE-1, ROUGE-2 and ROUGE-L) were used. We employed the limited-length ROUGE recall-only evaluation (75 words) for comparison of DUC to avoid bias, and the full-length F1 score to evaluate the CNN/Daily Mail dataset. We used this measure to compare the produced summary with state-of-the-art approaches and to analyse the effect of local feature weighting in the same approach.

We evaluated ExDos from various perspectives, including automatic accuracy evaluation of the results, human preference evaluation, the effect of local feature weighting,[^3]

TAble 4.1: ROUGE score (\%) Comparison on DUC2002 Dataset

| Model | ROGUE-1 Score | ROGUE-2 Score | ROGUE-L Score |
| :--- | :---: | :---: | :---: |
| Lead-3 | 43.6 | 21.0 | 40.2 |
| ILP | 45.4 | 21.3 | 40.3 |
| TGRAPH $^{4}$ | 48.1 | 24.3 | N/A |
| URANK | 48.5 | 21.5 | N/A |
| NN-SE | 47.4 | 23.0 | 43.5 |
| SummaRuNNer | 46.6 | 23.1 | 43.03 |
| HSSAS | 52.1 | 24.5 | 48.8 |
| ExDoS | 52.5 | 24.7 | 48.8 |

parameter analysis and efficiency analysis. The initial number of clusters was set to the best value estimated by the silhouette approach [185].

The ROUGE results are illustrated in Table 4.1 and 4.2. According to Table 4.1 (DUC2002 dataset), ExDoS outperforms most state-of-the-art approaches and competes with HSSAS. Results on the CNN/Daily Mail dataset follow the same trend as DUC2002. Note that the score is generally lower compared to DUC2002. This is because the gold-standard summaries include paraphrasing. Meanwhile, HSSAS [111] is a neural network model that has a hierarchical structured self-attention mechanism to create both sentence and document embedding, and BanditSum [112] is a neural network model that considers summarisation as a CB problem. The latter receives a document and chooses a sequence of sentences to include in the summary, where the policy is to maximise the ROUGE score. Our model is a simple, efficient model that achieves better results in terms of ROUGE score in most cases, while offering other benefits such as interpretability. We performed an analysis of variance test to evaluate the significant supremacy of our approach statistically. Results show that ExDoS outperforms the baselines, including ILP, TGRAPH, URANK and NN-SE, with a significant margin $(p<0.01)$, while competing with HSSAS and BanditSum.[^4]

Table 4.2: ROUGE score (\%) Comparison on CNN/Daily Mail Using F1 Variant of ROUGE

| Model | ROGUE-1 Score | ROGUE-2 Score | ROGUE-L Score |
| :--- | :---: | :---: | :---: |
| Lead-3 | 39.2 | 15.7 | 35.5 |
| NN-SE | 35.4 | 13.3 | 32.6 |
| SummaRuNNer | 39.9 | 16.3 | 35.1 |
| HSSAS | 42.3 | 17.8 | 37.6 |
| BanditSum | 41.5 | 18.7 | 37.6 |
| ExDoS | 42.1 | 18.9 | 37.7 |

Table 4.3: Estimation of Features Importance

|  | Feature <br> set | Freq <br> based | Word <br> based | Similarity <br> based | Position <br> based | Linguistic <br> based |
| :---: | :--- | :--- | :--- | :---: | :---: | :---: |
| 웡 | Summary | 0.39 | 0.06 | 0.35 | 0.51 | 0.22 |
|  | Not summary | 0.21 | 0.09 | 0.25 | 0.42 | 0.20 |
| 乙 | Summary | 0.33 | 0.04 | 0.46 | 0.31 | 0.29 |
|  | Not summary | 0.24 | 0.01 | 0.37 | 0.38 | 0.44 |

## Feature Importance Evaluation

In addition to being modern, ExDoS learns the relevance of features separately for each class, as reported in Table 4.3. The reported weights are the average weights in each feature set. Based on observations, we concluded that in DUC2002, the position-based features play a major role in selecting summaries. Evidently, the most important features are the frequency-based ones in the 'summary' class and the similarity features for those in 'not summary'. In the CNN/Daily Mail dataset, the similarity-based feature has a major effect on discriminating both classes, probably due to the paraphrased standard summaries.


Figure 4.6: Both graphs show the number of iterations versus the score in both datasets.

Table 4.4: Effects of Dynamic Local Feature Weighting

|  | DUC2002- <br> ROUGE-1 | DUC2002- <br> ROUGE-2 | CNN/Mail- <br> ROUGE-1 | CNN/Mail- <br> ROUGE-2 |
| :---: | :---: | :---: | :---: | :---: |
| ExDoS + <br> weighting | 51.7 | 24.7 | 41.1 | 18.5 |
| ExDoS - <br> weighting | 43.3 | 20.1 | 38.7 | 14.3 |

## Evaluating Effect of Local Feature Weighting

To evaluate the effect of local feature weighting, we conducted an ablation study to compare results to the global weighting of the same procedure. The results are reported in Table 4.4. Evidently, local feature weighting significantly affects the summarisation result in both datasets.

## Efficiency Evaluation

ExDoS is an efficient approach in terms of its complexity. The computational complexity of ExDoS is determined as $O\left(K \times N_{k} \times I\right)$, where $K$ is the number of clusters, $N_{k}$ is the number of samples in the most populated cluster $(\operatorname{Max}=N)$, and $I$ represents the maximum number of iterations where $I<<N_{K}$. In Fig. 4.6, the number of iterations versus score value is reported to illustrate the efficiency of ExDoS based on the number of iterations needed to converge the algorithm.


Figure 4.7: Both graphs show the learning parameters $(\alpha, \gamma)$ and the corresponding ROUGE-1.

## Parameter Analysis

As in other parametric models, ExDoS has certain hyper-parameters that need to be tuned. The learning-rate parameters of weights and centres $(\alpha, \gamma)$ control the speed of convergence in the gradient-descent algorithm. When the learning rate is sufficiently small, the algorithm achieves linear convergence; when it is large, the probability of converging to a suitable local optimum decreases. $\beta$ is another key hyper-parameter that regulates the slope of the sigmoid function, where $S_{\beta}(R(s))=1 /\left(1+e^{(\beta(1-R(s)))}\right)$. For small values of $\beta$, the sigmoid derivative is almost constant. Conversely, for large values of $\beta$, learning happens when the distance ratio $(R(s))$ is close to 1 . Two other parameters are $\phi$ and $\lambda$, which control the coherency.

To find the best parameters, we tested different combinations of learning rates $(\alpha, \gamma)$. These combinations and the corresponding evaluation metric (ROUGE-1) are reported in Fig. 4.7. It is noteworthy that the gradient-descent-based learning schemes always converge to a local optimum. When running the algorithm, we empirically observed that it has an effective convergence rate. The two other parameters $(\phi, \lambda)$ were also tested using different values, reported in Fig. 4.8. Since these two parameters control the coherency and redundancy, they do not significantly affect ROUGE. Therefore, the combination of these variables is reported in terms of score value.


Figure 4.8: Both graphs show the learning parameters $(\phi, \lambda)$ and the corresponding score value.

Table 4.5: Human Evaluation Result

| Model | Informativeness | Non-redundancy | Overall |
| :---: | :---: | :---: | :---: |
| Lead-3 | $13 \%$ | $21 \%$ | $20 \%$ |
| SummaRuNNer | $17 \%$ | $19 \%$ | $16 \%$ |
| HSSAS | $20 \%$ | $16 \%$ | $21 \%$ |
| BanditSum | $23 \%$ | $22 \%$ | $18 \%$ |
| ExDoS | $27 \%$ | $22 \%$ | $25 \%$ |

## Human Evaluation

While ROUGE serves as a rough measure of coverage, it only compares the n-gram units. Therefore, using 20 random sample DUC2002 test documents, we conducted a human experiment to evaluate the model based on other criteria, such as informativeness, redundancy and overall quality. Twenty-five MTurk participants attended the task, each without any specific prior background. Participants were presented with a news article and summaries generated using different approaches. The output of these systems was shown to them, and participants were asked to rank the summaries based on the aforementioned criteria. Human results reported in Table 4.5 represent the voting percentage of participants for each approach (ties were not allowed). Evidently, ExDoS performed better than most state-of-the-art methods in all measures, but, in terms of redundancy, competes with BanditSum. Overall, ExDoS achieved significant performance. This is an interesting result and demonstrates that ExDoS performs well
using only clustering information without sophisticated constraint optimisation (ILP, TGRAPH) or the complex architecture of a neural network (HSSAS and BanditSum).

### 4.2 Summary

This chapter proposed a general-purpose extractive approach for summarising documents. We evaluated the proposed model automatically and empirically (human analysis) on the two common benchmark datasets, CNN/Daily Mail and DUC2002. As shown, the algorithm achieved better results than most state-of-the-art methods in terms of efficiency and performance. The human evaluation also proves that the proposed model is proficient in generating instructive and compelling summaries. Besides, the post-trained weights represent the importance of each feature in discriminating against each class. To understand the role of local feature weighting and new feature spaces, we consider the performance of ExDoS through local weighing and without weighting. Estimating the features' importance is a fundamental step in summarisation.

## Towards Interactive Document

## Summarisation

Automatic document summarisation is a long-studied area covering different perspectives. It is necessary to articulate the effects and needs of data reduction for analysis, management, commercialisation and personalising purposes. Summarisation facilitates perceiving and extracting embedded insights that are hidden within data. However, understanding data is challenging due to the subjectivity aspect of the analysis goal. Users seek to find only information relevant to a topic and in an organised and coherent structure. In the general form, summarisation takes a topic-related set of articles and generates a summary that bears the most crucial information. The produced summary is, in general, a few selected sentences.

The main drawbacks of existing MDS are as follows:

- MDS produces a single, general and flat summary for all users. Therefore, summaries are neither interpretable nor personalised, but rather unstructured and, therefore, ill-suited for further analysis.
- Existing methods are designed to create short summaries (3-6 sentences) and are incapable of producing more extended outputs. Therefore, all details are omitted even if a user is interested in more information.
- MDS depends on reference/gold-standard summaries made by humans, which are subjective and costly.

Studies have shown that when people are exposed to several documents at once, they rarely make a fully formulated summary [5]. Instead, their first attempt is to find a general idea and then gradually go in depth if they find it interesting. One study in the literature demonstrates that the most common search strategy among participants is to provide an 'overview first, filter and selection', and then discuss the details [186]. That said, each user has different information needs that should be considered when making summaries. Moreover, they might be interested in exploring different directions based on background knowledge, situation and context, due to personal bias. Indeed, these high-level interests will vary over time. For example, when a researcher wants to read a paper, the first step is to read the title and the abstract. The researcher would continue to study the details and methodology only if they are interested. As an example of context, take the litany of information available on the internet about COVID-19. While one might be interested in reading about the symptoms, another might want to research the outbreak locations or perhaps the death toll. The same applies for researchers investigating summarisation. A researcher might be eager to know what summarisation is and, thus, focus their interest on different categories of summarisation, such as extractive or abstractive approaches. Another important issue in this context regards structured summaries, which make further analysis possible. For example, a user might select the summary length or analyse summaries based on different categories.

In contrast to a generic summary that is unique for all users, this chapter provides


Figure 5.1: Traditional summarisation approaches are depicted on the left. (A) Extractive approach (the most informative sentences are selected); (B) Abstractive approach (summaries are generated in the form of new sentences). (C, D) NARS process (a hierarchical summarisation approach).

user-based hierarchical summaries. The motivation for this approach is based on how our brain efficiently categorises the perceived information. The proposed approach help users with general knowledge about a topic to explore a wide range of information.

We propose a general hierarchical personalised summarisation framework, called NARS, to improve the drawbacks of traditional summarisation methods in various aspects. We also propose two variants of NARS - a SNARS and a FNARS. The goal is to develop intelligent narrative summaries employing the features extracted from users' engagement. To achieve this goal, we propose a hierarchical structure to prevent users from becoming overwhelmed with less important information at first glance, and to facilitate the selection process. Instead of providing a short and static summary, we present an intelligent and interactive summarisation approach that enables users to navigate through the summary hierarchy and retrieve more in-depth information upon request. Overall, our approach aims to (i) engage users in the summarisation process and guarantee interactive speeds even for extensive text collections, and (ii) eliminate the need for reference summaries, which is one of the most challenging issues facing the summarisation problem. A comparison of NARS with traditional state-of-the-art summarisation approaches is shown in Fig. 5.1.

The unique contributions of this chapter are as follows. First, we propose a formal definition of multi-aspect hierarchical summarisation. We focused on users' desire to better understand document summaries rather than obtain only accuracy. We then introduce NARS, a hierarchical personalised summarisation approach through which users can specify the levels of detail that benefit them in various ways. This includes:

- customised summary length (i.e., users determine the length of the summary)
- generality v. specificity (The structured output and navigation ability of the approach mean that users learn fast without being overwhelmed by information. This also helps users gradually create a hierarchy by navigating through the summary. The organised output also clearly highlights both minor details and main concepts.)
- interaction (i.e., users interact with the summary to better understand one or multiple topics.)

Next are reference summary requirements, which see the summaries' dynamic structure eliminate the need for reference summaries. This is possible because optimisation of an algorithm that is based on certain gold-standard summaries is not required.

We then propose two models, the SNARS and FNARS. The output is a wellstructured summary that helps users by producing both organised output (i.e., coherent and collated information in one centralised summary) and multifaceted summaries. This means the models generate concentrated summaries that can answer a user's query by filtering the hierarchy branches upon request. Users can also trace the hierarchy based on various criteria in SNARS.

### 5.1 NARS

Previous approaches have used supervised or unsupervised methods that show promising results in terms of accuracy (compared to gold-standard summaries) to tackle the summarisation problem. Research on MDS mainly ignores the usefulness of the approach for the user. Instead, the literature mostly focuses on the accuracy of the
produced summaries, resulting in inflexible summaries. Besides, most will optimise their system based on gold-standard summaries generated by human experts, which are costly, subjective and time consuming. In contrast to previous approaches, we propose a new task for MDS, called NARS, which gathers the related information and collates it into a shorter format. The proposed approach was called 'narrative summaries' since it provides information in a logical order, from the most indicative sentences to more informative sentences. We also propose a hierarchical structure to prevent users from becoming cognitively overwhelmed when receiving a complete summary at once. The proposed problem has all the MDS requirements, as well as additional complexities of multifaceted and hierarchical summarisation.

We define a general framework with two main phases involving (i) hierarchical clustering and (ii) hierarchical summarisation over said clustering (Fig. 5.2). Further proposed are two models based on these phases - the SNARS and FNARS. In a semistructured model, the representation unit is a sentence. We then define three objective functions to cluster sentences based on topic, time, location and a combination of the three, in such a way that is both coherent and in a logical order. Since the individual cluster summaries for a given level should be logically distinct, we also propose another objective function in the summarisation phase to maximise coherence and salience while avoiding redundant sentences. The summary is also required to fit within the given budget size (user parameter).

In a fully structured model, the unit is a concept. We defined an objective function to cluster related concepts hierarchically in different levels of generalisation and specification. Then, the summary takes the form of a hierarchical concept map, where each level is a summary. The proposed solution conveys critical information logically, allowing the user to quickly gain an idea and overview of the content without much reading.



Figure 5.2: NARS's hierarchical structure, where nodes correspond to sentences in SNARS and concepts in FNARS.

### 5.1.1 Problem Definition

Given a set of related documents $D=\left\{D_{1}, D_{2}, \ldots, D_{n}\right\}$, the output is a hierarchical summary where the top-level nodes indicate more general information, and the 'children' indicate more detailed information related to the 'parent' nodes. The defined structure has the following properties relative to previous approaches:

- It is a storytelling process in which the information present at the top level is general and abstract. The summary grows upon the user's request, particularly if they are interested in answering 'when', 'where' and 'who' questions.
- By navigating down the hierarchy, the user perceives the summary effectively by understanding the relationship between parent and child nodes.
- Summaries are selected based on measures of fluency, redundancy and being indicative.


### 5.1.2 Proposed Framework

Overall, NARS is both a semi-structured and fully structured summarisation approach with two main components: (i) hierarchical clustering and (ii) the ability to summarise over the produced clustering to generate hierarchical summaries. The clustering part creates the boundaries for the summarisation task in the second step. In a semistructured model (SNARS), the unit of representation is one sentence. In this model, time, topic and location are the primary measures in forming hierarchies. Therefore, this approach is appropriate for storytelling and to answer where, when and what type questions. In the second model (FNARS), concepts are the representation unit, with a concept map constructed hierarchically for summarising entire contents. This model is best suited when there are related topics with a redundant concept. The model's architecture is depicted in Fig. 5.3, and Algorithm 6 demonstrates the general framework.

### 5.2 SNARS

This section defines the SNARS tasks considered in our approach. Since sentences are the representative unit in this structure, this model is considered an extractive summarisation approach.

### 5.2.1 Problem Definition

Given a set of related documents $D=\left\{D_{1}, D_{2}, \ldots, D_{n}\right\}$ and the limited size of summaries $b$ as input, the output is a multi-aspect hierarchical textual summary called $S$.

Hierarchical multi-aspect summaries $(S)$ have a graph structure, where each node represents a sentence. The top-level nodes indicate more general information, while the children indicate more specific information related to the parent nodes. As mentioned, SNARS has two main components - hierarchical multifaceted clustering and the ability

```
Algorithm 1 Narrative summaries
    Input: Hierarchical summaries
    Output: Hierarchical summaries
    Pre-processing
        Semi-structured NARS (SNARS): Sentence labelling
        Fully-structured NARS (FNARS): Concept and relation extraction
    Hierarchical clustering
        SNARS: Multifaceted entropy-based clustering of sentences
        FNARS: Co-reference clustering of concepts and relations
    Summarization over hierarchical clusters
        SNARS: Optimising based on redundancy, fluency, and being indicative
        FNARS: Optimising based on entropy loss function
    return Hierarchical summary
```

to summarise over the produced clustering. The clustering component defines the boundaries for the summarisation task in the second step. Then, for each cluster, a sentence is selected as the representative of that cluster. Hence, the number of sentences at each level is equivalent to the cluster numbers. The output of hierarchical clustering serves as the input to the summarisation process. Thus, functional clustering should have three properties, including:

- considerably high enough distance between clusters (inter-cluster distance)
- comparatively low distance inside each cluster (intra-cluster distance)
- uniformity in terms of size.

For reference, we call these conditions the 'main clustering conditions'. The designed recursive clustering algorithm automatically chooses the optimal clusters' number at each step. The challenge here is to find the best measure to cluster documents in a natural and fluent way. We also clustered sentences based on three measures for representing the summaries inside the hierarchy. This includes (i) topic-based clustering, (ii) time-aware (temporal) clustering, (iii) location-aware clustering, and (iv)



Figure 5.3: (A) Documents are pre-processed. (B) Hierarchical clustering is performed. (C) Created summaries are shown to users for interaction, where nodes correspond to sentences in SNARS and concepts in FNARS.

hybrid time/location/topic clustering. Each of these models is explained in Sec. 5.2.2 to 5.2 .4 , including the summarisation process based on these criteria.

### 5.2.2 Hierarchical Time-aware Clustering

This model's objective is to cluster related sentences in different timelines in b groups, meeting the 'main clustering conditions'. We timestamped all sentences individually using SUTime. ${ }^{1}$ SUTime is a temporal tagger for recognising and normalising temporal expressions in English text; it is also used to annotate documents with temporal information. We used a set of rules to determine if the sentence's timestamps refer to the root verb. The article date is used in case of no given timestamp. We also propose a novel recursive clustering algorithm with the goal to maximise the objective function in Eq. 5.1 over all clusters (C), where $\mathrm{C}=\left\{c_{1}, c_{2}, . ., c_{k}\right.$ and $k=b$, using a local search algorithm.

$$
J_{1}(C)=\alpha_{1} \sum_{c \in C} \sum_{s_{i}, s_{j} \in c} \text { similarity }\left(s_{i}, s_{j}\right)-\beta_{1} \sum_{c \in C} \sum_{B_{t} \in c} p\left(B_{t}\right) \log p\left(B_{t}\right)+\min _{c \in C} \operatorname{size}(c)
$$

We implemented hierarchical clustering top-down at each time, solving for Eq. 5.1. The parameters $\alpha_{1}$ and $\beta_{1}$ control the effect of time and topic, which are determined[^5]using grid search algorithm over a evaluation set. The first term in Eq. 5.1 is the pairwise similarity of sentences in each cluster, indicating the first condition (intracluster distance). For this purpose, we used cosine similarity [15]. The second term in Eq. 5.1 is the inter-cluster distance. After acquiring the timestamp $(t)$, we find the boost-time $\left(B_{t}\right)$ of articles, defined as the time at which the published article number's difference in a day $(\lambda($ Day $))$ and its previous day $(\lambda($ PDay $))$ is at maximum [145]. Thus, consider Eq. 5.2.

$$
B_{t}=\max \{\lambda(\text { Day })-\lambda(\text { PDay })\}, \forall D a y, P D a y \in t
$$

where PDay is one day before Day for the entire timestamp $(t)$ in which we are searching. We defined the number of boost times as the number of clusters, equivalent to the budget size (b). Accordingly, we assigned all sentences to each boost time, as in Eq. 5.3.

$$
\begin{array}{r}
\text { TimeLabel }(s)=B_{t} \quad \text { if } B_{t-1}<\text { SentenceTime }(s)<B_{t} \\
\forall s \in S
\end{array}
$$

where $S$ is the set of all the available sentences, and SentenceTime $(s)$ returns the time associated with sentence $s$. The second term in Eq. 5.1 is to minimise the entropy of time labels in each cluster to meet the inter-cluster distance condition. Therefore, $p\left(B_{t}\right)$ is the probability of label $B_{t}$ comparing to other time labels in each cluster. Finally, the third term in Eq. 5.1 is the uniformity condition to prevent generating clusters with a small number of samples. The first and second values are between 0 and 1 . The third value is the normalised size of a cluster with minimum size divided by other clusters' average number size, to avoid bias.

### 5.2.3 Hierarchical Location-aware Clustering

We considered location as an important feature to create the hierarchy. We used the location extracted by entity recognition using the Stanford NLP service. If there was no information for the location, we categorised this as 'other'. We next applied the
same procedure for the location as for the time and performed top-down hierarchical clustering at each point solving for Eq. 5.4. The two parameters $\alpha_{2}$ and $\beta_{2}$ control the effect of location and topic, which are calculated using grid search over a development set. The goal is to find the best organisation for hierarchical clusters by maximising the following objective functions in Eq. 5.4.

$$
J_{2}(C)=\alpha_{2} \sum_{c \in C} \sum_{s_{i}, s_{j} \in c} \text { similarity }\left(s_{i}, s_{j}\right)-\beta_{2} \sum_{c \in C} \sum_{B_{l} \in c} p\left(B_{l}\right) \log p\left(B_{l}\right)+\min _{c \in C} \operatorname{size}(c)
$$

The definition of all of the terms in Eq. 5.4 is the same as Eq. 5.1. We defined location-boost labels $\left(B_{l}\right)$ where the number of articles in a location is the maximum, similar to Eq. 5.3. In practise, labelling location is not as simple as time since various labels lead to many clusters. Therefore, we defined two levels of labelling - country and city - and used a local search to find the best combination for choosing the boost location to maximise the inter-cluster distance.

### 5.2.4 Hierarchical Topic-based and Hybrid Time-Location Clustering

The best splitting procedure is one that generates a naturally flowing summary. In real-world scenarios, sometimes the article's inflation can be a combination of time, location and/or topic. As such, we defined another objective function based on only the topic. The objective function is based on the cosine similarity of sentences (first term in Eq. 5.1), defined as $J_{3}$. Therefore, instead of forcing the summaries to be split based on location or time, we made a combination of the two and selected the maximum value at each level (Eq. 5.5).

$$
\max \left\{J_{1}(C), J_{2}(C), J_{3}(C)\right\}
$$

### 5.2.5 Summarising Over the Hierarchies

At each level of the hierarchy, we need to define the representative sentences for each cluster using the hierarchy and clusters' structure. Therefore, the problem transforms and we must select the best sentence as the representative of each cluster. We defined three main measures to select representative sentences, including being indicative, redundancy and smoothness (fluency).

The variable 'being indicative' (I) is based on two aspects: generality and salience (Eq. 5.6).

$$
I(s)=G(s)+S(s)
$$

The first measure, generality, indicates if the selected sentence is general enough to represent all sentences in a cluster. To assess the generality of a sentence $\left(s_{k}\right)$, we generated a similarity graph for all sentences in the cluster, such as $c_{j}$. We then calculated the normalised sum of similarity of all neighbours of a sentence as the value of generality of that sentence (Eq. 5.7).

$$
G\left(s_{k}\right)=\frac{1}{\operatorname{size}\left(c_{j}\right)}\left(\sum_{\substack{i=1 \\ i \neq k}}^{\text {size }\left(c_{j}\right)} \operatorname{Similarity}\left(s_{i}, s_{k}\right)\right), \forall s_{i} \in S_{c_{j}}, \forall c_{j} \in C
$$

where the similarity measure is the cosine similarity [15], $S_{j}$ is the set of all sentences in cluster $c_{j}, C$ is the set of all clusters, and $\operatorname{size}\left(c_{j}\right)$ returns the number of sentences in a cluster $c_{j}$. Another measure that should be considered when selecting the best sentence is its 'salience'. We estimated the importance of each feature in making summaries using ExDos and, therefore, trained a log-linear regression based on five critical types of features: these are frequency-based features (TF-IDF, RIDF, gain and word co-occurrence), word-based features (upper-case words and signature words), similarity-based features (Word2Vec and Jaccard measure), sentence-level features (position, length cut-off and size), name entities [75], and the ROUGE measure as the final score to predict salience.

Next, the 'redundancy' $(R)$ measure for a sentence is defined as the combination of a sentence's embedding similarity with the previously selected sentences.

To maximise the 'fluency' $(F)$ of the produced summary $(F)$, we require two coherence types - the parent and child coherency, and coherency within each summary level. For this purpose, we used G-Flow [183], a graph model used for selection and ordering, which balances coverage and coherence. This model relies on the approximate discourse graph, where each node is a sentence and edges indicate whether a sentence coherently follows one other. The indicators include coreference, discourse cues, de-verbal nouns, and more. Coherence is defined as the sum of the edge weights between successive summary sentences. The coherence of a summary is the sum of all sentences' coherence in a summary.

Next is 'optimisation'. Combining these variables unifies our objective function into a single objective function, defined in Eq. 5.8.

$$
\operatorname{maximize}: \operatorname{Score}(S) \triangleq I(S)+\gamma F(S)-\phi R(S)
$$

where $I(S)$ represents the indicative measure of the summary, which summarises the generality and salience of the selected parents. $R$ is the redundancy measure, $F(S)$ is the fluency measure, and $\gamma$ and $\phi$ are the control parameters for the effect of fluency and redundancy, which are calculated using grid search over a development set. We approximated a solution using the hill-climbing algorithm with a random start over the space of hierarchical summaries. According to each step's dependency on the previous one, we recursively start from the root, finding the best sentence at each level, and then move down towards the leaves. At each point, the search algorithm is allowed to add a new sentence, remove a sentence or replace two sentences. While this search algorithm works well in practise, the branching factor becomes large when the budget and input document size are large. Thus, we also set the initial summary for random restarts such that the highest indicative sentences are selected first. The other sentences are subsequently added based on their overall defined score. When no other sentence can be added to the summary according to budget size, the algorithm is terminated.

### 5.3 FNARS

A structured summary has the advantage of being used as an overview of a collection of documents. It also facilities using the summaries for further analysis and processes. This model substitutes a hierarchical concept map as a structured presentation style for summarisation. A concept map is a labelled graph, where nodes present concepts and edges are the relations among nodes [15].

### 5.3.1 Problem Definition

The input is a set of related documents $D=\left\{D_{1}, D_{2}, \ldots, D_{n}\right\}$ and the output is a hierarchical concept map showing the general topics on higher levels and specific ones on lower levels, satisfying a specified size limit, $b$. This model also follows the general structure of NARS defined in Sec. 5.1, based on the hierarchical clustering of concepts and making summaries over hierarchies.

### 5.3.2 Extracting Concepts and Relations

Concepts and relations need to be extracted before undertaking any other process. Concept and relation extraction aims to identify spans in a set of documents used as labels for concepts and relations in the concept map. To this end, we relied on open information extraction [187], an approach that extracts binary propositions from the text. Using the sentence, 'the Pharmaceutical Benefits Scheme subsidises cancer treatments', the output of Open IE is 'the Pharmaceutical Benefits Scheme $\xrightarrow{\text { subsidises }}$ cancer treatments'. 'The Pharmaceutical Benefits Scheme' and 'cancer treatments' are two concepts, and 'subsidises' is the relation between them. Any extracted concept that does not contain at least one noun token or is longer than five tokens is omitted.

### 5.3.3 Hierarchical Clustering of Concepts

We describe hierarchical clustering as output that serves as input in the summarisation process. We employed a recursive clustering algorithm to define the summary structure. Clusters in the hierarchical structure represent a concept set, making sense to summarise together. The algorithm first requires finding the semantic similarity of two concepts $c_{1}$ and $c_{2}$. We used both semantic and lexical similarity as the features [15], including the normalised Levenshtein distance, the Jaccard coefficient between stemmed content words, semantic similarity based on latent semantic analysis [188], and WordNet [189]. Then, we modelled the similarity as a binary classification using logistic regression such that a positive classification, $y=1$, means that mentions are coreferent (Eq. 5.9).

$$
P\left(y=1 \mid c_{1}, c_{2}, \theta\right)=\operatorname{Sigmoid}\left(\theta^{T} \delta\left(c_{1}, c_{2}\right)\right)
$$

where $\delta\left(c_{1}, c_{2}\right)$ are the features, $\theta$ denotes the learnt parameters, and the sigmoid function is defined using Eq. 5.10.

$$
S_{\theta}(z)=\left(\frac{1}{1+e^{\theta(1-z)}}\right)
$$

After evaluating the similarity of two concepts based on different similarity measures, we need to partition similar concepts. The goal is to hierarchically cluster similar concepts utilising the similarity probability of two concepts. We used an ILP function to find an optimised partitioning schema that maximally agrees with the pairwise classifications [190]. Let $x_{p} \in\{0,1\}$ be a binary value representing the coreference of mentions $c_{1}, c_{2}$ being in the same cluster. The goal is to optimise the cross-entropy loss function in Eq. 5.11 using a greedy local search to partition similar concepts at each level of the hierarchy.

$$
\sum_{p \in C^{2}} c(p) x_{p}+(1-c(p))\left(1-x_{p}\right)
$$



Figure 5.4: Example of a hierarchical concept map: two levels of hierarchy are coloured, and each node's children is shown to users if they select a parent node.

### 5.3.4 Summarising Over Hierarchies

After partitioning concepts at different hierarchical levels, we can now construct the hierarchical concept map, a graph where $G=(C, R)$ (the nodes representing concepts $C)$. An edge with label $r$ exists for every proposition $\left(c_{1}, r, c_{2}\right)$ between the nodes. For each concept, $c_{i}$, we selected the most frequent and shortest mention as its label to choose the most generic and representative label. Fig. 5.4 is an example of the proposed hierarchical concept map (FNARS).

### 5.4 Experiments and Evaluation

This section presents the experimental set-up for implementing and assessing our summarisation model. The three variants of ROUGE (ROUGE-1, ROUGE-2 and ROUGEL) were used. ROUGE-1 and ROUGE-2 evaluate informativeness, and ROUGE-L (LCS) evaluates fluency. We used the limited-length ROUGE recall-only evaluation (75 words) to compare DUC2002 to avoid bias, and the full-length F1 score to evaluate the CNN/Daily Mail dataset.

Since our goal is to improve the application of summaries for users, the effect of hierarchical summaries cannot be measured using ROUGE. Therefore, we also conducted a human experiment to evaluate the model. For this purpose, we analysed four aspects of user requirements and designed a series of micro-tasks for each experiment, covering information coverage, knowledge extraction and effectiveness (speed), and users' preference. We selected not recently published articles to avoid bias in understanding the topics. Thirty-five MTurk participants attended the task, with no specific prior background in summarisation. To ensure the human subjects understood the study's objective, the workers were asked to complete a qualification task, requiring them to write a summary of a news article. The results that did not have meaning or structure were labelled as spam and removed manually from the data. For example, in the qualification tasks, we asked users to write a summary explaining the main parts of a document. Some results could not pass the qualification task. Another example is the short response time, proving that the answers are random or not carefully provided in advance. We analyse four evaluation aspects including (i) information coverage (how much information the summary covers), (ii) knowledge extraction (how much users can learn from summaries), (iii) effectiveness (the users' learning speed) and (iv) user preference (the users' preference compared to other approaches).

## Information Coverage

To automatically evaluate SNARS using traditional state-of-the-art approaches, consider the summaries as the first level of the hierarchy. Besides, considering all hierarchical levels leads to a high ROUGE value that generates an unfair comparison while exceeding the summary limit size.

To evaluate FNARS, we concatenated all concepts as a textual summary considering the limit size (b). The ROUGE results are illustrated in Table 5.1 and 5.2. According to Table 5.1 (DUC2002 dataset), SNARS outperforms most state-of-the-art approaches and competes with HSSAS and ExDos. Results on the CNN/Daily Mail dataset follow[^6]

TABLE 5.1: ROUGE Score ( $\%$ ) Comparison on DUC2002 Dataset

| Model | ROUGE-1 | ROUGE-2 | ROUGE-L |
| :--- | :---: | :---: | :---: |
| Lead-3 | 43.6 | 21.0 | 40.2 |
| ILP | 45.4 | 21.3 | 40.3 |
| TGRAPH $^{2}$ | 48.1 | 24.3 | N/A |
| URANK | 48.5 | 21.5 | N/A |
| NN-SE | 47.4 | 23.0 | 43.5 |
| SummaRuNNer | 46.6 | 23.1 | 43.03 |
| HSSAS | 52.1 | 24.5 | 48.8 |
| ExDos | 52.5 | 18.7 | 37.6 |
| SNARS | 52.9 | 24.8 | 48.9 |
| FNARS | 48.3 | 23.8 | 47.3 |

the same trend as DUC2002. Since we did not consider the hierarchical structure of summaries, this is a promising result that proves even the first level of both NARS techniques can compete with most state-of-the-art approaches.

The proposed approach generates a hierarchical structure that facilitates navigation rather than producing one optimised summary. Most state-of-the-art approaches will optimise their system based on reference summaries, with ROUGE being the measure with which to evaluate the common n-grams in both reference and generated summaries. Therefore, we used systems that were optimised based on a reference summary, and compared them with another reference summary with a better ROUGE value than our proposed approach. Note that the score in the CNN/Daily Mail dataset is generally lower compared to DUC2002. This is because gold-standard summaries include paraphrasing. Evidently, FNARS did not present promising results in terms of the ROUGE measure. This was expected, as FNARS is an abstract model that does not provide detail. Its advantage instead rests in its structured format, which facilitates further processing for users. Nonetheless, FNARS helps users to understand the topics in a dataset quickly, while simultaneously highlighting the relations between concepts. The human evaluation of coverage aspect aims to evaluate how information

TABLE 5.2: Score Comparison on CNN/Daily Mail Using F1 Variant of ROUGE

| Model | ROUGE-1 | ROUGE-2 | ROUGE-L |
| :--- | :---: | :---: | :---: |
| Lead-3 | 39.2 | 15.7 | 35.5 |
| NN-SE | 35.4 | 13.3 | 32.6 |
| SummaRuNNer | 39.9 | 16.3 | 35.1 |
| HSSAS | 42.3 | 17.8 | 37.6 |
| BanditSum | 41.5 | 18.7 | 37.6 |
| ExDos | 42.1 | 18.9 | 37.7 |
| Transformer | 40.9 | 18.2 | 37.2 |
| BERTSUM+Transformer | 43.2 | 20.2 | 39.6 |
| SNARS | 42.9 | 19.1 | 37.8 |
| FNARS | 40.1 | 18.6 | 37.1 |

is scattered throughout the hierarchy. We asked MTurk workers to read an article on a topic and then select the three most important sentences and concepts and then three most critical secondary sentences and concepts.

We combined responses from participants according to the topic and chose the three most basic primary and secondary sentences and concepts. We manually analysed the presence of these sentences and concepts in the first and second levels of the hierarchy using different summarisation approaches. We also evaluated the position of sentences and concepts in the hierarchy. Next evaluated were the SNARS and FNARS based on the recall measure, the percentage of essential sentences, and concepts mentioned at the first and second top levels. We repeated this experiment for 30 topics and averaged the recall measures. SNARS retrieved $92.1 \%$ of all important sentences at the first level and $7.3 \%$ at the second level; FNARS retrieved $63 \%$ of all critical concepts at the first level and $26.9 \%$ at the second level. This experiment illustrates that even the first level of hierarchy works as a general summarisation approach containing the most critical sentences. Besides, users are allowed to navigate the hierarchy should they desire more detail, as in FNARS. However, since the representing unit in FNARS is a concept and a concept map, rather than a sentence hierarchy, this puts far less cognitive burden on



Figure 5.5: Time each user took to answer predefined questions when reading different summarisation approaches.

users in terms of navigation.

## Knowledge Extraction and Speed

Evaluating the information users gain by allowing them the freedom to seek what they desire based on personal interest is a challenging task. As such, we designed two experiments that contain an approximation evaluation.

In the first experiment, we gave 10 MTurk workers two minutes to read a summary generated by a traditional competitor approach (ExDos), the full text, and NARS variants. We chose different topics for each user to avoid bias by learning from other summaries. Then, participants were asked to write down their understanding. We could not evaluate the result automatically using the ROUGE measure, as the concepts were all paraphrased by the users. Therefore, an evaluator manually assessed the understating level and details based on participants' answers without knowing which approach was used (again, to avoid bias). We also prepared a predefined list of answers and scored workers' responses based on the percentage of concepts covered by their answers. The results show that users are able to identify general information when reading any of the summaries (the scores were all above 8). However, the MTurk workers could identify more details when SNARS was shown to them. Conversely,



Figure 5.6: Accuracy of users' answers when reading summaries generated using different approaches.

users who answered by reading the FNARS could mention broader concepts but in less detail.

In the second task, 10 workers were given a set of predefined questions and asked to respond to a specific summary. The questions were selected to cover different aspects (e.g., either more detailed or more general). Each question came with multiple answers from which to select. Participants' speed and the accuracy of their answers were recorded. Fig. 5.5 and 5.6 show that reading a full text takes time but helps users answer questions correctly. In contrast, traditional approaches take less time but yield less accurate results. For example, answering using FNARS took the least amount of time, since few details are provided, but discouraged correct answers, as users were forced to respond using inference. In contrast, answers based on SNARS demonstrated reasonable results in terms of both time and accuracy.

## User Preference

To present how the proposed approach could improve the drawbacks of previous approaches, we considered the following seven properties:



Figure 5.7: User preferences based on different aspects mentioned in Table 4.5(tie is allowed).

Table 5.3: Comparing Previous Approaches Based on Different Features

|  | F1 | F2 | F3 | F4 | F5 | F6 | F7 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Original Text | - | - | - | + | - | - | - |
| Traditional | + | + | - | - | - | - | - |
| Timeline | $*$ | + | $*$ | $*$ | $*$ | - | - |
| Document Thread | $*$ | + | - | - | - | - | - |
| Concept Map | $*$ | + | + | - | + | - | - |
| SUMMA | + | + | + | + | + | - | + |
| NARS | + | + | + | + | + | + | + |

F1:Overview; F2: Redundancy; F3: Relation; F4: Detail; F5: User friendly; F6: Multifaceted; F7: Personalised. (The notion + shows a fully positive indicator of the property; - is a fully negative indicator of the property; $*$ is a partial indicator of the property).

- Overview-whether a summary provides an overview of a document.
- Redundancy-if the summary removes any redundant parts.
- Relation-the relation (if any) between factors in documents.
- Details - whether details can be accessed in the produced summary.
- User-friendliness-if the model is easy to use.
- Multifaceted - if the hierarchy is based on one feature, such as time, or multiple features.
- Personalisation - if the summary can be tailored to individual users.

We compared the state-of-the-art categories based on the criteria in Table 5.3. These approaches include traditional approaches, timelines, document thread approaches, concept map summarisation, and SUMMA. The proposed approach-a hierarchical personalised summarisation - has all the key features of a proper summary (defined in Table 5.3). To evaluate how hierarchical summarisation can help users obtain their required information, we selected news articles covering various topics. We then asked 10 MTurk workers to rank their preferred summary among six competitors with various structures, considering the different aspects mentioned in Table 5.3 (with ties permitted). The results (percentage) are averaged among 10 workers and are illustrated in Fig. 5.7. Overall, SNARS achieves better results across the criteria in all metrics.

### 5.5 Summary

This chapter proposed NARS, a novel personalised interactive hierarchical summarisation approach that enables users to explore whatever information they desire with minimal reading required. NARS is in contrast to a generic summary and is unique for all users. Users are able to obtain information based on their individual needs and interests by navigating the personalised hierarchy. Two NARS variants were proposed,
the SNARS and the FNARS. FNARS provides a more concise overview of information, while SNARS provides greater detail. Conversely, FNARS is a fully structured model and can be used for further analysis. The proposed approaches help users with general knowledge about a topic to explore a wide range of information. As such, we evaluated our approach using both automatic and human evaluation, considering four aspects: information coverage, knowledge extraction, effectiveness and user preference. The results prove the use of the proposed approach as a personalised summarisation technique.

## Towards Personalized Document

## Summarisation

Making a user-specific summary is a challenging task. In a personalised approach, the system needs to know about users' background knowledge or interests. When we do not have access to this prior knowledge base, the system requires interaction to acquire feedback for modelling user interests. Along this line, we provide human-in-the-loop approaches to create a personalised summary that understands individual needs better. Further, it eliminates the need for reference summaries, which is a challenging issue for summarisation tasks. The goal of this chapter is to answer the following questions:

- What structures are required to help users seek their desired information?
- How can we use human feedback so that summarisation approaches can adapt to
users' needs?
- Can we simulate users' behaviour to predict their ideal summary?
- How can we eliminate the need for reference summaries to reduce the summarisation cost?
- Can user preferences over concepts provide personalised summaries that reflect users' interests with less cognitive load?
- Can domain expert knowledge be embedded in the learning process?
- How can user preferences and domain expert experiences be combined to automatically generate the desired summaries?

We provide three solutions to answer these questions. We propose human-in-theloop summarisation approaches to generate personalised summaries that can capture users' interests and needs. First, we propose a novel optimisation algorithm that directly reflects users' interest in making extractive summaries, called 'adaptive summaries'. Second, we propose a preference-based interactive summarisation algorithm that extracts users' interests and generates user-adapted results. The proposed method, SumRecom, learns to predict users' preferences by utilising their feedback and creating a behavioural model following an RL approach. Predicting users' desired structured summary is another challenge addressed in this chapter, called 'summation'.

### 6.1 Adaptive Summaries

Adaptive summaries are extractive concept-based summarisation models that interact with users to generate content-specific summaries instead of single inflexible summaries. The system learns gradually from information provided by users while interacting with them in an iterative loop. We allowed even novice users to interactively explore, manipulate and analyse sizeable, unstructured text document collections to integrate their



Figure 6.1: An overview of the proposed approach (Adaptive Summaries). 1) Summaries are initiated with ExDos. 2) Users integrate their preferences in making summaries by giving feedback in an iterative loop. 3) An example of user interaction.

user-specific notion of importance. Our model also employs an ILP optimisation function to maximise user-desired content selection. An overview of the proposed approach is illustrated in Fig. 6.4.

The input is a set of documents, and the output is a human-readable summary consisting of a group of sentences set according to the user's preference. As mentioned, users are allowed to provide their feedback in an iterative loop and can also choose which concepts they deem important and that degree of importance. Moreover, they can define the confidence level in their choices and can even select which concepts not to include in the final summary. The proposed approach learns to select sentences that maximise the summary score according to user feedback. To guarantee interactive speed and keep users engaged, we propose a heuristic approach for selecting users' queries. Sec. 6.1.1 formally defines the summarisation tasks specified in this model.

### 6.1.1 Problem Definition

The input is a set of documents $D=\left\{D_{1}, D_{2}, \ldots, D_{N}\right\}$, and each document consists of a sequence of sentences $S=\left[s_{1}, s_{2}, \ldots, s_{n}\right]$. Each sentence $s_{i}$ is a set of concepts $\left\{c_{1}, c_{2}, \ldots, c_{k}\right\}$, where a concept can be a word (unigram) or a sequence of words. This framework optimises the summarisation outcome for a specific user. Therefore, the user interacts with the system, and their feedback is used to make the summaries. Feedback comes in three forms, characterised as:

- action, $A$, or accepting $(\mathrm{A}=1)$ or rejecting $(\mathrm{A}=-1)$ the value of extracted concepts
- concept weight, $W$, or corresponding to a concept's importance according to the user's opinion
- confidence level, conf, representing one's confidence in choosing each action.

The output is a set of sentences in $S$ according to the budget limit (b) defined by the user.

### 6.1.2 Methodology

The goal of adaptive summaries is to incorporate user preferences to generate a summary. Therefore, a continuous objective function is defined for analytically optimising the user preference. In the first iteration, a summary is generated using ExDos, which ranks sentences based on a general notion of importance using dynamic local feature weighting. It also demonstrates sentences in groups based on their similarity to help users select content. The user can then choose an action $A$,, denoting a concept, where the values can either be accepted $(A=1)$ or rejected $(A=-1)$. Next, for each concept, users can define a weight, $W$, corresponding to a concept's importance based on personal opinion. The user then defines the level of confidence, conf, for the chosen action. When the action is accepted, this weight represents the importance of the concept, and when the action is rejected, the weights represent the value of no relation. The logic behind this is that not all concepts have an equal level of importance. For example, when a user searches for the specific symptoms of an illness, a headache may not be
as important as sneezing from one perspective to another. Conversely, a fever may not be as unrelated as acne. The overall objective function, which is an ILP, is defined in Eq. 6.1.

$$
\begin{aligned}
\operatorname{maximize} & \sum_{s_{i} \in D} \sum_{c_{j} \in s_{i}} A \times \operatorname{con} f(A) \times W_{c_{j}} \\
\text { s.t. } & \sum_{s \in \text { Summary }} \text { length }(s)<b,
\end{aligned}
$$

where $A$ is the action, $c_{j}$ is the concept in a given sentence $\left(s_{i}\right)$, D denotes the source documents, $W_{c_{j}}$ is the corresponding user preference weight for the concept $c_{j}$, and $b$ is the summary length given by the user. The objective function in Eq. 6.1 maximises the occurrence of concepts with maximum weights and maximum confidence level. The following is an in-depth description of the proposed approach:

- To accelerate the process of making a summary, in the first iteration, the sentences are ranked by ExDos. Then, weights are updated based on user feedback. To prevent users from being overwhelmed, similar sentences (with common concepts) are grouped and shown to the user simultaneously.
- If the weight of a concept is updated in an iteration, the weight is also updated for every occurrence of that concept.
- If the user rejects a sentence $\left(A_{s_{i}}=-1\right)$, then the weight of the sentence is set to $0\left(W_{s_{i}}=0\right)$. However, the system does not update the weights of concepts included in the sentence, as there may be different reasons for its rejection, such as redundancy or lack of importance.
- A concept is only selected if it is present in at least one of the selected sentences.
- The number of sentences is a user parameter defined in each iteration, and the confidence in feedback is set to 1 by default.
- If there are no more concepts to query, the process is terminated.

The pseudo code of the proposed algorithm is reported in Algorithm 2.

```
Algorithm 2 Adaptive Summaries
    Input: Document cluster
    Output: Optimal summary generated by user \((S)\)
    RankedSentences \(\leftarrow \operatorname{ExDos}(D)\)
    : While user is not satisfied
        Concepts \(\leftarrow\) ExtractNewConcepts \((\) RankedSentences)
        if Concepts \(\neq \emptyset\)
            Ask user for action (A), importance(W), and confidence (Conf)
            Select sentences to maximize Eq. 6.1
    return Summary(S)
```


### 6.1.3 Experiment

This section presents the experimental set-up for implementing and assessing the summarisation model. In traditional approaches, to evaluate a summarisation system, the mean ROUGE scores across clusters are averaged. Adaptive summaries are evaluated using mean ROUGE scores across clusters per standard summary.

It is worth mentioning that this approach aims at facilitating the creation of summaries for individual users, not for improving the general accuracy of summaries. Since this approach is interactive, it requires humans to interact with the system for a user study-based evaluation. However, collecting data for different settings from different humans is too expensive. Thus, we simulated users' behaviour by generating feedback using two variations of the proposed approach.

In the first approach (AdaptiveDictionary), we defined a dictionary for 10 clusters of topics including the essential concepts and weights, with defined actions for each concept. In the second one (AdaptiveReference), the reference summaries are considered the users' feedback. The concepts are essential if they are presented in the reference summary. Therefore, we assigned the maximum weight for the presented concepts. We compared our approach with both traditional and personalised approaches, the
results of which are reported in Table 6.1 and 6.2 for both datasets. As discovered, the proposed approach nearly surpasses the competitors for both datasets.

The ROUGE analysis with real users does not show any pattern of increasing or decreasing. However, this is expected since the approach aims to optimise the ouput summary for individual users and is not a gold-standard summary.

To compare each concept's unit's effect, we evaluated our approach based on three unit measures: unigrams, bigrams and sentences. Although our model reaches the

TABLE 6.1: ROUGE score comparison on CNN/DailyMail using F1 variant of ROUGE.

| Model | Rouge-1 Score | Rouge-2 Score | Rouge-L Score |
| :--- | :---: | :---: | :---: |
| LEAD-3 | 39.2 | 15.7 | 35.5 |
| NN-SE | 35.4 | 13.3 | 32.6 |
| SummaRuNNer | 39.9 | 16.3 | 35.1 |
| HSSAS | 42.3 | 17.8 | 37.6 |
| BANDITSUM | 41.5 | 18.7 | 37.6 |
| Adaptive dictionary | 42.9 | 20.1 | 38.2 |
| Adaptive reference | 41.4 | 19.7 | 32.1 |

TABLE 6.2: ROUGE score ( $\%$ ) comparison on DUC-2002 dataset.

| Model | Rouge-1 Score | Rouge-2 Score | Rouge-L Score |
| :--- | :---: | :---: | :---: |
| LEAD-3 | 43.6 | 21.0 | N/A |
| NN-SE | 47.4 | 23.0 | N/A |
| SummaRuNNer | 46.6 | 23.1 | N/A |
| HSSAS | 52.1 | 24.5 | N/A |
| Upper Bound | 47.4 | 21.6 | 18.7 |
| Avinesh-Al | 44.8 | 18.8 | 16.8 |
| Avinesh-Joint | 44.4 | 18.2 | 16.5 |
| Adaptive dictionary | 50.4 | 22.1 | 18.4 |
| Adaptive reference | 46.5 | 20.1 | 18.8 |



Figure 6.2: Left graph shows the ROUGE-1 based on iteration number, and the right graph shows the ROUGE-2 based on iteration number. The green samples represent the permitted concept unit in unigrams, blue denotes bigrams and red represents sentences.

upper bound when using unigram-based feedback, it requires significantly more iterations and feedback to converge, as shown in Fig. 6.2. We further analysed the speed (iterations) and the accuracy (ROUGE-1 and ROUGE-2) for different concepts' units for DUC2002. The CNN/Daily Mail dataset follows the same trend. The graphs show that when the permitted selection unit is a unigram, the ROUGE-1 score is higher. However, it takes more iterations to converge. For ROUGE-2, both the bigram and unigram have higher scores; however, the former converges sooner.

Another experiment considered the ROUGE scores versus the number of iterations. Fig. 6.3(A) and 6.3(B) show the results for the DUC2002 dataset for two versions of adaptive summary, using a dictionary and a reference summary as feedback, respectively. Fig. 6.3(B) represents the models evaluated based on the action number (A) taken by the users to converge to the upper bound within 10 iterations. While adaptive summaries incorporate user feedback to generate summaries, they require interaction. Therefore, there is a need to predict users' behaviours.

### 6.2 SumRecom

Making a user-specific summary involves (i) acquiring relevant information about a user, (ii) aggregating and integrating that information into a user model, and (iii)


Figure 6.3: (A) Number of iterations and ROUGE-1 for DUC2002. (B) Number of iterations versus ROUGE-2 values. (C) Number of actions versus iterations for DUC2002.

generating the personalised summary. As such, we incorporated human-in-the-loop systems and created a personalised summary that can predict users' needs based on samples of their feedback. The rationale behind this was to evaluate the quality of a summary based on a domain expert's knowledge given users' feedback, and to keep humans in the loop through interaction. To reduce users' cognitive burden when providing feedback, we considered two aspects. First, feedback should be given based on preference, and second, users' preferences should be formed as concepts and not complete summaries. Moreover, users are allowed to define the detailed properties of the produced summaries, thus, helping to reduce the search space by leveraging their feedback.

The proposed method, SumRecom, is a preference-based interactive summarisation approach that extracts users' interests to generate user-adapted results. SumRecom predicts users' desired summaries by incrementally adapting the underlying model through interaction. The proposed approach has two steps involving (i) the user preference extractor and (ii) the summariser. Our model employs active learning and preference learning to extract users' preference in selecting content. SumRecom also utilises ILP to maximise user-desired content selection based on the given feedback. It then proposes an IRL algorithm using domain expert knowledge for evaluating the quality of summaries based on the given feedback. The learnt reward function is used to



Figure 6.4: Overview of the SumRecom approach. Active and preference-based learning are used to extract users' preferences. The learnt preference ranked function is used to produce the desired summary using IRL for learning the reward. An RL algorithm is proposed for learning the optimal policy.

learn the optimal policy to produce the desired summary using RL. A general overview of the algorithm is depicted in Fig. 6.4. Before explaining the proposed method, we observe preference-based and reinforcement-based approaches used for summarisation.

### 6.2.1 Preference-based and Reinforcement-based Approaches

There is increasing research interest on using preference-based feedback and RL algorithms in summarisation. For example, one approach is to learn a sentence ranker function based on human preferences on sentence pairs [167]. The ranker function is then used to assess the summaries' quality by calculating the number of high-ranked sentences inserted in the summary. RL-based approaches are employed for extractive and abstractive summarisation recently [113-115].

Most existing RL-based document summarisation systems employ heuristic methods to determine the reward function and, therefore, are not dependant on reference summaries $[113,116]$. Other approaches use different ROUGE measure variants as the reward function and, therefore, require reference summaries for estimating the reward value $[114,115,117]$. However, neither ROUGE nor the heuristics-based methods can determine users' preferences as the reward [191]. Therefore, using these imprecise reward models can critically deceive the RL-based summariser. The reward quality is the biggest bottleneck for RL-based summarisation [118].

## Summary1.

The historic California drought hurts the rest of the union, too. That's because California is a breadbasket to the nation. California is growing more than a third of its vegetables and nearly two-thirds of its fruits and nut. Jerry Brown to announce a mandatory $25 \%$ cutback in water consumption in all cities.

## Summary 2.

The historic California drought hurts the rest of the union, too. California is growing more than a third of its vegetables and nearly twothirds of its fruits and nut. It is an expanding natural disaster now in its fourth year. Jerry Brown to announce a mandatory $25 \%$ cutback in water consumption in all cities.

Figure 6.5: Comparing two summaries that put significant cognitive burden on users.

Both preference-based and RL algorithms have been used in summarisation simultaneously. The first approach is SPPI $[168,169]$, a policy-gradient RL algorithm that rewards are made based on the given preference-based feedback. One drawback with SPPI is that it suffers heavily from the high sample complexity problem. However, the complexity of SPPI is a severe problem. Another recent preference-based RL approach is APRIL [170], which has two stages. First, the users rank candidate summaries, and then a neural RL agent is used to find the optimal summary. However, preferring one summary to another in both approaches puts considerable burden on users. It is worth mentioning that summarisation aims to provide users with a summary that reduces the need to read multiple documents. Although asking users to favour a summary to another in multiple rounds among a summary space that includes all randomly possible combinations of sentences puts additional cognitive load on them, this still outweighs the demand of reading. Fig. 6.5 represents an example of this comparison, where the challenge to read summaries increases as the summary length increases.

### 6.2.2 Methodology

One of the ultimate goals of machine learning is to provide predictability. Part of this concerns personalisation, which is fundamental to constructing tailored summaries. Hence, we propose a human-in-the-loop approach to better capture users' needs. SumRecom considers the summarisation problem a recommender system, where the goal
is to suggest a personalised summary to a user based on their preferences. This novel framework has two components-(i) the user preference extractor and (ii) the summariser. The user preference extractor is responsible for querying the user and potentially receiving their feedback using active preference learning; the summariser aims to learn how to create summaries that are tailored to users' needs based purely on their feedback [192]. The process is depicted in Fig. 6.6 and the overall algorithm is reported in Algorithm 3.

## User Preference Extractor

Understanding users' interests is the first step towards making personalised summaries. Individual interests can be extracted implicitly based on personal profiles, browsing history, likes or dislikes, or by retweeting content on social media [193]. Consequently, interaction is gauged to predict users' perspectives in a variety of circumstances based on the feedback they have provided in the past. This feedback can be in any form, such as a mouse click or an edit to a post on social media. Further, experiments suggest that preference-based interactive approaches put less cognitive burden on human subjects compared to asking for absolute ratings or labels, as in a binary decision [167, 194]. For example, asking users to compare two concepts, such as 'cancer treatment' and 'cancer symptoms', compared to scoring each of these concepts requires less cognitive workload. Conversely, it is equally challenging for users to decide the value of a summary using a scoring scheme. Therefore, to reduce cognitive load, queries are in the form of concept selection, where feedback denotes user preference.

Concept selection aims to find the critical information among the source documents, as humans can quickly assess the importance of concepts given a topic. Since the notion of importance is specific to a particular topic or user, we queried users' preference over concepts, as it is easier to prefer one concept to another rather than select important concepts. However, to collect sufficient data for a meaningful conclusion, we required users to interact with the system in many rounds to simulate ideal user feedback data. Therefore, active learning was used to reduce the number of interaction rounds. To recap, we used active preference learning in an interaction loop to maximise the



Figure 6.6: SumRecom approach in more detail: 1) The left side is the user preference extractor using active preference learning over concepts, and 2) the right side is the summarizer including reward learning (IRL) and policy learning (RL).

information gained from small preferences samples, hence, reducing the complexity.

```
Algorithm 3 SumRecom algorithms.
    1: Input: Document cluster d
    : Output: Optimal summary for a user
    3: \(\quad\) Concepts \(\leftarrow\) Concept extraction (d)
    4: Modeling User Preference
    5: \(\quad\) Query pairs \(\leftarrow\) Active Learner (concepts)
    6: User Preferences \(\leftarrow\) Query pairs (user)
    7: \(\quad\) Ranker function \(\leftarrow\) Preference learner (user preferences)
    8: The summariser
    9: \(\quad\) Summaries \(\leftarrow\) Summary generator (ranking function)
    10: \(\quad\) Summary ranker \(\leftarrow\) Reward learner (summaries)
    11: \(\quad\) Optimal Policy \(\leftarrow\) Policy learner (summary ranker)
```

Preference learning. Preference learning is a classification method that learns how to rank instances based on observed preference information. It learns based on a set of pairwise preferred items and by obtaining the total ranking of objects [195].

To formally define the preference learning in the proposed algorithm, let $D$ be the input space and $d$ a cluster of documents. Also define $C(d)$ as all the extracted concepts from document cluster $x$. Therefore, we have the concept space $C(d)=\left\{c_{1}, c_{2}, . ., c_{N}\right\}$
with $N$ concepts. The goal is to query users' pairwise preference among a set of concepts $\left\{p\left(c_{11}, c_{21}\right), p\left(c_{12}, c_{22}\right), \ldots, p\left(c_{1 n}, c_{2 n}\right)\right\}$, where $p\left(c_{1 i}, c_{2 i}\right)$ is a preference instance shown to users in $i-t h$ round, and Eq. 6.2 is as such:

$$
p\left(c_{1 i}, c_{2 i}\right)= \begin{cases}1, & \text { if } c_{1 i}>c_{2 i} \\ 0, & \text { otherwise }\end{cases}
$$

where $>$ indicates the preference of $c_{1 i}$ over $c_{2 i}$. Then, preference learning aims to predict the overall ranking of concepts. The goal is to find a mapping function to transform data to real numbers, called utility function utility function $U$ such that $c_{i}>c_{j} \rightarrow U\left(c_{i}\right)>U\left(c_{j}\right)$, where $\mathrm{U}$ is a function $U: C \rightarrow \mathbb{R}$. In this problem, the ground-truth utility function $(U)$ measures each concept's importance based on users' attitudes ( no two items in $C(d)$ have the equal $U$ value). Finding the utility function is a regression learning problem that is well studied in machine learning. In this problem, the ranking function $(R)$ measures the importance of each concept based on users' attitude towards other concepts, defined in Eq. 6.3.

$$
R\left(c_{i}\right)=\sum \mathbb{1}\left\{U\left(c_{i}\right)>U\left(c_{j}\right)\right\}, \forall c_{j} \in C(d)
$$

where $\mathbb{1}$ is the indicator function. Therefore, $R$ gives the rank of $c_{i}$ among all extracted concepts in $d\left(C_{d}\right)$.

The Bradley-Terry model [196] is a probability model widely used in preference learning. Given a pair of individuals $c_{i}$ and $c_{j}$ drawn from some population, it estimates the probability that the pairwise comparison $c_{i}>c_{j}$ turns out true. Having $n$ observed preference items, the model approximates the ranking $R$ by computing the maximum likelihood estimate using Eq. 6.4.

$$
\begin{aligned}
J_{x}(w)= & \sum_{i \in n}\left[p\left(c_{1 i}, c_{2 i}\right) \log H\left(c_{1 i}, c_{2 i} ; w\right)+\right. \\
& {\left.\left.\left[p\left(c_{2 i}, c_{1 i}\right) \log H\left(c_{2 i}, c_{1 i} ; w\right)\right)\right)\right] }
\end{aligned}
$$

where $H(c)$ is the logistic function defined in Eq. 6.5.

$$
H\left(c_{i}, c_{j} ; w\right)=\frac{1}{1+\exp \left[U^{*}\left(c_{j} ; w\right)-U^{*}\left(c_{i} ; w\right)\right]}
$$

$U^{*}$ is the approximation of $\mathrm{U}$ parameterised by $w$, which can be learnt through different function approximation techniques. A linear regression model is designed for this purpose, defined in Eq. 6.6.

$$
U(c ; w)=w^{T} \phi(c)
$$

where $\phi(c)$ is the representation feature vector of concept $c$. For any $c_{i}, c_{j} \in C$, the ranker prefers $c_{i}$ over $c_{j}$ if $w^{T} \phi\left(c_{i}\right)>w^{T} \phi\left(c_{j}\right)$. By maximising the $J_{x}(w)$ in Eq. 6.4 we have Eq. 6.7

$$
w^{*}=\operatorname{argmax}_{w} J_{x}(w)
$$

The resulting $w^{*}$ using stochastic gradient ascent optimisation will be used to estimate $U^{*}$, which, can be used to produce the approximated ranking function $R^{*}$ : $C \rightarrow \mathbb{R}$. Maximisation of this objective function will assure those high probabilities are assigned to pairs with low loss. SumRecom learns a ranking over concepts and uses the ranking to guide the summariser.

Active Learning. To emphasise the need for active learning, consider a scenario in which we have $M$ sentences to summarise, and each sentence has four unique concepts on average. As a result, the number of unique concepts is $4 \times M$. Therefore, the number of pairwise preferences to query the user to have a complete comparison in this setting is equal to $\binom{4 M}{2}=\frac{4 M!}{2!(4 M-2)!}$. As an example, if $M=100$, this number is equal to 79,800 , which is impossible. Therefore, the aim of active learning is to find the minimum subset of best samples in our problem, as well as the best pairs, to query the user and gain the most information. Thus, the number of examples with which to query users is much lower than the number required in regular supervised learning. There are different strategies to find the minimum subset of best samples. Examples include $[197]:$

- balance exploration and exploitation: The exploration and exploitation of the data space representation are used to choose samples. In this strategy, the active learning problem is modelled as a CB problem.

```
Algorithm 4 Modeling User Preference.
    Input: Concepts, learning rate \(\left(\gamma_{1}\right)\), query budget \(t\)
    Output: Concept ranker function ( \(\mathrm{R})\)
    While \(\mathrm{i}=0, \ldots, \mathrm{t}\)
        \(\left(c_{1 i}, c_{2 i}\right) \leftarrow\) Select a pair based on Eq. 6.10
        \(p\left(c_{1 i}, c_{2 i}\right) \leftarrow\) Query user for the feedback
        \(w_{i+1}=w_{i}+\gamma_{1} \frac{\delta J_{x}(w)}{w}\) based on Eq. 6.4
    return ranker function \((R)\)
```

- expected model change: The policy behind this model is to select the samples that would most change the current model.
- expected error or variance reduction: This strategy selects samples that would most reduce the model's generalisation error or variance.
- uncertainty sampling: The idea is to select samples for which the current model is least certain of the correct output.
- conformal predictors: This method works based on the similarity of a sample with previous queried samples.
- query by committee: Here, different models are trained. The samples with which most models disagree, called the 'committee', have the potential to be queried.

As a solution, we propose a heuristic approach (presented in Algorithm 4) for selecting query sample pairs. The approach aims to select the most diverse concepts to compare at first and gradually move to similar ones to reduce the search space. For this purpose, we partitioned the concepts into clusters based on different similarity measures.

We used semantic and lexical similarity as the features. A similar measure was proposed by Falke et al. [15] for grouping similar concepts in the process of making a concept map. These features include normalised Levenshtein distance, Jaccard coefficient between stemmed content words, semantic similarity based on latent semantic
analysis [188], WordNet [189], and word embedding [198]. Then, we modelled the similarity as a binary classification using logistic regression such that a positive classification, $y=1$, denotes coreferent concepts, as in Eq. 6.8.

$$
P\left(y=1 \mid c_{1}, c_{2}, \theta\right)=\operatorname{Sigmoid}\left(\theta^{T} \delta\left(c_{1}, c_{2}\right)\right)
$$

where $\delta\left(c_{1}, c_{2}\right)$ are the features, $\theta$ the learnt parameters, and the sigmoid function is defined in Eq. 6.9.

$$
S_{\theta}(z)=\left(\frac{1}{1+e^{\theta(1-z)}}\right)
$$

Based on the similarity of the two concepts, we used an ILP function to find an optimised partitioning schema that maximally matches with the pairwise classifications and is transitive due to the constraints [190]. Let $x_{i j} \in\{0,1\}$ be a binary value representing the coreference of concepts $\left(c_{i}, c_{j}\right)$ and $p\left(c_{i}, c_{j}\right)$ denotes their coreference probabilities. The goal is to optimise the objective function in Eq. 6.10 using a greedy local search to partition similar concepts.

$$
\begin{aligned}
& \sum_{c_{i}, c_{j} \in C^{2}} p\left(c_{i}, c_{j}\right) x_{i j}+\left(1-p\left(c_{i}, c_{j}\right)\right)\left(1-x_{i j}\right) \\
& \text { s.t. } x_{i k} \geq x_{i j}+x_{j k}-1 \quad \forall i, j, k \in[1, . .,|C|] \text { and } i \neq j \neq k
\end{aligned}
$$

After partitioning similar concepts in each iteration (the number of iterations is equal to the query budget), we selected two concepts in different partitions. These concepts are chosen based on the trained similarity measure and by minimising the similarity of concepts chosen and previously queried pairs to gain maximum information.

## The Summariser

The user preference extractor's output is the ranking function that estimates each concept's importance based on user feedback. The summariser is responsible for making the desired summaries based on the given preferences. The summariser consists of
three phases-(i) a summary generator; (ii) an IRL to learn how to evaluate generated summaries based on an expert's evaluation history; and iii) an RL to learn how to generate the desired summary for the user.

The summary generator. Learning the importance of concepts for a user, $R$ function, we constructed summaries that are likely suited to users' desire to reduce the summary search space. Let $C(d)$ be the set of concepts in the input documents $d, p_{c_{i}}$ is the existence of the concept $c_{i}$ in the output to which $c_{i}$ belongs in this sentence, $w_{i}$ is the concept's weight (importance), $l_{j}$ denotes the sentence length $j, p_{s_{j}}$ is the existence of sentence $j$ in the output, and $L$ is the summary length constraint defined by the user. Based on these definitions, we formulated the following optimisation function (Eq. 6.11) using ILP, which selects sentences with important concepts based on user feedback:

$$
\max \sum_{i} w_{i} p_{c_{i}} \text { where } \forall i \in[1, . .,|C|] \text { and } \forall c_{i} \in s_{j} \sum_{j} l_{j} p_{s_{j}}<L
$$

Weights are based on the $\mathrm{R}$ function learnt in the previous part. Then, a summary pool is made using Eq. 6.11. To generate a diverse summary pool, among top score summaries (according to Eq. 6.11), we selected summaries with no redundancy. This is defined as the similarity of sentences within a summary without considering a user's mentioned concepts divided by the summary length. Document summarisation is then formulated as a sequential decision-making problem, solved by a proposed RL algorithm.

Problem Definition. We formulated summarisation as a discrete optimisation problem inspired by the APRIL approach [170]. Let $Y_{d}$ indicate the set of all extractive summaries for the document cluster $d$, where $y_{d} \in Y_{d}$ is a potential summary for document cluster $d$. The summarisation task is to transform each input $d$ to the best summary in $Y_{d}$ for the learnt preference ranking function. Extractive MDS is defined as a sequential decision-making problem that sequentially chooses sentences and adds them to a draft summary. Therefore, it can be defined as an episodic Markov decision process (MDP) problem.

An episodic MDP is a tuple $(S, A, P, R, T)$, where $S$ is the set of states, $A$ is the set of actions, $P: S \times A \times S \rightarrow \mathbb{R}$ is the transition function, $R(S, A)$ is the reward for performing an action $(A)$ in a state $(\mathrm{S})$, and $T$ is the set of terminal states. In the extractive MDS context, a state is a draft summary and A includes two types of actions - adding a new sentence to the current draft summary or terminating the summary construction process [118]. The reward function $R$ returns the reward score once the action is terminated; otherwise, it returns 0 because the summary is still under development and, hence, cannot be evaluated. A policy $\pi(S, A): S \times A \rightarrow R$ in an MDP defines the selection of actions in state S.

Episodic MDP for modelling document summarisation has two components: (i) reward, or what is defined as a good summary; and (ii) policy, or how to select sentences (actions) to maximise the rewards. State-of-the-art summarisation approaches are divided into two categories: cross-input paradigms and input-specific paradigms [118]. The former employs RL algorithms such that the agent interacts with a ground-truth reward oracle over multiple episodes to learn a policy that maximises the accumulated reward in the episode. The learnt policy is then applied to unseen data at test time (in this problem to generate summaries using new data). However, learning such a cross-input policy requires significant data, time, and tuning parameters because of the broad search spaces and delayed rewards. Conversely, a more efficient alternative to learning a policy is to learn input-specific RL policies which do not require parallel data or reward oracles. However, these policies depend on handcrafted rewards, so they are challenging to create to fit all inputs [118].

SumRecom takes advantage of two categories of cross-input and input-specific RL. First, it learns a cross-input reward at the training time and then employs the learnt reward to train an input-specific policy at test time.

The reward learner. SumRecom is inspired by IRL [192], where instead of the policy, it first learns the reward utilising a domain expert to find optimal trajectories. The demonstrator is a domain expert who can evaluate two summaries based on user feedback. The domain expert can be another RL agent trained to become an advisor for other learner agents, or a human. To learn the ground-truth reward, numeric scores
indicating the summaries' quality and preferences over summary pairs are used [199]. In practice, leveraging preference learning reduces the cognitive load and, consequently, the inevitable noise in evaluating summaries. SumRecom learns from preference-based (pairwise) feedback that ranks preferences over summary pairs. Then, the summaries are queried to the demonstrator for evaluation.

For point-based oracles, we drew $L$ sample outputs from the summary pool without replacement. We used ExDos to evaluate the summaries based on three measures: coverage, salience and redundancy. In each iteration, unique summaries compared with previously selected samples were chosen for query. The same approach was also selected for preference-based summaries. We then queried their score values $(V)$ from the oracle and used a regression algorithm to minimise the average mean squared error between $V$ and the approximate value $V^{*}$, where the loss function is defined in Eq. 6.12.

$$
\mathcal{L}^{M S E}=\frac{1}{L} \sum_{i=1}^{L}\left(V^{*}-V\right)^{2}
$$

In pairwise oracles, we denote the collected preferences by $P_{s}=\left\{p\left(y_{11}, y_{12}\right), \ldots, p\left(y_{11}, y_{2 l}\right)\right\}$, where $y$ denotes the summary and $l$ sample pairs are queried. Then, the procedure is the same as in Eq. 6.4 using the cross-entropy loss function, defined in Eq. 6.13 and Eq. 6.14.

$$
\begin{gathered}
\mathcal{L}^{C E}=-\sum_{i \in l}\left[p\left(y_{1 i}, y_{2 i}\right) \log H\left(y_{1 i}, y_{2 i} ; w\right)+\right. \\
\left.\left.\left[p\left(y_{2 i}, y_{1 i}\right) \log H\left(y_{2 i}, y_{1 i} ; w\right)\right)\right)\right]
\end{gathered}
$$

where

$$
H\left(y_{1 i}, y_{2 i} ; w\right)=\frac{1}{1+\exp \left[V^{*}\left(y_{j} ; w\right)-V^{*}\left(y_{i} ; w\right)\right]}
$$

The output is the ranked function, $V$, which demonstrates each summary's reward compared to the others. Since such a demonstrator is hardly available in practise, SumRecom leverages an approximate function to learn the reward.

The policy learner. The goal of policy learning is to search for optimal solutions in MDP environments. We modelled the summarisation problem as an episodic MDP,

```
Algorithm 5 Summariser
    1: Input: Concept ranker \((\mathrm{R})\), learning rate \(\left(\gamma_{2}\right)\)
    Output: Optimal summary for a user (S)
    3: Summaries \(\leftarrow\) Generating summaries using Eq. 6.11.
    4: While \(\mathrm{i}=0, \ldots, \mathrm{t}\)
    5: \(\quad\left(y_{1 i}, y_{2 i}\right) \leftarrow\) Select a pair based on Eq. 6.13 from summaries
    6: \(\quad p\left(y_{1 i}, y_{2 i}\right) \leftarrow\) Query user for the feedback
    7: \(\quad w_{t+1}=w_{t}-\gamma_{2} \frac{\mathcal{L}^{C E}(w)}{\delta w}\) based on Eq. 6.12 or Eq.6.13.
    8: \(\quad \pi^{*}=\operatorname{argmax} R^{R L}(\pi \mid x)=\operatorname{argmax} \sum_{y i n Y} \pi(y) V(y)\)
```

meaning that each action's reward is equal to 0 if the state is not terminated. At each step, the agent can perform either of the two actions - add another sentence to the summary or terminate it. The immediate reward function $R(S, A)$ assigns the reward if $S$ is the terminate state. The reward in SumRecom is the learnt expert's reward, $V$. A policy $\pi$ defines the strategy to add sentences to the draft summary to build the summary for the user. SumRecom then defines $\pi$ as the probability of choosing a summary of $y$ among all summaries $Y$, denoted as $\pi(y)$. Therefore, the optimal policy, $\pi^{*}$, is the function that finds the desired summary for a given input based on users' feedback. The expected reward of applying policy $\pi$ is defined in Eq. 6.15.

$$
R^{R L}(\pi \mid d)=\mathbb{E}_{y \in Y} R(y)=\sum_{y \in Y} \pi(y) R(y)
$$

where $R(y)$ is the reward for selecting summary $y$ in document cluster $\mathrm{d}$. In our problem, the reward is the ranker approximated by the domain expert, $V$. Therefore, the accumulated reward to be maximised in our problem is equal to Eq. 6.16.

$$
R^{R L}(\pi \mid d)=\sum_{y \in Y} \pi(y) V(y)
$$

The MDP aims to find the optimal policy $\pi^{*}$ that has the highest predicted reward

(Eq. 6.17).

$$
\pi^{*}=\operatorname{argmax} R^{R L}(\pi \mid d)=\operatorname{argmax} \sum_{y \in Y} \pi(y) V(y)
$$

We used the linear temporal difference algorithm to obtain $\pi^{*}$. The summariser algorithm is explained in Algorithm 5.

### 6.2.3 Experiment

This section presents the experimental set-up for implementing and assessing the proposed model. First, we explain the evaluation settings and then present the results for analysis. SumRecom is evaluated from different evaluation aspects, including:

- the effect of different features in approximating preference learning algorithms used in the model, including concept and summary preferences
- the use of different strategies for active learning
- the role of the query budget in both concepts and summary preferences
- the quality of produced summaries
- a human study to evaluate SumRecom from users' perspective
- the effect of different values for parameters
- an ablation study to evaluate different components of the proposed framework.


## Feature Analysis

Before evaluating the effect of concept preference in summarisation, it is important to explain the ground-truth concept ranker function $(U)$ and the approximate function $\left(U^{*}\right)$. The ground-truth concept ranker function $(U)$ indicates the importance of each concept. We defined a predefined list of preferences over concepts and the groundtruth concept ranker value for 10 clusters to simulate users' preferences. To estimate the approximate function $\left(U^{*}\right)$, we defined a linear model $U^{*}(c)=W^{T} \phi(c)$ where $\phi$ are


Figure 6.7: Features for estimating the ranker function for preferred concepts.

the features. To this end, a set of features, whose importance was validated using ExDos (including surface-level and linguistic-level features), was used. Surface-level features include frequency-based features (TF-IDF, RIDF, gain, and word co-occurrence), word-based features (upper-case words and signature words), similarity-based features (Word2Vec and Jaccard measure), sentence-level features (position, length cut-off and length), and named entities. Linguistic features are generated based on a semantic graph, including the average weights of connected edges, the merge status of a sentence as a binary feature, the number of concepts merged with a concept, and the number of concepts connected to that concept. We defined different combinations of features, $\{2,5,8,10,12,15\}$, starting from the most critical feature based on the importance estimated using ExDos. We repeated the experiments for 10 cluster documents. The results of ROUGE-1 and ROUGE-2 are reported in Fig. 6.7.

The results show that the model performs better after adding more features; however, the last set of features did not significantly affect ROUGE values. It is worth mentioning that adding more features also increases complexity. To simulate domain expert
knowledge for evaluating summaries based on the available feedback (reward), we modelled the ground-truth summary reward (V) based on the three measures (ROUGE-1, ROUGE-2 and the redundancy) defined in Eq. 6.18.

$$
V=\alpha R O U G E 1+\beta R O U G E 2-\gamma \text { Redundancy }
$$

ROUGE-1 and ROUGE-2 are extensively used for human evaluation of summary quality. Redundancy is defined as the similarity of sentences within a summary without considering the user's mentioned concepts, divided by the summary length. To approximate the ground-truth reward function, we employed a linear function as $V^{*}=w^{T} \lambda(y)$, where $\lambda(y)$, which denotes both features and concepts in addition to ROUGE-1 and ROUGE-2 as the complete feature set. The results follow the same trend in Fig. 6.7, except that adding ROUGE-1 and ROUGE-2 as the feature set improves the performance of the final summaries by an average of .13 times.

## Active Learning Strategy Analysis

To evaluate the effect of the proposed heuristic approach for active learning, we compared SumRecom with six different strategies explained in Sec. 6.2.2. ROUGE-1 and ROUGE-2 results for each strategy are reported in Fig. 6.8, proving the supremacy of the proposed heuristic approach for our problem. As shown, the conformal approach performs similar to the proposed heuristic function. Besides, the change model is superior in both cases, proving that selecting the most diverse concepts results in better summaries.

## Query Budget Analysis

We also measured the effectiveness of users' query budget size in the process. We chose the query size among the selection of $\{10,15,20,25,30,35\}$, demonstrating each user's respective amount of feedback. The results are reported in Fig. 6.9. As expected, increasing the feedback number concurrently increases the ROUGE score significantly.


Figure 6.8: Comparing different strategies used in active learning.

However, the difference rate simultaneously decreases in the process.

## Summary Evaluation

To evaluate the coverage aspect of summaries generated by SumRecom, we used the reference summaries so that the mentioned concepts that exist in reference summaries receive the maximum score by the ranked function. Here, the reward function is the ROUGE score after comparing summary references. We compared SumRecom to state-of-the-art strength competitors including APRIL and SPPI on three benchmark datasets reported in Table 6.3, 6.4 and 6.5. The results show the supremacy of SumRecom. Indeed, the main goal of this approach is to help users create their desired


Figure 6.9: effect of query budget size in the quality of summaries.

summary while assuming little cognitive load. Thereafter, we conducted a study to evaluate cognitive load within this context.

## Human Analysis

The goal of SumRecom is to help users generate the desired summary with low cognitive load. Therefore, we conducted two human experiments to evaluate the model. We hired 15 MTurk workers to perform the tasks without any specific prior background

TABLE 6.3: Comparing SumRecom on DUC2001 Dataset

| Model | ROUGE-1 | ROUGE-2 | ROUGE-L |
| :--- | :---: | :---: | :---: |
| APRIL | 0.325 | 0.070 | 0.26 |
| SPPI | 0.232 | 0.068 | 0.259 |
| SumRecom | 0.341 | 0.078 | 0.28 |

TABLE 6.4: Comparing SumRecom on DUC2002 Dataset

| Model | ROUGE-1 | ROUGE-2 | ROUGE-L |
| :--- | :---: | :---: | :---: |
| APRIL | 0.351 | 0.078 | 0.279 |
| SPPI | 0.350 | 0.077 | 0.278 |
| SumRecom | 0.372 | 0.083 | 0.333 |

required. Ten document clusters were randomly selected from the DUC datasets, and each participant was presented with five random documents to avoid any subject bias, with two minutes to read each article. To ensure the human subjects understood the study's objective, workers were asked to complete a qualification task first. They were required to write a summary of their understanding. We also manually removed spam answers from the results. Spam was defined based on the qualification task and the response time (i.e., a very short answer time is unacceptable, as it proves random and/or imprecise).

In the first experiment, participants were asked to define their preferences by comparing some concepts. The generated summary based on the given feedback and four other general summaries were shown, and participants were asked to choose their preferred summary. Approximately $83 \%$ of participants selected the generated summary

TABLE 6.5: Comparing SumRecom on DUC2004 Dataset

| Model | ROUGE-1 | ROUGE-2 | ROUGE-L |
| :--- | :---: | :---: | :---: |
| APRI L | 0.373 | 0.093 | 0.293 |
| SPPI | 0.372 | 0.093 | 0.293 |
| SumRecom | 0.382 | 0.945 | 0.301 |

Table 6.6: Overview of the Parameters Used in Simulation Experiments

| Parameter | Description | Value |
| :---: | :---: | :--- |
| $\mathrm{L}$ | User input | Summary length |
| $\alpha$ | 0.8 | ROUGE-1 coefficient for ground truth reward in Eq. 6.18 |
| $\beta$ | 0.5 | ROUGE-2 coefficient for ground truth reward in Eq. 6.18 |
| $\gamma$ | 0.25 | redundancy coefficient for ground truth reward in Eq. 6.18 |
| $\gamma_{1}$ | 0.001 | learning rate for concept preference in Eq. 6.4 |
| $\gamma_{2}$ | 0.005 | learning rate for summary preference in Eq. 6.12 |

Table 6.7: Comparing SumRecom, SumRecom-AC and SumRecom-PR on DUC2001 Dataset

| Model | ROUGE-1 | ROUGE-2 | ROUGE-L |
| :--- | :---: | :---: | :---: |
| SumRecom-AC | 0.103 | 0.031 | 0.140 |
| SumRecom-PR | 0.112 | 0.001 | 0.129 |
| SumRecom | 0.341 | 0.078 | 0.28 |

produced by SumRecom. Then, the produced approach for each summary was provided. Participants were asked to define their satisfaction level and evaluate the produced summary based on their given feedback by assigning a rating between 0 and 10 . The average rating of summaries produced by SumRecom was 8.2 , demonstrating a reasonable level of satisfaction.

In the second experiment, to assess whether users can obtain the information they desire from a summary, participants were asked to answer a question about each topic by selecting an answer among a selection of potential responses. The questions were defined by the authors and covered both specific and general information. Participants' answers and their level of confidence in responding were recorded. An evaluator then assessed their accuracy. Among the 15 workers, $86.67 \%$ were completely confident in their answers; however, only $80 \%$ were accurate.

Table 6.8: Comparing SumRecom, SumRecom-AC and SumRecom-PR on DUC2002 Dataset

| Model | ROUGE-1 | ROUGE-2 | ROUGE-L |
| :--- | :---: | :---: | :---: |
| SumRecom-AC | 0.190 | 0.018 | 0.132 |
| SumRecom-PR | 0.157 | 0.021 | 0.198 |
| SumRecom | 0.572 | 0.083 | 0.333 |

Table 6.9: Comparing SumRecom, SumRecom-AC and SumRecom-PR on DUC2004 Dataset

| Model | ROUGE-1 | ROUGE-2 | ROUGE-L |
| :--- | :---: | :---: | :---: |
| SumRecom-AC | 0.111 | 0.033 | 0.143 |
| SumRecom-PR | 0.200 | 0.021 | 0.182 |
| SumRecom | 0.382 | 0.945 | 0.301 |

## Parameter Analysis

As in other parametric models, SumRecom has some hyper-parameters that require tuning. A wide range of these values was tested, and the correlation between them subsequently analysed. To reduce the need for reading and to help researchers replicate the proposed algorithm, Table 6.6 summarises the parameters with the same description used in our simulation experiments.

Table 6.10: Comparing SumRecom and SumRecom-GE

| Dataset | SumRecom |  | SumRecom-GE |  |
| :--- | :--- | :--- | :--- | :--- |
|  | ROUGE-1 | ROUGE-2 | ROUGE-1 | ROUGE-2 |
| DUC2001 | 0.341 | 0.078 | 0.222 | 0.021 |
| DUC2002 | 0.572 | 0.083 | 0.189 | 0.047 |
| DUC2004 | 0.382 | 0.945 | 0.109 | 0.510 |


#### Abstract

Ablation Study To evaluate each component's incremental contribution in our proposed framework, we ran ablation studies comparing our model ablations against each other. First, we evaluated the preference extractor, and, thus, removed active learning by selecting random pairs from the concept database, called SumRecom-AC. Then, the whole preference learner component was removed, called SumRecom-PR. The ROUGE scores of these approaches compared with the reference summaries after 10 complete runs are averaged and compared in Table 6.7, Table 6.8 and 6.9, respectively. The results clearly show the effect of both active learning and preference learning.

In another experiment to evaluate the role of learning, the summaries generated by a summary generator were considered output, called SumRecom-GE. The results are reported in Table 6.10, based on the average of 10 produced summaries.


# 6.3 Summation 

Lack of structure makes summaries challenging to process, but attempting to predict both personalised and structured summaries is a whole other task. As such, we propose a hierarchical personalised concept-based summarisation approach called 'Summation', which sums up a collection of documents to a concise hierarchical concept map. Instead of providing a short and static summary, Summation engages users by querying their preferences to learn what they desire. An RL algorithm is then used to provide a personalised summary of unseen topic-related documents. Summation provides a concise overview of a document collection for a specific user, structures it across document boundaries, and can be used as a navigator in document collections.

### 6.3.1 Problem Definition

The input is a set of documents $D=\left\{D_{1}, D_{2}, \ldots, D_{N}\right\}$ and each document consists of a sequence of sentences $S=\left[s_{1}, s_{2}, \ldots, s_{n}\right]$. Each sentence $s_{i}$ is a set of concepts $\left\{c_{1}, c_{2}, . ., c_{k}\right\}$, where a concept can be a word (unigram) or a sequence of words. The
output is a personalised hierarchical concept map. This novel framework has two components, an organiser and a summariser, explained in Sec. 6.3.2 and 6.3.3, respectively.

### 6.3.2 Organiser (Structuring Unstructured Data)

The first step is to structure unstructured information by making a hierarchical concept map. A concept map is a graph with directed edges, where nodes indicate concepts and edges indicate relations. Both concepts and relations are sequences of related words representing a semantic unit. Consequently, the first step in creating a concept map is to identify all concepts and relations. Here, we propose hierarchical clustering to form the hierarchical concept map. Abstract labels are created to make summaries concise and coherent.

## Concept and Relation Extraction

Concepts come in different syntactic types, including nouns, proper nouns, more complex noun phrases, and verb phrases that describe activities [15]. For this purpose, we used open information extraction (OIE) [187] through which the entities and relations are obtained directly from the text. OIE finds binary propositions from a set of documents in the form of $\left(\mathrm{Con}_{1}, R, \mathrm{Con}_{2}\right)$, which are equivalent to the desired concepts and relations. For example, the output for the sentence, 'cancer treatment is underpinned by the Pharmaceutical Benefits Scheme', is:

Cancer treatment $\xrightarrow{\text { is underpinned }}$ by the Pharmaceutical Benefits Scheme

Balancing precision and recall in extracting concepts is a challenging task. High precision means all identified spans will be defined as mentions of a concept. Therefore, some constructions are usually missed, and this lowers the recall. Conversely, a high recall is necessary since missed concepts can never be in a summary. Achieving a higher recall may cause extracting many mentions and increasing false positives. Generalisability is also essential. The reason is that extracting a particular syntactic structure might generate only correct mentions, causing too broad mentions. Ideally, a proper method applies to many text types. To avoid meaningless and long concepts,
we processed the OIE results such that concepts with less than one noun token or more than five tokens are omitted. The original nouns also replace pronouns. If an argument is a conjunction indicating conj-dependency in the parse tree, we split them.

## Concept Map Construction

Among various extracted concepts and relations, multiple expressions can refer to the same concept while not using precisely the same words; that is, they can also use synonyms or paraphrases. However, distinguishing similar concepts to group them is challenging and subjective. For example, adding a modifier can completely change the meaning of a concept based on the purpose of summarisation. Consequently, grouping them may lead to propositions that are not stated in the document. Therefore, we need to group every subset that contains mentions of a single, unique concept. Scalability is another critical issue. For example, pairwise comparisons of concepts cause a quadratic run-time complexity applicable only to limited-sized document sets. The same challenges exist for relation grouping. However, we first grouped all mentions by the concepts' pairs, and then performed relation grouping. Therefore, this task's scope and relevance are much smaller than when concepts are used. Therefore, in practise, comparison-based quadratic approaches are feasible. Moreover, as the final goal is to create a defined size summary, the summary size significantly affects the level of details in grouping concepts. This is because the distinction between different mentions of a concept might not be required, as it is a subjective task. Ideally, the decision to merge must be made based on the final summary map's propositions to define the necessary concept granularity.

We further propose hierarchical conceptual clustering using $\mathrm{k}$-means with word embedding vectors to tackle this problem, as it spans a semantic space. Therefore, word embedding clusters give a higher semantic space, grouping semantically similar word classes under the Euclidean metric constraint defined below. Before defining the proposed hierarchical conceptual clustering, we review word embedding schemes used in the proposed model.

Word Embedding. Word embedding is a learnt representation of text such that
the same meaning words have similar representations. Different techniques can be used to learn a word embedding from the text. Word2Vec [198] is an example of a statistical model for learning a word embedding representation from a text corpus, utilising different architectures. As such, we used skip-gram and bag of character ngrams in our experiments. The skip-gram model uses the current word for predicting the surrounding words by increasing the weights of nearby context words more than other words using a neural network model. One drawback of skip-gram is its inability to detect rare words. In another model, authors define an embedding method by representing each word as the sum of the vector representations of its character ngrams, known as 'bag of character n-grams' [200]. If the training corpus is small, character n-grams will outperform the skip-gram (of words) approach. ${ }^{1}$

Conceptual Hierarchical Clustering. Given word (concept) embeddings learnt from a corpus, $\left\{v_{w_{1}}, v_{w_{2}}, \ldots, v_{w_{T}}\right\}$, we propose a novel recursive clustering algorithm to form a hierarchical concept map, $H$. This variable denotes a set of concept maps organised into a hierarchy that incrementally maintains hierarchical summaries from the most general node (root) to the most specific summary (leaves). Within this structure, any non-leaf summary generalises the content of its children nodes. Hierarchical summarisation has two critical strengths in the context of large-scale summarisation. First, the initial information under review is small and grows upon users' request, so as not to overwhelm them. Second, the parent-to-child links facilitate user navigation and drilling down for more details on interesting topics. The hierarchical conceptual clustering minimises the objective function Eq. 6.19 over all $\mathrm{k}$ clusters as $\mathrm{C}=\left\{c_{1}, c_{2}, . ., c_{k}\right\}$.

$$
J=\sum_{k=1}^{K} \sum_{t=1}^{|T|}\left|v_{w_{t}}-c_{k}\right|^{2}+\alpha \min _{c \in C} \operatorname{size}(c)
$$

where $c_{k}$ is the randomly selected centre $k-t h$ cluster. The second term is the evenness of the clusters, added to avoid clusters with small sizes. $\alpha$ tunes the evenness factor, which was defined by employing a grid search over a development set. We also implemented hierarchical clustering top-down at each time, optimising Eq. 6.19. After[^7]defining the clusters, we must find the concept that best represents every concept at the lower levels to ensure hierarchical abstraction. A concise label is the desired label for each node; however, shortening mentions can introduce propositions that are not asserted by a text. For example, the concept labelled 'students' can change in meaning where the emphasis is on a few students or some students. To this end, a centre of a cluster at each level of the hierarchy was defined as a label. The inverse distance to the cluster centres is the membership degree or the similarity to each label. The cluster distance for a word $w_{t}$ is defined as $d_{v_{w_{t}}}$. Consequently, the membership of each word $w_{t}$ in cluster $c_{k}$ to its label is the inverse distance defined in Eq. 6.20.

$$
m_{v_{w_{t}}}=\frac{1}{d_{v_{w_{t}}}}=\frac{1}{\left|c_{k}-v_{w_{t}}\right|^{2}} \quad \forall w_{t} \in c_{k}
$$

We then fine-tuned $\mathrm{K}$ within the 5-50 range based on the dataset size and chose the cluster number according to gap statistic value [201]. The output $H$ can be directly used as a new dataset for other actions, such as browsing, querying, data mining process, or any other procedures requiring a reduced but structured version of data. The hierarchical clustering can also be pruned at each level to represent a summarised concept map for different purposes or users. Therefore, $H$ is fed to the summariser for pruning to generate a personalised summary. Moreover, by using preference-based learning and RL, we learn users' preferences in making personalised summaries for unseen topic-related documents, discussed in Sec. 6.3.3.

### 6.3.3 Summariser

The hierarchical concept map produced in the previous step is given to the summariser to make the desired summaries for users based on their given preferences. Therefore, the summariser consists of two phases-(i) predicting user preferences and (ii) generating the desired summary.

## Predicting User Preference

The first step towards creating personalised summaries is to understand users' interests. The same procedure in SumRecom is used for extracting users' preferences; however,
the selection of sentences is among hierarchy nodes. $H$ is the hierarchical concept map, where at the $i-t h$ level of the hierarchy there exist $m_{i}$ nodes defining a label l. $L=\left\{l_{11}, \ldots, l_{n m_{i}}\right\}$ is the set of all labels, where $l_{i 1}$ indicates the first node at $i-t h$ level of the hierarchy and $n$ is the number of levels, and $L_{i}$ indicates the labels at $i-t h$ level. We queried users with a set of pairwise concepts at the same levels, $\left\{p\left(l_{i 1}, l_{i 2}\right), p\left(l_{i 2}, l_{i 3}\right), \ldots, p\left(l_{i m_{i}-1}, p\left(l_{i m_{i}}\right)\right\}\right.$, where $p\left(l_{i 1}, l_{i 2}\right)$ is defined in Eq. 6.21.

$$
p\left(l_{i 1}, l_{i 2}\right)= \begin{cases}1, & \text { if } l_{i 1}>l_{i 2} \\ 0, & \text { otherwise }\end{cases}
$$

where $>$ indicates the preference of $l_{i 1}$ over $l_{i 2}$. Preference learning aims to predict the overall ranking of concepts, which requires transforms concepts into real numbers, called utility function. The utility function $U$ such that $l_{i}>l_{j} \rightarrow U\left(l_{i}\right)>U\left(l_{j}\right)$, where $U$ is a function $U: C \rightarrow \mathbb{R}$. In this problem, the ground-truth utility function $(U)$ measures each concept's importance based on users' attitudes, defined as a regression learning problem. According to $U$, we defined the ranking function, $R$, measuring the importance of each concept towards other concepts based on users' attitude. This is defined in Eq. 6.22.

$$
R\left(l_{i}\right)=\sum \mathbb{1}\left\{U\left(l_{i}\right)>U\left(l_{j}\right)\right\}, \forall l_{i}, l_{j} \in L
$$

where $\mathbb{1}$ is the indicator function. The Bradley-Terry model [196] is a probability model widely used in preference learning. Given a pair of individuals $l_{i}$ and $l_{j}$ drawn from some population, the model estimates the probability that the pairwise comparison $l_{i}>l_{j}$ is true. Having $n$ observed preference items, the model approximates the ranking function $R$ by computing the maximum likelihood estimate in Eq. 6.23.

$$
J_{x}(w)=\sum_{i \in n}\left[p\left(l_{i}, l_{j}\right) \log F\left(l_{i}, l_{j} ; w\right)+p\left(l_{j}, l_{i}\right) \log F\left(l_{j}, l_{i} ; w\right)\right]
$$

where $F(l)$ is the logistic function defined in Eq. 6.24.

$$
F\left(l_{i}, l_{j} ; w\right)=\frac{1}{1+\exp \left[U^{*}\left(l_{j} ; w\right)-U^{*}\left(l_{i} ; w\right)\right]}
$$

Here, $U^{*}$ is the approximation of $U$ parameterised by $w$, which can be learnt using different function approximation techniques. In our problem, a linear regression model was designed for this purpose, defined as $U(l ; w)=w^{T} \phi(l)$, where $\phi(l)$ is the representation feature vector of the concept $l$. For any $l_{i}, l_{j} \in L$, the ranker prefers $l_{i}$ over $l_{j}$ if $w^{T} \phi\left(l_{i}\right)>w^{T} \phi\left(l_{j}\right)$.

By maximising the $J_{x}(w)$ in Eq. $6.23, w^{*}=\operatorname{argmax}_{w} J_{x}(w)$, the resulting $w^{*}$ using stochastic gradient ascent optimisation will be used to estimate $U^{*}$, and consequently the approximated ranking function $R^{*}: C \rightarrow \mathbb{R}$. Thus, Summation learns a ranking over concepts and uses the ranking to generate personalised summaries.

## Generating Personalised Summaries

The summarisation task is to transform the input $d$ to the best summary in $Y(d)$ for the learnt preference ranking function. This problem can be defined as a sequential decision-making problem, starting from the root, sequentially selecting concepts and adding them to a draft summary.Therefore, it can be defined as an MDP problem.

An MDP is a tuple ( $S, A, R, T$ ), where $S$ is the set of states, $A$ is the set of actions, $R(s, a)$ is the reward for performing an action $(a)$ in a state $(s)$, and $T$ is the set of terminal states. In our problem, a state is a draft summary, and $A$ includes two types of action - either adding a new concept to the current draft summary or terminating the construction process if it reaches users' limit size. The reward function $R$ returns an evaluation score in one of the termination states or 0 in other states.

A policy $\pi(s, a): S \times A \rightarrow R$ in an MDP defines the selection of actions in state $s$. The goal of RL algorithms is to learn a policy that maximises the accumulated reward. The learnt policy trained on specific users' interests is used on unseen data at the test time (in this problem to generate summaries in new and related topic documents).

We defined the reward as the summation of all concepts' importance included in the summary. A policym defines the strategy to add concepts to the draft summary to build a user's desired summary. We defined $\pi$ as the probability of choosing a summary of $y$ among all possible summaries within the limit size using different hierarchy paths, $Y(d)$, denoted as $\pi(y)$. The expected reward of performing policy $\pi$, where $R(y)$ is the

```
Algorithm 6 Summation
    1: Input: Document cluster d
    : Output: Summary (H) and optimal policy
    Organiser
        Concepts and Relations \(\leftarrow\) Concept and relations extraction (d)
        \(H \leftarrow\) Hierarchical conceptual clustering (concepts)
    6: Summariser (User preference learner)
    7: \(\quad\) User preferences \(\leftarrow\) Query pairs (user)
    8: \(\quad\) Ranker function \(\leftarrow\) Preference learner (user preferences)
    9: Summariser (RL learner)
    10: \(\quad\) Optimal policy \(\leftarrow\) Policy learner ( ranker function)
    11: Summary \((H)\) and optimal
```

reward for selecting summary $y$, is defined in Eq. 6.25.

$R^{R L}(\pi \mid d)=\mathbb{E}_{y \in Y(d)} R(y)=\sum_{y \in Y(d)} \pi(y) R(y)$

The goal of MDP is to find the optimal policy $\pi^{*}$ that has the highest expected reward. Therefore, the optimal policy, $\pi^{*}$, is the function that finds the desired summary for a given input based on user feedback (Eq. 6.26).

$$
\pi^{*}=\operatorname{argmax} R^{R L}(\pi \mid d)=\operatorname{argmax} \sum_{y \in Y(d)} \pi(y) R(y)
$$

We also used the linear temporal difference algorithm to obtain $\pi^{*}$. The process is explained in Algorithm 6.

### 6.3.4 Experiment

This section presents the experimental set-up for implementing and assessing our summarisation model. Summation was evaluated from different evaluation aspects, first from the organiser's output, and then concerning the hierarchical concept map (H), which can be served individually to users as the structured summarised data. Next,
we evaluated $\mathrm{H}$ using both human and automatic evaluation techniques to answer the following questions:

- Do users prefer hierarchical concept maps to explore new and complex topics?
- How much do users learn from a hierarchical concept map?
- How coherent is the produced hierarchical concept map?
- How informative are summaries in the form of a hierarchical concept map?

Personalised summaries generated on test data were also evaluated from various perspectives to analyse the effect of RL and preference learning. This helped to assess the effect of different features in approximating the proposed preference learning-based system, as well as the performance of an RL algorithm and the information coverage in terms of ROUGE.

## Hierarchical Concept Map Evaluation

To answer the questions in Sec. 6.3.4, we performed three experiments. First, within the same limit size as the reference summaries, we compared the summaries produced by three models - using ExDos, which is a traditional approach; using a traditional hierarchical approach [145]; and using a structured summarisation approach [15] on selected documents (with ROUGE-1 and ROUGE-2 scores based on the reference summaries). The average ROUGE-1 for Summation was 0.65 and ROUGE-2 was 0.48 . The structured approach [15] showed similar performance with ROUGE-1 and ROUGE-2 at 0.65 and 0.45 , respectively. Meanwhile, traditional hierarchical approaches [145] produced a ROUGE-1 of 0.27 and ROUGE-2 of 0.18 . In the same task, the percentage of covered unigrams and bigrams based on documents were also compared. Both Summation and the structured approach covered approximately $4 \%$ unigrams and $2 \%$ bigrams, but dropped below $1 \%$ in both cases when testing the hierarchical approaches. In the third experiment, all competitors' outputs were rated based on three measures, including usability in exploring new topics, level of informativeness, and coherency. Summation's rate for the first and second criteria was $96 \%$ and $94 \%$, respectively. However, it was


Figure 6.10: Evaluating different feature sets for estimating the ranker function.

$34 \%$ for coherency. We removed all concepts with low similarity to their parents based on a different threshold at each level. After repeating the same experiment, and rate of coherency increased to $76 \%$.

## Feature Analysis

Before evaluating the effect of conceptual preference, it is important to explain the ground-truth concept ranker function $(U)$ and the approximate function $\left(U^{*}\right)$, indicating the importance of concepts. To estimate the approximate function $\left(U^{*}\right)$, we defined a linear model $U^{*}(c)=W^{T} \phi(c)$, where $\phi$ are the features. To this end, a set of features (whose importance was validated in ExDos) was used, including surface-level and linguistic-level features. Surface-level features include frequency-based features (TF-IDF, RIDF, gain and word co-occurrence), word-based features (upper-case words and signature words), similarity-based features (Word2Vec and Jaccard measure) and named entities. Linguistic features are generated using semantic graphs and include the average weights of connected edges, the merge status of concepts as a binary feature, the number of concepts merged with a concept, and the number of concepts connected to the concept. We defined different combinations of features with different sizes, $\{2,5,8,10\}$, starting from the most critical one. Then, we repeated the

TABLE 6.11: Comparing Summation with Benchmark Datasets

| Model | ROUGE-1 | ROUGE-2 | ROUGE-L |
| :--- | :---: | :---: | :---: |
| Traditional structured [15] | 0.346 | 0.090 | 0.251 |
| Traditional hierarchical [145] | 0.211 | 0.013 | 0.149 |
| Summation | 0.731 | 0.651 | 0.681 |

experiments for 10 cluster documents. We used the concepts included in the reference summary as preferences, and then evaluated the concept coverage in a concept map compared to the reference summaries using ROUGE-1 and ROUGE-2. The results reported in Fig. 6.10 show that the model's performance improved after adding more features.

## Summary Evaluation

To avoid subjectivity in the evaluation process, we used the reference summaries as feedback. The mentioned concepts that exist in reference summaries receive the maximum score by the ranked function. We compared the summaries produced by three models, including the traditional approach (ExDos), a range of hierarchical approaches [145], and a structured summarisation approach [15], each tested on randomly selected documents from three datasets using ROUGE-1, ROUGE-2 and ROUGE-L scores based on the references summaries. The average results reported in Table 6.11 show the supremacy of Summation in selecting specific contents.

### 6.4 Summary

This chapter provided three solutions to address the problem of personalised summarisation. First, we proposed an interactive and personalised MDS approach using user feedback. This included the selection or rejection of concepts, defining the importance of a concept, and users' confidence level. We also proposed a summary recommendation framework that interactively learns how to generate personalised summaries based
on that feedback. We provided two structures, first to predict extractive summaries (sentence based), and second to make structured summaries. We empirically examined the validity of the proposed models using simulated user feedback. Results verified that the proposed frameworks show promising results in terms of ROUGE score as well as human evaluation. The results also showed that user feedback could be integrated into intelligent systems to help them obtain their desired information.

## Summarisation Applications

This chapter proposes solutions to the information overload problem across different domains using summarisation. We address three specific applications including:

- the use of summarisation in detecting anomalies in network traffic data
- the application of summarisation in healthcare analytics problems
- the use of summarisation to narrate business process data.

Each section discusses each problem, the state-of-the-art approaches in each domain, the proposed solutions, and the experiments conducted.

### 7.1 Detecting Anomalies Through Summarisation

Monitoring network traffic data to detect hidden patterns of anomalies is a challenging and time-consuming task that requires high computing resources. To this end, an appropriate summarisation technique is important, as it can effectively substitute for original data. A network summary can reveal what is happening in a network and managing the network instantly. However, one drawback is that the summarised data may remove existing anomalies. Therefore, it is vital to create a summary that can reflect the same pattern as the original data. For example, the summary should still give insight into most browsing websites, regularly used applications, and incoming traffic patterns. Three scenarios in which effective summarisation can aid traffic data collection $[202]$ include:

- providing network administrators with an overview of what is happening in a network
- use of summarised network traffic data as input in anomaly detection algorithms to reduce computing costs
- summarising intrusion detection alarms, thus, facilitating an administrator's duties.

A concise representation of the data helps both the administrator and the analysis algorithms in all mentioned scenarios. Different data summarisation techniques are designed for other applications such as transactional data or stream data [203], which can also be applied to traffic data. However, this has some drawbacks regarding anomaly detection:

- Clustering is the most used summarisation approach. Here, the data centre is considered the summarised data output. The problem is that the cluster centers might not be part of the original data.
- Detecting frequent item sets is another approach that only captures frequent items in a summary. Therefore, they ignore infrequent anomalies.perform well on summaries, as they do not contain any anomalies.
- Semantics-based techniques do not keep the same samples in the summarised data.
- Statistical-based techniques such as sampling do not ensure presence of anomalies in summaries since they use a sampling-based summarisation technique.

Evidently, not all summarisation approaches are appropriate for anomaly detection. There is great need for an efficient network traffic summarisation (NTS) technique to ensure that automated summaries more closely resemble the original network traffic data. In this context, summarisation aims to synopsise original data with interesting patterns, like anomalies, and normal data with the same distribution pattern.

We propose an intelligent summarisation approach for identifying hidden anomalies, called INSIDENT. The proposed approach guarantees to keep the original data distribution in summarised data, and employs similar ones to ExDos (see Ch. 4). As such, we investigate the adaptation of clustering and KNN algorithms to create a summary.

INSIDENT is an intelligent summarisation approach for detecting anomalies in network traffic datasets, which guarantees the preservation of original data distribution. The proposed algorithm is used in two scenarios-(i) as a pre-processing approach for performing anomaly detection, and (ii) to detect anomalies in supervised problems, since the algorithm reveals the hidden structure of data. The proposed summarisation technique can also be used in various domains in which big data requires mining for interesting and relevant patterns.

### 7.1.1 Related Work

Anomaly detection techniques perform poorly when the data size increases due to increased false alarms and high computational cost. Therefore, summarisation can be a beneficial alternative tool. However, existing summarisation techniques cannot accurately represent the rare anomalies in a dataset. This section presents the related work on traffic data summarisation, along with anomaly detection techniques. For anomaly detection purposes, a good summary should be representative of all samples in the original dataset.

## Network Analysis Tools

Different network analysis tools summarise network traffic data, such as traffic flow analysis tools, flow-tools, network visualisation tools, and network monitoring tools [204]. Each produces a graphical report using different measurements, such as network bandwidth or latency. However, these tools only characterise and aggregate traffic samples regarding a single feature, such as the source address or protocol. As a result, they are suitable only to extract insights and not for further processing tasks such as anomaly detection. Besides, the purpose of a summary is to produce an accurate description of the network's traffic patterns. Consequently, the summarisation technique should identify traffic patterns according to any desired combinations of features efficiently.

## Statistical Approaches

Statistical approaches aim to determine the statistical distribution of data that could approximate the original data pattern. Sampling is a common technique in this category in which a sample is a subset of the dataset. Sampling techniques include simple random sampling, systematic sampling, cluster random sampling, stratified random sampling, and multistage random sampling $[205,206]$. However, summarised data using sampling is under the threat of removing anomalies. To solve this problem, one recent study [204] proposed a sampling-based summarisation technique called SUCh, employing sampling and the modified Chernoff bound technique to add anomalous instances in summary. SUCh is more computationally effective and is also capable of identifying rare anomalies. However, an essential aspect of summarisation is describing all different traffic behaviour patterns. Although SUCh ensures the presence of anomalies, it ignores other types of traffic data, as it focuses only on anomalous data.

## Machine Learning Approaches

Supervised and unsupervised learning have been widely used for knowledge discovery. Two common machine learning algorithms used in summarising network traffic data are frequent item sets and clustering.

Frequent item sets are sets of items that appear more frequently than other samples. Different algorithms are used to detect frequent item sets [207]; however, they are most appropriate for detecting frequent items and not rare anomalies.

The two main clustering-based algorithms for network traffic data summarisation include centroid-based and feature-wise intersection clustering algorithms. In centroidbased summarisation, after clustering samples, centroids are used to form a summary. Different variations of the $\mathrm{k}$-means algorithm are also to handle high-dimensional data $[178,208]$. In a feature-wise intersection-based summarisation algorithm, the summary is generated from each cluster utilizing the feature-wise intersection of the samples after clustering $[202,207]$. Then, all clusters' summaries are linked to produce the output. This approach is best suited to datasets with identical attribute values and, therefore, are not appropriate for detecting rare anomalies.

## Semantic-based Approaches

Semantic-based approaches are not suitable for anomaly detection since the produced summary is not part of the original data. Examples include linguistic summaries, which are based on fuzzy algorithms. These approaches produce text representations that explain essential aspect to enhance human understanding of network traffic summaries [209]. Attribute-oriented induction is another semantic-based approach that aims to express data in a brief and general manner [210]. This induction technique is a generalisation process that abstracts a large dataset from a low conceptual level to a relatively high conceptual level. Other semantic-based approaches include fascicles [211], using association rules and perform lossy semantic compression. SPARTAN is another semantic-based summarisation technique [212] that generalises the fascicles method.

## Anomaly Detection Techniques

Detecting anomalies is a vital task, aiming to identify anomalous or abnormal data. Anomalies are any patterns in original data that do not follow the well-defined nature of regular patterns, indicating notable but unusual events that may negatively affect
the system. Therefore, they require prompt critical actions. An anomaly can be categorised as a $[213]$ :

- point anomaly (when a sample differs from the regular pattern)
- contextual (or conditional) anomaly (when a sample behaves anomalously in a special context)
- collective anomaly (when a collection of samples behave anomalously).

Different supervised, unsupervised and semi-supervised approaches have been proposed for this purpose. These techniques include classification-based network anomaly detection algorithms such as support vector machines [214], Bayesian network models [215], neural networks [216], and rule-based approaches [217]. Statistical anomaly detection techniques include a mixture model, signal-processing technique [218], and principal component analysis [219]. Other categories include information theory-based and clustering-based methods $[203]$.

### 7.1.2 Proposed Approach (INSIDENT)

This section discusses the proposed methodology. We first define the problem and then discuss the algorithm.

## Problem Definition

$x_{i}$ is a sample vector and $X=\left[x_{1}, x_{2}, \ldots, x_{N}\right]$ is the traffic data consisting of $N$ sample, where $x_{i} \in R^{d}$, and $\mathrm{d}$ denotes the number of features. $K$ is the number of clusters, and cluster centroids are denoted by $c$. Further, $x_{=}$is the closest similar sample to $x$, and $s_{\neq}$is the closest different sample. An example of network traffic data with few attributes is reported in Table 7.1. The goal is to find a cluster of similar samples and representatives for each cluster as the summary $S$, where the same distribution is retained but smaller in size.

Table 7.1: Example of Network Traffic Samples

| Source IP | Source port | Destination IP | Destination port | Protocol |
| :--- | :---: | :---: | :---: | :---: |
| 192.168.5.10 | 1234 | 192.168 .1 .1 | 80 | TCP |
| 192.168.5.12 | 4565 | 192.168 .1 .2 | 20 | TCP |
| 192.168.5.10 | 20 | 192.168 .28 .80 | 119 | HTTP |
| 192.168 .5 .10 | 70 | 192.168 .1 .1 | 50 | TCP |
| 211.204 .12 .10 | 31 | 192.168 .28 .80 | 119 | HTTP |
| 192.168 .5 .1 | 3214 | 192.168 .1 .2 | 86 | TCP |

## Methodology

Previous approaches used different clustering or sampling algorithms to summarise data. However, there is no guarantee that the summarised data has the same distribution as the original data, and, therefore, cannot substitute the original data. Thus, we employed the same procedure as in ExDos and investigated the adaptation of clustering and the KNN algorithm to understand the data's underlying structure. For this reason, the error rate of the nearest neighbour classifier in each cluster was minimised by locally weighting features in each cluster. INSIDENT transforms the feature space into a new feature space by weighting features separately in each cluster, where outliers are more easily recognised in the new feature space. To this end, the weighted Euclidean distance is used where the distance between vectors $x$ and $x_{i}$ is defined as in Eq.7.1.

$$
d_{w}\left(x, x_{i}\right)=\sqrt{\sum_{j=1}^{d} w_{j}\left(x_{j}-x_{i j}\right)^{2}}
$$

and $w_{j}$ is the corresponding weight of $j-t h$ feature. The weights are arranged in a $d \times K$ weight matrix $W=\left\{w_{i j}, 1 \leq i \leq d, 1 \leq j \leq K\right\}$, where $d$ is the number of features and $K$ is the number of clusters. Therefore, for each cluster, there is a vector of weights corresponding to each feature, representing the importance of each feature in each cluster. The objective function is designed to minimise the error of $1 \mathrm{NN}$ in each cluster by regulating the weights of each feature and consequently clustering centres.

To estimate the error of 1NN, the approximation function in Eq.7.2 was used [182].

$$
J(\mathbf{W})=\frac{1}{N} \sum_{s \in X S} S_{\beta}\left(\frac{d_{w}\left(x, x_{=}\right)}{d_{w}\left(x, x_{\neq}\right)}\right)
$$

where the sample $x_{=}$is the nearest similar sample, and the sample $x_{\neq}$is the closest different sample to the input sample $x$. Respectively, $d_{w}$ is the weighted Euclidean distance and $S_{\beta}$ is the sigmoid function, defined in Eq. 7.3.

$$
S_{\beta}(z)=\left(\frac{1}{1+e^{\beta(1-z)}}\right)
$$

The objective function of k-means, which aims to minimise the errors in each cluster, is defined in Eq. 7.4.

$$
J(\mathbf{W}, \mathbf{C})=\sum_{k=1}^{K} \sum_{i=1}^{\left|N_{K}\right|} d_{W_{K}}^{2}\left(x_{i}, c_{K}\right)
$$

Thus, the overall objective function is defined in Eq.7.5.

$$
J(\mathbf{W}, \mathbf{C})=\left(\sum_{k=1}^{K} \sum_{i=1}^{\left|N_{K}\right|} d_{W}^{2}\left(s_{i}, c_{K}\right)+\frac{1}{N} \sum_{k=1}^{K} \sum_{i=1}^{\left|N_{K}\right|} S_{\beta}\left(\frac{d_{w}(x, x=)}{d_{w}\left(x, x_{\neq}\right)}\right)\right)
$$

where the first term is the objective function of k-means, and the second term is the summation of the classification errors over the $K$ clusters.

Two parameters are optimised in this objective function. The first is the weights matrix. The feature-dependent weights associated with the sample $x_{=}$are trained to more closely match $x$ while pushing the sample $x_{\neq}$further from $x$. Then, the cluster centroid update is based on the learnt weighted distance. Since this function is differentiable, we can analytically use gradient descent to estimate the matrix $W$, guaranteeing convergence. The iterative optimisation of a learning parameter like w is given in Eq. 7.6.

$$
W^{t+1}=W^{t}-\alpha\left(\frac{J(\mathbf{W}, \mathbf{C})}{\delta(W)}\right)
$$

To simplify the formula, the function $R(x)$ is defined in Eq. 7.7 [182]

$$
R_{w}\left(x_{i}\right)=\left(\frac{d_{w}\left(x_{i}, x_{i,=}\right)}{d_{w}\left(x_{i}, x_{i, \neq}\right)}\right)
$$

The partial derivative of $J(W, C)$ with respect to $W$ is then calculated in Eq. 7.8.

$$
\frac{\delta J(\mathbf{W}, \mathbf{K})}{\delta W_{K}} \cong \sum_{i=1}^{\left|N_{K}\right|} 2 W_{K} \odot\left(x_{i}-C_{K}\right)^{2}+\frac{1}{N} \sum_{i=1}^{\left|N_{K}\right|} S_{\beta}^{\prime}\left(R\left(x_{i}\right)\right) \frac{\delta R\left(x_{i}\right)}{\delta W_{k}}
$$

where $\odot$ is the inner product and $\frac{\delta R\left(x_{i}\right)}{\delta W_{K}}$ is defined in Eq. 7.9.

$$
\frac{\delta R\left(s_{i}\right)}{\delta W_{K}}=\frac{1}{d_{W_{K}}^{2}}\left(x_{i}, x_{i, \neq}\right)\left(\frac{1}{R\left(x_{i}\right)} W_{K} \odot\left(x_{i}-x_{i,=}\right)^{2}-R\left(x_{i}\right) W_{K} \odot\left(x_{i}-x_{i, \neq}\right)^{2}\right)
$$

The derivative of $S_{\beta}(z)$ is defined in Eq.7.10.

$$
S_{\beta}(z)^{\prime}=\frac{\delta S_{\beta}(z)}{\delta z}=\frac{\beta e^{\beta(1-z)}}{\left(1+e^{\beta(1-z)}\right)^{2}}
$$

The partial derivative of $J(\mathbf{W}, \mathbf{C})$ with respect to $C$, is calculated as in Eq. 7.11.

$$
\frac{J(\mathbf{W}, \mathbf{C})}{\delta C_{k}} \cong \sum_{i=1}^{\left|N_{k}\right|}-2 W_{k}^{2} \odot\left(x_{i}-C_{k}\right)
$$

Since we need to optimise the weight of features for each cluster's samples, along with the centre of the clusters, we first updated $W$ in each cluster and then updated $C$ (centre of clusters). The INSIDENT algorithm is depicted in Algorithm 6 for added clarification. Since the algorithm performs in an iterative process using gradient descent, the simplest clustering (k-means) and (KNN) algorithms were used for efficiency. However, $\mathrm{k}$-means is one of the most reliable and widely used clustering algorithms. So too is the KNN, which has been successfully used in many pattern-recognition applications [220]. Thus, similar samples are close to each other in the new feature space, meaning both 'point' and 'contextual' (or conditional) anomalies are also easily detectable. In the case of collective anomalies, we selected the number of each cluster's representative based on its size to maintain the same distribution pattern as the original data.

### 7.1.3 Experiments and Evaluation

In this section, the dataset, evaluation method and performance of INSIDENT are explained and compared with existing state-of-the-art approaches.

## Data Set

Experiments on six benchmark datasets were performed. The details of datasets and the distribution of normal and anomalous samples in each dataset are reported in Table 7.2. KDD1999 contains collective anomalies, whereas the other five datasets contain only rare anomalies. These rare anomalous datasets are from the SCADA network, including real SCADA (WTP), simulated anomalies (Sim1 and Sim2), and injected anomalies (MI and MO).

## Evaluation Metrics

To evaluate the network traffic summary, we explain two widely used summary evaluation metrics: conciseness and information loss [221]. First, conciseness denotes the size of the summary, which influences the quality of the output. At the same time, it is important to create a summary that can reflect the underlying data patterns. Conciseness is defined as the ratio of the input dataset size $(N)$ and the summarised dataset size $(S)$, defined in Eq. 7.12.

$$
\text { Conciseness }=\frac{N}{S}
$$

Second, information loss is defined as the ratio of the number of samples not present by samples present in a summary, defined in Eq. 7.13.

$$
\text { InformationLoss }=\frac{L}{T}
$$

where $\mathrm{T}$ is the number of unique samples represented by the summary, and $\mathrm{L}$ defines the number of samples not presented in the summary.

To evaluate the performance of the anomaly detection algorithms used in supervised approaches, three measures-accuracy, recall and F1-were used. Before we define these measures, four values need clarification [213]. These are:

- true positive (TP), or the number of anomalies correctly identified as anomalous

TABLE 7.2: Dataset Description

| Dataset | Sample number | Normal percentage | Anomalies percentage |
| :--- | :---: | :---: | :---: |
| KDD1999 | 494020 | 19.69 | 80.310 |
| WTP | 527 | 97.34 | 2.66 |
| MI | 4690 | 97.86 | 2.14 |
| MO | 4690 | 98.76 | 1.24 |
| Sim1 | 10501 | 99.02 | 0.98 |
| Sim2 | 10501 | 99.04 | 0.96 |

- false positive (FP), or the number of normal data incorrectly identified as an anomaly
- true negative (TN), or the number of normal data correctly identified as normal
- false negative (FN), or the number of anomalies incorrectly identified as normal.

Based on these definitions, evaluation metrics are defined in Eq.7.14, 7.15 and 7.16.

$$
\begin{gathered}
\text { Accuracy }=\frac{T P+T N}{T P+T N+F P+F N} \\
\text { Recall }=\frac{T P}{T P+F N} \\
F 1=\frac{2 T P}{2 T P+F P+F N}
\end{gathered}
$$

## Result Analysis

This section discusses the INSIDENT performance along with the anomaly detection results.

Anomaly detection evaluation. The baseline algorithms include nearest neighbourbased algorithms( KNN [222], local outlier factor [LOF] [223], connectivity-based outlier factor [COF] [224], local correlation integral [LOCI] [225], local outlier probability [LoOP] [226], INFLO [227]), clustering-based approaches (cluster-based LOF

TABLE 7.3: Real SCADA Dataset (WTP) Results

| Model | WTP-Recall | WTP-Accuracy | WTP-F1 |
| :--- | :---: | :---: | :---: |
| KNN | 85.71 | 97.39 | 85.71 |
| LOF | 78.57 | 97.38 | 78.57 |
| COF | 57.14 | 97.35 | 57.14 |
| LOCI | 85.71 | 97.39 | 85.71 |
| LoOP | 42.85 | 97.33 | 42.85 |
| INFLO | 57.14 | 97.35 | 57.14 |
| CBLOF | 92.85 | 97.40 | 92.85 |
| LDCOF | 85.71 | 97.39 | 85.71 |
| CMGOS | 57.14 | 97.35 | 57.14 |
| HBOS | 28.57 | 97.32 | 28.57 |
| LIBSVM | 85.71 | 97.39 | 85.71 |
| INSIDENT | 94.87 | 97.91 | 94.87 |

[CBLOF] [228], local density cluster-based outlier factor [LDCOF] [229], clusteringbased multivariate Gaussian outlier score [CMGOS] [229]), and statistical approaches (histogram-based outlier score [HBOS], library for support vector machines [LIBSVM] [230].

These approaches are compared with INSIDENT on different variations of the SCADA dataset, including WTP, MI, MO, and Sim1 and Sim2; their values are reported by Mohiuddin et al. [213]. Results are reported in Table 7.3, 7.4 and 7.5.

Table 7.3 shows that for the real SCADA dataset (WTP), INSIDENT has higher values. The clustering-based anomaly detection technique (CBLOF) performs next best, and third is the nearest neighbour-based approach. This is expected and proves that the combination of clustering and KNN can, indeed, perform better. Conversely, the statistical-based approach (HBOS) did not perform well.

Table 7.4 displays the results on simulated datasets (Sim1 and Sim2). LIBSVM has better recall than the other approaches, and INSIDENT performs second best. Finally, the clustering-based approaches do not perform well on the simulated datasets.

For the datasets with injected anomalies (MI, MO), INSIDENT, along with the

TABLE 7.4: Simulated SCADA Datasets Results (Sim1 and Sim2)

| Model | Sim1-Recall | Sim1-Acc | Sim1-F1 | Sim2-Recall | Sim2-Acc | Sim2-F1 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| KNN | 64.7 | 99.03 | 64.7 | 63 | 99.05 | 63 |
| LOF | 0 | 99.01 | 0 | 0 | 99.03 | 0 |
| COF | 0 | 99.01 | 0 | 2 | 99.03 | 2 |
| LOCI | 0 | 99.01 | 0 | 0 | 99.03 | 0 |
| LoOP | 0.98 | 99.01 | 0.98 | 0 | 99.03 | 0 |
| INFLO | 0 | 99.01 | 0 | 0 | 99.03 | 0 |
| CBLOF | 0 | 99.01 | 0 | 0 | 99.03 | 0 |
| LDCOF | 0 | 99.01 | 0 | 0 | 99.03 | 0 |
| CMGOS | 18.62 | 99.02 | 18.62 | 97 | 99.05 | 97 |
| HBOS | 30.39 | 99.02 | 30.39 | 27 | 99.04 | 6 |
| LIBSVM | 74.50 | 99.03 | 74.50 | 68 | 99.05 | 68 |
| INSIDENT | 72.13 | 99.07 | 72.13 | 78.21 | 99.05 | 78.21 |

clustering-based approaches, are the best, followed by nearest neighbour-based approaches. It is interesting to observe that the recall and F1 values are identical for all the anomaly detection techniques. This is because the top $N$ anomalies match the actual anomalies in the dataset, meaning the recall and F1 scores are constantly the same.

Network Traffic Summarization Evaluation. The KDD dataset was used for summarisation evaluation. Summarisation size, which defines conciseness, is considered a constraint in summarisation algorithms. When the summary is small, it has maximum information loss. Conversely, when conciseness is small, the summary contains the whole dataset and, thus, incurs no information loss. Therefore, information loss and conciseness are orthogonal parameters. We used five different summary sizes,

Table 7.5: Simulated SCADA Datasets with Injected Anomalies Results (MI and MO)

| Model | MI-Recall | MI-Acc | MI-F1 | MO-Recall | MO-Acc | MO-F1 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| KNN | 96 | 97.09 | 96 | 91.37 | 98.77 | 91.37 |
| LOF | 38.33 | 97.43 | 38.33 | 55.17 | 98.76 | 55.17 |
| COF | 9 | 97.82 | 9 | 25.86 | 98.75 | 25.86 |
| LOCI | 91 | 97.9 | 91 | 84.48 | 98.77 | 84.48 |
| LoOP | 10 | 97.83 | 10 | 27.58 | 98.75 | 27.58 |
| INFLO | 12 | 97.83 | 12 | 43.10 | 98.76 | 43.10 |
| CBLOF | 24 | 97.84 | 24 | 63.79 | 98.76 | 63.79 |
| LDCOF | 100 | 97.91 | 100 | 63.79 | 98.76 | 63.79 |
| CMGOS | 100 | 97.91 | 100 | 50 | 98.76 | 50 |
| HBOS | 98 | 97.91 | 98 | 65.51 | 98.76 | 65.51 |
| LIBSVM | 86 | 97.9 | 86 | 91.37 | 98.77 | 91.37 |
| INSIDENT | 100 | 98.76 | 100 | 94.21 | 99.04 | 94.21 |

with information loss measured for each summary size. In practise, a network manager/analyst decides the summary size based on the network. The results are compared with NTS and feature-wise intersection-based summarisation approaches [231]. Since our algorithm is based on k-means, we tested it three times with different initial points for each summary size. Results are depicted in Fig. 7.1. The percentage of anomalies compared with SUCh [204] is reported in Tablee 7.6, proving that INSIDENT effectively preserves the percentage of anomalies in generated summaries.

TABLE 7.6: Comparing the Distribution of Anomalies in Summaries and Original Data

| Dataset | Original data | SUCh Alg. | INSIDENT |
| :--- | :---: | :---: | :---: |
| WTP | 2.66 | N/A | 2.33 |
| MI | 2.14 | 2.61 | 2.16 |
| MO | 1.24 | 1.46 | 1.21 |
| Sim1 | 0.98 | 1.04 | 1.01 |
| Sim2 | 0.96 | 0.94 | 0.97 |



Figure 7.1: Result of comparing information loss based on different summary sizes. FIB: forwarding information base; NTS: network traffic summarisation

### 7.2 Summarisation in Healthcare Analytics

The ever-increasing amount of available text data makes it challenging for humans to extract only what they need. This problem is even more vital in the medical domain, where accessing up-to-date information is essential. Biomedical information is accessible in various forms. Examples include biomedical literature), medical records, multimedia documents, information from the web, and a host of other diverse formats such as journal articles and patient records used to progress the latest advances in a particular field of study. Biomedical literature helps clinicians and researchers to assess, develop and validate their proposed hypotheses and conduct new experiments [232]. However, the extensiveness of available resources has introduced greater need for superior information extraction [233] and knowledge discovery techniques in academia and medical research. Intelligent content summarisation approaches are helpful tools in situations where an overview of a set of documents is needed. However, in the medical context, the generated summary must be tailored to suit two different user preference types: physicians and patients.

State-of-the-art text summarisation approaches in the biomedical domain cover a wide range of subfields, including biomedical literature [234-236], treatment document summarisation [237], evidence-based medical care [238], drug information [239],clinical decision support and notes [240, 241], and electronic health records [242]. However,
traditional summarisation approaches are incapable of considering users' specific needs, uncertainty and interactivity within the information-seeking process.

We propose a novel embedding method, called Summary $2 \mathrm{vec}$, in which each summary is presented within a novel architecture by a fixed-length vector covering various aspects of the information space. Summary2vec is remedial to design automatic services for various analytic purposes that require information-seeking activities. Specifically, we leverage Summary2vec to produce a hierarchical summarisation structure that helps users better navigate a textual hierarchy and gain more in-depth information upon request. Then, instead of providing a short and static summary, we present an interactive summarisation approach that engages users in the summarisation process. The unique contribution of this section is as follows:

- We introduce and formalise a theoretically grounded method for embedding summaries, called Summary2vec, and propose a novel neural network architecture. Vectorised summaries facilitate exploration of various aspects of the information space. Therefore, the method could be used as inputs to a wide range of machine learning models to solve real-world problems. It also helps in explaining to end users the decisions made by the system.
- We propose a hierarchical clustering approach and apply Summary2vec to produce a hierarchical summary structure that can help users navigate and explore different aspects of the information space.
- We provide evidence in the form of experiments, in which the model is trained and applied for personalised summarisation.


### 7.2.1 Related Work

There are many practical scenarios where people are facing an extensive collection of text with a particular goal. Recently, summarisation application has gained interest among the medical research community due to the tremendous increase of available information.

Physicians and researchers must sift through an increasing amount of published journals, conference proceedings, medical websites, electronic medical records and portals on the internet to pinpoint what they need. The more documents which one has to face, the more complex the task becomes as the result of information overload. However, information is only valuable when it becomes reduced and meaningful, and tailored to the user's interests. In these scenarios, information-seeking activities go beyond fact-checking and aim at expanding one's insight and discovering conceptual knowledge boundaries [3]. As hardware advances and cloud usage empowers immense information processing, document summarisation becomes an essential tool to ensure that users benefit from the information availability.

Document summarisation creates a short, limited-size text, representing the important contents [243]. Different techniques including extractive and abstractive approaches, single-document summarisation or MDS, and query-focused summarisation are proposed. This section discusses the key problems of text summarisation in the medical domain.

## Extractive Document Summarisation in the Medical Domain

MiTAP, or MITRE text and audio processing, is an extractive approach proposed for single and multiple documents $[244,245]$. MiTAP intends to monitor infectious disease outbreaks and other biological threats according to epidemiological reports, news wire feeds, email and online news in various languages.

The process begins by filtering and normalising the collected information. MiTAP leverages human-created rules to determine the data, source, article title, and body used to select paragraph, sentence, and part-of-speech tags. Then, a named entity recogniser is used to detect dates, diseases and victim descriptions using human-created rules. Finally, the document is processed with WebSumm [246] to generate summaries.

MUSI, multilingual summarisation for the internet, [247] is a cross-lingual querybased summarisation system that uses Italian and English articles extracted from the Journal of Anaesthesiology to create summaries in French and German using features such as cue phrases, query words and the position of the sentences to form the summary.

To test their approach, Johnson et al. [248] used articles published by the Journal of the American Medical Association to rank a series of extracted sentences according to each document's cluster signature. The approach takes medical documents filtered by a query as input and clusters them. A summary is produced by pairing the cluster signature to sentences to be summarised. Elsewhere, Kan et al. [249, 250] proposed an approach called Centrifuser, which is the summarisation engine of the PERSIVAL project. The input is articles retrieved by its search engine based on patient records and user queries. For each article, the authors create a topic tree presenting the sectioning of articles. A composite topic tree is then generated by merging all topic trees, adding detail nodes and matching the nodes with the query. Next, they choose the representative sentences for each topic. The last step involves ordering those sentences using topics ordering and physical position sentences.

## Abstractive Document Summarisation in the Medical Domain

MUSI [247] generates either extractive summaries or abstractive summaries. After selecting sentences for extractive summarisation, it maps them into a predicate argument structure representation using tokenising, chunking, shallow syntactic parsing, morphological analysis, dependency analysis, and mapping to the internal representation. Finally, natural language generation systems are used to create summaries of those extracted sentences.

TRESTLE (text retrieval extraction and summarisation technologies for large enterprises) is another system that relies on named entity recognition for producing singlesentence summaries of pharmaceutical newsletters [251]. Drug names and diseases are named entities and are linked to the newsletter from which they have been extracted.

## Personalised Summarisation in the Medical Domain

Centrifuser and PERSIVAL produce other types of abstractive summary [252]. They create an informative abstractive summary based on the users' preferences (i.e., physicians, patients or relatives). The system takes three different sources as input, including patient records, consisting of structured and unstructured documents; journal medical
articles extracted from online medical journals, mainly in the field of cardiology; and users' queries $[252]$.

## Multimedia Document Summarisation in the Medical Domain

Ebadollahi et al. [253] and Xingquan et al. [254] present systems that perform document summarisation using multimedia content such as echocardiograms (ECGs) and medical videos, respectively [248]. ECGs are usually videotaped and are transcribed into a digital format. Summarising an ECG involves selecting the most interesting video frames and enabling users to navigate through the ECGs to find their required parts with ease [253]. The output can be a static summary made by selecting the extracted key frames or a dynamic summary made by a concatenation of the video's small extracted sequences.

## Summarisation from a Cognitive Science Perspective

SummIt-BMT (summarise it in bone marrow transplantation) is a query-based summarisation system based on the cognitive model that deals with summarising MEDLINE articles and abstracts for a bone marrow transplant-a specialised field of internal medicine [255]. First, users create a search scenario based on the domain ontology concepts. The scenario is converted to a MEDLINE query and its corresponding articles are included. Pieces of text pointing to the query are given as output. As such, we propose Summary2vec, a summary embedding approach that provides a low-dimensional learnt continuous vector representation of summaries covering various aspects of information space. Summary2vec is inspired by Word2vec, which represents document vocabulary, wherein words are mapped to vectors of real numbers.

Word2vec can capture the context of a word in a document, the semantic and syntactic similarity, and relations with other words. Similar to Word2vec, the whole information space (document clusters) is considered a document, and each summary a word. We treated each summary as an independent unit of meaning that conveys information about one or more aspects of a large information space, and propose a hierarchical structure using Summary2vec to facilitate personalised summarisation to



Figure 7.2: Summary2vec architecture. Summaries are transformed into word units to be embedded. Sequences of word vectors are encoded to build a sentence matrix. Attention to the sentence matrix is applied to make sentence embedding, which is encoded to make the summary matrix. The concatenated output of two parallel networks, corresponding to two summaries, is fed into a fully connected network to estimate the summary's similarity.

better analyse the information space.

### 7.2.2 Summary2vec

The goal of Summary2vec is to create a numeric representation of summaries as an individual related unit of meaning conveying one or more aspects of information space. Therefore, it is easier for users to obtain the desired information, gain insights and answer complex questions. Summary2vec is remedial to design automatic services for various analytic purposes that require information-seeking activities.

## Problem Definition

We define input $D$ as a set of related documents, and $d$ is a cluster of documents in $D . Y(d)$ is all the summaries that can be built given document cluster $d$, and $y \in Y(d)$ is a potential summary with limited size $b$. The goal of Summary2vec as a summary embedding algorithm is to map each input summary y to a vector. After, any arithmetic operations or comparison is conceivable on summary vectors.

## Methodology

The proposed architecture depicted in Fig. 7.2 is a nested model composed of four components, including embedding, encoding, attend and similarity estimation. Each summary in this architecture is a set of sentences, and each sentence a group of words. Therefore, we began by tokenising the text into words and embedding the words into vectors.

A word embedding is a learnt representation of text such that words with the same meaning have similar representations. Different techniques are used to learn a word embedding from the text. Word2vec [198] is an example of a statistical method to learn a distributed representation of words, utilising different architectures. We used the skip-gram model, which uses the current word to predict the surrounding window of context words by increasing the weights of nearby context words using a neural network model. More formally, given a sequence of training words $\left\{w_{1}, w_{2}, w_{3}, \ldots, w_{T}\right\}$, the goal is to maximise the average log probability as in Eq. 7.18 [198].

$$
J=\frac{1}{T} \sum_{t=k}^{T-k} \operatorname{logp}\left(w_{t} \mid w_{t-k}, \ldots, w_{t+k}\right)
$$

The prediction task is typically done through a multiclass classifier, such as softmax. Therefore, we have Eq. 7.18.

$$
p\left(w_{t} \mid w_{t-k}, \ldots, w_{t+k}\right)=\frac{e^{y_{w_{t}}}}{\sum_{i} e^{y_{i}}}
$$

Each of $y_{i}$ is a normalised $\log$ probability for each output word $i$, computed in

Eq. $7.19[198]$.

$$
y=b+U h\left(w_{t-k}, \ldots, w_{t+k} ; W\right)
$$

where $U, b$ are the softmax parameters, and $h$ is constructed by concatenation or the average of word vectors extracted from $W$. The neural network-based word vectors are typically trained using stochastic gradient descent, where the gradient is obtained through back propagation [198]. The embedding $v_{w_{t}}$ is a vector representation of the word $w_{t}$. We used Stanford's GloVe model for word embedding. ${ }^{1}$

Next, we built a hierarchical model from a sequence of word embeddings for building sentence embeddings using a bidirectional RNN (LSTM). Given a sequence of word vectors $S=\left\{v_{w_{1}}, \ldots, v_{w_{n}}\right\}$, first the encode step computes a representation, called sentence matrix $(n \times 1)$, where each row represents the meaning of each token in the context of the rest of the sentence. We used LSTM for this purpose, responsible for computing an intermediate representation, denoting the tokens in context. The vector for each token is computed in two parts - one part by a forward pass, and another by a backward pass, defined in Eq. 7.20.

$$
\begin{gathered}
F_{i}=\mathcal{G}\left(v_{w_{i}}, \mathcal{G}(S)\right), \forall i \in n \\
B_{l-(i-1)}=\mathcal{G}\left(v_{l-(i-1)}, \mathcal{G}(S)\right)
\end{gathered}
$$

where $\mathcal{G}$ is the feed-forward network using the ReLU activation function. $F_{i}$ is the $i$-th forward network, $l$ is the sentence embedding size, and $B_{i}$ is the $i$-th backward network.

To obtain the full vector, we concatenated them together as Eq. 7.21.

$$
C_{[l \times 2 n]}=[F, B]
$$

where $[.,$.$] denotes the concatenation of two matrices. Therefore, matrix \mathrm{C}$ has the shape of $l \times 2 n$.[^8]

The attend component condenses the matrix representation produced by the encoder to a single vector used as the input to another standard feed-forward network with $\tanh$ activation function. One key advantage the attention mechanism has over other reduction operations is that it characterises input as an auxiliary context vector. This auxiliary context vector specifies which information to discard. The reduced vector is tailored to the network, consuming it to compensate for the information loss in reducing the matrix to a vector.

In this architecture, we followed the same attention mechanism proposed by Yang et al. [256], which takes two matrices and outputs a single vector. The context vector computed regarding a context vector learnt as a model parameter. This makes the attention mechanism a pure reduction operation, which could be used in place of any sum or average pooling step. The attention takes the output of the encoder as in Eq. 7.22.

$$
\begin{array}{r}
e_{i}=\mathcal{M}(C) \\
\alpha_{i}=\operatorname{softmax}\left(e_{i}\right) \\
o_{i}=\alpha_{i} \times D_{i}
\end{array}
$$

where $\mathcal{M}$ is a feed-forward network with $\tanh$ activation function, and $C$ is the concatenated output matrix of the previous step. Vector oi is the output of the attend step to be utilised as the input of the second encode step. Finally, $D_{[1 \times 2 n]}=\sum_{i=1}^{l} C[i k]$, where $C[i k]$ represents one row of matrix $C$, and $k=2 n$. Hence, $D$ is a single vector that resulted from the summation of all the rows of $C$, as shown in Fig. 7.2. A sequence of sentence condensed embedding as the output of the attend step $\left(o_{i}\right)$ is given to another encoder, a bidirectional LSTM, to make the summary matrix. A pair of these networks is set up to produce attention summary vectors from the other summaries, as well be compared and to create an estimation. Once the summaries have been compressed (reduced) into a single vector, we can learn the similarity measure between different attention summary vectors using target representation. The concatenated vector is fed into a fully connected network to estimate the similarity of summaries. Once summary embeddings are trained, vectorised representations of summaries can be used as input



Figure 7.3: (A) Summary embeddings are produced. (B) The hierarchical summaries are made based on the proposed hierarchical clustering approach.

to a wide range of machine learning models. Sec. 7.2.3 explains the application of Summary2vec in personalised summarisation.

### 7.2.3 Personalised Summarisation

Traditional MDS approaches produce a uniform summary for all users without considering individual interests. Therefore, they suffer from two significant limitations. First, they only provide static summaries that cannot be tailored to specific needs. Second, most existing summarisation systems cannot explain the generated summary or allow users to explore various aspects of the generated summary. Consequently, the granularity of the summary cannot be determined, and the output is neither interpretable nor personalised. Unfortunately, a single summary is unlikely to serve all users in a large population, so the challenge is extracting the desired information from multiple online information sources tailored to a user's specialty and interest. As a result, there is a need for summaries to cater to individual interests and personal background.

Moreover, users' required information is scattered in a large information space. Therefore, users must undertake the challenging and time-consuming task of searching
that space to find what they desire. Summary2vec facilitates personalised summarisation and other information-seeking activities required to quickly and easily understand the information space by vectorising each summary as an individual semantic-related entity. Employing the output of Summary2vec, we propose a hierarchical summarisation structure wherein higher levels of the hierarchy contain the most general aspects and user interaction can occur (depicted in Fig. 7.3).

We propose a novel recursive clustering algorithm that uses summary embeddings learnt from a corpus as $S=\left\{v_{s_{1}}, v_{s_{2}}, \ldots, v_{s_{N}}\right\}$. The hierarchical structure incrementally maintains the most generic information on top (roots). The parent-to-child links facilitate navigating and drilling down on interesting topics. Summary2vec facilitates the clustering of summaries using summary vectors. The hierarchical conceptual clustering minimises the objective function (Eq. 7.23) over all $k$ clusters as $C=\left\{c_{1}, c_{2}, . ., c_{k}\right\}$.

$$
J=\sum_{k=1}^{K} \sum_{t=1}^{|S|}\left|v_{s_{t}}-c_{k}\right|^{2}+\alpha \min _{c \in C} \operatorname{size}(c)
$$

where $c_{k}$ is the randomly selected centre of $k-t h$ cluster. The second term is the evenness of the clusters added to avoid clusters with small sizes, and $\alpha$ tunes the evenness factor set employing a grid search over the development set. We implemented hierarchical clustering top-down at each time optimising Eq. 7.23. Similar summaries can easily be found by comparing users' selected summary's vector with any other summary. Besides, the output of hierarchical summarisation helps users navigate the hierarchy to find what they need.

### 7.2.4 Evaluation

The proposed approach is, to the best of our knowledge, the first designed for interactive and hierarchical summarisation of medical data. Therefore, evaluation of the approach is challenging, as there is no baseline. We evaluated the proposed approach using a PubMed dataset.

PubMed consists of more than 26 million citations for biomedical literature. The
dataset was collected from sources such as MEDLINE, life science journals and published online ebooks. It also contains links to public access ${ }^{2}$ text-based content from PubMed Central and other publishers' websites. The data was divided into train, test and validation sets.

We randomly built summaries by selecting sentences and measuring their similarity using ExDos. We trained the network, defining the word embedding size as 300 and the sentence embedding size as 100 . We then evaluated Summary2vec using the root means square error (RMSE) as the evaluation measure, defined in Eq. 7.24.

$$
R M S E=\sqrt{\frac{1}{P} \sum_{i=1}^{P}\left(\text { Similarity }_{p_{i}}-\text { Similarity }_{r_{i}}\right)^{2}}
$$

where $P$ is the number of summary pairs, Similarity is the predicted similarity by the network, and Similarity S $_{r}$ is the actual similarity value. If we define $N_{t} r a i n$ rain as the number of train sentences and the summary length as $l$, then the summary set size is equal to $S_{\text {size }}=\binom{N_{\text {train }} n}{l}$. Consequently, the number of summary pairs is equal to $\binom{S_{\text {size }}}{2}$.

To evaluate the network, we selected summaries with four different sizes chosen from the set of $\{3,5,7,10\}$. The RMSE values are reported in Table 7.7. Evidently, as the number of sentences in a summary increases, the similarity of the summaries also increases. Consequently, it is more probable to be over-fitted. In our experiments, we set the summary length at 5. Since RMSE evaluates the performance of the network trained for estimating summary similarities, we evaluated the produced summary vector using the proposed hierarchical summarisation approach. We also performed human studies, as the primary purpose of the approach is to help users find what they desire.

One challenge of hierarchical clustering in producing hierarchical summaries is finding the optimal number of clusters. To tackle this problem, we used the gap statistic $[201]$ defined in Eq. 7.25.

$$
\operatorname{Gap}_{n}(k)=E_{n} \log \left(W_{k}\right) *-\log (W k)
$$[^9]

TAble 7.7: valuating Summary Size Effect According to RMSE Value

| Summary Size | Train RMSE | Test RMSE |
| :---: | :---: | :---: |
| 3 | 0.22 | 0.31 |
| 5 | 0.09 | 0.12 |
| 7 | 0.10 | 0.22 |
| 10 | 0.04 | 0.25 |

where $W_{k}$ is the clusters' score using objective functions, and $E_{n} *$ is the expectation under a sample of size $\mathrm{n}$ from a reference distribution. We performed the gap statistic at each level using values from $5,10,15,20,25,30$. The best value at each level was chosen.

Since the purpose of a hierarchical summary is to help users retrieve information, we analysed two aspects of user requirements: (i) information coverage (how much information the summary covers), and (ii) knowledge extraction (how much users can learn from summaries). We conducted human experiments and designed a series of micro-tasks for each experiment. Thirty MTurk workers were hired to complete the tasks.

Five document clusters were randomly selected from the datasets. Each evaluator was presented with three documents, to avoid subject bias, and was given two minutes to read each article. To ensure the human subjects understood the study's objective, workers were asked to complete a qualification task first. They were required to write a summary of their understanding and answer questions before undertaking any test. We manually removed spam from the results.

We analysed the information coverage aspect first automatically using $\operatorname{ROUGE}{ }_{n}[8]^{3}$.

To automatically evaluate the proposed approaches, we compared the approach with ExDos. We also compared the percentage of common unigrams and bigrams between these two approaches and the summary written by workers within the same summary[^10]size (100 words) at the first level of the hierarchy. The ROUGE-1 and ROUGE-2 scores were $28 \%$ and $13 \%$ higher than ExDos, at $76 \%$ and $51 \%$, respectively.

Moreover, for human evaluation of information coverage, we asked MTurk workers to read an article on the same topic and identify the five most common sentences (summary size). We aggregated responses from 10 workers for each topic, and then analysed the presence of these sentences at the first levels of the hierarchy. Then, we evaluated them based on the recall measure - the percentage of essential sentences mentioned at the first level. We repeated this experiment for five topics and averaged the recall measures. The proposed approach contained $91 \%$ of all important sentences mentioned by workers at the first level and $5 \%$ at the second level. This experiment illustrates that the first hierarchy level works as a general summarisation tool containing only the most critical sentences. Users are also allowed to navigate the hierarchy should they require more details.

To assess the possibility of users finding their desired information (knowledge extraction), the workers were asked to answer questions on new topics using hierarchical summarisation. Questions were selected to contain both detailed and general topics. Participants' level of confidence in answering the questions as well as their responses were recorded and assessed by an evaluator for accuracy. Among the 16 workers, $86 \%$ were completely confident in their answers, but only $52 \%$ answered entirely accurately. The same experiment was repeated using the ExDos output as a traditional competitor approach. This time, only $23 \%$ answered completely accurately, and the average confidence level was $31 \%$.

### 7.3 Summarising Business Process Data

The large amount of raw data generated by IoT-enabled devices provides real-time intelligence to organisations, and this can enhance knowledge-intensive processes [257]. The problem with understanding the behaviour of information systems as well as the processes and services they support has become a priority in both medium and large
enterprises. This is demonstrated by the proliferation of tools for the analysis of process executions, system interactions and system dependencies, and by recent research on process data warehousing, discovery and mining [258]. Accordingly, identifying business needs and determining solutions to business problems requires the analysis of business process data $[259,260]$; this, in turn, will help discover useful information and support decision-making for enterprises. For example, one intervention that has emerged as a potential solution to the challenges facing law enforcement officers is the use of an interactive constable in a patrol system. In these processes, it is not sufficient to focus on data storage and analysis and the knowledge workers (e.g., investigators) will need to collect, understand and relate big data (scattered across various systems) to process and communicate their findings, support evidence, and make decisions. Therefore, we present a scalable and extensible IoT-enabled process data analytics pipeline known as iProcess [261]. This helps analysts better absorb data from IoT devices, extract knowledge, and link the two to process (execution) data.

We present novel techniques to summarise the linked IoT and process data to construct process narratives. Summarisation techniques presented in this section include a novel approach that helps analysts understand and relate big IoT as well as process data to communicate and support their findings with ease. The proposed approach will enhance data-driven techniques for improving risk-based decision-making in knowledgeintensive processes. We present a set of innovative, fine-grained and intuitive analytical services to discover patterns and related entities, and further enrich them with complex data structures (e.g., time series, hierarchies and subgraphs) to construct narratives. We also propose a framework and algorithms for summarising the (big) process data and constructing process narratives. This helps us complete the first step towards enabling storytelling with process data. Before explaining the details of the proposed method, we provide an example of the motivating scenario in Sec. 7.3.1.

### 7.3.1 Motivating Scenario: Missing People

Between 2008 and 2015, over 305,000 people were reported missing in Australia (aic.gov.au/), an average of 38,159 reports each year. In the United States (nij.gov/), there are as
many as 100,000 active missing person's cases on any given day. The first few hours following a person's disappearance are the most crucial. The sooner police are able to piece together the sequence of events and actions right before a disappearance, the greater the chance of finding a missing person. This entails gathering information about the person, including physical appearance, their activities on both social media and in the physical/social realm, the data and communication stored in phone calls and emails, and information collected through public means (e.g., CCTV).

The investigation process is a data-driven, knowledge-intensive and collaborative one. The information associated with an investigation (case process) is usually complex, entailing the collection and presentation of many different types of documents and records. It is also common that separate investigations may affect other investigation processes. Nonetheless, the more evidence (knowledge and facts extracted from the data in the data lake [262]) collected, the better related cases could be linked explicitly. Although law enforcement agencies use data analysis, crime prevention, surveillance, communication, and data sharing technologies to improve their operations and performance, in sophisticated and data-intensive cases such as missing persons there remain many challenges. For example, fast and accurate information collection and analysis is vital in law enforcement applications [263]. From the policymaker perspective, this trend calls for the adoption of innovations and technologically advanced business processes that can help law enforcers detect and prevent criminal acts. Enabling IoT data in law enforcement processes will give investigators access to a potential pool of data evidence. Then, the challenge is to prepare the big process data for analytics, summary, to construct narratives and to help analysts link these narratives to uncover facts with ease.

We aim to address this challenge by supplying police officers with internet-enabled smart devices (e.g., phones and watches). This will assist them in the process of collecting evidence, provide access to location-based services to identify and locate resources (CCTV, cameras on on-duty officers, police cars, drones and more), organise all these islands of data in a knowledge lake [264-266], and feed that information into a scalable and extensible IoT-enabled process data analytics pipeline. Fig. 7.4 illustrates



Figure 7.4: IoT-enabled process data analytics pipeline.

this framework, explained in greater detail in Sec. 7.3.2.

### 7.3.2 Process Data Lake and Process Knowledge Lake

To understand data-driven knowledge-intensive processes, we leveraged CoreDB (a data lake as a service)[262] to identify (IoT, private, social and open) data sources and ingest the big process data in the data lake. CoreDB manages multiple database technologies (from relational to NoSQL), offers a built-in design for security and tracing, and provides a single REST API to organise, index and query the data and metadata in the data lake. We leveraged the knowledge lake [264] to transform raw data (unstructured, semi-structured and structured data sources) into a contextualised data and knowledge basis that is maintained by and made available to end users and applications.

### 7.3.3 Data Summaries and Narratives Construction

In this phase, we present an online analytical processing server (OLAP)-style [267] technique as an alternative to query and analysis techniques. This approach will isolate the process analyst from explicitly analysing different dimensions such as time, location, activity, actor and more. Instead, the system will be able to use interactive (artefacts, actors, events, tasks, time, location, etc.) summary generation to select and



Figure 7.5: Process knowledge graph schema. (A) A sample OLAP dimension, and (B) an interactive graph summary $(C)$.

sequence narratives dynamically. This novel summarisation method will enable process analysts to choose one or more dimensions (i.e., attributes and relationships) based on their specific goal, and further interact with small and informative summaries. This will facilitate the process analysts undergo to analyse data from various dimensions. Fig. 7.5(B) illustrates a sample OLAP dimension.

In OLAP [267], cubes are defined as sets of partitions, organised to provide a multidimensional and multilevel view (where partitions are considered the unit of granularity). Dimensions are defined as perspectives used for examining the data within constructed partitions. In police investigation scenarios, such as the 2013 Boston bombing, process cubes can enable effective analysis of the process knowledge graph from different perspectives and with multiple granularities - for example, by aggregating and relating all the evidence from a person of interest, location of the incident and more. Following this, we define a process cube as such.

Definition 1 (Process Cube) A process cube is defined to extend decision support on multidimensional networks (e.g., process graphs), considering both data objects and the relationships between them. We reused and extended the definition for graph cubes proposed in our previous work [267, 268]. In particular, given a multidimensional network $N$, the graph cube is obtained by restructuring $N$ in all possible aggregations of a set of node/edge attributes $A$, where for each aggregation $A^{\prime}$ of $A$, the measure
is an aggregate network $G^{\prime}$ w.r.t. $A^{\prime}$. We also defined possible aggregations upon multidimensional networks using regular expressions. In particular, $Q=\left\{q_{1}, q_{2}, \ldots, q_{n}\right\}$ is a set of $\mathrm{n}$ process cubes, where each $q_{i}$ is a process cube (a placeholder for a set of related entities and/or relationships among them) and can be encoded using regular expressions. In this context, each process cube $q_{i}$ can extensively support multiple information needs with the graph data model (e.g., Definition 1) and one algorithm (regular language reachability). The set of related process cubes $Q$ is designed to be customisable by local domain experts (who have the most accurate knowledge about their requirement) to codify their knowledge into regular expressions. These expressions can describe paths through the nodes and edges in the attributed graph: then, $Q$ can be constructed once and reused for other processes. The key data structure behind the process cube is the process knowledge graph (i.e., a graph of typed nodes), which represents process-related entities (such as process instances, models, artefacts, actors, data sources and information items), and typed edges, which label the relationships of the nodes to one another (illustrated in Fig. 7.5(A)). We leveraged the graph mining algorithms in our previous work [267] to walk the graph from one set of interesting entities to another via the relationship edges, and to discover which entities are ultimately transitively connected. We then grouped them in folder nodes (set of related entities) and path nodes (set of related patterns). We used correlation conditions [269] to partition the process knowledge graph based on a set of dimensions derived from the attributes of node entities. We used a path condition [267] as a binary predicate defined on the attributes of a path. This allowed us to identify whether two or more entities are related through that path.

Definition 2 (Dimensions) Each process cube $q_{i}$ has a set of dimensions $D=\left\{d_{1}, d_{2}, \ldots, d_{n}\right\}$, where each $d_{i}$ is a dimension name. Each dimension $d_{i}$ is represented by a set of elements (E), where elements are the nodes and edges of the process knowledge graph. In particular, $E=\left\{e_{1}, e_{2}, \ldots, e_{m}\right\}$ is a set of $m$ elements, where each ei is an element name. Each element ei is represented by a set of attributes (A), where $A=\left\{a_{1}, a_{2}, \ldots, a_{p}\right\}$ is a set of $\mathrm{p}$ attributes for element $e_{i}$, and each $a_{i}$ is an attribute name. A dimension $d_{i}$
can be considered a given query that requires grouping graph entities in a certain way. Correlation conditions and path conditions can be used to define such queries.

A dimension uniquely identifies a subgraph in the process knowledge graph, which we call a 'summary'. Now, we introduce the new notion of 'narrative'.

Definition 3 (Narrative) A narrative $N=\{S, R\}$ is a set summaries $S=\left\{s_{1}, s_{2}, \ldots, s_{n}\right\}$ and a set of relationships $R=\left\{r_{1}, r_{2}, \ldots, r_{m}\right\}$ among them, where $s_{i}$ is a summary name and $r_{j}$ is a relationship of type 'part-of' between two summaries. This type of relationship enables the zoom-in and zoom-out operations (see Fig. 7.5(C)) to link different pieces of a story, and further enables analysts to interact with narratives. Each summary $S=\{$ Dimension, View - Type, Provenance $\}$, identified by a unique dimension $D$, relates to a view type $V T$ (e.g., process, actor or data view), and is assigned to a provenance code snippet $P$ to document the evolution of the summary over time. (More nodes and relationships can be added to the process knowledge graph over time.) We leveraged our work [270] to document the evolution of summaries over time.

The formalism of the summary $S$ will enable users to consider different dimensions and views of a narrative, including the event structure (narratives are about something happening), the purpose of a narrative (narratives about actors and artefacts), and the role of the listener (narratives are subjective and depend on the perspective of the process analyst). Also considered was the importance of time and provenance, as narratives may have different meanings over time. As such, we developed a scalable summary generation algorithm that supports three types of summaries. Fig. 7.6 illustrates the scalable summary generation process. The three summary types are as follows:

- Entity summaries use correlation conditions to summarise the process knowledge graph based on a set of dimensions deriving from the attributes of node entities. In particular, a correlation condition is a binary predicate defined on the attributes of attributed nodes in the graph, allowing users to identify whether two or more nodes are potentially related. Algorithm 1 in Fig. 7.6 will generate all
possible entity summaries. For example, one possible summary may include all related images captured in the same location. Another summary may include all related images captured in the same timestamp.
- Relationship summaries use correlation conditions to summarise the process knowledge graph based on a set of dimensions deriving from the attributes of attributed edges. Algorithm 2 in Fig. 7.6 will generate all possible relationship summaries. For example, one possible summary may include all related relationship types 'controlled-by' and have the following attributes: 'Controlled-by (role $=$ 'Investigator'; time $=$ ' $\tau_{1}$ '); location $=' 255.255 .255 .0^{\prime}$ )'. Within the relationship summaries we also store the nodes from and to the relationship (in this context, the process instance and the actor).
- Path summaries use path conditions to summarise the process knowledge graph based on a set of dimensions deriving from the attributes of nodes and edges in a path. (A path is a transitive relationship between two entities showing a sequence of edges from the start entity to the end.) In particular, a path condition must be defined on the attributes of nodes and edges, allowing users to identify whether two or more entities (in a given process knowledge graph) are potentially related through that path. Algorithm 3 in Fig. 7.6 will generate all possible path summaries. For example, one possible relationship summary includes all related images captured in the same location and contains the same information item (e.g., a missing person). Another relationship summary includes all related tweets or emails sent on timestamp $\tau_{1}$ and includes the keyword 'Maisie' (the missing person).


### 7.3.4 Process Analytics

In this phase, we present a spreadsheet-like interface on top of the scalable summary generation framework. The goal is to enable analysts to interact with the narratives



Figure 7.6: Scalable summary generation.

and control the resolutions of summaries. A narrative $N$ can be analysed using three operations. These are:

- roll up - to aggregate summaries by moving up along one or more dimensions, and to provide a smaller summary with fewer details
- drill down-to disaggregate summaries by moving down dimensions, and to provide a larger summary with more details
- slice and dice - to perform selection and projection on snapshots.

To achieve this goal, we used spreadsheets and organised all the possible summaries in the rows and columns of a grid. Each tab in the spreadsheet defines a summary type (e.g., entity, relationship or path summary), the rows in a tab are mapped to the dimensions (e.g., attributes of an entity), and the columns in a tab are mapped to various data islands in the data lake. Each cell contains a specific summary.

We created a set of machine learning algorithms available as a service, purposed to



Figure 7.7: Presenting a spreadsheet-like interface on top of the scalable summary generation framework $[1]$.

help analysts manipulate and use the summaries in spreadsheets. This supports the following functions:

- The roll-up operation performs aggregation on a spreadsheet tab, either by climbing up a concept hierarchy (i.e., rows and columns, which represent the dimensions and data islands accordingly) or by climbing down a concept hierarchy (i.e., dimension reduction).
- The drill-down operation is the reverse of roll up. This function navigates from less detailed summaries to more detailed summaries. It can be realised either by stepping down a concept hierarchy or introducing additional dimensions. For example, in Fig. 7.7, applying the drill-down operation on the cell intersecting time (dimension) and CCTV1 (data source) will provide a more detailed summary, grouping all the items over different points in time. As another example, applying the drill-down operation on the cell intersecting country (dimension) and Twitter (data source) will provide a more informative summary, grouping all the tweets sent in different countries.
- The slice operation performs a selection on one dimension of the given tab, resulting in a sub-tab. The dice operation defines a sub-tab by performing a selection on two or more dimensions. This will enable analysts, for example, to see tweets from two dimensions, such as time and location. The slice-and-dice



Figure 7.8: Taxonomy of the machine learning algorithms used as a service to streamline the process of acquiring knowledge when interacting with the summaries.

operation can be simply seen as a regular expression that groups together different entity and/or relationship summaries (presented in the spreadsheet tabs), and weaves them together to construct path summaries, illustrated in Fig. 7.7.

### 7.3.5 Implementation and Evaluation

We focus on the motivating scenario to assist knowledge workers in the domain of law enforcement to collect information from an investigation scene, and from IoT-enabled devices of interest (including mobile phones), with greater ease. The goal here is to contribute to the research and thinking towards making police work more effective and efficient, while augmenting officers' knowledge and decision management processes through superior information and communication technology.

We developed ingestion services to extract the raw data from IoT devices such as CCTVs, location sensors in police cars and smart watches (to detect the location of people on duty), and police drones. These services will persist the data in the data
lake. Next, inspired by Google Knowledge Graph (developers.google.com/knowledgegraph/), we focused on constructing a policing process knowledge graph - an IoT infrastructure that can collaborate with internet-enabled devices to collect data, understand events and facts, and assist law enforcement agencies in analysing and understanding the situation to choose the best next step in their processes. There are many systems that can be used at this level to extract information items from artefacts (such as emails, images and social items), including our curation APIs [271], Google Cloud Platform (cloud.google.com/) and Microsoft's Computer Vision API (azure.microsoft.com/).

We have identified many useful machine learning algorithms that helped us summarise knowledge graphs and extract complex data structures, such as time series, hierarchies, patterns and subgraphs, each subsequently linked to such entities as business artefacts, actors and activities. Fig. 7.8 illustrates the taxonomy of these services. We used a spreadsheet-like dashboard that permits easy interaction for knowledge workers accessing the summaries. The dashboard enables monitoring the entities (e.g., IoT devices, people and locations) and searching for facts (e.g., suspects, evidences and events). A set of services has been developed to link the dashboard to the knowledge graph and the data summaries.

Fig. 7.9 plots the performance of our access structure as a function of available memory for the entity/relationship and path summaries. These summaries have been generated from a Twitter dataset containing over 15 million tweets, persisted and indexed in the MongoDB (mongodb.com) database in our data lake. For the path summaries, we have limited the depth of the path to form a maximum of three transitive relationships between the start and end nodes. This experiment was performed on the Amazon EC2 platform using instances running the Ubuntu Server 14.04. The memory size is expressed as a percentage of the size required to fit the largest partition of data in the hash access structure in the physical memory. For efficient access to single cells (i.e., a summary), we built a partition-level hash access structure, where the partitions will be stored as memory and the operations will be evaluated one partition at a time. If a summary does not fit in the memory, we incur an I/O if a referenced cell is not cached. In the case of an entity/relationship summary (see Fig. 7.9(A)), this occurs


Figure 7.9: Scalability with the size of physical memory for entity and relationship summaries. (B) Scalability with the size of physical memory for path summaries.

when the available memory is around $40 \%$ of the largest summary. For the path summary (see Fig. 7.9(B)), this occurs when the available memory is around $30 \%$ of the largest summary.

### 7.4 Summary

This chapter proposed solutions to the information overload problem in different domains through summarisation, proving its importance and flexibility. We explained and provided both the challenges and state-of-the-art approaches in each domain. We also offered solutions to each of the applications and evaluated the proposed models, addressing three specific applications in the process. These include:

- the use of summarisation in detecting anomalies in network traffic data
- application of summarisation in healthcare analytic problems
- using summarisation to narrate business process data.


## Conclusion and Feature Work

This chapter summarises the contributions and findings in this dissertation and outlines possible directions for future research.

### 8.1 Summary of Contributions

This dissertation has shown that personalised and human-in-the-loop summarisation is an important task, but it is fraught with many challenges that have not been addressed adequately in the field. Ch. 2 provides an overview of document summarisation and proposes a new categorisation schema for state-of-the-art summarisation approaches based on existing gaps in the field. Ch. 3 summarised the experimental setting and
the dataset used to evaluate the models. Overall, this thesis made three major contributions towards addressing the problem of personalised and human-in-the-loop summarisation, discussed as follows.

Ch. 4 introduced the central problem of feature engineering in document summarisation. We proposed a general-purpose extractive approach for summarising documents. As shown, the algorithm achieved better results than most state-of-the-art methods in terms of efficiency and performance, and found that features are not equally important. Besides, the post-trained weights represent the importance of each feature in discriminating against each class.

We also proposed NARS, a novel personalised interactive hierarchical summarisation approach that enables users to explore the information they desire with minimal reading required (Ch. 5). NARS is in contrast to a generic summary that is unique for all users, who, by navigating the personalised hierarchy, can search for information based on their own needs and interests. Two variants of the approach, a SNARS and a FNARS, were also proposed. FNARS provides a more concise overview of information, while SNARS offers greater detail. Conversely, FNARS is a fully structured model that can be used for further analysis. Overall, the proposed approaches help users with general knowledge about a topic to explore a wide range of information. We evaluated our approach using both automatic and human evaluation, considering four aspects: information coverage, knowledge extraction, effectiveness and user preference.

Given the limited amount of work on interactive and personalised MDS, we studied this problem by optimising summaries based on user feedback (Ch. 6). We subsequently proposed a summary recommendation framework that interactively learns how to generate personalised summaries. Employing user feedback and domain expert knowledge in a single framework demonstrated the proposed approach's ability to generate personalised summaries. We also studied predicting structured and personalised summaries that can help tackle the variety and volume of big generated data. We highlighted the benefit of using RL algorithms in personalised summarisation, but realised that defining the reward to capture user feedback poses a significant challenge. That said, evaluating a personalised summarisation approach remains an even greater challenge.

Finally, Ch. 7 proposed new summarisation models to tackle the problem of information overload in various domains, including network traffic data, health analytics, and business process data. We proposed Summary2vec, a summary embedding algorithm that can offer a solution to feature engineering in document summarisation.

### 8.2 Open Challenges and Future Directions

Many possible directions have emerged for future study as the output of the research discussed in this dissertation. These are as follows.

### 8.2.1 Personalised Feature Engineering for Summarisation

Recent advances in neural network approaches eliminate the need for feature engineering in different applications. However, for personalised approaches, there is still a need for feature engineering [272]. One research direction concerns personalised approaches for feature engineering as the basis for personalised summarisation using techniques based on crowd knowledge.

Besides, existing research on summarization incorporating human-in-the-loop systems is limited due to current challenges [273]. First, capturing users' interests is a significant challenge in providing effective personalised summaries. This is because users are generally reluctant to specify their preferences, as entering lists of interests may be a tedious and time-consuming task. Besides, people's interests are not static and change over time. Therefore, techniques that extract implicit information about users' preferences are a next-step approach for generating effective personalised summaries. Another potential direction is to use human feedback history on new domains using transfer learning.

### 8.2.2 Summary Representation and Visualisation

One alternative direction to approaching interactive summarisation concerns summary representation. Different forms of feedback to extract user interests need to be evaluated from users' perspectives and cognitive load [274-277]. Examples include learning the process of graph construction or navigation from users' perspectives. Another extension of this work is to take advantage of users' queries in generating personalised summaries, using approaches such as storytelling with data [278, 279]. Identifying the appropriate summary size and the number of feedback loops is another crucial aspect of the summarisation process.

One promising direction is to refine the user interface and combine the summarisation ideas in this dissertation with different visualisation techniques. These can then be used as storytelling tools. Designing intelligent user interfaces can help researchers better analyse different effects and obstacles when interacting with users and, thus, improve interaction quality, reducing users' cognitive load and avoiding additional noise.

### 8.2.3 Real-time Summarisation and Performance Boosting

The largest stumbling block facing the proposed methodologies concerns the processing time, which was not prioritised in this study. Therefore, one possible extension is to employ scaling techniques to make personalised real-time summaries, which can process streaming input data quickly and rapidly alter the summary based on recent data [280].

### 8.2.4 Datasets and Evaluation Metrics

The most interesting finding of this dissertation is that evaluating a personalised summary is the most challenging part of designing a summarisation model. Evaluating a personalised summarisation approach is difficult due to the high subjectivity of the problem. There is also an equal need for test datasets that provide sufficient contextual information [281, 282]. Future work in this domain could focus on using crowdsourcing techniques $[283,284]$ to facilitate personalised summarisation, both for evaluation and creation purposes in various domains.

### 8.2.5 Summarizing Business Process Data

In today's knowledge-, service-, and cloud-based economy, businesses accumulate massive amounts of data from a variety of sources [270, 285]. In order to understand businesses one may need to perform considerable analytics over large hybrid collections of heterogeneous and partially unstructured data that is captured related to the process execution [286? ]. This data, usually modeled as graphs, increasingly come to show all the typical properties of big data: wide physical distribution, diversity of formats, non-standard data models, independently-managed and heterogeneous semantics. Few related work [267, 287], focused on summarizing big process data, by extending Online analytical processing (OLAP) approach to discover concept hierarchies for entities based on both data objects and their interactions in process graphs.

As an ongoing and future work, we are extending our summarization framework to enable explorative querying and understanding of big process data. This is an important line of future work, as understanding process data requires scalable and process-aware methods to support querying, exploration and analysis of the process data in the enterprise because [288, 289]: (i) with the large volume of data and their constant growth, the process data analysis and querying method should be able to scale well; and (ii) the process data analysis and querying method should enable users to express there needs using process-level abstractions. A novel applications would be summarizing process data to personalize recommendations [290, 291]. In particular, modern Recommendation Systems will require to access and understand the big data built on top of the large data islands. This is important as the growing enhancement in interconnection, storage, as well as data management has made it possible to connect to data deluge from the big data, which in turn, can lead to making intelligent and accurate personalization and recommendations [292].

### 8.2.6 Different Domains and Applications

Our proposed models to tackle information overload have shown encouraging results, and we conceive their application in many problems where require human and computers to work cooperatively. Different solutions in various domains were employed in Ch. 7, including traffic data, health data and business process data. The proposed embedding algorithm, Summary2vec, is perhaps well suited in this context as well in many other real-world scenarios. Moreover, the produced summaries are all in text format. Making summary vectors for other types of content such as video and/or image is also required.

## References

[1] F. Amouzgar, A. Beheshti, S. Ghodratnama, B. Benatallah, J. Yang, and Q. Z. Sheng. isheets: a spreadsheet-based machine learning development platform for data-driven process analytics. In International Conference on Service-Oriented Computing, pp. 453-457 (Springer, 2018). xxiv, 165

[2] K. M. G. Hoq. Information overload: Causes, consequences and remedies-a study. Philosophy and progress pp. 49-68 (2014). 1

[3] G. Marchionini. Exploratory search: From finding to understanding. Commun. ACM 49(4), 41-46 (2006). URL https://doi.org/10.1145/1121949.1121979. 2,145

[4] O. Pollar. Surviving information overload how to find, filter, and focus on what's important (Crisp Learning, 2004). 2

[5] V. Gupta and G. S. Lehal. A survey of text summarization extractive techniques. Journal of emerging technologies in web intelligence 2(3), 258 (2010). 2, 3, 5, 17, 32,64

[6] S. Berkovsky, T. Baldwin, and I. Zukerman. Aspect-based personalized text summarization. In International Conference on Adaptive Hypermedia and Adaptive Web-Based Systems, pp. 267-270 (Springer, 2008). 4

[7] S. Park and D. U. An. Automatic query-based personalized summarization that uses pseudo relevance feedback with nmf. In Proceedings of the 4 th International

Conference on Uniquitous Information Management and Communication, pp. $1-7(2010) .4$

[8] C.-Y. Lin. Rouge: A package for automatic evaluation of summaries. Text Summarization Branches Out (2004). 5, 41, 42, 155

[9] P. Pirolli and S. Card. The sensemaking process and leverage points for analyst technology as identified through cognitive task analysis. In Proceedings of international conference on intelligence analysis, vol. 5, pp. 2-4 (McLean, VA, USA, 2005). 8

[10] G. Chin Jr, O. A. Kuchar, and K. E. Wolf. Exploring the analytical processes of intelligence analysts. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, pp. 11-20 (2009).

[11] S. M. Yimam, H. Ulrich, T. von Landesberger, M. Rosenbach, M. Regneri, A. Panchenko, F. Lehmann, U. Fahrer, C. Biemann, and K. Ballweg. new/s/leakinformation extraction and visualization for investigative data journalists. In Proceedings of ACL-2016 System Demonstrations, pp. 163-168 (2016). 8

[12] K. Kirkpatrick. Putting the data science into journalism. Communications of the ACM 58(5), 15 (2015). 8

[13] K. van Noortwijk. Integrated legal information retrieval: new developments and educational challenges. European Journal of Law and Technology 8(1) (2017).

[14] A. Jackson, J. Lin, I. Milligan, and N. Ruest. Desiderata for exploratory search interfaces to web archives in support of scholarly activities. In 2016 IEEE/ACM Joint Conference on Digital Libraries (JCDL), pp. 103-106 (IEEE, 2016). 8

[15] T. Falke. Automatic Structured Text Summarization with Concept Maps. Ph.D. thesis, Technische Universität (2019). 8, 21, 23, 36, 72, 74, 76, 77, 102, 117, 124, 126

[16] S. Ghodratnama, A. Beheshti, M. Zakershahrak, and F. Sobhanmanesh. Extractive document summarization based on dynamic feature space mapping. IEEE Access 8, 139084 (2020). 9

[17] H. Borko and C. L. Bernier. Abstracting concepts and methods. (1975). 14

[18] H. P. Luhn. A statistical approach to mechanized encoding and searching of literary information. IBM Journal of research and development 1(4), 309 (1957). 14

[19] A. Aries, W. K. Hidouci, et al. Automatic text summarization: What has been done and what has to be done. arXiv preprint arXiv:1904.00688 (2019). 14

[20] D. Das and A. F. Martins. A survey on automatic text summarization. Literature Survey for the Language and Statistics II course at CMU 4(192-195), 57 (2007). $15,30,32$

[21] D. R. Radev, E. Hovy, and K. McKeown. Introduction to the special issue on summarization. Computational linguistics 28(4), 399 (2002). 15, 16

[22] Z. Zhang, S. S. Ge, and H. He. Mutual-reinforcement document summarization using embedded graph based sentence clustering for storytelling. Information processing \& management 48(4), 767 (2012). 15

[23] W. Song, L. C. Choi, S. C. Park, and X. F. Ding. Fuzzy evolutionary optimization modeling and its applications to unsupervised categorization and extractive summarization. Expert Systems with Applications 38(8), 9112 (2011). 15, 32, 43

[24] C. E. Shannon. A mathematical theory of communication. The Bell system technical journal $27(3), 379(1948) .15$

[25] H. Jing. Sentence reduction for automatic text summarization. In Sixth Applied Natural Language Processing Conference, pp. 310-315 (2000). 16

[26] E. Marsi, E. Krahmer, I. Hendrickx, and W. Daelemans. On the limits of sentence compression by deletion. In Empirical methods in natural language generation, pp. 45-66 (Springer, 2009). 16

[27] J. Clarke and M. Lapata. Modelling compression with discourse constraints. In Proceedings of the 2007 Joint Conference on Empirical Methods in Natural Language Processing and Computational Natural Language Learning (EMNLPCoNLL), pp. 1-11 (2007). 16

[28] K. Knight and D. Marcu. Statistics-based summarization-step one: Sentence compression. AAAI/IAAI 2000, 703 (2000). 16

[29] K. Knight and D. Marcu. Summarization beyond sentence extraction: A probabilistic approach to sentence compression. Artificial Intelligence 139(1), 91 (2002). 16

[30] Y. Miao and P. Blunsom. Language as a latent variable: Discrete generative models for sentence compression. arXiv preprint arXiv:1609.07317 (2016). 16

[31] K. Filippova, E. Alfonseca, C. A. Colmenares, Ł. Kaiser, and O. Vinyals. Sentence compression by deletion with lstms. In Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing, pp. 360-368 (2015). 16

[32] Y. Zhao, Z. Luo, and A. Aizawa. A language model based evaluator for sentence compression. In Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers), pp. 170-175 (2018). 16

[33] S. M. Shieber and Y. Schabes. Synchronous tree-adjoining grammars (1991). 16

[34] S. Wubben, E. Krahmer, A. van den Bosch, and S. Verberne. Abstractive compression of captions with attentive recurrent neural networks (2016). 16

[35] N. Yu, J. Zhang, M. Huang, and X. Zhu. An operation network for abstractive sentence compression. In Proceedings of the 27th International Conference on Computational Linguistics, pp. 1065-1076 (2018). 16

[36] H. P. Luhn. The automatic creation of literature abstracts. IBM Journal of research and development $\mathbf{2}(2), 159$ (1958). 18, 24

[37] P. B. Baxendale. Machine-made index for technical literature-an experiment. IBM Journal of research and development 2(4), 354 (1958).

[38] H. P. Edmundson. New methods in automatic extracting. Journal of the ACM (JACM) 16(2), 264 (1969). 18, 24

[39] K. McKeown and D. R. Radev. Generating summaries of multiple news articles. In Proceedings of the 18th annual international ACM SIGIR conference on Research and development in information retrieval, pp. 74-82 (1995). 18

[40] K. Sarkar. Using domain knowledge for text summarization in medical domain. International Journal of Recent Trends in Engineering 1(1), 200 (2009). 18

[41] A. Farzindar and G. Lapalme. Legal text summarization by exploration of the thematic structure and argumentative roles. In Text Summarization Branches Out, pp. 27-34 (2004). 18

[42] L. H. Reeve, H. Han, and A. D. Brooks. The use of domain-specific concepts in biomedical text summarization. Information Processing \& Management 43(6), 1765 (2007). 18

[43] B. Sharifi, M.-A. Hutton, and J. Kalita. Summarizing microblogs automatically. In Human language technologies: The 2010 annual conference of the north american chapter of the association for computational linguistics, pp. 685-688 (2010). 18

[44] Y. Duan, Z. Chen, F. Wei, M. Zhou, and H. Y. Shum. Twitter topic summarization by ranking tweets using social influence and content quality. In Proceedings of COLING 2012, pp. 763-780 (2012). 18

[45] G. Kim, L. Sigal, and E. P. Xing. Joint summarization of large-scale collections of web images and videos for storyline reconstruction. In Proceedings of the IEEE Conference on computer vision and pattern recognition, pp. 4225-4232 (2014). 18

[46] B. B. Moon. Interactive football summarization (2009). 18

[47] H. M. Zawbaa, N. El-Bendary, A. E. Hassanien, and T.-h. Kim. Event detection based approach for soccer video summarization using machine learning. International Journal of Multimedia and Ubiquitous Engineering 7(2), 63 (2012). 18

[48] A. Khosla, R. Hamid, C.-J. Lin, and N. Sundaresan. Large-scale video summarization using web-image priors. In Proceedings of the IEEE conference on computer vision and pattern recognition, pp. 2698-2705 (2013). 19

[49] D. Potapov, M. Douze, Z. Harchaoui, and C. Schmid. Category-specific video summarization. In D. Fleet, T. Pajdla, B. Schiele, and T. Tuytelaars, eds., Computer Vision - ECCV 2014, pp. 540-555 (Springer International Publishing, Cham, 2014). 19

[50] M. Gygli, H. Grabner, and L. Van Gool. Video summarization by learning submodular mixtures of objectives. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR) (2015). 19

[51] V. Qazvinian, D. Radev, and A. Özgür. Citation summarization through keyphrase extraction. In COLING 2010, pp. 895-903 (2010). 19

[52] H. Lin and J. Bilmes. A class of submodular functions for document summarization. In Association for Computational Linguistics: Human Language Technologies, pp. 510-520 (2011). 19

[53] A. Abdi, S. M. Shamsuddin, and R. M. Aliguliyev. Qmos: Query-based multidocuments opinion-oriented summarization. Information Processing \& Management 54(2), 318 (2018). 19

[54] N. Vanetik and M. Litvak. Multilingual summarization with polytope model. In Proceedings of the 16th Annual Meeting of the Special Interest Group on Discourse and Dialogue, pp. 227-231 (Association for Computational Linguistics, Prague, Czech Republic, 2015). URL https://www.aclweb.org/anthology/w15-4632. 19

[55] S. Thomas, C. Beutenmüller, X. de la Puente, R. Remus, and S. Bordag. ExB text summarizer. In Proceedings of the 16th Annual Meeting of the Special Interest Group on Discourse and Dialogue, pp. 260-269 (Association for Computational Linguistics, Prague, Czech Republic, 2015). URL https://www.aclweb.org/ anthology/w15-4637. 21

[56] M. Vicente, Ó. Alcón, and E. Lloret. The University of Alicante at MultiLing 2015: approach, results and further insights. In Proceedings of the 16th Annual Meeting of the Special Interest Group on Discourse and Dialogue, pp. 250-259 (Association for Computational Linguistics, Prague, Czech Republic, 2015). URL https://www.aclweb.org/anthology/w15-4636. 19, 21

[57] I. Mani. Summarization evaluation: An overview (2001). 20

[58] J.-Y. Delort and E. Alfonseca. Dualsum: a topic-model based approach for update summarization. In Proceedings of the Association for Computational Linguistics, pp. 214-223 (2012). 20

[59] G. Erkan and D. R. Radev. Lexrank: Graph-based lexical centrality as salience in text summarization. Journal of Artificial Intelligence Research 22, 457 (2004). $20,28,30$

[60] C. Barros, E. Lloret, E. Saquete, and B. Navarro-Colorado. Natsum: Narrative abstractive summarization through cross-document timeline generation. Information Processing \& Management 56(5), 1775 (2019). 20, 28

[61] P. Mehta and P. Majumder. Effective aggregation of various summarization techniques. Information Processing \& Management 54(2), 145 (2018). 21, 28

[62] R. Othman, R. Belkaroui, and R. Faiz. Customer opinion summarization based on twitter conversations. In Proceedings of the 6th International Conference on Web Intelligence, Mining and Semantics, pp. 1-10 (2016). 21

[63] J.-U. Heu, I. Qasim, and D.-H. Lee. Fodosu: multi-document summarization
exploiting semantic analysis based on social folksonomy. Information processing \& management 51(1) (2015). 21, 28

[64] K. Bontcheva. Generating tailored textual summaries from ontologies. In European Semantic Web Conference, pp. 531-545 (Springer, 2005). 21

[65] K. Ježek and J. Steinberger. Automatic text summarization (the state of the art 2007 and new challenges). In Proceedings of Znalosti, pp. 1-12 (Citeseer, 2008). 22

[66] E. Hovy, C.-Y. Lin, et al. Automated text summarization in summarist. Advances in automatic text summarization 14, 81 (1999). 22

[67] M. Hassel and N. Mazdak. Farsisum-a persian text summarizer. In Proceedings of the workshop on computational approaches to Arabic script-based languages, pp. 82-84 (2004). 22

[68] M. Gambhir and V. Gupta. Recent automatic text summarization techniques: a survey. Artificial Intelligence Review 47(1), 1 (2017). 22

[69] A. Nenkova and A. Bagga. Facilitating email thread access by extractive summary generation. Recent advances in natural language processing III: selected papers from RANLP 2003, 287 (2004). 22

[70] P. S. Newman and J. C. Blitzer. Summarizing archived discussions: a beginning. In Proceedings of the 8th international conference on Intelligent user interfaces, pp. $273-276$ (2003). 22

[71] Q. Mei and C. Zhai. Generating impact-based summaries for scientific literature. In Proceedings of ACL-08: HLT, pp. 816-824 (2008). 22

[72] K. Church and W. Gale. Inverse document frequency (idf): A measure of deviations from poisson. In Natural language processing using very large corpora, pp. 283-295 (Springer, 1999). 24

[73] C.-Y. Lin and E. Hovy. Identifying topics by position. In Fifth Conference on Applied Natural Language Processing, pp. 283-290 (1997). 24

[74] D. R. Radev, S. Blair-Goldensohn, and Z. Zhang. Experiments in single and multidocument summarization using mead. In First document understanding conference, p. 1 À8 (Citeseer, 2001). 25

[75] Y. K. Meena, P. Dewaliya, and D. Gopalani. Optimal features set for extractive automatic text summarization. In 2015 Fifth International Conference on Advanced Computing 8 Communication Technologies, pp. 35-40 (IEEE, 2015). 25, $27,47,74$

[76] R. Ferreira, F. Freitas, L. de Souza Cabral, R. D. Lins, R. Lima, G. França, S. J. Simske, and L. Favaro. A context based text summarization system. In 2014 11th IAPR International Workshop on Document Analysis Systems, pp. 66-70 (IEEE, 2014). 27

[77] Y. K. Meena and D. Gopalani. Analysis of sentence scoring methods for extractive automatic text summarization. In Proceedings of the 2014 international conference on information and communication technology for competitive strategies, pp. $1-6$ (2014). 27

[78] M. A. Fattah and F. Ren. Ga, mr, ffnn, pnn and gmm based models for automatic text summarization. Computer Speech \& Language 23(1), 126 (2009). 27

[79] R. Shardan and U. Kulkarni. Implementation and evaluation of evolutionary connectionist approaches to automated text summarization (2010). 27

[80] A. Abuobieda, N. Salim, A. T. Albaham, A. H. Osman, and Y. J. Kumar. Text summarization features selection method using pseudo genetic-based model. In 2012 International Conference on Information Retrieval \& Knowledge Management, pp. 193-197 (IEEE, 2012). 27

[81] M. Mendoza, S. Bonilla, C. Noguera, C. Cobos, and E. León. Extractive singledocument summarization based on genetic operators and guided local search. Expert Systems with Applications 41(9), 4158 (2014). 27

[82] R. A. García-Hernández and Y. Ledeneva. Single extractive text summarization based on a genetic algorithm. In Mexican Conference on Pattern Recognition, pp. 374-383 (Springer, 2013). 27

[83] Z. Cao, F. Wei, S. Li, W. Li, M. Zhou, and W. Houfeng. Learning summary prior representation for extractive summarization. In Proceedings of the 53rd Annual Meeting of the Association for Computational Linguistics, vol. 2, pp. 829-833 (2015). 27,33

[84] H. Niu, W. Xu, H. Akbarzadeh, H. Parvin, A. Beheshti, and H. Alinejad-Rokny. Deep feature learnt by conventional deep neural network. Comput. Electr. Eng. 84, 106656 (2020). 27

[85] J. Cheng and M. Lapata. Neural summarization by extracting sentences and words. In Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 484-494 (2016). 27, 33, 43

[86] R. Nallapati, F. Zhai, and B. Zhou. Summarunner: A recurrent neural network based sequence model for extractive summarization of documents. In hirty-First AAAI Conference on Artificial Intelligence (2017). 27, 33, 40, 43

[87] Y. Wu and B. Hu. Learning to extract coherent summary via deep reinforcement learning. In Thirty-Second AAAI Conference on Artificial Intelligence (2018). 27,33

[88] S. Narayan, S. B. Cohen, and M. Lapata. Ranking sentences for extractive summarization with reinforcement learning. In Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics:

Human Language Technologies, Volume 1 (Long Papers), pp. 1747-1759 (2018). 27,33

[89] M. Mohamed and M. Oussalah. Srl-esa-textsum: A text summarization approach based on semantic role labeling and explicit semantic analysis. Information Processing \& Management 56(4), 1356 (2019). 28

[90] M. Allahyari, S. Pouriyeh, M. Assefi, S. Safaei, E. D. Trippe, J. B. Gutierrez, and K. Kochut. Text summarization techniques: a brief survey. arXiv preprint arXiv:1707.02268 (2017). 29

[91] K. Woodsend and M. Lapata. Automatic generation of story highlights. In Proceedings of the 48th Annual Meeting of the Association for Computational Linguistics, pp. 565-574 (Association for Computational Linguistics, 2010). 30, 43

[92] T. Vodolazova, E. Lloret, R. Muñoz, and M. Palomar. Extractive text summarization: can we use the same techniques for any text? In International conference on Application of Natural Language to Information Systems, pp. 164-175 (Springer, 2013). 30

[93] S. Hariharan and R. Srinivasan. Studies on graph based approaches for single and multi-document summarizations. International Journal of Computer Theory and Engineering 1, 5 (2009). 30,31

[94] S. Hariharan, T. Ramkumar, and R. Srinivasan. Enhanced graph based approach for multi-document summarization. the International Arab Journal of Information Technology 10, 4 (2013). 30,31

[95] D. Parveen, H.-M. Ramsl, and M. Strube. Topical coherence for graph-based extractive summarization. In Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing, pp. 1949-1954 (2015). 30, 43

[96] X. Wan. Towards a unified approach to simultaneous single-document and multidocument summarizations. In Proceedings of the 23rd international conference
on computational linguistics, pp. 1137-1145 (Association for Computational Linguistics, 2010). 30, 43

[97] R. Mihalcea and P. Tarau. Textrank: Bringing order into text. In Proceedings of the 2004 conference on empirical methods in natural language processing, pp. $404-411$ (2004). 30

[98] N. Alami, M. Meknassi, and N. En-nahnahi. Enhancing unsupervised neural networks based text summarization with word embedding and ensemble learning. Expert systems with applications 123, 195 (2019). 30

[99] N. K. Nagwani and S. Verma. A frequent term and semantic similarity based single document text summarization algorithm. International Journal of Computer Applications 17, 2 (2011). 31

[100] Y. Sankarasubramaniam, K. Ramanathan, and S. Ghosh. Text summarization using wikipedia. Information Processing \& Management 50(3), 443 (2014). 31

[101] F. M. Suchanek, G. Kasneci, and G. Weikum. Yago: a core of semantic knowledge. In Proceedings of the 16th international conference on World Wide Web, pp. $697-706$ (2007). 31

[102] J. M. Sanchez-Gomez, M. A. Vega-Rodríguez, and C. J. Perez. Experimental analysis of multiple criteria for extractive multi-document text summarization. Expert Systems with Applications 140, 112904 (2020). 31

[103] J. M. Sanchez-Gomez, M. A. Vega-Rodríguez, and C. J. Pérez. Extractive multidocument text summarization using a multi-objective artificial bee colony optimization approach. Knowledge-Based Systems 159, 1 (2018). 31

[104] S. Mandal, G. K. Singh, and A. Pal. Pso-based text summarization approach using sentiment analysis. In Computing, Communication and Signal Processing, pp. 845-854 (Springer, 2019). 32

[105] V. Priya and K. Umamaheswari. Enhanced continuous and discrete multi objective particle swarm optimization for text summarization. Cluster Computing 22(1), 229 (2019). 32

[106] W. S. El-Kassas, C. R. Salama, A. A. Rafea, and H. K. Mohamed. Automatic text summarization: A comprehensive survey. Expert Systems with Applications p. $113679(2020) .32$

[107] D. Patel, S. Shah, and H. Chhinkaniwala. Fuzzy logic based multi document summarization with improved sentence scoring and redundancy removal technique. Expert Systems with Applications 134, 167 (2019). 32

[108] D. M. Dunlavy, D. P. O'Leary, J. M. Conroy, and J. D. Schlesinger. Qcs: A system for querying, clustering and summarizing documents. Information processing \& management $43(6), 1588$ (2007). 32, 43

[109] D. Shen, J.-T. Sun, H. Li, Q. Yang, and Z. Chen. Document summarization using conditional random fields. In IJCAI, vol. 7, pp. 2862-2867 (2007). 33, 43

[110] J. Pennington, R. Socher, and C. Manning. Glove: Global vectors for word representation. In Proceedings of the 2014 conference on empirical methods in natural language processing (EMNLP), pp. 1532-1543 (2014). 33

[111] K. Al-Sabahi, Z. Zuping, and M. Nadher. A hierarchical structured self-attentive model for extractive document summarization (hssas). IEEE Access 6, 24205 (2018). $33,43,56$

[112] Y. Dong, Y. Shen, E. Crawford, H. van Hoof, and J. C. K. Cheung. Banditsum: Extractive summarization as a contextual bandit. In EMNLP, pp. 3739-3748 (2018). $33,43,56$

[113] S. Ryang and T. Abekawa. Framework of automatic text summarization using reinforcement learning. In Proceedings of the 2012 Joint Conference on Empirical Methods in Natural Language Processing and Computational Natural Language Learning, pp. 256-265 (2012). 33, 96

[114] R. Pasunuru and M. Bansal. Multi-reward reinforced summarization with saliency and entailment. arXiv preprint arXiv:1804.06451 (2018). 33, 96

[115] R. Paulus, C. Xiong, and R. Socher. A deep reinforced model for abstractive summarization. In International Conference on Learning Representations (2018). 33,96

[116] C. Rioux, S. A. Hasan, and Y. Chali. Fear the reaper: A system for automatic multi-document summarization with reinforcement learning. In Proceedings of the 2014 conference on empirical methods in natural language processing (EMNLP), pp. 681-690 (2014). 33, 96

[117] W. Kryściński, R. Paulus, C. Xiong, and R. Socher. Improving abstraction in text summarization. arXiv preprint arXiv:1808.07913 (2018). 33, 96

[118] Y. Gao, C. M. Meyer, M. Mesgar, and I. Gurevych. Reward learning for efficient reinforcement learning in extractive document summarisation. arXiv preprint arXiv: 1907.12894 (2019). 33, 96, 105

[119] S. Wang, X. Zhao, B. Li, B. Ge, and D. Tang. Integrating extractive and abstractive models for long text summarization. In 2017 IEEE International Congress on Big Data (BigData Congress), pp. 305-312 (IEEE, 2017). 34

[120] I. K. Bhat, M. Mohd, and R. Hashmy. Sumitup: A hybrid single-document text summarizer. In Soft computing: Theories and applications, pp. 619-634 (Springer, 2018). 34

[121] X. Liu, Z. Nie, N. Yu, and J.-R. Wen. Biosnowball: automated population of wikis. In ACM SIGKDD international conference on Knowledge discovery and data mining (2010). 34

[122] O. Kolomiyets, S. Bethard, and M. F. Moens. Extracting narrative timelines as temporal dependency structures. In Proceedings of the 50th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 88-97 (2012). 34

[123] Q. Do, W. Lu, and D. Roth. Joint inference for event timeline construction. In Proceedings of the 2012 Joint Conference on Empirical Methods in Natural Language Processing and Computational Natural Language Learning, pp. 677687 (2012). 34

[124] R. Yan, X. Wan, J. Otterbacher, L. Kong, X. Li, and Y. Zhang. Evolutionary timeline summarization: a balanced optimization framework via iterative substitution. In Proceedings of the 34th international ACM SIGIR conference on Research and development in Information Retrieval, pp. 745-754 (2011). 34

[125] R. Yan, L. Kong, C. Huang, X. Wan, X. Li, and Y. Zhang. Timeline generation through evolutionary trans-temporal summarization. In Proceedings of the 2011 Conference on Empirical Methods in Natural Language Processing, pp. 433-443 (2011). 35

[126] R. Swan and J. Allan. Automatic generation of overview timelines. In Proceedings of the 23rd annual international ACM SIGIR conference on Research and development in information retrieval, pp. 49-56 (2000). 35

[127] H. L. Chieu and Y. K. Lee. Query based event extraction along a timeline. In Proceedings of the 27th annual international ACM SIGIR conference on Research and development in information retrieval, pp. 425-432 (2004).

[128] C. G. Akcora, M. A. Bayir, M. Demirbas, and H. Ferhatosmanoglu. Identifying breakpoints in public opinion. In Proceedings of the first workshop on social media analytics, pp. 62-66 (2010).

[129] P. Hu, M. Huang, P. Xu, W. Li, A. K. Usadi, and X. Zhu. Generating breakpointbased timeline overview for news topic retrospection. In 2011 IEEE 11th International Conference on Data Mining, pp. 260-269 (IEEE, 2011).

[130] R. Kessler, X. Tannier, C. Hagege, V. Moriceau, and A. Bittar. Finding salient dates for building thematic timelines. In Association for Computational Linguistics, pp. 730-739 (2012). 35

[131] R. Nallapati, A. Feng, F. Peng, and J. Allan. Event threading within news topics. In The thirteenth ACM international conference on Information and knowledge management (2004). 35

[132] A. Ahmed and Q. Ho. Unified analysis of streaming news. In WWW, pp. 267-276 (2011). 35

[133] X. Tang and C. C. Yang. Tut: a statistical model for detecting trends, topics and user interests in social media. In Information and knowledge management, pp. 972-981 (2012). 35

[134] D. Shahaf and C. Guestrin. Connecting the dots between news articles. In Proceedings of the 16th ACM SIGKDD international conference on Knowledge discovery and data mining, pp. 623-632 (2010). 35

[135] J. Gillenwater, A. Kulesza, and B. Taskar. Discovering diverse and salient threads in document collections. In Proceedings of the 2012 Joint Conference on Empirical Methods in Natural Language Processing and Computational Natural Language Learning, pp. $710-720$ (2012). 35

[136] D. Shahaf, C. Guestrin, and E. Horvitz. Trains of thought: Generating information maps. In Proceedings of the 21st international conference on World Wide Web, pp. 899-908 (2012). 35

[137] D. Shahaf, C. Guestrin, and E. Horvitz. Metro maps of science. In Proceedings of the 18th ACM SIGKDD international conference on Knowledge discovery and data mining, pp. $1122-1130$ (2012). 35

[138] A. Haghighi and L. Vanderwende. Exploring content models for multi-document summarization. In Annual Conference of the Association for Computational Linguistics (2009). 35

[139] K. Takahashi, T. Miura, and I. Shioya. Hierarchical summarizing and evaluating for web pages. In EROW (2007).

[140] D. Lawrie, W. B. Croft, and A. Rosenberg. Finding topic words for hierarchical summarization. In Proceedings of the 24th annual international ACM SIGIR conference on Research and development in information retrieval, pp. 349-357 (2001). 35

[141] A. Celikyilmaz and D. Hakkani-Tur. A hybrid hierarchical model for multidocument summarization. In 48 th Annual Meeting of the Association for Computational Linguistics (2010). 35

[142] Y. Ouyang, W. Li, and Q. Lu. An integrated multi-document summarization approach based on word hierarchical representation. In Proceedings of the ACLIJCNLP 2009 Conference Short Papers, pp. 113-116 (2009). 35

[143] C. C. Yang and F. L. Wang. Fractal summarization: summarization based on fractal theory. In Proceedings of the 26th annual international ACM SIGIR conference on Research and development in informaion retrieval, pp. 391-392 (2003). 35

[144] F. L. Wang, C. C. Yang, and X. Shi. Multi-document summarization for terrorism information extraction. In International Conference on Intelligence and Security Informatics, pp. 602-608 (Springer, 2006). 35

[145] J. Christensen, S. Soderland, G. Bansal, et al. Hierarchical summarization: Scaling up multi-document summarization. In Proceedings of the 52nd annual meeting of the association for computational linguistics (volume 1: Long papers), pp. 902-912 (2014). 35, 36, 72, 124, 126

[146] J. D. Novak, D. B. Gowin, and G. D. Bob. Learning how to learn (cambridge University press, 1984). 36

[147] A. Oliveira, F. C. Pereira, and A. Cardoso. Automatic reading and learning from text. In Proceedings of the international symposium on artificial intelligence (ISAI) (Citeseer, 2001). 36

[148] J. Villalon and R. A. Calvo. Concept extraction from student essays, towards concept map mining. In 2009 Ninth IEEE International Conference on Advanced Learning Technologies, pp. 221-225 (IEEE, 2009). 36

[149] A. V. D. Leake. Jump-starting concept map construction with knowledge extracted from documents. In In Proceedings of the Second International Conference on Concept Mapping (CMC (Citeseer, 2006).

[150] C. Z. Aguiar, D. Cury, and A. Zouaq. Automatic construction of concept maps from texts. In Conference on Concept Mapping-CMC. Tallinn. Retrieved from http://cmc. ihmc. us/cmc2016papers/cmc2016-p90. pdf.[GS SEARCH] (2016). 36

[151] K. Rajaraman and A.-H. Tan. Knowledge discovery from texts: a concept frame graph approach. In Proceedings of the eleventh international conference on Information and knowledge management, pp. 669-671 (2002). 36

[152] A. Zouaq and R. Nkambou. Building domain ontologies from text for educational purposes. IEEE Transactions on learning technologies 1(1), 49 (2008).

[153] K. Zubrinic, D. Kalpic, and M. Milicevic. The automatic creation of concept maps from documents written using morphologically rich languages. Expert systems with applications 39(16), $12709(2012) .36$

[154] I. Qasim, J.-W. Jeong, J.-U. Heu, and D.-H. Lee. Concept map construction from text documents using affinity propagation. Journal of Information Science 39(6), 719 (2013). 36

[155] A. Borisov, M. Wardenaar, I. Markov, and M. de Rijke. A click sequence model for web search. In The 41 st International ACM SIGIR Conference on Research 6 Development in Information Retrieval, pp. 45-54 (2018). 36

[156] M. Denkowski, C. Dyer, and A. Lavie. Learning from post-editing: Online model
adaptation for statistical machine translation. In Proceedings of the 14th Conference of the European Chapter of the Association for Computational Linguistics, pp. 395-404 (2014). 36

[157] J. Kreutzer, S. Khadivi, E. Matusov, and S. Riezler. Can neural machine translation be improved with user feedback? arXiv preprint arXiv:1804.05958 (2018). 36

[158] C. Lawrence and S. Riezler. Counterfactual learning from human proofreading feedback for semantic parsing. arXiv preprint arXiv:1811.12239 (2018). 36

[159] Adam: A method for stochastic optimization. arXiv preprint arXiv:1412.6980 (2014). 36

[160] C. Orasan and L. Hasler. Computer-aided summarisation-what the user really wants. In LREC, pp. 1548-1551 (2006). 36

[161] T. C. Craven. Abstracts produced using computer assistance. Journal of the American Society for Information Science 51(8), 745 (2000).

[162] M. Narita, K. Kurokawa, and T. Utsuro. A web-based english abstract writing tool using a tagged ej parallel corpus. In LREC (2002). 36

[163] O. Shapira, H. Ronen, M. Adler, Y. Amsterdamer, J. Bar-Ilan, and I. Dagan. Interactive abstractive summarization for event news tweets. In Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing: System Demonstrations, pp. 109-114 (2017). 36

[164] A. Leuski, C.-Y. Lin, and E. Hovy. ineats: interactive multi-document summarization. In The Companion Volume to the Proceedings of 41 st Annual Meeting of the Association for Computational Linguistics, pp. 125-128 (2003). 37

[165] S. Jones, S. Lundy, and G. W. Paynter. Interactive document summarisation using automatically extracted keyphrases. In Proceedings of the 35th Annual Hawaii International Conference on System Sciences, pp. 1160-1169 (IEEE, 2002). 37

[166] P. Avinesh and C. M. Meyer. Joint optimization of user-desired content in multidocument summaries by learning from user feedback. In Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 1353-1363 (2017). 37

[167] M. Zopf. Estimating summary quality with pairwise preferences. In Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers), pp. $1687-1696$ (2018). $37,96,98$

[168] A. Sokolov, J. Kreutzer, S. Riezler, and C. Lo. Stochastic structured prediction under bandit feedback. In Advances in neural information processing systems, pp. $1489-1497$ (2016). 37,97

[169] J. Kreutzer, A. Sokolov, and S. Riezler. Bandit structured prediction for neural sequence-to-sequence learning. arXiv preprint arXiv:1704.06497 (2017). 37, 97

[170] Y. Gao, C. M. Meyer, and I. Gurevych. April: Interactively learning to summarise by combining active preference learning and reinforcement learning. arXiv preprint arXiv: 1808.09658 (2018). $37,97,104$

[171] K. M. Hermann, T. Kocisky, E. Grefenstette, L. Espeholt, W. Kay, M. Suleyman, and P. Blunsom. Teaching machines to read and comprehend. In Advances in neural information processing systems, pp. 1693-1701 (2015). 40

[172] J. Steinberger and K. Ježek. Evaluation measures for text summarization. Computing and Informatics $\mathbf{2 8}(2), 251$ (2012). 41

[173] P. Over, H. Dang, and D. Harman. Duc in context. Information Processing \& Management 43(6), 1506 (2007). 41

[174] L. Ermakova, J. V. Cossu, and J. Mothe. A survey on evaluation of summarization methods. Information Processing \& Management 56(5), 1794 (2019). 42

[175] R. M. Aliguliyev. A new sentence similarity measure and sentence based extractive technique for automatic text summarization. Expert Systems with Applications $\mathbf{3 6 ( 4 )}(2009) .43$

[176] Z. Li, Z. Peng, S. Tang, C. Zhang, and H. Ma. Text summarization method based on double attention pointer network. IEEE Access 8, 11279 (2020). 47

[177] R. Rautray, R. Dash, and R. Dash. Performance analysis of modified shuffled frog leaping algorithm for multi-document summarization problem. Informatica $43(3)(2019) .47$

[178] S. Ghodratnama and R. Boostani. An efficient strategy to handle complex datasets having multimodal distribution. In ISCS 2014: Interdisciplinary Symposium on Complex Systems, pp. 153-163 (Springer, 2015). 47, 133

[179] S. Ghodratnama and H. A. Moghaddam. Content-based image retrieval using feature weighting and c-means clustering in a multi-label classification framework. Pattern Analysis and Applications pp. 1-10 (2020). 47

[180] C. D. Manning, M. Surdeanu, J. Bauer, J. Finkel, S. J. Bethard, and D. McClosky. The Stanford CoreNLP natural language processing toolkit. In Association for Computational Linguistics (ACL) System Demonstrations, pp. 55-60 (2014). URL http://www.aclweb.org/anthology/P/P14/P14-5010. 50

[181] D. Rusu, L. Dali, B. Fortuna, M. Grobelnik, and D. Mladenic. Triplet extraction from sentences. In Proceedings of the 10, 8 (2007). 50

[182] R. Paredes and E. Vidal. Learning weighted metrics to minimize nearest-neighbor classification error. IEEE Transactions on Pattern Analysis and Machine Intelligence 28(7), 1100 (2006). 52, 136

[183] J. Christensen, Mausam, S. Soderland, and O. Etzioni. Towards coherent multidocument summarization. In Proceedings of North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL 2013) (2013). 53, 75

[184] R. Stuart, N. Peter, et al. Artificial intelligence: a modern approach (2003). 55

[185] P. J. Rousseeuw. Silhouettes: a graphical aid to the interpretation and validation of cluster analysis. Journal of computational and applied mathematics 20, 53 (1987). 56

[186] Y.-a. Kang, C. Gorg, and J. Stasko. How can visual analytics assist investigative analysis? IEEE Transactions on Visualization and Computer Graphics 17(5), 570 (2010). 64

[187] O. Etzioni, M. Banko, S. Soderland, and D. S. Weld. Open information extraction from the web. Communications of the ACM 51(12), 68 (2008). 76, 117

[188] S. Deerwester, S. T. Dumais, G. W. Furnas, T. K. Landauer, and R. Harshman. Indexing by latent semantic analysis. Journal of the American society for information science 41(6), 391 (1990). 77, 103

[189] G. A. Miller, R. Beckwith, C. Fellbaum, D. Gross, and K. J. Miller. Introduction to wordnet: An on-line lexical database. International journal of lexicography $3(4), 235$ (1990). 77,103

[190] R. Barzilay and M. Lapata. Aggregation via set partitioning for natural language generation. In Proceedings of the Human Language Technology Conference of the NAACL, Main Conference, pp. 359-366 (2006). 77, 103

[191] A. T. Chaganty, S. Mussman, and P. Liang. The price of debiasing automatic metrics in natural language evaluation. arXiv preprint arXiv:1807.02202 (2018). 96

[192] P. Abbeel and A. Y. Ng. Apprenticeship learning via inverse reinforcement learning. In Proceedings of the twenty-first international conference on Machine learning, p. 1 (2004). 98, 105

[193] A. Alhindi, U. Kruschwitz, C. Fox, and M.-D. Albakour. Profile-based summarisation for web site navigation. ACM Transactions on Information Systems (TOIS) 33(1), 1 (2015). 98

[194] D. C. Kingsley and T. C. Brown. Preference uncertainty, preference learning, and paired comparison experiments. Land Economics 86(3), 530 (2010). 98

[195] J. Fürnkranz and E. Hüllermeier. Preference learning and ranking by pairwise comparison. In Preference learning, pp. 65-82 (Springer, 2010). 99

[196] M. Szummer and E. Yilmaz. Semi-supervised learning to rank with preference regularization. In Proceedings of the 20th ACM international conference on Information and knowledge management, pp. 269-278 (2011). 100, 121

[197] B. Settles. Active learning literature survey. Tech. rep., University of WisconsinMadison Department of Computer Sciences (2009). 101

[198] T. Mikolov, I. Sutskever, K. Chen, G. S. Corrado, and J. Dean. Distributed representations of words and phrases and their compositionality. NIPS 26, 3111 (2013). $103,119,149,150$

[199] J. Kreutzer, J. Uyheng, and S. Riezler. Reliability and learnability of human bandit feedback for sequence-to-sequence reinforcement learning. arXiv preprint arXiv:1805.10627 (2018). 106

[200] P. Bojanowski, E. Grave, A. Joulin, and T. Mikolov. Enriching word vectors with subword information. Transactions of the Association for Computational Linguistics 5, 135 (2017). 119

[201] R. Tibshirani, G. Walther, and T. Hastie. Estimating the number of clusters in a data set via the gap statistic. Journal of the Royal Statistical Society 63(2), 411 (2001). 120, 154

[202] D. Hoplaros, Z. Tari, and I. Khalil. Data summarization for network traffic monitoring. Journal of network and computer applications 37, 194 (2014). 130, 133

[203] M. Ahmed. Data summarization: a survey. Knowledge and Information Systems $58(2), 249(2019) .130,134$

[204] M. Ahmed. Intelligent big data summarization for rare anomaly detection. IEEE Access 7, 68669 (2019). 132, 142

[205] W. G. Cochran and G. William. Sampling techniques. new york: John wiley \}́ sons (1977). 132

[206] S. Ghodratnama and M. SadrAldini. An innovative sampling method for massive data reduction in data mining. In The 3rd Iran Data Mining Conf., Tehran (2009). 132

[207] V. Chandola and V. Kumar. Summarization-compressing data into an informative representation. Knowledge and Information Systems 12(3), 355 (2007). 133

[208] P. Wendel, M. Ghanem, and Y. Guo. Scalable clustering on the data grid. In 5th IEEE International symposium cluster computing and the Grid (ccGrid) (2005). 133

[209] F. M. Pouzols, D. R. Lopez, and A. B. Barros. Summarization and analysis of network traffic flow records. In Mining and control of network traffic by computational intelligence, pp. 147-189 (Springer, 2011). 133

[210] J. Han and Y. Fu. 16 exploration of the power of attribute-oriented induction in data mining. Ad... ces in Know Ledge Discover and Data M ining. Cambridge: AAAI/'\&I1T Press, 1 g96 pp. 399-42l (1996). 133

[211] H. Jagadish, J. Madar, and R. T. Ng. Semantic compression and pattern extraction with fascicles. In $V L D B$, vol. 99, pp. 186-97 (1999). 133

[212] S. Babu, M. Garofalakis, and R. Rastogi. Spartan: A model-based semantic compression system for massive data tables. ACM SIGMOD Record 30(2), 283 (2001). 133

[213] M. Ahmed, A. Anwar, A. N. Mahmood, Z. Shah, and M. J. Maher. An investigation of performance analysis of anomaly detection techniques for big data in
scada systems. EAI Endorsed Trans. Indust. Netw. \& Intellig. Syst. 2(3) (2015). $134,138,140$

[214] I. Balabine and A. Velednitsky. Method and system for confident anomaly detection in computer network traffic (2017). US Patent 9,843,488. 134

[215] C. Kruegel, D. Mutz, W. Robertson, and F. Valeur. Bayesian event classification for intrusion detection. In 19th Annual Computer Security Applications Conference, 2003. Proceedings., pp. 14-23 (IEEE, 2003). 134

[216] G. Poojitha, K. N. Kumar, and P. J. Reddy. Intrusion detection using artificial neural network. In 2010 Second International conference on Computing, Communication and Networking Technologies, pp. 1-7 (IEEE, 2010). 134

[217] Y. Yang, K. McLaughlin, T. Littler, S. Sezer, and H. Wang. Rule-based intrusion detection system for scada networks. In 2nd IET Renewable Power Generation Conference (RPG 2013), pp. 1-4 (IET, 2013). 134

[218] M. Thottan and C. Ji. Anomaly detection in ip networks. IEEE Transactions on signal processing 51(8), 2191 (2003). 134

[219] M.-L. Shyu, S.-C. Chen, K. Sarinnapakorn, and L. Chang. A novel anomaly detection scheme based on principal component classifier. Tech. rep., MIAMI UNIV CORAL GABLES FL DEPT OF ELECTRICAL AND COMPUTER ENGINEERING (2003). 134

[220] O. Anava and K. Levy. $k^{*}$-nearest neighbors: From global to local. In Advances in Neural Information Processing Systems, pp pp. 4916-4924 (2016). 137

[221] M. Ahmed, A. N. Mahmood, and M. J. Maher. An efficient technique for network traffic summarization using multiview clustering and statistical sampling. EAI Endorsed Trans. Scalable Inf. Syst. 2(5), e4 (2015). 138

[222] S. Ramaswamy, R. Rastogi, and K. Shim. Efficient algorithms for mining outliers from large data sets. In Proceedings of the 2000 ACM SIGMOD international conference on Management of data, pp. 427-438 (2000). 139

[223] M. M. Breunig, H.-P. Kriegel, R. T. Ng, and J. Sander. Lof: identifying densitybased local outliers. In Proceedings of the 2000 ACM SIGMOD international conference on Management of data, pp. 93-104 (2000). 139

[224] J. Tang, Z. Chen, A. W. Fu, and D. W. Cheung. Capabilities of outlier detection schemes in large datasets, framework and methodologies. Knowledge and Information Systems 11(1), 45 (2007). 139

[225] S. Papadimitriou, H. Kitagawa, P. B. Gibbons, and C. Faloutsos. Loci: Fast outlier detection using the local correlation integral. In Proceedings 19th international conference on data engineering (Cat. No. 03CH37405), pp. 315-326 (IEEE, 2003). 139

[226] H.-P. Kriegel, P. Kröger, E. Schubert, and A. Zimek. Loop: local outlier probabilities. In Proceedings of the 18 th ACM conference on Information and knowledge management, pp. 1649-1652 (2009). 139

[227] W. Jin, A. K. Tung, J. Han, and W. Wang. Ranking outliers using symmetric neighborhood relationship. In Pacific-Asia Conference on Knowledge Discovery and Data Mining, pp. 577-593 (Springer, 2006). 139

[228] Z. He, X. Xu, and S. Deng. Discovering cluster-based local outliers. Pattern Recognition Letters 24(9-10), 1641 (2003). 140

[229] M. Amer and M. Goldstein. Nearest-neighbor and clustering based anomaly detection algorithms for rapidminer. In Proc. of the 3rd RapidMiner Community Meeting and Conference (RCOMM 2012), pp. 1-12 (2012). 140

[230] M. Amer, M. Goldstein, and S. Abdennadher. Enhancing one-class support vector machines for unsupervised anomaly detection. In Proceedings of the ACM SIGKDD workshop on outlier detection and description, pp. 8-15 (2013). 140

[231] M. Ahmed, A. N. Mahmood, and M. J. Maher. A novel approach for network traffic summarization. In International Conference on Scalable Information Systems, pp. 51-60 (Springer, 2014). 142

[232] W. W. Fleuren and W. Alkema. Application of text mining in the biomedical domain. Methods 74, 97 (2015). 143

[233] S. Beheshti, B. Benatallah, S. Venugopal, S. H. Ryu, H. R. Motahari-Nezhad, and W. Wang. A systematic review and comparative analysis of cross-document coreference resolution methods and tools. Computing 99(4), 313 (2017). 143

[234] M. Moradi and N. Ghadiri. Quantifying the informativeness for biomedical literature summarization: An itemset mining method. Computer methods and programs in biomedicine 146, 77 (2017). 143

[235] M. Moradi and N. Ghadiri. Different approaches for identifying important concepts in probabilistic biomedical text summarization. Artificial intelligence in medicine 84, 101 (2018).

[236] M. Moradi. Cibs: A biomedical text summarizer using topic-based sentence clustering. Journal of biomedical informatics 88, 53 (2018). 143

[237] H. Zhang, M. Fiszman, D. Shin, C. M. Miller, G. Rosemblat, and T. C. Rindflesch. Degree centrality for semantic abstraction summarization of therapeutic studies. Journal of biomedical informatics 44(5), 830 (2011). 143

[238] M. Fiszman, D. Demner-Fushman, H. Kilicoglu, and T. C. Rindflesch. Automatic summarization of medline citations for evidence-based medical treatment: a topicoriented evaluation. Journal of biomedical informatics 42(5), 801 (2009). 143

[239] M. Fiszman, T. C. Rindflesch, and H. Kilicoglu. Summarizing drug information in medline citations. In AMIA Annual Symposium Proceedings, vol. 2006, p. 254 (American Medical Informatics Association, 2006). 143

[240] M. A. Morid, M. Fiszman, K. Raja, S. R. Jonnalagadda, and G. Del Fiol. Classification of clinically useful sentences in clinical evidence resources. Journal of biomedical informatics 60, 14 (2016). 143

[241] H. Moen, L.-M. Peltonen, J. Heimonen, A. Airola, T. Pahikkala, T. Salakoski, and S. Salanterä. Comparison of automatic summarisation methods for clinical free text notes. Artificial intelligence in medicine 67, 25 (2016). 143

[242] R. Pivovarov and N. Elhadad. Automated methods for the summarization of electronic health records. Journal of the American Medical Informatics Association $\mathbf{2 2 ( 5 ) , ~} 938$ (2015). 143

[243] A. Nenkova and K. McKeown. Automatic summarization (Now Publishers Inc, 2011). 145

[244] L. Damianos, S. Wohlever, J. Ponte, G. Wilson, F. Reeder, T. McEntee, R. Kozierok, L. Hirschman, and D. Day. Real users, real data, real problems: the mitap system for monitoring bio events. In Proceedings of the second international conference on Human Language Technology Research, pp. 357-362 (2002). 145

[245] K. R. McKeown, N. Elhadad, and V. Hatzivassiloglou. Leveraging a common representation for personalized search and summarization in a medical digital library. In 2003 Joint Conference on Digital Libraries, 2003. Proceedings., pp. 159-170 (IEEE, 2003). 145

[246] I. Mani and E. Bloedorn. Summarizing similarities and differences among related documents. Information Retrieval 1(1), 35 (1999). 145

[247] A. Lenci, R. Bartolini, N. Calzolari, A. Agua, S. Busemann, E. Cartier, K. Chevreau, and J. Coch. Multilingual summarization by integrating linguistic resources in the mlis-musi project. In LREC, vol. 2, pp. 1464-1471 (2002). 145,146

[248] D. B. Johnson, Q. Zou, J. D. Dionisio, V. Z. Liu, and W. W. Chu. Modeling medical content for automated summarization. Annals of the New York Academy of Sciences 980(1), 247 (2002). 146, 147

[249] M.-Y. Kan, K. McKeown, and J. L. Klavans. Applying natural language generation to indicative summarization. In Proceedings of the ACL 2001 Eighth European Workshop on Natural Language Generation (EWNLG) (2001). 146

[250] M.-Y. Kan, K. R. McKeown, and J. L. Klavans. Domain-specific informative and indicative summarization for information retrieval. In In: Workshop on text summarization (DUC 2001 (Citeseer, 2001). 146

[251] R. Gaizauskas, P. Herring, M. Oakes, M. Beaulieu, P. Willett, H. Fowkes, and A. Jonsson. Intelligent access to text: Integrating information extraction technology into text browsers. In Proceedings of the First International Conference on Human Language Technology Research (2001). 146

[252] N. Elhadad and K. R. McKeown. Towards generating patient specific summaries of medical articles. In In Proceedings of NAACL-2001 Workshop "Automatic (Citeseer, 2001). 146, 147

[253] S. Ebadollahi, S.-F. Chang, H. D. Wu, and S. Takoma. Echocardiogram video summarization. In Medical Imaging 2001: Ultrasonic Imaging and Signal Processing, vol. 4325, pp. 492-501 (International Society for Optics and Photonics, 2001). 147

[254] X. Zhu, J. Fan, M.-S. Hacid, and A. K. Elmagarmid. Classminer: mining medical video for scalable skimming and summarization. In Proceedings of the tenth ACM international conference on Multimedia, pp. 79-80 (2002). 147

[255] S. Afantenos, V. Karkaletsis, and P. Stamatopoulos. Summarization from medical documents: a survey. Artificial intelligence in medicine 33(2), 157 (2005). 147

[256] Z. Yang, D. Yang, C. Dyer, X. He, A. Smola, and E. Hovy. Hierarchical attention networks for document classification. In Proceedings of the 2016 conference of the North American chapter of the association for computational linguistics: human language technologies, pp. 1480-1489 (2016). 151

[257] F. Schiliro, A. Beheshti, S. Ghodratnama, F. Amouzgar, B. Benatallah, J. Yang, Q. Z. Sheng, F. Casati, and H. R. Motahari-Nezhad. icop: Iot-enabled policing processes. In International Conference on Service-Oriented Computing, pp. 447452 (Springer, 2018). 156

[258] W. Van Der Aalst and et al. Process mining manifesto. In International Conference on Business Process Management, pp. 169-194 (Springer, 2011). 157

[259] S. Beheshti, B. Benatallah, S. Sakr, D. Grigori, H. R. Motahari-Nezhad, M. C. Barukh, A. Gater, and S. H. Ryu. Process Analytics - Concepts and Techniques for Querying and Analyzing Process Data (Springer, 2016). 157

[260] S. Beheshti, B. Benatallah, H. R. M. Nezhad, and S. Sakr. A query language for analyzing business processes execution. In Business Process Management - 9th International Conference, BPM 2011, Clermont-Ferrand, France, August 30 September 2, 2011. Proceedings, vol. 6896 of Lecture Notes in Computer Science, pp. 281-297 (Springer, 2011). 157

[261] A. Beheshti, F. Schiliro, S. Ghodratnama, F. Amouzgar, B. Benatallah, J. Yang, Q. Z. Sheng, F. Casati, and H. R. Motahari-Nezhad. iprocess: Enabling iot platforms in data-driven knowledge-intensive processes. In Business Process Management Forum - BPM Forum 2018, Sydney, NSW, Australia, September 9-14, 2018, Proceedings, vol. 329 of Lecture Notes in Business Information Processing, pp. 108-126 (Springer, 2018). 157

[262] A. Beheshti, B. Benatallah, R. Nouri, V. M. Chhieng, H. Xiong, and X. Zhao. Coredb: a data lake service. In Proceedings of the 2017 ACM on Conference on Information and Knowledge Management, CIKM 2017, Singapore, November 06 - 10, 2017, pp. 2451-2454 (2017). 158, 159

[263] A. A. Braga and D. L. Weisburd. Police innovation and crime prevention: Lessons learned from police research over the past 20 years (2015). 158

[264] A. Beheshti, B. Benatallah, R. Nouri, and A. Tabebordbar. Corekg: a knowledge lake service. PVLDB (2018). 158,159

[265] A. Beheshti, B. Benatallah, Q. Z. Sheng, and F. Schiliro. Intelligent knowledge lakes: The age of artificial intelligence and big data. In Web Information Systems Engineering - WISE 2019 Workshop, Demo, and Tutorial, Hong Kong and Macau, China, January 19-22, 2020, Revised Selected Papers, vol. 1155 of Communications in Computer and Information Science, pp. 24-34 (Springer, 2019).

[266] A. Beheshti, B. Benatallah, A. Tabebordbar, H. R. Motahari-Nezhad, M. C. Barukh, and R. Nouri. Datasynapse: A social data curation foundry. Distributed Parallel Databases 37(3), 351 (2019). 158

[267] S. Beheshti, B. Benatallah, and H. R. Motahari-Nezhad. Scalable graph-based OLAP analytics over process execution data. Distributed and Parallel Databases



[268] M. Hammoud, D. A. Rabbou, R. Nouri, S. Beheshti, and S. Sakr. DREAM: distributed RDF engine with adaptive query planner and minimal communication. Proc. VLDB Endow. 8(6), 654 (2015). 160

[269] H. R. Motahari-Nezhad, R. Saint-Paul, F. Casati, and B. Benatallah. Event correlation for process discovery from web service interaction logs. The VLDB Journal, The International Journal on Very Large Data Bases 20(3), 417 (2011). 161

[270] S. Beheshti, B. Benatallah, and H. R. M. Nezhad. Enabling the analysis of crosscutting aspects in ad-hoc processes. In CAiSE, pp. 51-67 (2013). 162, 173

[271] S. Beheshti, A. Tabebordbar, B. Benatallah, and R. Nouri. On automating basic data curation tasks. In WWW 2017, pp. 165-169 (2017). 167

[272] S. Ghodratnama, A. Beheshti, M. Zakershahrak, and F. Sobhanmanesh. Intelligent narrative summaries: From indicative to informative summarization. Big Data Research 26, 100257 (2021). 171

[273] S. Ghodratnama, M. Zakershahrak, and A. Beheshti. Summary2vec: Learning semantic representation of summaries for healthcare analytics. In 2021 International Joint Conference on Neural Networks (IJCNN), pp. 1-8 (2021). 171

[274] F. Schiliro, A. Beheshti, and N. Moustafa. A novel cognitive computing technique using convolutional networks for automating the criminal investigation process in policing. In Intelligent Systems and Applications - Proceedings of the 2020 Intelligent Systems Conference, IntelliSys 2020, London, UK, September 3-4, 2020, Volume 1, vol. 1250 of Advances in Intelligent Systems and Computing, pp. 528-539 (Springer, 2020). 172

[275] M. Zakershahrak and S. Ghodratnama. Are we on the same page? hierarchical explanation generation for planning tasks in human-robot teaming using reinforcement learning. arXiv preprint arXiv:2012.11792 (2020).

[276] M. Zakershahrak, S. R. Marpally, A. Sharma, Z. Gong, and Y. Zhang. Order matters: Generating progressive explanations for planning tasks in human-robot teaming. arXiv preprint arXiv:2004.07822 (2020).

[277] M. Zakershahrak, Z. Gong, N. Sadassivam, and Y. Zhang. Online explanation generation for planning tasks in human-robot teaming. In 2020 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pp. 6304-6310 (IEEE). 172

[278] A. Beheshti, A. Tabebordbar, and B. Benatallah. istory: Intelligent storytelling with social data. In Companion of The 2020 Web Conference 2020, Taipei, Taiwan, April 20-24, 2020, pp. 253-256 (ACM / IW3C2, 2020). 172

[279] A. Tabebordbar, A. Beheshti, and B. Benatallah. Conceptmap: A conceptual approach for formulating user preferences in large information spaces. In Web Information Systems Engineering - WISE 2019 - 20th International Conference, Hong Kong, China, November 26-30, 2019, Proceedings, vol. 11881 of Lecture Notes in Computer Science, pp. 779-794 (Springer, 2019). 172

[280] S. Ghodratnama, M. Zakershahrak, and F. Sobhanmanesh. Am i rare? an intelligent summarization approach for identifying hidden anomalies. In International Conference on Service-Oriented Computing, pp. 309-323 (Springer, 2020). 172

[281] A. Beheshti, V. M. Hashemi, and S. Yakhchi. Towards context-aware social behavioral analytics. In MoMM 2019: The 17th International Conference on Advances in Mobile Computing \& Multimedia, Munich, Germany, December 24, 2019, pp. 28-35 (ACM, 2019). 172

[282] S. Ghodratnama, M. Zakershahrak, and F. Sobhanmanesh. Adaptive summaries: A personalized concept-based summarization approach by learning from users' feedback. In International Conference on Service-Oriented Computing, pp. 281293 (Springer, 2020). 172

[283] A. Beheshti, K. Vaghani, B. Benatallah, and A. Tabebordbar. Crowdcorrect: A curation pipeline for social data cleansing and curation. In Information Systems in the Big Data Era - CAiSE Forum 2018, Tallinn, Estonia, June 11-15, 2018, Proceedings, vol. 317 of Lecture Notes in Business Information Processing, pp. 24-38 (Springer, 2018). 172

[284] M. A. Serhani, H. T. E. Kassabi, K. Shuaib, A. N. Navaz, B. Benatallah, and A. Beheshti. Self-adapting cloud services orchestration for fulfilling intensive sensory data-driven iot workflows. Future Gener. Comput. Syst. 108, 583 (2020). 172

[285] U. Shahbaz, A. Beheshti, S. Nobari, Q. Qu, H. Paik, and M. Mahdavi. irecruit: Towards automating the recruitment process. In Service Research and Innovation - 7th Australian Symposium, ASSRI 2018, Sydney, NSW, Australia, September 6, 2018, and Wollongong, NSW, Australia, December 14, 2018, Revised Selected Papers, vol. 367 of Lecture Notes in Business Information Processing, pp. 139152 (Springer, 2018). 173

[286] A. Beheshti, B. Benatallah, and H. R. Motahari-Nezhad. Processatlas: A scalable
and extensible platform for business process analytics. Softw. Pract. Exp. 48(4), 842 (2018). 173

[287] S. Beheshti, B. Benatallah, H. R. M. Nezhad, and M. Allahbakhsh. A framework and a language for on-line analytical processing on graphs. In Web Information Systems Engineering - WISE 2012 - 13th International Conference, Paphos, Cyprus, November 28-30, 2012. Proceedings, vol. 7651 of Lecture Notes in Computer Science, pp. 213-227 (Springer, 2012). 173

[288] A. Beheshti, B. Benatallah, H. R. Motahari-Nezhad, S. Ghodratnama, and F. Amouzgar. A query language for summarizing and analyzing business process data. CoRR abs/2105.10911 (2021). 2105.10911, URL https://arxiv. org/abs/2105.10911. 173

[289] S. Beheshti, B. Benatallah, and H. R. Motahari-Nezhad. Galaxy: A platform for explorative analysis of open data sources. In Proceedings of the 19th International Conference on Extending Database Technology, EDBT 2016, Bordeaux, France, March 15-16, 2016, Bordeaux, France, March 15-16, 2016, pp. 640-643 (OpenProceedings.org, 2016). 173

[290] A. Beheshti, S. Yakhchi, S. Mousaeirad, S. M. Ghafari, S. R. Goluguri, and M. A. Edrisi. Towards cognitive recommender systems. Algorithms 13(8), 176 (2020). 173

[291] S. Yakhchi, A. Beheshti, S. M. Ghafari, M. A. Orgun, and G. Liu. Towards a deep attention-based sequential recommender system. IEEE Access 8, 178073 (2020). 173

[292] M. Elahi, A. Beheshti, and S. R. Goluguri. Recommender systems: Challenges and opportunities in the age of big data and artificial intelligence. In Data Science and Its Applications, pp. 15-39 (Chapman and Hall/CRC, 2021). 173


[^0]:    ${ }^{1}$ https://duc.nist.gov/

    ${ }^{2} \mathrm{https}: / /$ github.com/abisee/cnn-dailymail

[^1]:    ${ }^{3}$ https://www.mturk.com/

[^2]:    ${ }^{1}$ http://knowitall.cs.washington.edu/gflow/

[^3]:    ${ }^{3}$ http://www.cnn.com/2015/04/03/us/california-drought/

[^4]:    ${ }^{4}$ Rouge-L results for TGRAPH and URANK are not reported.

[^5]:    ${ }^{1}$ available as part of the Stanford CoreNLP pipeline: https://nlp.stanford.edu/software/sutime.html

[^6]:    ${ }^{2}$ ROUGE-L results for TGRAPH and URANK are not reported.

[^7]:    ${ }^{1}$ We used fastText for word embedding: https://fasttext.cc/docs/en/support.html

[^8]:    ${ }^{1}$ https://nlp.stanford.edu/projects/glove/

[^9]:    ${ }^{2}$ https://catalog.data.gov/dataset/pubmed.

[^10]:    ${ }^{3}$ We run ROUGE 1.5.5: http://www.berouge.com/Pages/defailt.aspx with parameters -n $2-\mathrm{m}-\mathrm{u}$ -c 95 -r 1000 -f A -p 0.5 -t 0

