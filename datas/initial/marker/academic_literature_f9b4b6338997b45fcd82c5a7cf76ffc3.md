# Knowledge Representation In Graphs Using Convolutional Neural Networks

Armando Vieira Lidinwise, 1 Quality Court, WC2A 1HR London, UK
armando@lidinwise.com

## Abstract

Knowledge Graphs (KG) constitute a flexible representation of complex relationships between entities particularly useful for biomedical data. These KG, however, are very sparse with many missing edges (facts) and the visualisation of the mesh of interactions nontrivial. Here we apply a compositional model to embed nodes and relationships into a vectorised semantic space to perform graph completion. A visualisation tool based on Convolutional Neural Networks and Self-Organised Maps (SOM) is proposed to extract high-level insights from the KG. We apply this technique to a subset of CTD,
containing interactions of compounds with human genes / proteins and show that the performance is comparable to the one obtained by structural models.

## 1 Introduction

Knowledge Graphs (KG) are knowledge representation structures commonly used to store complex structured or unstructured data. Graphs can be direct or indirect with vertices representing entities (words, entities or concepts) and edges representing relationships between these entities. A KG contains two forms of knowledge: relational knowledge and categorical knowledge. Relational knowledge encodes the relationship between entities while categorical knowledge encodes the attributes of entities.

Multi-relational graphs encodes data via knowledge databases, or semantic networks, and are widely used in the Semantic Web and for knowledge representation in bioinformatics (Gene Ontology, for instance) or natural language processing (WordNet). In these graphs facts are modelled as triples in the form (subject, predicate, object), where a predicate either models the relationship between two entities or between an entity and an attribute value.

Note that any information of the KB can be represented via a triple or a concatenation of several triples. Such data sources are equivalently termed multi-relational graphs and they can be represented by a tensor, where each component represents an adjacency matrix of a single predicate.

Graph databases, such as Freebase [2], constitute rich repositories of annotated information that can be used for questions and answering applications.

Simple or compositional questions can be formulated as, "What chemical can increase expression of protein X in cell Y given that it was exposed to a substance Z?". However, KG are very incomplete and sparsely connected.

An elegant solution to solve the data incompleteness is using vector space representations and control the dimensionality of the vectors to obtain good generalization on new facts [21]. These methods are inspired in deep learning that is becoming the state-of-the-art approach for natural language processing tasks relying on distributed representations.

For instance, the Word2vec model [7], have been proposed to capture the semantics of words through the context - the principle is that words that are semantically similar should be closer to similar context words. The drawback of this approach is that the learned representations are mainly based on words, or entities, co-occurrences and cannot capture the relationship between two syntactically or semantically similar words if either of them yields very little context information.

In spite of their strong ability for representing complex data, multirelational graphs are still complicated to understand, relations can be missing or invalid, there can be redundancy among entities because several nodes actually refer to the same concept, etc. Furthermore, most multi-relational graphs are very large in terms of numbers of entities and of relation types which make visualization knowledge representation hard - for example, Freebase contains more than 20 millions entities and billions of facts. Finally, most relations are localized on very few nodes - the so called fat-tail effect -
making inference of new facts regarding most entities very hard.

Here we use a recent compositional methods for KG completion where the learning process is framed as the inference of new connections between nodes [6]. This model addresses the problem of exploring relationships that goes beyond simple triples capturing chains of causality to generate and test hypothesis in the biomedical context.

We also address the problem of visualisation of information contained in these graphs, a complex task as some nodes may have thousands of edges
(relations) of dozens of different types. The combinatorial explosion of the number of possible causality relations severely constrains the use of graphical display tools.

This work addresses these issues by applying a deep convolution network to visualize information contained in graphs with distributed representations.

We demonstrate how to extract semantic fingerprints and show how they are useful for knowledge discovery and classification problems.

This paper is organised as follows: section 2 presents the model for embeddings and new facts discovery. Section 3 describes the data and Section 4 describes the SOM model, the semantic fingerprints obtained and some results. Section 5 describes the CNN model applied to the self-organized maps.

Section 6 presents the an application to the protein compound prediction and Section 7 contains the conclusions and future work.

## 2 The Compositional Model For Graph Embeddings

Much work for knowledge graph completion was based on symbolic methods.

These methods represent knowledge through simple algebraic operations but they are, in general, not tractable. Recently, a powerful approach for this task is to encode every element (entities and relations) of a knowledge graph into a low-dimensional embedding vector space. Among these methods, TransE [4]
is a simple and effective one with state-of-the-art link prediction precision.

It learns low-dimensional embeddings for every entity and relation in the KG where the basic idea is that every relation is regarded as a vectorial translation in the embedding space. For a triplet (*h, r, t*), the embedding h is close to the embedding t by adding the embedding vector r, so that h+r ≈ t. TransE is suitable for 1-to-1 relations, but less robust dealing with 1-to-N, N-to-1 or N-to-N relations. The model is training by minimising a loss function of how good new links are predicted in the test set.

Recently a compositional model was proposed [6]. In this model the objective function to be minimised the following max-margin objective function:

$$J(\Theta)=\sum_{i=1}^{N}\sum_{t^{\prime}\in\mathcal{N}(q)}\left[1-\text{margin}(q_{i},t_{i},t^{\prime})\right]_{+},\text{margin}(q,t,t^{\prime})=\text{score}(q,t)-\text{score}(q,t^{\prime}),\tag{1}$$
$$\left(2\right)$$

where the parameters are the membership operator, the traversal operators, and the entity vectors:

$$\Theta=\cup\left\{T_{r}:r\in R\right\}\cup\left\{x_{e}\in R^{d}:e\in E\right\}.$$

The idea is to query not just simple triples but arbitrary complex ones from a set of path query training examples {(qi, ti)}
N
i=1 with path lengths ranging from 1 to L. While most models are trained only for objectives functions with queries of path length 1, this objective function takes into account extended composed paths.

## 2.1 Transe Model

There are many possible implementations of T and M, but we will use TransE [3] due to its simplicity and performance on knowledge base completion.

Given a training set S of triples (*h, l, t*) composed of two entities h, t ∈ E
(the set of entities) and a relationship l ∈ L (the set of relationships), the model learns vector embeddings of the entities and the relationships that minimizes a given loss function. TransE works on the idea that a relation induced by the edges can be captured by a translation of the embeddings. It uses the scoring function:

$$\mathrm{score}(s/r,t)=-\|x_{s}+w_{r}-x_{t}\|_{2}^{2}.$$

. (3)
where xs, wr and xt are all d-dimensional vectors and the model membership operator is defined as:
(*v, x*t) = −kv − xtk 2 2(4)
and the traversal operator Tr(xs) = xs+wr. TransE can handle a path query q = s/r1/r2/ *· · ·* /rk using

$$\operatorname{score}(q,t)=-\|x_{s}+w_{r_{1}}+\cdot\cdot\cdot+w_{r_{k}}-x_{t}\|_{2}^{2}.$$
. (5)
$\left(3\right)$. 

$$\left(5\right)$$

| WordNet   | CTD     |         |
|-----------|---------|---------|
| Relations | 11      | 42      |
| Entities  | 38 696  | 24 382  |
| Train     | 112 581 | 316 321 |
| Test      | 10 000  | 30 000  |

Table 1: Statistics of the databases used to train and test the models.

## 2.2 Implementation

We use Stochastic Gradient Descent (SGD) [11] to optimize J(Θ), which is a non-convex objective function. We initialise all parameters with i.i.d.

Gaussians of variance 0.25 and use a mini-batch size of 100 examples, and a step size in [0.001, 0.1] (chosen via cross-validation). For each example q, we sample 10 negative entities t 0 ∈ N (q). As suggested by [6], during training, all of the entity vectors are constrained to lie on the unit ball, and we clipped the gradients to the median of the observed gradients if the update exceeded 3 times the median. The dimensionality of the encodings was set to d = 50, a margin of 1 and we use the L2 metric.

The models were implemented based on Theano libraries [1] that are very fast and scalable.

## 3 Data Description And Training

We will use two knowledge base completion datasets consisting of single-edge queries, a subset of WordNet [17] and CTD [9], as described in Table 1. The original CTD, contains around 575 150 nodes (genes, chemicals, diseases, proteins, etc) and 2 965 279 edges. For this work we only consider relations between compounds (chemicals) and genes - mostly, but not all, coding for proteins. This information was extracted from manual annotations of around a hundred thousand scientific publications.

CTD is very different from WordNet since it is a bipartite graph between compounds and genes and in WordNet both head and target entities are arbitrary words. In WordNet relations can be reversed but not in CTD.

There are about 1700 different types of relationships between compounds and genes. We only consider the ones with more than 1000 facts, ending up with 42 relations types and 316 321 facts used for training.

Following [6] we generate path queries by performing random walks on the graph thus generating an extended set of auxiliary training data.

We start from the training graph Gtrain formed by edges in the training set. New training examples are generated as follows:

1. Uniformly sample a path length L ∈ {1*, . . . , L*max}, and uniformly sample a starting entity s ∈ E.
2. Perform a random walk beginning at entity s and continuing L steps.

(a) At step i of the walk, choose a relation ri uniformly from the set of relations incident on the current entity e.

(b) Choose the next entity uniformly from the set of entities reachable via ri.
3. Output a query-answer pair, (*q, t*), where q = s/r1/ *· · ·* /rL and t is the final entity of the random walk.

Paths of length 1 were not sampled and we added all of the edges from Gtrain to the dataset.

## 4 The Som Visualisation

Self-Organized Maps (SOM) is an algorithm for supervised or unsupervised clustering useful to represent high-dimensional data into a topographic twodimensional map. SOM were introduced by Kohonen [10] as an unsupervised learning process that learns the distribution of a set of patterns without any class information. A pattern is projected from an input space to a position in the map and information is coded as the location of an activated node. The advantage of SOM is that it provides a topological ordering of the classes where similarity is preserved and its useful for classification of data which a large number of categories - as is our case where is difficult to define class boundaries. A SOM can be seen as a dimensionality reduction technique that use a neighbourhood function to preserve the topological properties of the input space.

A SOM operates in two modes: training and mapping. "Training" builds a map with input examples, while "mapping" classifies the unseen input vectors. In our case we use SOM to aggregate the embeddings obtained from the compositional TransE model.

![6_image_0.png](6_image_0.png)

Figure 1: Code-vectors obtained from the Self Organized Map for the embeddings of the CTD database and the quality of each node.

The advantage of SOM over other methods, like t-SNE, is that is simpler to interpret the results and it lends itself to a more flexible representation.

Next section explains how these maps can be interpreted and their usefulness in the biomedical context.

We used a rectangular 50x50 map with circular boundary conditions.

Figure 2 describes the codevectors of the compounds embeddings for the CTD database using a embedding dimension of d = 50 and the quality of each node.

In Figure 2 we group the SOM cells into five categories, identified by colours. Each region correspond to a specific pattern of interaction between a set of genes and compounds. We can see that there are some well defined compact segments while others have a more scattered pattern (green). The explanation of these clusters will be detailed below.

In order to verify the results, we aggregate the SOM code-vectors into five clusters and project the interactions of the compounds with a set of genes aggregated by these clusters - see Table 2.

Ir order to access the quality of the projection, for a specific cell in the SOM map we select the chemicals associated with it, Cij and the genes that, in the TransE model, has a short distance. From the CTD database we 7

![7_image_0.png](7_image_0.png)

them select the corresponding genes associated with these compounds and extract all the genes that have interactions with these chemicals. Based on these entities, we build a sub-graph and evaluate the Jaccard distances of all the chemical Cij . We run an algorithm for all the cells in the SOM and compute a global ratio for evaluate the semantic capability of the clustering just obtained. The value was 1.37, which contrast with the initial value of 0.0031, a factor of about 400 - all type of interactions were considered. This shows that the aggregation made by the SOM has semantic meaning and is informative about the interactions in the original graph.

For similar genes interaction patterns we expect similar mappings, as is fact the case for IL10 (interleukin 10) and EDN1 (endothelin 1). Note that this does not implies that the two genes are similar, only that they have a similar interaction pattern.

## 4.1 From Fingerprints To Drug Discovery

Now that we know that the SOM represents meaningful information, we can go an extra step in terms of interpreting the results and help the researcher visualizing the data and test new hypothesis.

The traditional concept that drugs exert their activities by modulating

| Genes   | c1   | c2   | c3   | c4   | c5   |
|---------|------|------|------|------|------|
| All     | 843  | 819  | 341  | 189  | 268  |
| IL10    | 3    | 42   | 59   | 103  | 5    |
| EDN1    | 2    | 23   | 51   | 119  | 1    |
| UGT     | 38   | 79   | 47   | 146  | 13   |
| TIA     | 1    | 0    | 1    | 49   | 0    |
| AHR     | 24   | 98   | 43   | 125  | 3    |

Table 2: Results from the fingerprints in the gene space: number or compounds that interact with each gene and the cluster membership.

one target of particular relevance to a disease has guided the pharmaceutical industry in recent decades. However, there is evidence that this process is incomplete since many drugs do interact with multiple targets [12]. Furthermore, a significant number of chemical compounds have failed to get approved due to serious clinical side-effects observed during later-stages [11].

The lesson in that multi-target interactions of drugs are largely unknown and poorly understood.

For a drug to have the desired effect we need to modulate a set of targets to achieve efficacy, while avoiding others to reduce the risk of side effects. By considering all types of interactions between compounds and proteins, our method can be useful for the development multi target drugs.

Since we know the components involved in each disease, we can create its unique fingerprint based on the activation level of each code-vector in respect to the genes involved in the disease. In Figure 4 we plot the fingerprint for the lung and ovary cancer, i.e., genes that are involved in onset of the disease.

We quantise the distances to the code-vectors into colours (red an euclidian distance below 0.1, green a distance between 0.1 and 0.2). All other higher distances were not consider.

The SOM fingerprint is helpful for visualizing the differences between the sets using distances between molecular fingerprints of the molecules.

This technique clusters compounds (or genes) with similar interaction patterns with each other in the best matching cell while also maintaining a 2-dimensional grid of cells such that similar compounds or genes (depending on the mapping being used) appear in adjacent cells. Note that this pattern is not necessarily related to the structure or function of the genes/compounds being considered.

![9_image_0.png](9_image_0.png)

## 5 Analysis Of Som Maps With Cnn

SOM fingerprints are very useful for visualization but they are limited in terms of abstract features extraction. In this section we will apply the findings learnt to build a supervised model for protein docking problem using a Convolutional Neural Network. CNN are powerful neuronal networks specially designed to capture invariant features in images setting the state-ofthe-art in terms of image classification [18]. They also have a very interesting property in terms of capturing abstract representation of high-dimensional data. We will apply them to a very well known and important problem in structural biology: protein docking. We call this combination of SOM
fingerprints and supervised CNN the SOME model.

This problem is in general ill-posed and not sufficiently constrained: many models can fit the data thus achieving poor generalization. Convolutional networks (CNN) incorporate hard constraints on learning and are good at detecting invariants on data, either to translation or deformation, which make them particularly useful for image analysis. They use three basic concepts:
i) local receptive fields, ii) weight sharing, and iii) spatial subsampling.

The network we will use consists of a set of layers, each of which contains one or more planes. Normalized images enter at the input layer and each unit receives input from a small neighborhood in the planes of the previous layer.

The weights forming the receptive field for a plane are forced to be equal at all points in the plane. Each plane can be considered as a feature map which has a fixed feature detector that is convolved with a local window which is scanned over the planes in the previous layer. Multiple planes are usually