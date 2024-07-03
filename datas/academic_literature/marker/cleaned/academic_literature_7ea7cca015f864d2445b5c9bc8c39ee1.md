# Quiver Laplacians And Feature Selection Otto Sumray1,2, Heather A. Harrington2,3,4,5, Vidit Nanda2

ABSTRACT. The challenge of selecting the most relevant features of a given dataset arises ubiquitously in data analysis and dimensionality reduction. However, features found to be of high importance for the entire dataset may not be relevant to subsets of interest, and vice versa. Given a feature selector and a fixed decomposition of the data into subsets, we describe a method for identifying selected features which are compatible with the decomposition into subsets. We achieve this by re-framing the problem of finding compatible features to one of finding sections of a suitable quiver representation. In order to approximate such sections, we then introduce a Laplacian operator for quiver representations valued in Hilbert spaces. We provide explicit bounds on how the spectrum of a quiver Laplacian changes when the representation and the underlying quiver are modified in certain natural ways. Finally, we apply this machinery to the study of peak-calling algorithms which measure chromatin accessibility in single-cell data. We demonstrate that eigenvectors of the associated quiver Laplacian yield locally and globally compatible features.

## 1. Introduction

When working with large quantities of unstructured data, it is often convenient –
and on occasion, indispensable - to employ a family of real-valued *features* defined on the dataset. It has, for instance, become standard practice within natural language processing to embed words into Euclidean space based on their relative proximity to each other in a substantial corpus of text [23]. In this case, the coordinates serve as features. Regardless of how such an embedding has been obtained, one immediately seeks to simplify matters by identifying those features which are most relevant to the task at hand. There are several ways of quantifying the relevance of a given feature - one may use domain-specific context, optimise a statistical quantity such as variance, or exploit the presence of labelled training data, etc. This process of *feature selection* forms a cornerstone of data analysis.

Examples of well-known feature selectors include principal components [26], LASSO [32]
and recursive feature elimination [15], to name but a few.

arXiv:2404.06993v1 [stat.ML] 10 Apr 2024 We focus here on feature selection in the presence of an auxiliary decomposition of the



given dataset. As a toy example of the situation which we have in mind, let us consider the plots in Figure 1 of two features defined on datasets which have been decomposed into two overlapping subsets A and B.

Suppose we rank the relevance of features by their variance. In Figure 1.I, feature 1 is most relevant for subsets A, B, and A ∩ B, but would not be more relevant than feature 2 on their union A ∪ B. On the other hand in Figure 1.II, feature 1 is most relevant for A, and feature 2 for B, but both are equally relevant for A ∩ B and A ∪ B. Such unfortunate inconsistencies arise quite frequently, especially in biological contexts - we are often interested in features defined on datasets that are naturally organised by types, sub-types and so forth, such as disease or cell types. For such data, any feature selection process
(which remains agnostic to the decomposition) is liable to select features that are irrelevant to certain subsets while ignoring features that are relevant to certain subsets.

This Paper. Here we present a principled framework for selecting features on a finite set X that are consistent with respect to a decomposition of X into a *cover* U . Crucially, the subsets of X which comprise U are allowed to admit arbitrary overlaps. Given the immense diversity of available feature selectors and their inner workings, we adopt an abstract approach. Let K denote either the field R of real numbers or the field C of complex numbers. For our purposes, a feature selector S is any deterministic process that
(1) accepts as input some finite collection F of functions X → K, and
(2) outputs a subspace S
F
X
of the K-linear span V(F ) of F.

We assume an inner product structure on V(F ), but impose no further constraints on S;
as such, the results and constructions of this paper may be applied verbatim to any of the standard feature selectors. Similarly, there are no constraints on the cover U besides the requirement that X =SU∈U U.

For the purposes of these introductory remarks, let us call a nonempty subset σ ⊂ U
admissible whenever the intersection |σ| :=TU∈σ U is nonempty. Our quest here is to isolate the largest subspace of S
F
X
that is compatible with respect to the decomposition of X into admissible subsets. Two forms of compatibility are studied here: *local* and global.

Given an admissible subset σ ⊂ U , a feature v : |σ| → R in S
F
|σ| is locally compatible with U if for every admissible τ ⊂ U with |τ*| ⊃ |*σ|, there is some feature v
+ : |τ| → R in S
F
|τ| whose restriction to |σ| coincides with v. In other words, a locally compatible feature is one which continues to be selected as we pass to larger admissible subsets. Conversely, consider a collection of features {vσ}, one for each admissible σ. Such a collection is globally compatible with U if for each pair |σ*| ⊂ |*τ| of admissible subsets, the orthogonal projection π F
τ: V(F ) ↠ S
F
|τ| sends vσ to vτ. Thus, every globally compatible feature is generated by functions {vU : U → R | U ∈ U } such that the orthogonality relation
(vU − vU′) ⊥ S
F
U∩U′
holds in V(F ) for every U, U′ ∈ U .

The first question addressed in our work here is:
Fix a feature selector S and a cover U of X. Given an input F family of functions X → R, to what extent can we efficiently discover all of the locally and globally compatible features output by S?

We approach this problem by recasting it in the language of quiver representations. The underlying quiver QU is a directed graph whose vertices are admissible sets, with a single edge σ → τ whenever |σ*| ⊂ |*τ|. The output of S with input F induces a representation A• = A
S,F
- of Q valued in the category of finite dimensional Hilbert spaces. Explicitly, each vertex σ is assigned the Hilbert space Aσ := S
F
|σ|
, while each edge σ → τ is assigned the linear map Aσ→τ : Aσ → Aτ obtained by restricting π F
τto S
F
|σ|
. We show that the sections of this representation (as introduced in [30] and generalised to the multilinear setting in [24]), recover all the globally compatible features. Similarly, sections of this representation over certain augmented sub-quivers yield all the locally compatible features of S.

The presence of noise severely impairs the compatibility framework described above.

The main difficulty is that one never obtains an exact equality between (projections of)
features selected over an admissible set |τ| and features selected over an admissible subset |σ|. The best-case scenario is that features in Aσ lie *near*1the restriction of some feature in Aτ. In fact, exact equality may not even be desirable - often, features are highly correlated, and collapsing together such features will further reduce the dimension of the space of selected features. Thus, there are many compelling reasons to seek a less rigid compatibility framework built around approximate sections of quiver representations.

With this consideration in mind, the second question addressed in this paper is:
To what extent can we define and efficiently compute the approximate sections of a quiver representation?

We address this challenge by introducing a new Laplacian operator.

The **quiver Laplacian** L introduced here is a (Hermitian, positive semidefinite) endomorphism of the *total space* Tot(A•) := ∏σ Aσ. In the special case where every Aσ is 1Here proximity is determined by the inner product metric on V(F ).

one-dimensional and all orthogonal projection maps are identities, L coincides with the ordinary graph Laplacian of QU . We note that Laplacians have been defined for several discrete algebraic/combinatorial objects: from the original case of graphs [3], to simplicial complexes [12, 17], hypergraphs [2] and principal bundles on graphs [10]. Most closely related to our quiver Laplacian are the analogous operators defined for cellular sheaves in
[16] (but see also [11, 25]). The space of sections of a quiver representation coincides precisely with the kernel of the affiliated quiver Laplacian. Armed with the quiver Laplacian, we are able to define, for every ϵ > 0, the ϵ*-approximate sections* of a quiver representation as those normalised vectors x ∈ Tot(A
S,F
- ) which satisfy ⟨x, Lx⟩ ≤ ϵ. Thus, the spans of eigenvectors of L associated to small nonzero eigenvalues of L delineate special families of approximate sections. Motivated by these considerations, we establish a host of fundamental properties for quiver Laplacians and their spectra.

Finally, we use the spectrum of an appropriate quiver Laplacian to study feature selection (as given by a *peak-calling* algorithm) for chromatin accessibility2 data from [28].

Our dataset comes from single-cell sequencing. This type of data has several properties which make the Laplacian-driven approach particularly appropriate:
(1) The dimensionality is massive - a naïve estimate assumes that every genomic position might be accessible, giving around 3 billion features. Therefore, feature selection (via peak-calling) becomes a crucial intermediate step towards making the analysis tractable.

(2) Different cell types have different relevant features, and it is important to make the feature selection process compatible with the types of cells under consideration. This makes it necessary to consider peaks not only for the entire dataset, but also for certain distinguished subsets.

(3) In many relevant cases where the data arise from diseases such as cancer or from the immune system (e.g. T cells), the cells might exhibit plasticity and their type is therefore not well-defined. In such cases, our distinguished subsets might overlap and should be modelled by a cover rather than a partition.

(4) There is some stochasticity in the output of peak-calling algorithms - in particular, the accessible genomic positions are only known approximately. Thus, the accessibility status of nearby positions is not independent; we capture this phenomenon via the inner product structure on feature space.

Summary of Results. Let Q be a finite quiver with vertex set Q0, edge set Q1 and maps s, t : Q1 → Q0 which specify the source and target vertices of each edge. We consider representations of Q - each such representation A• assigns a finite-dimensional
(real or complex) Hilbert space Av to every vertex v ∈ Q0 and a linear map Ae: As(e) →
At(e)to every edge e ∈ Q1. We write LA for the Laplacian of A• (see Definition 4.2 below for details), and arrange its eigenvalues as

$$0\leq\lambda_{1}(\mathbf{A})\leq\lambda_{2}(\mathbf{A})\leq\cdots\leq\lambda_{n}(\mathbf{A}),$$

where n := dim Tot(A•) is the total dimension of A•.

Here is a simplified version of our first main result, which provides upper bounds on Laplacian eigenvalues of a representation A′•in terms of eigenvalues of A• whenever there exists a family of vertex-indexed linear maps Av → A′v.

THEOREM (I). Let A• and A′•be two representations of Q, and consider any vertex-indexed collection τ = {τv : Av → A′v | v ∈ Q0} *of linear maps. Write q for the dimension of* ker τ viewed as a (block diagonal) map Tot(A•) → Tot(A′•
)*. There exist positive constants* α, β, γ –
each dependent on τ *– such that the inequality*

$$\lambda_{k}(\mathbf{A}^{\prime})\leq\alpha\cdot\lambda_{k+q}(\mathbf{A})+\beta\cdot{\sqrt{\lambda_{k+q}(\mathbf{A})}}+\gamma$$
$$h o l d s\,f o r\,e v e r y\,k\,i n\,\left\{1,2,\ldots,n-q\right\}.$$

The full statement of this result, along with explicit formulas for α, β and γ, is recorded in Theorem 5.2. If τ is a morphism of quiver representations A• → A′•, then both β and γ vanish and we are left with a much simpler bound λk(A′) ≤ α · λk+q(A).

Our next main result takes the form of a *spectral stability* result for feature selectors.

The main challenge here is that the total spaces of two representations A
S,F
- and A
T,F
•
may have different dimensions, so even the number of eigenvalues of the corresponding Laplacians could be different. Nevertheless, let µS and µT be the probability measures on R given by taking the average of Dirac measures concentrated at the eigenvalues λi(AS,F )	and λj(AT,F )	, respectively. We obtain, in Corollary 5.5, the following bound on the 1-Wasserstein distance W1(µS, µT) between these two measures.

THEOREM (II). Let S and T be two feature selectors defined on a finite set X which is equipped with a cover U . Fix a finite collection F of functions X → K. For each admissible set σ*, define*

$$c_{\sigma}:=\left|\dim\mathbf{S}_{|\sigma|}^{\mathcal{F}}-\dim\mathbf{T}_{|\sigma|}^{\mathcal{F}}\right|\quad\,\,\,\,a n d\quad\epsilon_{\sigma}:=\operatorname{dist}_{\mathbf{Gr}}\left(\mathbf{S}_{|\sigma|}^{\mathcal{F}},\mathbf{T}_{|\sigma|}^{\mathcal{F}}\right),$$

where the latter expression invokes the Grassmannian distance between subspaces of V(F )*. Define* c := ∑σcσ and ϵ := maxσ ϵσ*. There exist trigonometric polynomials f and g such that*

$(\;\;\bullet\;\bullet)\;=\;\bullet\;\bullet$
$$W_{1}\left(\mu_{\mathbf{S},\,\mu_{\mathbf{T}}}\right)\leq\frac{|Q_{1}^{\mathcal{W}}|}{m}\Big{[}f(\epsilon)\cdot c+g(\epsilon)\cdot(m-c)\Big{]},$$  _where $|Q_{1}^{\mathcal{W}}|$ is the number of edges in $Q^{\mathcal{W}}$ and $m=\max\{\dim\operatorname{Tot}(\mathbf{A}_{\epsilon}^{\mathbf{S},\mathcal{F}}),\dim\operatorname{Tot}(\mathbf{A}_{\epsilon}^{\mathbf{T},\mathcal{F}})\}$._
We note that c = 0 if and only if the two feature selectors assign equidimensional spaces to each admissible set. Explicit formulas for f and g are provided in Section 5. Crucially, we have g(0) = 0; in the equidimensional case, the first term in our bound vanishes and the second term approaches 0 as ϵ → 0.

Our next main result provides several flavours of eigenvalue interlacing inequalities for quiver Laplacians which hold when quivers (and the overlaid representations) are modified in certain natural ways.

THEOREM (III). Let A• be a representation of Q. The following inequalities hold for appropriate integers i. The constants k,r, w1, w2 which appear below depend on A• *as well as the* modification performed to create a new representation A′•*of a new quiver Q*′.

(1) If Q′is obtained by removing edges from Q and A′•is the restriction of A• to Q′*, then* λk+i(A•) ≤ λk+i(A
′•
) ≤ λk+r+i(A•).

(2) If Q′is obtained by removing vertices (and incident edges) from Q and A′•is the restriction of A• to Q′*then*

λi(A•) − w1 ≤ λi(A
$$\mathbf{\lambda}_{\bullet}^{\prime})\leq\lambda_{k+i}(\mathbf{A}_{\bullet}$$
) ≤ λk+i(A•) − w2.

(3) If Q′and A′•*are the result of performing an admissible homotopy of Q, then*

$$\varphi^{-2}\lambda_{i}({\bf A_{\bullet}})\leq\lambda_{i}({\bf A_{\bullet}^{\prime}})\leq\varphi^{2}\lambda_{i}({\bf A_{\bullet}})$$
$$\mathbf{\Psi}_{\bullet}^{\prime})\leq\varphi^{2}\lambda_{i}(\mathbf{A}_{\bullet})$$

where φ *is the golden ratio.*
(4) If Q′and A′•are the result of performing an admissible Kron reduction of A•*, then* λi(A•) ≤ λi(A
′•
) ≤ λi+r(A•).

Detailed versions of these results, including explicit formulas for various constants as well as precise definitions of admissible homotopy and Kron reduction, are located in Section 6. In order to state and prove these results in an appropriately general setting, we define *sheaves* on quivers - these are almost identical to cellular sheaves [6, 5, 16] on graphs, except that our graphs are allowed to have self-loops.

As mentioned above, much of our work here has been motivated by the desire to better understand and improve peak-calling algorithms on datasets X which come naturally equipped with a decomposition U into subsets. For this purpose, it is convenient to combine the quiver representations whose sections give locally and globally compatible features of a given feature selector S into a single representation of a larger quiver. This combined representation, denoted NS,F
•, is described in Section 3.1. By design, its sections correspond to features which are both locally and globally compatible with U along F,
and we naturally seek its approximate sections. Unfortunately, extracting spectral data for its Laplacian presents a serious computational challenge - both the underlying quiver and the total dimension are typically much larger than QU and A
S,F
- . The third main result of this paper is a remedy which takes the form of a *reduction theorem*.

THEOREM (IV). Let S be a feature selector on a set X equipped with a cover U such that QU
is weakly connected. Let NS,F
•*be the combined representation associated to a finite collection* F
of functions X → K*. Fix a vertex* σ ∈ QU
0
. There exists a new quiver Q′ with a single vertex and |QU
0 | edges along with a representation A′•of Q′satisfying two properties:

(1) For each vertex τ of QU , let idτ *be the identity map on* S
F
|τ|
and let ι
# $\iota_{\tau}^{\mathcal{F}}:\mathbf{S}_{|\tau|}^{\mathcal{F}}\hookrightarrow\mathbf{V}$
|τ|
,→ V(F )
denote the inclusion map (which is adjoint to π
). Then, the Laplacian of A′•is
map (which is adjoint to $\pi_{\tau}^{\mathscr{F}}$). Then, the La_  $$L_{\mathbf{A}^{\prime}}=\sum_{\tau\in Q_{0}^{\mathscr{F}}}\left[\operatorname{id}_{\sigma}-\pi_{\sigma}^{\mathscr{F}}\iota_{\tau}^{\mathscr{F}}\pi_{\tau}^{\mathscr{F}}\iota_{\sigma}^{\mathscr{F}}\right]$$
$\downarrow$ . 
(2) *Let n be the total dimension of* NS,F
•. There exist positive constants C1 and C2, which depend only on A
S,F
- , such that the inequalities

$$C_{1}\cdot\lambda_{i}(\mathbf{N_{\bullet}^{S,\mathscr{F}}})\leq\lambda_{i}(\mathbf{A_{\bullet}^{\prime}})\leq C_{2}\cdot\lambda_{i+k}(\mathbf{N_{\bullet}^{S,\mathscr{F}}})$$  _hold for every $i$ in $\{1,2,\ldots,n\}$, with $k:=n-\dim\mathbf{S_{|\sigma|}^{\mathscr{F}}}$._
The full statement of this result is recorded in Theorem 7.1.

Finally, we examined a single-cell chromatin accessibility (ATAC-seq) dataset from
[28]; here X is a dataset consisting of around 3 × 104tumour-infiltrating T cells, while the input F consists of 20,000 binary-valued features X → R. To build a cover U of X,
we used a standard notion of genomic proximity between cells, constructed a 15-nearest neighbour graph, and expanded the communities of that graph by one hop. This produces a quiver QU with 87 vertices. We then ran the MACS2 peak-calling algorithm [39] to find the 1,000 most accessible regions for each admissible set and built a quiver Laplacian for a variant of the combined representation of S (as described in Theorem 7.2).

OBSERVATION (V). The first 3,000 eigenvectors of the quiver Laplacian described above had the following properties:
(1) *The majority of eigenvectors displayed a tight grouping of genomic positions (around 150* consecutive base-pairs out of approximately 3 billion) across the vertices.

(2) *Most eigenvectors were supported in most of the vector spaces assigned to vertices of the* quiver. In particular, one such eigenvector that was supported on every vertex, lay near the gene FAM72D, which is involved in the cell cycle and hence active for every type of T cell.

(3) Conversely, the support of a handful of eigenvectors was localised to a very small subset of vertices. One such eigenvector lay near the gene STAT3, which regulates Th1, Th17 and Treg cells; this eigenvector was supported on just 3 vertices, each of which corresponds to admissible subpopulations particularly rich in these three types of T cells.

Thus, eigenvectors of the quiver Laplacian were able to isolate relevant and consistent meta-features across different scales within the given dataset.

Outline. The paper is structured as follows: §2 describes how a feature selector together with a cover of the data yields a quiver representation. In §3 we describe both local and global compatibility of features with respect to the cover. We also describe how these features can be computed simultaneously as sections of a larger quiver representation. §4 introduces the quiver Laplacian and how its eigenvectors may be used to approximate the space of sections. §5 studies how a transformation of quiver representations relates the spectra of the respective representations and bounds their spectral distance. This then gives a stability of the spectrum of the representation associated to a feature selector. §6 bounds the changes in the spectrum of a quiver Laplacian when the underlying quiver undergoes various operations. §7 then uses these operations to simplify the computation of approximate sections of a feature selector. Finally, in §8 we use quiver Laplacians to extract (approximately) compatible peaks in single-cell chromatin accessibility data.

## Acknowledgements

OS is supported by Ludwig Cancer Research. VN and HAH are grateful for the support provided by the UK Centre for Topological Data Analysis EPSRC grant EP/R018472/1.

HAH gratefully acknowledges funding from the Royal Society. VN is partially supported by US AFOSR grant FA9550-22-1-0462. OS would like to thank Renee Hoekzema, Ka Man (Ambrose) Yim, Phil Xie, and Xin Lu for many helpful conversations. For the purpose of Open Access, the authors have applied a CC BY public copyright licence to any Author Accepted Manuscript (AAM) version arising from this submission.

## 2. From Feature Selection To Quiver Representations

Given a finite set X and a field K, let X
∗ be the K-vector space which consists of all functions X → K. Denote by Sub(X
∗) the collection of all subsets of X
∗(not necessarily subspaces), and for each such subset F write V(F ) to indicate the subspace of X
∗ given by the K-linear span of F. Let Grk(X
∗) be the Grassmannian of k-dimensional subspaces of X
∗for each k ≥ 0, and consider the disjoint union

$$\mathbf{Gr}_{\infty}(X^{*}):=\coprod_{k\geq0}\mathbf{Gr}_{k}(X^{*}).$$

Here is the main object of study in this work.

DEFINITION 2.1. A **feature selector** on X is any map S : Sub(X
∗) → Gr∞(X
∗), such that for each input F ⊂ X
∗, the corresponding output S
F
X
is a subspace of V(F ).

We now fix a feature selector S on X; readers may wish to keep the following concrete example in mind throughout the remainder of §2.

EXAMPLE 2.2. Among the most well-known and ubiquitous feature selectors is *principal components analysis* [19] - here,
- X is a finite origin-centered subset of some real Euclidean space Rn,
- K is the field R of real numbers, and
- F is the set {x *7→ ⟨*x, p⟩} of maps given by taking inner products with the unit vectors p.
For a fixed k ≪ n, the output S
F
Xis the vector space spanned by the k inner product functions (or equivalently, the k unit vectors) along which the variance in X is maximised.

Our goal here is to find a principled framework for relating the vector subspaces S
F
Y
to each other for a fixed F as Y ranges over subsets of X. Already for principal components analysis, it is clear that there need not be any coherent relationship between S
F
X
and S
F
Y
for arbitrary Y ⊂ X - for instance, neither one is guaranteed to be a subspace of the other within V(F ). It therefore becomes necessary to constrain the family of subsets under consideration. Here we will describe how to relate the subspaces S
F
Y
for Y ranging over the lattice of subsets generated from a chosen *cover* U of X. We recall that any such U is a finite collection of nonempty subsets satisfying X =SU∈U U.

DEFINITION 2.3. The **quiver associated to a cover** U of X is the directed graph QU
whose
(1) vertices are subsets σ ⊂ U whose *support* |σ| :=TU∈σ U is nonempty; and,
(2) there is a unique directed edge σ → τ whenever σ properly contains τ (and hence |σ*| ⊂ |*τ|).

We now re-assemble the algebraic data of S to produce a *representation* of QU , i.e.,
an assignment of vector spaces to vertices and linear maps to edges [29]. Implicit in the construction below is the choice of an inner product structure on X
∗, which allows us to define adjoints of linear maps, and hence, orthogonal projections onto subspaces.

For each vertex σ of QU , let ι F
σ: S
F
|σ|
,→ V(F ) denote the inclusion map and let π F
σ:
V(F ) ↠ S
F
|σ| denote its adjoint, i.e., the orthogonal projection in X
∗ with respect to our chosen inner product.

DEFINITION 2.4. For each subset F ⊂ X
∗, the **S-representation** of QU along F consists of the following assignments A• = A
S,F
- :
(1) every vertex σ of QU is assigned the vector space Aσ := S
F
|σ|
, which is a subspace of V(F ||σ|
) and hence3of V(F ); moreover,
(2) every edge σ → τ of QU is assigned the K-linear map Aσ→τ : Aσ → Aτ given by π F
τ ◦ ι F
σ.

It may be worth noting that the vertices of QU are simplices in the *nerve* of the cover U
[8], and every edge σ → τ in QU corresponds to a face relation (where the simplex τ lies in the boundary of the simplex σ). In particular, it follows from the definition of QU above that the existence of adjacent edges σ → τ → γ forces the existence of the edge σ → γ. We call A• a **sheaf** on the nerve of U if it satisfies the following *associativity criterion*: for every such pair of adjacent edges, the map Aσ→γ must equal the composite Aτ→γ ◦ Aσ→τ. In general, we do not expect this associative property to hold when A• arises from a feature selector. The next section contains our attempt to rectify this shortcoming.

## 3. Compatibility And Sections

Here we use the S-representation to define and study two notions of compatibility for a feature selector S on X against a cover U when invoked with input F ⊂ X
∗:
(1) Fix a vertex σ ∈ QU
0
. An element vσ ∈ A
S,F
σ is *locally compatible* with U if

$$\begin{array}{c}{{\tau\otimes\sigma}}\\ {{\iota_{\sigma}^{\mathcal{F}}(v_{\sigma})=\iota_{\tau}^{\mathcal{F}}\circ\mathbf{A}_{\sigma\to\tau}(v_{\sigma})}}\end{array}$$  by edge $\sigma\to\tau$ in $O_{1}$.  
holds for every edge σ → τ in Q1.

(2) A collection vσ ∈ Aσ | σ ∈ QU
0 Aσ→τ(vσ) = vτ
	is *globally compatible* with U if the equality

$$\mathrm{holds~for~every~edge}\;\sigma\rightarrow\tau\;\mathrm{in~}Q^{\mathcal{U}}.$$
This notion of local compatibility checks whether or not (the orthogonal projections of) a given feature vσ which has been selected by S over |σ| continue to be selected over all greater subsets |τ*| ⊃ |*σ| generated by the cover U . In this sense, local compatibility tests the robustness of selected features as we decrease the depth of the cover. Already for principal component analysis, it is clear that not every feature will be locally compatible, i.e., in general Aσ→τ has a non-trivial kernel. Global compatibility, on the other hand, tests features horizontally across the quiver - to be globally compatible, the vectors of a family {vσ} must map coherently onto each other under the linear maps of A• as we traverse zigzag paths in QU of the form σ1 → τ1 ← σ2 → τ2 *← · · · ←* σk → τk.



FIGURE 2. Example of different compatibility conditions.

We defer the study of local compatibility for now, and will focus on global compatibility.

3.1. Global Compatibility and Sections. Let Q = (s, t : Q1 → Q0) be a finite quiver and let A• be a representation of Q valued in the category **FdHilb**(K) of finite-dimensional Hilbert spaces over the field K ∈ {R, C}. The *total space* of A• is defined as the product

$$\operatorname{Tot}(\mathbf{A}_{\bullet}):=\prod_{i\in Q_{0}}\mathbf{A}_{i}.$$
$$(1)$$
Ai. (1)
Since Q is finite, Tot(A•) inherits a finite-dimensional Hilbert space structure from its Ai factors. Motivated by the global compatibility criterion from Definition 3.2, we highlight a relevant subspace of the total space below.

DEFINITION 3.1. A tuple γ := (γi ∈ Ai| i ∈ Q0) in Tot(A•) is called a **section** of A• if for every edge e in Q1 we have Ae(γs(e)
) = γt(e).

Sections of quiver representations were introduced in [30] along with an effective algorithm for their computation - see [30, Sec 5.2]. Sections are closely related to the compatibility criteria from Definition 3.2. In particular, if S is a feature selector on a set X, then the sections of A
S,F
- are exactly globally compatible features of S against the cover U . Sections can also be used to compute locally compatible features, as we will now describe.

## 3.2. Local Compatibility.

DEFINITION 3.2. A feature selector S on X is **locally compatible** with U on F ⊂ X
∗
if the following triangle of vector spaces commutes for each edge σ → τ of QU :

$$\mathbf{A}_{\sigma}^{\mathsf{S},\mathcal{F}}\xrightarrow{\qquad\mathbf{A}_{\sigma\to\tau}^{\mathsf{S},\mathcal{F}}}\mathbf{A}_{\tau}^{\mathsf{S},\mathcal{F}}$$
Equivalently, the identity $\iota_\nu^\mathcal{F}=\iota_\tau^\mathcal{F}\circ\pi_\tau^\mathcal{F}\circ\iota_\nu^\mathcal{F}$ holds for every edge $\sigma\to\tau$ of $Q^\mathcal{U}$. 
It will be useful to rephrase this compatibility condition entirely within the realm of quiver representations by blowing up the above triangle to a square. To this end, we introduce another representation C• = C
F
- of QU which may be associated to every F ⊂
X
∗(and which does not depend on S). This *constant representation* assigns Cσ := V(F )
to every vertex σ and the identity map to each edge σ → τ. For each vertex σ, there is an evident inclusion map ι F
σ: A
S,F
σ,→ C
F
σ, since the codomain is V(F ) and the domain is its subspace S
F
|σ|
. Now, for every edge σ → τ we have a diagram of four linear maps:



$$\quad(2)$$. 
The vertical maps ι F prescribe a *morphism of quiver representations* from A
S,F
- to C
F
•if and only if the above diagram commutes for every edge σ → τ in QU . By definition of C
F
•, the bottom edge of this diagram is precisely V(F )=−→ V(F ), so this square is an elementary modification of the triangle from Definition 3.2. Thus, we have arrived at the following straightforward result.

PROPOSITION 3.3. The feature selector S *is locally compatible with* U on F ⊂ X
∗if and only if the collection of maps

$$\left\{\iota_{\sigma}^{\mathcal{F}}:\mathbf{A}_{\sigma}^{\mathbf{S},\mathcal{F}}\hookrightarrow\mathbf{C}_{\sigma}^{\mathcal{F}}\right\}$$

indexed by vertices σ of QU *prescribe a morphism of quiver representations* A
S,F
- → C
F
•.

As described earlier, a morphism τ between quiver representations A• and A′•is a collection

$$\tau=\left\{\tau_{v}:\mathbf{A}_{v}\to\mathbf{A}_{v}^{\prime}\mid v\in Q_{0}\right\}$$

of linear maps τv such that
$$\mathbf{A}_{e}^{\prime}\circ\tau_{s(e)}=\tau_{t(e)}\circ\mathbf{A}_{t(e)}$$
e ◦ τs(e) = τt(e) ◦ At(e)(3)
for each edge e ∈ Q1. The commutivity condition in (3) can be too strong for quiver
representations obtained from data, so we will define a *transformation* τ between quiver
representations as a collection of linear maps
$\mathbf{s},\mathcal{R}$
$$\tau=\left\{\tau_{v}:\mathbf{A}_{v}\to\mathbf{A}_{v}^{\prime}\mid v\in Q_{0}\right\}$$
without the commutivity condition.

DEFINITION 3.4. Let Q be a quiver. For each vertex u ∈ Q0 define the **floret** of based at u to be the following quiver F
Q,u:
(1) the set of vertices is the disjoint union F
Q,u 0 = {u} ⊔ {ve| (e : u → v) ∈ Q1} .

In other words, there is a distinguished copy of u, which we label u0 henceforth, and an additional object denoted ve for every edge in Q1 from u to v.

(2) Define the set of edges of F
Q,u as F
Q,u 1 = {eLD,eDL : u0 → ve| (e : u → v) ∈ Q1} .

In other words, for each edge e : u → v in Q there are two distinct edges eLD and eDL from u0 to vein F
Q,u.

Now suppose A• and A′• are representations of the quiver Q with a transformation τ :
A• → A′•. Define the following representation F
τ,u
- of F
Q,u:

$$\begin{array}{l}{{\mathbf{F}_{u_{0}}^{\tau,u}=\mathbf{A}_{u}}}\\ {{\mathbf{F}_{e_{L D}}^{\tau,u}=\mathbf{A}_{e}^{\prime}\circ\tau_{u}}}\end{array}$$

u0 = Au F
e ◦ τu F
$$\begin{array}{l}{{\mathbf{F}_{v_{e}}^{\tau,u}=\mathbf{A}_{v}^{\prime}}}\\ {{\mathbf{F}_{e_{D L}}^{\tau,u}=\tau_{t(e)}\circ\mathbf{A}_{e}.}}\end{array}$$

See Figure 3.4 for an illustration.

Constructing the floret now allows us to compute locally compatible features: in the case where the transformation is ι F : A
S,F
- → C
F
- as in Proposition 3.3, the sections Γ(F
ιF σ
•) are exactly the locally compatible features at σ.

The representation F
τ,u
•



Q,u
3.3. Bicompatible features. In Section 4 below, we will consider the problem of discovering features which satisfy approximate versions of the local and global compatibility criteria. For this purpose, it will be helpful to construct a single quiver whose sections correspond to features which are both locally and globally compatible. The first step in this construction is a method for gluing quivers and their representations. Let Q = (s, t : Q1 → Q0) and Q′ = (s
′, t
′: Q′1 → Q′0
) be two quivers.

DEFINITION 3.5. For each subset R ⊂ Q0 × Q′0
, let Q ∪R Q′ be the **merged quiver**
whose
(1) vertex set is the quotient V := (Q0 ⊔ Q′0
)/R,
(2) edge set is the disjoint union E := Q1 ⊔ Q′1
,
and source/target maps are given as follows. Let ρ be the composite Q0 ,→ Q0 ⊔ Q′0 ↠ V,
and define ρ
′: Q′0 → V similarly. If e ∈ E lies in Q1, then its source and target vertices are ρ ◦ s(e) and ρ ◦ t(e); and if e lies in Q′1
, then its source and target vertices are ρ
′ ◦ s
′(e) and ρ
′ ◦ t
′(e) respectively.

Fix representations A• of a quiver Q and A′• of another quiver Q′.

DEFINITION 3.6. Let R ⊂ Q0 × Q′0 be any subset for which we have Ai = A′j whenever
(i, j) lies in R. The **merged representation** of A• and A′•, denoted (A ∪R A′)•, is the following representation of Q ∪R Q′. To vertices, it assigns

$$(\mathbf{A}\cup_{R}\mathbf{A}^{\prime})_{i}:={\begin{cases}\mathbf{A}_{i}\\ \mathbf{A}_{i}^{\prime}\\ \mathbf{A}_{i}=\mathbf{A}_{j}^{\prime}\\ \mathbf{A}_{j}=\mathbf{A}_{i}^{\prime}\end{cases}}$$

ii ∈ Q′0
$$\begin{array}{l}{{i\in Q_{0}\;\mathrm{and}\;(i,j)\notin R\;\mathrm{for}\;\mathrm{any}\;j\in Q_{0}^{\prime}}}\\ {{i\in Q_{0}^{\prime}\;\mathrm{and}\;(j,i)\notin R\;\mathrm{for}\;\mathrm{any}\;j\in Q_{0}}}\\ {{\mathrm{if}\;(i,j)\in R}}\\ {{\mathrm{if}\;(j,i)\in R}}\end{array}$$
Ai = A′jif (i, j) ∈ R
And on edges, we have

$$(\mathbf{A}\cup_{R}\mathbf{A}^{\prime})_{e}:={\begin{cases}\mathbf{A}_{e}&{{\mathrm{if~}}e\in Q_{1},}\\ \mathbf{A}_{e}^{\prime}&{{\mathrm{if~}}e\in Q_{1}^{\prime}.}\end{cases}}$$

One may embed both Tot(A•) and Tot(A′•
) within the total space of the merged representation in the natural way, and it is readily seen that the space of sections of (A ∪R A′)•



is (isomorphic to) the intersection Γ(A•) ∩ Γ(A′•
).

Returning to the case of interest, let S be a feature selector on a finite set X; consider a cover U of X and a subset F ⊂ X
∗. Let QbU be the quiver given by the disjoint union of florets I σindexed by vertices σ ∈ QU
0
, and let Ab S,F
- be the representation of QbU given by the floret functors Bσ. We define R ⊂ (QU )0 × QbU
0as the collection

$$R:=\left\{(\sigma,\sigma_{0})\mid\sigma\in Q_{0}^{\mathcal{U}}\right\},$$

where σ0 is the central vertex of I σ.

DEFINITION 3.7. The **combined S-representation** (of QU ∪R QbU , along F) is the merged representation NS,F
•:=
AS,F ∪R Ab S,F•
.

By design, the sections of NS,F
•correspond to relevant features which are both locally and globally compatible with U . We call these sections the **bicompatible features** of S.

EXAMPLE 3.8. Suppose U = {U1, U2} is a cover of X, such that U1 ∩ U2 ̸= ∅. Define τ1 = {U1} , τ2 = {U2} and σ = {U1, U2}. The quiver QU is

$$\mathbf{\partial}=\mathbf{\partial}\sigma\mathbf{\partial}.$$
τ1 σ τ2.
Consider a bicompatible feature, i.e., a section x ∈ Γ(NS,F
•). By definition, we have ι F
τ2
(xτ2
) = ι F
σ
(xσ) = ι F
τ1
(xτ1
), hence Γ(NS,F
•) ∼= ι F (S
F
|τ1|
) ∩ ι F (S
F
|σ|
) ∩ ι F (S
F
|τ2|
).

Thus, bicompatible features are the ones which are relevant for every U ∈ U .

3.4. Dual Representations. If one is also interested in features which are relevant for some - but not all - U ∈ U , then it becomes necessary to consider a different notion of bicompatibility. Given a quiver Q = (s, t : Q1 → Q0), its *dual Q*∗is the quiver with the same vertices and edges but with source and target maps interchanged, i.e., s
∗:=
t and t
∗:= s. Every representation A• of Q valued in **FdHilb**(K) induces a unique dual representation A∗• of Q∗, which is obtained by taking the adjoint of every edge map:
namely, (A∗)e:= (Ae)
∗for each e ∈ Q1.

When A• is the S-representation (from Definition 2.4) of a feature selector S• along some input F, the fact that ι F
σ and π F
σform an adjoint pair for each vertex σ ∈ QU
0 implies that for every edge σ → τ in QU , we have
(A
S,F )
∗
τ→σ = (π F
τ ◦ ι F
σ
)
∗ = π F
σ ◦ ι F
τ.

DEFINITION 3.9. The **mixed S-representation** (of (QU )
∗ ∪R QbU , along F) is the merged representation MS,F
•:=
(AS,F )
∗ ∪R Ab S,F•
.

Let us revisit Example 3.8 with a view towards understanding the sections of MS,F
•.

These sections are given by the direct sum Γ(MS,F
•) ∼= (ιτ1
(S
F
|τ1|
) ∩ ισ(S
F
|σ|
)
⊥) ⊕ (ιτ2
(S
F
|τ2|
) ∩ ισ(S
F
|σ|
)
⊥) ⊕ Γ(NS,F
•).

In this case, ιτ1
(S
F
|τ1|
) ∩ ισ(S
F
|σ|
)
⊥ corresponds to features that are relevant to U1 but not to U1 ∩ U2. Note that
(ιτ1
(S
F
|τ1|
) ∩ ισ(S
F
|σ|
)
⊥) ∩ (ιτ2
(S
F
|τ2|
) ∩ ισ(S
F
|σ|
)
⊥)
might not be trivial, i.e. there could be a feature relevant to both U1 and U2 but not to U1 ∩ U2, and hence this feature corresponds to two independent sections.

## 4. The Quiver Laplacian And Approximate Sections

So far, we have reframed compatibility-testing of feature selectors in terms of finding the sections of a quiver representation. However, the space of sections might be trivial [30, Sec 5.1]. Rather than seeking exact solutions, we endeavour to find approximate sections.

4.1. The Quiver Laplacian. Let **FdHilb**(K) denote the category of finite-dimensional Hilbert spaces over the field K ∈ {R, C}; every morphism A : U → V in this category admits an *adjoint* morphism A
∗: V → U characterised by ⟨Au, v⟩ = ⟨u, A
∗v⟩ for all (u, v)
in U × V. Here we fix a finite quiver Q = (s, t : Q1 → Q0) and consider a representation A• of Q valued in **FdHilb**(K). We recall the total space from (1) and define *target space* of A• as the direct product

$$\operatorname{Tar}(\mathbf{A}_{\bullet}):=\prod_{e\in Q_{1}}\mathbf{A}_{t(e)}.$$

Since we have assumed that Q is finite, both these spaces inherit a Hilbert space structure from the individual factors of the form Av. We will denote the identity map on Av by idv rather than idAv
.

DEFINITION 4.1. Given an **FdHilb**(K)-valued quiver representation A• of Q, its **boundary operator**
BA : Tot(A•) −→ Tar(A•)
is the linear map given in component form by

$$(B_{\mathbf{A}})_{e,v}={\begin{cases}\mathbf{A}_{e}-\operatorname{id}_{v}&{{\mathrm{if}}\,s(e)=t(e)=v,}\\ \mathbf{A}_{e}&{{\mathrm{if}}\,s(e)=v{\mathrm{~and~}}t(e)\neq v,}\\ -\operatorname{id}_{v}&{{\mathrm{if}}\,s(e)\neq v{\mathrm{~and~}}t(e)=v,}\\ \mathbf{0}&{{\mathrm{otherwise.}}}\end{cases}}$$

If the quiver Q is finite, then it follows from a simple calculation that ker BA is isomorphic (as a Hilbert space) to the space Γ(Q; A•) of A•'s sections. From the boundary operator of a quiver representation, we can construct another associated operator, the Laplacian, which will allow us to compute approximate sections.

DEFINITION 4.2. The **Laplacian** of A• is the endomorphism LA : Tot(A•) → Tot(A•)
given by

$${\cal L}_{\bf A}=B_{\bf A}^{*}B_{\bf A}.$$

In component form, we have

$$(L_{\mathbf{A}})_{v,v}=\sum_{\begin{subarray}{c}e\in Q_{1}\\ s(e)=v\end{subarray}}\mathbf{A}_{e}^{*}\mathbf{A}_{e}+\sum_{\begin{subarray}{c}e\in Q_{1}\\ t(e)=v\end{subarray}}\mathrm{id}_{v}-\sum_{\begin{subarray}{c}e\in Q_{1}\\ s(e)=t(e)=v\end{subarray}}[\mathbf{A}_{e}^{*}+\mathbf{A}_{e}]$$  and for $u\neq v$  $$(L_{\mathbf{A}})_{u,v}=-\sum_{\begin{subarray}{c}e\in Q_{1}\\ s(e)=u\\ t(e)=v\end{subarray}}\mathbf{A}_{e}^{*}-\sum_{\begin{subarray}{c}e\in Q_{1}\\ s(e)=v\\ t(e)=u\end{subarray}}\mathbf{A}_{e}.$$

Since ker LA = ker BA, the kernel of LA also computes the sections of A•. The main advantage of considering LA rather than BA in this context is that it is a Hermitian and positive semi-definite matrix. As such, it enjoys favourable spectral properties; in particular, all of its eigenvalues are all real and non-negative. We shall order these eigenvalues in increasing fashion, with multiplicity:

$$\lambda_{1}(L_{\mathbf{A}})\leq\cdots\leq\lambda_{n}(L_{\mathbf{A}})$$

where n := dim Tot(A•). If φ : A1• → A2•is an isomorphism of quiver representations with each φv a unitary map then

$${\cal L}_{\mathbf{A}^{1}}=\Phi\circ{\cal L}_{\mathbf{A}^{2}}\circ\Phi^{*},$$

where Φ = ∏v∈Q0 φv, thus we may speak unambiguously of the eigenvalues λi(A•) :=
λi(LA) of a quiver representation A•.

4.2. Approximate Sections. To measure the distance in Tot(A•) between an arbitrary vector x and the space Γ(A•) of sections, we consider the **Dirichlet energy**:

$${\mathcal{E}}_{\mathbf{A}}(x):=\langle x,L_{\mathbf{A}}x\rangle=\sum_{e\in Q_{1}}\|\mathbf{A}_{e}(x_{s(e)})-x_{t(e)}\|_{\mathbf{A}_{t(e)}}^{2}\in\mathbb{R}_{\geq0}$$

Here ⟨−, −⟩ is the induced inner product on Tot(A•), while and xv denotes the component of x in Av, and *∥ − ∥* denotes the norm induced by the inner product. As LA
is Hermitian, we can form an orthonormal eigenbasis e1, . . . ,en where ei corresponds to λi(A•). Writing x in this basis, we have

$${\mathcal{E}}_{\mathbf{A}}(x)={\mathcal{E}}_{\mathbf{A}}\left(\sum_{i}x_{i}e_{i}\right)=\sum_{i}\lambda_{i}(\mathbf{A}_{\bullet})x_{i}^{2}.$$
$=\;\sqrt{1+(1+x)^2}$
Thus, pEA(x) is the λ•-weighted distance from x to Γ(A•); and moreover,

$$\sum_{i:\lambda_{i}(\mathbf{A})=0}x_{i}e_{i}$$

is the closest vector to x in Γ(A•). This motivates the following definition. (A similar notion for cellular sheaves was introduced in [20]).

DEFINITION 4.3. For a quiver Q and an **FdHilb**(K)-valued representation A• of Q,
and ε*-approximate section* of A• is an x ∈ Tot(A•) such that ∥x∥ = 1 and EA(x) ≤ ε.

By Theorem B.1, if x ∈ span{e1, . . . ,ek} and ∥x∥ = 1, then x is a λk-approximate section.

Note this is not exhaustive: there can exist λk-approximate sections of A• that are not in the span of the first k eigenvectors, e.g. λ1x1e1 + λk+1xk+1ek+1for small enough xk+1.

Regardless, to compute approximate sections of a quiver representation one can compute eigenvectors of LA with small eigenvalues. As we have connected approximate sections with the spectra of the quiver representation, we now want to understand how the spectra changes if we perturb the quiver representation (§5), or the underlying quiver (§6).

## 5. Spectral Stability Of Feature Selectors

Let Q be a quiver and suppose A• and Ab• are two representations of Q. Suppose τ is
a collection {(τv : Av → Abv) : v ∈ Q0} of linear maps. Define the *defect* of τ at an edge
e ∈ Q1 to be
$$\partial(\tau,e)=\left\|\widehat{\mathbf{A}}_{e}\tau_{s(e)}-\tau_{t(v)}\mathbf{A}_{e}\right\|\,,$$
Here, and henceforth, the expression *∥ − ∥* when applied to a linear map between Hilbert
spaces will always indicate the operator norm - for M : V → W, the norm ∥M∥ equals
the supremum of ∥Mx∥W over unit vectors x ∈ V. Now the *total defect* of τ is:
$$\partial(\tau)=\left(\sum_{e\in Q_{1}}\partial(\tau,e)^{2}\right)^{\frac{1}{2}}.$$  also if such as $\tau$ are such as $\tau$.  
The defect of τ is zero if and only if when τ prescribes a morphism of quiver representations. Given bases of Tot(A•) and Tot(Ab•), we view τ as a block diagonal matrix. Let τ
+ denote its Moore-Penrose pseudoinverse. The values ∥τ∥ and ∥τ
+∥ are unique up to unitary transforms of Tot(A•) and Tot(Ab•). Finally, we let

$$\kappa(\tau):=\|\tau\|\ \|\tau^{+}\|.$$

be the *generalised condition number* of τ.

We seek to describe how the existence of τ forces a relationship between the Laplacian spectra of A• and Ab•. The first step in this direction is the following lemma.

LEMMA 5.1. For a matrix τ*, if x* ∈ (ker τ)
⊥ *then*

$$\|\tau x\|\geq\|\tau^{+}\|^{-1}\|x\|.$$
$$\begin{array}{l}{\lceil\bot\rceil}\end{array}$$

PROOF. Let u1, . . . , um and v1, . . . , vn be left and right singular vectors of τ respectively.

Let x = ∑
n i=1 xivi. Then τx = ∑
min{n,m}
i=1σixiui, but as x ∈ ker τ
⊥ we have that xj = 0 when σj = 0 or j > min{m, n}. Thus

$$\|\tau x\|\geq\left\|\sum_{i=1}^{\min\{n,m\}}\sigma_{+}x_{i}u_{i}\right\|=\sigma_{+}\|x\|=\|\tau^{+}\|^{-1}\|x\|$$  where $\sigma_{+}$ is the smallest non-zero singular value of $\tau$.  
The next theorem describes how the existence of a transformation between quiver representations constrains their eigenvalues. In the statement below (and henceforth), we use null(f) as a shorthand for the dimension of the kernel of a linear map f : U → V of finite-dimensional Hilbert spaces.

THEOREM 5.2. Suppose A• and Ab• *are two representations of a quiver Q whose total spaces* have dimensions n and m respectively. Let τ = {τv : Av → Abv | v ∈ Q0} be a collection of linear maps, viewed as a single map Tot(A•) → Tot(Ab•)*. Set q* := null(τ); for every integer k such that 1 ≤ k ≤ n − *q, we have*

$$\lambda_{k}(\widehat{\mathbf{A}})\leq\kappa(\tau)^{2}\lambda_{k+q}(\mathbf{A})+\partial(\tau)\|\tau^{+}\|\left[2\kappa(\tau)\lambda_{k+q}(\mathbf{A})^{\frac{1}{2}}+\partial(\tau)\|\tau^{+}\|\right].$$

In particular, if τ is a morphism of quiver representations, then ∂(τ) *vanishes and hence*

$\hdots=\mathfrak{D}(-)$. 
$$\lambda_{k}(\mathbf{\hat{A}})\leq\kappa(\tau)^{2}\lambda_{k+q}(\mathbf{A}).$$
PROOF. Let x1, . . . , xn and y1, . . . , ym be eigenvectors of A• and Ab• respectively, ordered by increasing eigenvalue. Suppose k is an integer such that 1 ≤ k ≤ n − q. Let l = k + q and define Xl = span{x1, . . . , xl} and Y
k = span{yk, . . . , ym}. As l = k + q we have that dim τ(Xl) ≥ k thus dim τ(Xl) + dim Y
kis at least m + 1 hence τ(Xl) and Y
kintersect nontrivially. Thus there exists some non-zero y ∈ τ(Xl) ∩ Y
k, and as y ∈ Y
k, by Theorem B.1 it holds that

$$\lambda_{k}({\widehat{\mathbf{A}}})\leq{\frac{1}{\|y\|^{2}}}\sum_{e\in Q_{1}}\left\|{\widehat{\mathbf{A}}}_{e}y_{s(e)}-y_{t(e)}\right\|^{2}.$$

Now we shall bound the right-hand side of the above. Since y ∈ τ(Xl) there exists some x ∈ Xl ∩ (ker τ)
⊥ such that τx = y. Using Lemma 5.1 have that

$${\frac{1}{\|\tau x\|^{2}}}\sum_{e\in Q_{1}}\left\|{\hat{\mathbf{A}}}_{e}\tau_{s(e)}x_{s(e)}-\tau_{t(e)}x_{t(e)}\right\|^{2}\leq{\frac{\|\tau^{+}\|^{2}}{\|x\|^{2}}}\sum_{e\in Q_{1}}\left\|{\hat{\mathbf{A}}}_{e}\tau_{s(e)}x_{s(e)}-\tau_{t(e)}x_{t(e)}\right\|^{2}.$$

Then applying the triangle inquality gives us

1 ∥τx∥ 2 ∑ e∈Q1 Abeτs(e)xs(e) − τt(e)xt(e)  2 ≤ ∥τ +∥ 2 ∥x∥ 2 ∑ e∈Q1 τt(e)Aexs(e) − τt(e)xt(e)  2 + 2 ∥τ +∥ 2 ∥x∥ 2 ∑ e∈Q1 τt(e)Aexs(e) − τt(e)xt(e)  Abeτs(e)xs(e) − τt(e)Aexs(e)  + ∥τ +∥ 2 ∥x∥ 2 ∑ e∈Q1 Abeτs(e)xs(e) − τt(e)Aexs(e)  2
and then with the Cauchy-Schwarz inequality we have

$$\frac{1}{\|\tau x\|^{2}}\sum_{e\in Q_{1}}\left\|\widehat{\mathbf{A}}_{e}\tau_{s}(e)x_{s}(e)-\tau_{t(e)}x_{t(e)}\right\|^{2}$$ $$\leq\kappa(\tau)^{2}\frac{1}{\|x\|^{2}}\sum_{e\in Q_{1}}\left\|\mathbf{A}_{e}x_{s}(e)-\tau_{t(e)}x_{t(e)}\right\|^{2}$$ $$\qquad+\kappa(\tau)\|\tau^{+}\|\left[\frac{1}{\|x\|^{2}}\sum_{e\in Q_{1}}\left\|\mathbf{A}_{e}x_{s(e)}-\tau_{t(e)}x_{t(e)}\right\|^{2}\right]^{\frac{1}{2}}\partial(\tau)+\|\tau^{+}\|^{2}\partial(\tau)^{2}$$

and finally since x ∈ Xl, we may apply Theorem B.1 to obtain

$$\frac{1}{\left\|\tau x\right\|^{2}}\sum_{e\in Q_{1}}\left\|\widehat{\mathbf{A}}_{e}\,\tau_{s(e)}x_{s(e)}-\tau_{t(e)}x_{t(e)}\right\|^{2}$$ $$\leq\kappa(\tau)^{2}\lambda_{l}(\mathbf{A})+2\kappa(\tau)\left\|\tau^{+}\right\|\lambda_{l}(\mathbf{A})^{\frac{1}{2}}\partial(\tau)+\left\|\tau^{+}\right\|^{2}\partial(\tau)^{2}$$
$$\begin{array}{l}{\bigsqcup}\end{array}$$

completing the proof. □
We shall now describe how Theorem 5.2 gives us a bound on the spectral pseudometric between quiver representations. If the total spaces of A and Ab• have the same dimension, then we can directly compare the associated Laplacian spectra. Following [14], we use the Wasserstein metric to perform such comparisons in order to account for the case where total spaces have different dimensions.

DEFINITION 5.3. For each real number r ≥ 0, let B(Q,r) be the set of representations A• of Q which satisfy maxe∈Q1
∥Ae∥ ≤ r.

By design, if A• ∈ B(Q,r), then its eigenvalues are bounded by |Q1|(r + 1)
2.

Given a representation A• of Q with total dimension n, its *spectral measure* is

$$\mu_{\mathbf{A}}=\sum_{i=1}^{n}\delta_{\lambda_{i}(\mathbf{A})}$$

where δλi(A)is the Dirac measure concentrated at λi(A). Given two probability measures µ1, µ2 on R≥0, a *coupling* γ of µ1 and µ2 is any probability measure on R≥0 × R≥0 whose marginals on each factor are µ1 and µ2 respectively. Denote by Γ(µ1, µ2) the set of all such couplings. Then the Wasserstein p-metric between µ1 and µ2 is defined as

$$W_{p}(\mu_{1},\mu_{2})=\operatorname*{inf}_{\gamma\in\Gamma(\mu_{1},\mu_{2})}\left(\int_{\mathbb{R}_{\geq0}\times\mathbb{R}_{\geq0}}\|x-y\|^{p}\,\mathrm{d}\gamma(x,y)\right)^{\frac{1}{p}}$$

Adapting the proof of Theorem 6.3 in [14] we have the following:
THEOREM 5.4. Suppose A•, Ab• ∈ B(Q,r) with total dimensions n and m respectively, where n ≥ m. Suppose τ is a non-zero transformation from A• to Ab•*. If* rank(η) ≥ null(η
∗) *then*

$$W_{1}(\mu_{\bf A},\mu_{\hat{\bf A}})\leq C$$

where C depends on τ, *n and r. Moreover, if* ∥τ∥, ∥τ
+∥ ≤ 1 + ε and ∂(τ), ∂(τ
∗) ≤ ε *for some* ε > 0*, then we have*

$$\operatorname*{lim}_{\varepsilon\rightarrow0}C=\frac{2\,\mathrm{null}(\tau)+2\,\mathrm{null}(\tau^{*})}{n}|Q_{1}|(r+1)^{2},$$

which, if null(τ) + null(τ
∗) < n/2*, will be less than naïve bound of* |Q1|(r + 1)
2.

PROOF. Define cτ = null(τ) + null(τ
∗). We will now define a coupling γ between µA and µAb . For each positive integer p, let [p] denote the set {1, 2, . . . , p − 1, p}. Setting ℓ = null(τ
∗) and and u = n − null(τ), define the following partition of [n] × [m]:

$P_{1}=\{(i,i):i\in[u]\setminus[\ell]\}$  $P_{2}=\{(i,j):i\in[\ell]\text{and}j\in[\ell]\}$  $\cup\ \{(i,j):i\in[\ell]\text{and}j\in[m]\setminus[u]\}$  $\cup\ \{(i,j):i\in[n]\setminus[u]\text{and}j\in[\ell]\}$  $\cup\ \{(i,j):i\in[n]\setminus[u]\text{and}j\in[m]\setminus[u]\}$  $P_{3}=\{(i,j):i\in[\ell]\text{and}j\in[u]\setminus[\ell]\}$  $\cup\ \{(i,j):i\in[n]\setminus[u]\text{and}j\in[u]\setminus[\ell]\}$  $P_{4}=([n]\times[m])\setminus(P_{1}\cup P_{2}\cup P_{3})\,.$
Now define the desired coupling γ as

$$\gamma=\sum_{\begin{array}{l}{{1\leq i\leq n}}\\ {{1\leq j\leq m}}\end{array}}w_{i j}\delta_{(\lambda_{i}({\bf A}),\lambda_{j}(\widehat{\bf A}))}\qquad{\mathrm{~where~}}\qquad w_{i j}=\left\{\begin{array}{l}{{\frac{1}{n}}}\\ {{\frac{1}{m(n-c_{\tau})}}}\\ {{\left({\frac{1}{m}}-{\frac{1}{n}}\right)\,\frac{1}{n-c_{\tau}}}}\\ {{0}}\end{array}\right.$$
n(i, j) ∈ P1,
m(n−cτ)(i, j) ∈ P2,
0 (i, j) ∈ P4.
$$\begin{array}{l}{{(i,j)\in P_{1},}}\\ {{(i,j)\in P_{2},}}\\ {{(i,j)\in P_{3},}}\\ {{(i,j)\in P_{4}.}}\end{array}$$

Set R = |Q1|(r + 1)
2, which is an upper bound for the eigenvalues of A•. Then using Theorem 5.2 for τ and τ
∗ and substituting R gives us κ(τ)
−2λi−null(τ
∗)
(A•) − aτ
∗,R ≤ λi(Ab•) ≤ κ(τ)
2λi+null(τ)
(A•) + bτ,R
with the constants

$$\begin{array}{l}{{a_{\tau^{*},R}=2\kappa(\tau)^{-1}\|\tau^{+}\|\partial(\tau^{*})\sqrt{R}+\kappa(\tau)^{-2}\|\tau^{+}\|^{2}\partial(\tau^{*})^{2},\mathrm{~and}}}\\ {{b_{\tau,R}=2\kappa(\tau)\|\tau^{+}\|\partial(\tau)\sqrt{R}+\|\tau^{+}\|^{2}\partial(\tau)^{2}.}}\end{array}$$

Computing cost of γ gives us

$$W_{1}(\mu_{\mathbf{A}},\mu_{\widehat{\mathbf{A}}})\leq\frac{1}{n}\Bigg{[}\sum_{k=\text{null}(\tau^{*})+1}^{n-\text{null}(\tau)}|\lambda_{k}(\mathbf{A_{\bullet}})-\lambda_{k}(\widehat{\mathbf{A_{\bullet}}})|+c_{\tau}R\Bigg{]}$$ $$\leq\frac{1}{n}\Bigg{[}\sum_{k=\text{null}(\tau^{*})+1}^{n-\text{null}(\tau)}(\kappa(\tau)^{2}\lambda_{k+\text{null}(\tau)}(\mathbf{A_{\bullet}})-\kappa(\tau)^{-2}\lambda_{k-\text{null}(\tau^{*})}(\mathbf{A}))\Bigg{]}$$
$$+\,(n-c_{\tau})(a_{\tau^{*},R}+b_{\tau,R})+c_{\tau}R\,\Biggr]\,.$$

Rearranging the sum on the right side yields

$$\frac{1}{n}\left[c_{\tau K}(\tau)^{2}R+(n-2c_{\tau})(\kappa(\tau)^{2}-\kappa(\tau)^{-2})R+(n-c_{\tau})(a_{\tau^{+},R}+b_{\tau,R})+c_{\tau}R\right],$$  which is the desired C.  
Suppose A, B are a pair of orthogonal matrices with dimensions n × k and n × l respectively. Then the matrix A
∗B is an orthogonal projection img B → img A, where img A
denotes the image of A. Let the singular values of A
∗B be σ1, . . . , σr where r = min{k, l}.

Then the principal angles between img A and img B are defined by cos θi = σi and the Grassmannian metric between img A and img B as defined by [37] is

$$d_{\mathbf{Gr}_{\infty}}(\operatorname{img}A,\operatorname{img}B):=\left(\sum_{i=1}^{r}\theta_{i}^{2}\right)^{\frac{1}{2}}.$$

COROLLARY 5.5. *Suppose* S, T : Sub(X
∗) → Gr∞(X
∗) *are two feature selectors on X and* suppose U *is a cover of X and* F ⊂ X
∗*. Suppose that*

$$\operatorname*{max}_{\sigma\in Q_{0}^{\mathcal{U}}}d_{\mathbf{Gr}_{\infty}}(\mathbf{S}_{|\sigma|}^{\mathcal{F}},\mathbf{T}_{|\sigma|}^{\mathcal{F}})\leq\varepsilon<\frac{\pi}{2}$$
for some ε > 0, and define
$$c=\sum_{\sigma\in Q_{0}^{\mathcal{H}}}|\dim\mathbf{S}_{|\sigma|}^{\mathcal{F}}-\dim\mathbf{T}_{|\sigma|}^{\mathcal{F}}|.$$
$\mathbb{E}^1=-\mathbb{E}^{\mathbb{M}}$ (... 
Then, W1(µAS,F , µAT,F ) *is no larger than*

$$\frac{4|Q_{1}|}{n}\bigg{[}(1\ +\ \cos^{2}\varepsilon)c\ +\ \left(2\sec\varepsilon\tan\varepsilon+(1+\sec^{2}\varepsilon)\tan^{2}\varepsilon+\sec^{2}\varepsilon-\cos^{2}\varepsilon\right)(n\ -\ c)\bigg{]}$$  _where $n=\max\{\dim\operatorname{Tot}(\mathbf{A_{\bullet}^{5,\mathscr{P}}}),\dim\operatorname{Tot}(\mathbf{A_{\bullet}^{7,\mathscr{P}}})\}$._
PROOF. Assume that dim S
F
- ≥ dim T
F
•. Define the transformation η with components ησ = π T
σι S
σ. Then cos ε ≤ ∥η∥ ≤ 1 and 1 ≤ ∥η
+∥ ≤ (cos ε)
−1. In order to bound ∂(η)
note that
∥ι S
σπ S
σ − ι T
σπ T
σ ∥2 = sin θσ,max ≤ sin ε, where θσ,max is the largest principal angle between S|σ| and T|σ|. This is known as the projection metric [37] where the equality can be seen from Theorem 2.6.1 in [13]. This then implies that, for each edge σ → τ, we have ∂(η, σ → τ) ≤ 2 sin ε thus ∂(η) ≤
2p|Q1| sin ε. Similarly, ∂(η
∗) ≤ 2p|Q1| sin ε. Applying Theorem 5.4 together with these bounds provide the result. □

## 6. Eigenvalue Inequalities For Quiver Operations

So far, we have described our problem as computing sections of a quiver representation. Here we seek to simplify the representation and the underlying quiver whilst preserving its space of sections and bounding the change in its eigenvalues. We will establish similar eigenvalue inequalities when the quiver itself is deformed via certain natural operations. The most convenient framework for extracting such inequalities is to upgrade the given quiver representation to a sheaf, as described below.

6.1. Sheaves over Quivers. Fix a quiver Q = (s, t : Q1 → Q0).

DEFINITION 6.1. An **FdHilb**(K)-valued **sheaf** A• over Q consists of:
- A finite-dimensional Hilbert space Av for each vertex v ∈ Q0,
- a finite-dimensional Hilbert space Ae for each edge e ∈ Q1, and
- for each for each edge e ∈ Q1, a pair of linear maps As(e)→e: As(e) → Ae and Ae←t(e): At(e) → Ae.

Such sheaves are closely related to representations of quivers. Every representation A• over Q induces a sheaf A• over Q by setting As(e)→e = Ae and Ae←t(e) = idt(e).

Conversely, every sheaf evidently induces a representation on the subdivision of Q where every edge e : u → v is decomposed into the zigzag u → e ← v. Thus, there is a natural notion of Laplacian for sheaves over a quiver, a special case4of which appears in [16].

4The only difference between our quiver sheaf Laplacian and the sheaf Laplacians of [16] over onedimensional cell complexes is that we allow edges to have the same source and target vertex. On the other hand, cellular sheaves and their Laplacians are also defined over regular cell complexes of dimension > 1.

DEFINITION 6.2. Suppose A• is a **FdHilb**(K)-valued sheaf over a quiver Q. Define Tot(A•) = ∏v∈Q0 Av and Tar(A•) = ∏e∈Q1 Ae.

(1) The **boundary operator** of A• is the linear map BA : Tot(A•) → Tar(A•) of A•
given in component form by

$$(B_{\mathcal{A}})_{e,v}=\left\{\begin{array}{l}{{\mathcal{A}_{v\to e}-\mathcal{A}_{e\gets v}}}\\ {{\mathcal{A}_{v\to e}}}\\ {{-\mathcal{A}_{e\leftarrow v}}}\\ {{0}}\end{array}\right.$$
$$\begin{array}{l}{{\mathrm{if~}s(e)=t(e)=v,}}\\ {{\mathrm{if~}s(e)=v\mathrm{~and~}t(e)\neq v,}}\\ {{\mathrm{if~}s(e)\neq v\mathrm{~and~}t(e)=v,}}\\ {{\mathrm{otherwise.}}}\end{array}$$
Av→e − Ae←v if s(e) = t(e) = v,
Av→eif s(e) = v and t(e) ̸= v,
−Ae←v if s(e) ̸= v and t(e) = v,
0 otherwise.
(2) The **Laplacian** of A• is then defined as LA = B
∗
A BA .

(3) Finally, the **Dirichlet energy** for A is the function EA : Tot(A•) → R given by

$${\mathcal{E}}_{{\mathcal{A}}}(x)=\sum_{e\in Q_{1}}\left\|{\mathcal{A}}_{s(e)\to e}(x_{s(e)})-{\mathcal{A}}_{e\gets t(e)}(x_{t(e)})\right\|_{{\mathcal{A}}_{e}}^{2}.$$

If one constructs a sheaf A• from a quiver representation A• of Q as described above, then the sheaf boundary operator BA coincides exactly with the quiver boundary operator BA; therefore the Laplacians of A and A , as well as their spectra, also coincide in this case.

6.2. Operations on the Quiver. This section describes how the spectrum of a sheaf, or indeed a representation, over a quiver changes under various combinatorial operations on the quiver. Removing an edge or a vertex gives bounds on the change in spectrum, as Proposition A.1 describes, however these may reduce the dimension of the space of sections. Propositions 6.5, 6.7, and 6.9 describe operations on the quiver, dependent on the sheaf, that preserve the space of sections. These are described for sheaves over a quiver but all these operations also preserve quiver representations. These intermediate results are used to simplify quivers (while bounding the change in eigenvalues) in our Proofs of Theorems 7.1 and 7.2.

DEFINITION 6.3. For a quiver Q, define an *edge pairing* as a collection P of pairs of distinct neighbouring edges (e 1 1
,e 1 2
), . . .(e m 1
,e m 2
) of Q such no two edges are repeated, i.e.

e i j
̸= e k l unless i = k and j = l. To simplify notation assume that each pair (e i 1
,e i 2
), the edges e i 1 and e i 2 are directed away from their common vertex u i. Label the other vertices for e i 1 and e i 2
, possibly the same vertex, as v i and w irespectively.



We then define QP as the *P-homotopic quiver* to Q where QP has the same nodes and edges as Q except with each edge e i 2 replaced by an edge e i 3 between v i and w i.



$$\bullet^{w^{i}}$$

For A• is a sheaf over Q and a pairing P of Q, say that A• is compatible with P if for each pair (e i 1
,e i 2
) ∈ P we have that Ae i 1
= Ae i 2 and Au i→e i 1
= Au i→e i 2
. Such a compatible sheaf induces a sheaf on QP as follows: define the sheaf A P
- on QP as the same as A•

```
on the common edges of Q and QP and otherwise by A P
                                                 e
                                                  i
                                                  3
                                                    = Ae
                                                        i
                                                        2
                                                         , A P
                                                            e
                                                            i
                                                            3←e
                                                               i
                                                               3
                                                                 = Ae
                                                                     i
                                                                     1←e
                                                                        i
                                                                        1
                                                                          and

```

A P
wi→e i 3
= Ae i 2←wi for each i. The next proposition shows the i-th eigenvalue of A P
•is bounded by a scalar multiple of the i-th eigenvalue of A•. First we will need a lemma.

LEMMA 6.4. Suppose X,Y, Z ∈ Rn*. Then*

$$\|X-Z\|^{2}+\|Z-Y\|^{2}\leq\varphi^{2}(\|X-Y\|^{2}+\|Y-Z\|^{2})$$
$1+\sqrt{5}$ . 
where φ *is the golden ratio* φ =
1+
√
5 2. This is also true for any metric space (M, d) *and can be* written as

$$d(X,Z)^{2}\leq\varphi^{2}d(X,Y)^{2}+\varphi d(Y,Z)^{2}.$$

PROOF. Let us abbreviate

$$x=\|Y-Z\|\qquad y=\|X-Z\|\qquad z=\|X-Y\|.$$

If any of x, y or z are zero, then the proposition is immediately true, so assume that x, y and z are strictly positive. By the triangle inequality, we have

$${\frac{x^{2}+y^{2}}{x^{2}+z^{2}}}\leq{\frac{x^{2}+(x+z)^{2}}{x^{2}+z^{2}}}.$$

We then want to know when the expression on the right side is maximised. As x, z > 0, there exists u > 0 for which x = uz. Substituting this into the right side gives

$${\frac{2u^{2}+2u+1}{u^{2}+1}},$$

which is maximised when u = φ. Thus, the maximum value of the ratio is φ 2. If X,Y, Z
are colinear with Y between X and Z and ∥Y − Z∥ = φ∥X − Y∥, then the maximum is attained, which shows that this inequality is sharp. □
PROPOSITION 6.5. For Q a quiver and P an edge pairing of Q, suppose that A• *is a sheaf on* Q compatible with P. Then the eigenvalues of A• and A P
•*are related by*

$$\varphi^{-2}\lambda_{j}(\mathcal{A}_{\bullet})\leq\lambda_{j}(\mathcal{A}_{\bullet}^{P})\leq\varphi^{2}\lambda_{j}(\mathcal{A}_{\bullet})$$

and vice-versa for j = 1, . . . , n where n is the total dimension of A•.

PROOF. Using Lemma 6.4 we have

EA (x) = ∑ (e i 1 ,e i 2 )∈P "Ae i 1←v ixv i − Au i→e i 1 xu i  2 Ae i 2 # Ae i 1 + Au i→e i 2 xu i − Ae i 2←wixwi  2 + ∑ unpaired e∈Q1 As(e)→exs(e) − Ae←t(e)xt(e)  2 As(e) ≤ φ 2 ∑ (e i 1 ,e i 2 )∈P "Au i→e i 1 xu i − Ae i 1←v ixv i  2 Ae i 3 # Ae i 1 + A P e i 3←v ixv i − A P wi→e i 3 xwi  2 + ∑ unpaired e∈Q1 As(e)→exs(e) − Ae←t(e)xt(e)  2 As(e) ≤ φ 2EA P (x).

Then by Theorem B.2

$$\lambda_{i}(\mathcal{A}_{\bullet})=\operatorname*{min}_{\dim V=i}\left[\operatorname*{max}_{x\in V\setminus0}{\frac{\mathcal{E}_{\mathcal{A}}(x)}{\langle x,x\rangle}}\right]\leq\operatorname*{min}_{\dim V=i}\left[\operatorname*{max}_{x\in V\setminus0}{\frac{\varphi^{2}\mathcal{E}_{\mathcal{A}}(x)}{\langle x,x\rangle}}\right]=\varphi^{2}\lambda_{i}(\mathcal{A}_{\bullet}^{p}).$$

proving the proposition. □
We note that Proposition 6.5 directly applies to graphs. Although we make no use of the following corollary, we hope that it will be of independent interest to spectral graph theorists.

COROLLARY 6.6. *Suppose G* = (V, E) *is a multigraph with n vertices. Suppose we have an* edge pairing P = (e 1 1
,e 1 2
), . . .(e m 1
,e m 2
) on G as in Definition 6.3. Let *G with the same nodes and* b edges as G except with each edge ei2 replaced by an edge ei3 between viand wi. Then the eigenvalues of LGb and LG *are related by*

$$\varphi^{-2}\lambda_{j}(L_{G})\leq\lambda_{j}(L_{\hat{G}})\leq\varphi^{2}\lambda_{j}(L_{G})$$

and vice-versa for j = 1, . . . , n.

PROPOSITION 6.7. Suppose A• is a sheaf over a quiver Q with total dimension n. Given a subquiver Q′, let A ′
- denote the restriction of A• *to Q*′.

6.7(a) If e ∈ Q1 *is an edge such that s*(e) = t(e) and As(e) = At(e) = id then λi(A ′
•
) =
λi(A•) *for i* = 1, . . . , *n where* A ′
•is A• restricted to the subquiver Q′of Q with the edge e removed.

6.7(b) *Suppose we have an edge pairing P* = (e 1 1
,e 1 2
), . . .(e m 1
,e m 2
) of Q such that for each i, the edges ei1
,e i 2 have the same source and target vertices. Assume that for each i, there exists a linear map Mi: Ae i 2
→ Ae i 1 satisfying both

$$\mathcal{A}_{s}(e_{1}^{i}){\rightarrow}e_{1}^{i}=M_{i}\mathcal{A}_{s}(e_{2}^{i}){\rightarrow}e_{2}^{i}\qquad\textit{and}\qquad\mathcal{A}_{e_{1}^{i}{\leftarrow}t}(e_{1}^{i})=M_{i}\mathcal{A}_{e_{2}^{i}{\leftarrow}t}(e_{2}^{i})$$

Let Q′*be the subquiver of Q with all the edges e*1 2
, . . . ,e n 2 removed, and let A ′
•be the restriction of A• to Q′*. Then, we have*

$$(1+\Gamma_{P})^{-1}\lambda_{i}(\mathcal{A}_{\bullet})\leq\lambda_{i}(\mathcal{A}_{\bullet}^{\prime})\leq\lambda_{i}(\mathcal{A}_{\bullet})$$
_for all $i=1,\ldots,n$, where $\Gamma_{P}:=\max_{i}\{\|M_{i}\|^{2}\}$._
PROOF. For 6.7(a), observe that EA (x) = EA ′(x) and thus the result follows from Theorem B.2. For 6.7(b), we have

$$\mathcal{E}_{\mathcal{A}}(x)\leq\sum_{(e_{1}^{i},e_{2}^{i})\in P}(1+\|M_{i}\|^{2})\left\|\mathcal{A}_{s(e_{1}^{i})\to e_{1}^{i}}\mathcal{X}_{s(e_{1}^{i})}-\mathcal{A}_{e_{1}^{i}\to t(e_{1}^{i})}\mathcal{X}_{t(e_{1}^{i})}\right\|^{2}$$ $$+\sum_{\text{unpaired}e\in\mathbb{Q}_{1}}\left\|\mathcal{A}_{s(e)\to e}\mathcal{X}_{s(e)}-\mathcal{A}_{e\gets t(e)}\mathcal{X}_{t(e)}\right\|_{\mathcal{A}_{s(e)}}^{2}$$ $$\leq(1+\Gamma_{P})\mathcal{E}_{\mathcal{A}^{\prime}}(x).$$
$\boxed{\Box}$
and the result follows from Theorem B.2. □
In the following, at the risk of causing ambiguity with self-loops, we will ignore the direction of edges in and use the relation v ∼ e if either s(e) = v or t(e) = v.

DEFINITION 6.8. Let Q be a quiver and let V be a subset of vertices such that there are no edges in Q between vertices of V. The **V-reduced quiver** QV is defined as follows. For each vertex v ∈ V,
(1) first remove v and any associated edges from Q;
(2) then, for each pair of edges (p, q) in Q such that u ∼ p ∼ v ∼ q ∼ w for vertices u, w ∈ Q0 \ V, add a new edge pq between u and w.

(We note in the second step above that if u = w, then pq forms a self-loop.) The resulting quiver is the desired QV.

FIGURE 5. An example of the reduction of a quiver Q with V = {v}.



We now describe an analogue of the Kron reduction of a graph [7] for sheaves over a quiver. As discussed in [16], Kron reduction does not work in general for sheaves over a (loopless) graph. However, as the next proposition shows, if one restricts the type of vertex removed, dependent on the sheaf, and moreover allows for loops in the underlying quiver, then Kron reduction is possible.

PROPOSITION 6.9. Given a sheaf A• over a quiver Q, assume that V ⊂ Q0 *is a subset of* vertices such that there are no edges in Q between vertices of V. Further suppose that for each v ∈ V there exists some real number αv > 0 such that for each edge e ∼ *v, we have*

_either_ $\mathscr{A}_{v\to e}^{*}\mathscr{A}_{v\to e}=\alpha_{v}\mathrm{id}_{v}$ _or_ $\mathscr{A}_{e\gets v}^{*}\mathscr{A}_{e\gets v}=\alpha_{v}\mathrm{id}_{v}$
as appropriate. Then there exists a sheaf $\mathscr{A}_{\bullet}^{V}$ over $Q^{V}$ such that $\Gamma(\mathscr{A}_{\bullet}^{V})\cong\Gamma(\mathscr{A}_{\bullet})$ and 
$$\lambda_{i}(\mathcal{A}_{\bullet})\leq\lambda_{i}(\mathcal{A}_{\bullet}^{V})\leq\lambda_{i+r}(\mathcal{A}_{\bullet})$$
for i = 1, . . . , n − r where n is the total dimension of A• *and r* = ∑v∈V dim Av.

PROOF. Consider the Laplacian LA . It can be written in a block form as

$$y f\mathcal{A}_{\bullet}\,a n d\,r=\sum_{v\in V}\dim\mathcal{A}_{v}.$$
$$\begin{array}{c c c}{{}}&{{}}&{{Q_{0}\setminus V}}&{{V}}\\ {{L_{\mathcal A}=\left(\begin{array}{c c}{{}}&{{X}}&{{}}\\ {{Y}}&{{}}\end{array}\begin{array}{c c}{{Y^{*}}}\\ {{D}}\end{array}\right)Q_{0}\setminus V}}\\ {{}}&{{}}&{{}}\end{array}.$$

As there are no edges between vertices of V, D is a diagonal matrix where the (v, v) block is dvαvid where dv is the degree of v. Thus D is invertible, and we can form the Schur complement

$$L_{\mathcal{A}}/D:=X-Y^{*}D^{-1}Y.$$
$${\mathrm{A~vector}}\begin{bmatrix}x&z\end{bmatrix}^{T}{\mathrm{~satisfies~}}$$
$${\begin{bmatrix}X&Y^{\dagger}\\ Y&D\end{bmatrix}}{\begin{bmatrix}x\\ z\end{bmatrix}}={\begin{bmatrix}0\\ 0\end{bmatrix}}$$

if and only if Xx + Y
†z = 0 and Yx + Dz = 0. As D is invertible this can be rearranged to Xx − YD−1Y
†x = 0 hence ker(LA/D) ∼= ker LA. For the interlacing, we can directly apply Theorem B.5.

We will now define the sheaf A V
•. As in Definition 6.8, we will ignore orientation of the edges and write u ∼ e if either s(e) = v or t(e) = v and Av∼e for the corresponding assigned linear map. If p ̸= q, define A V
u∼pq = (dvαv)
−1/2A ∗
v∼pAu∼p and likewise for w.

Otherwise, if p = q, define A V
u→pp = ZpAu∼p and A V
pp←u = 0 for a linear map Zp which we will now define. First observe that for every non-zero vector x, we have

$$\frac{1}{\alpha_{v}}x^{*}{\mathcal{A}}_{v\sim p}{\mathcal{A}}_{v\sim p}^{*}x\leq\frac{1}{\alpha_{v}}\|{\mathcal{A}}_{v\sim p}^{*}\|^{2}\|x\|^{2}=\frac{1}{\alpha_{v}}\|{\mathcal{A}}_{v\sim p}^{*}{\mathcal{A}}_{v\sim p}\|\,\|x\|^{2}=\|x\|^{2}$$

thus there exists some Zp such that

$$\mathrm{id}-\frac{1}{\alpha_{v}}{\mathcal{A}}_{v\sim p}{\mathcal{A}}_{v\sim p}^{*}=Z_{p}^{*}Z_{p}.$$

since the left-hand side is positive semi-definite.

Now we claim that LA V = LA /D. To do so, consider vertices u ∈ Q0 \ V and v ∈ V.

For each edge u ∼ p ∼ v, the contribution to the diagonal block indexed by (u, u) of LA /D is

$$\mathcal{A}_{u\sim p}^{*}\mathcal{A}_{u\sim p}-\frac{1}{d_{v}\alpha_{v}}\sum_{u\sim q\sim v}\mathcal{A}_{u\sim p}^{*}\mathcal{A}_{v\sim p}\mathcal{A}_{v\sim q}^{*}\mathcal{A}_{u\sim q}.$$

We need to show this is equal to the contribution from the new edges of A
Q
- . For each vertex u ∈ Q0 \ V, the contribution to the diagonal block is

∑ v∈V ∑u∼p∼v " A ∗ u∼pAu∼p − 1 dvαv ∑u∼q∼v A ∗ u∼pAv∼pA ∗ v∼qAu∼q # = ∑ v∈V ∑u∼p∼v A ∗ u∼pAu∼p − d u v dvαv A ∗ u∼pAv∼pA ∗ v∼pAu∼p  1 dvαv (A ∗ v∼pAu∼p − A ∗ v∼qAu∼q) ∗(A ∗ v∼pAu∼p − A ∗ v∼qAu∼q)  + ∑u∼p∼v u∼q∼v p̸=q
where d u vis the number of edges between u and v. The term on the last line corresponds to the new self-loops on u given by v. By the defining property of Zp, the term

$$\sum_{u\sim p\sim v}\left[{\mathcal A}_{u\sim p}^{*}{\mathcal A}_{u\sim p}-\frac{d_{v}^{u}}{d_{v}\alpha_{v}}{\mathcal A}_{u\sim p}^{*}{\mathcal A}_{v\sim p}{\mathcal A}_{v\sim p}^{*}{\mathcal A}_{u\sim p}^{*}\right]$$

equals

$$\sum_{u\sim p\sim v}\left[{\frac{d_{v}-d_{v}^{u}}{d_{v}\alpha_{v}}}{\mathcal{A}}_{u\sim p}^{*}{\mathcal{A}}_{v\sim p}{\mathcal{A}}_{v\sim p}^{*}{\mathcal{A}}_{u\sim p}+{\mathcal{A}}_{u\sim p}^{*}Z_{p}^{*}Z_{p}{\mathcal{A}}_{u\sim p}\right]$$

and thus corresponds with the contribution of the self-loop pp and the new edges to different vertices, as required. □

## 7. Reduction Of The Feature Selector Problem

Using the quiver operations in §6, we can reduce the number of vertices in the quiver whilst preserving the space of sections; this allows us to reduce the difficulty of computing approximate sections.

THEOREM 7.1. Let S be a feature selector on X, U a cover of X such that QU *is (weakly) connected, and* F ⊂ X
∗*. Fix a vertex* σ0 ∈ QF
0
. Then there exists a quiver Q′*and a representation* A′•of Q′*satisfying the following properties:*
(1) The quiver Q′ *has only one vertex and* |QF
0 | *edges.*
(2) The Laplacian of A′•is:

$$\sum_{\tau\in Q_{0}^{\mathcal{H}}}\left[\mathrm{id}_{\sigma_{0}}-\pi_{\sigma_{0}}^{\mathcal{F}}\iota_{\tau}^{\mathcal{F}}\pi_{\tau}^{\mathcal{F}}\iota_{\sigma_{0}}^{\mathcal{F}}\right],$$

QUIVER LAPLACIANS AND FEATURE SELECTION 29
(3) There exist constants C1, C2 > 0 that depend on S, U and F *such that*

$$C_{1}\lambda_{i}({\bf N_{\bullet}^{S,\mathcal{F}}})\leq\lambda_{i}({\bf A_{\bullet}^{\prime}})\leq C_{2}\lambda_{i+k}({\bf N_{\bullet}^{S,\mathcal{F}}})$$

for i = 1, . . . , n − k.

Here n is the total dimension of NS,F
•*and k* := n − dim A
S,F
σ0.

PROOF. We view NS,F
- as a sheaf A• over a quiver Q, defined as follows:

$$\begin{array}{l}{{Q_{0}=\left\{v_{\sigma}:\sigma\in Q_{0}^{\mathcal{U}}\right\}\cup\left\{v_{\sigma\tau}:(\sigma\rightarrow\tau)\in Q_{1}^{\mathcal{U}}\right\},}}\\ {{Q_{1}=\left\{e_{\sigma\tau},r_{\sigma\tau}^{D L},r_{\sigma\tau}^{L D}:(\sigma\rightarrow\tau)\in Q_{1}^{\mathcal{U}}\right\},}}\\ {{s(e_{\sigma\tau})=v_{\sigma},\quad t(e_{\sigma\tau})=v_{\tau},}}\\ {{s(r_{\sigma\tau}^{D L})=s(r_{\sigma\tau}^{L D})=v_{\sigma},\quad t(r_{\sigma\tau}^{D L})=t(r_{\sigma\tau}^{L D})=v_{\sigma\tau}.}}\end{array}$$

This is precisely the merged quiver on which NS,F
•is defined, except that we have dispensed with identity self-loops in light of Proposition 6.7(a). The desired sheaf A• assigns the following data to vertices and edges of Q for each σ ∈ QU
0
:

$$\begin{array}{l l l}{{\mathcal{A}_{v_{\sigma}\to v_{e\tau}}=\pi_{\tau}^{\mathcal{F}}\circ\iota_{\sigma}^{\mathcal{F}},}}&{{\qquad\mathcal{A}_{v_{\sigma}\gets v_{\tau}}=\mathrm{id},}}&{{\qquad\mathcal{A}_{v_{\sigma}\to p_{\tau}^{\mathcal{F}}}=\iota_{\tau}^{\mathcal{F}}\circ\pi_{\tau}^{\mathcal{F}}\circ\iota_{\sigma}^{\mathcal{F}},}}\\ {{\mathcal{A}_{p_{\tau}^{\mathcal{F}}\gets v_{\tau}}=\mathrm{id},}}&{{\qquad\qquad\mathcal{A}_{v_{\sigma}\to p_{\tau}^{\mathcal{F}}}=\iota_{\sigma}^{\mathcal{F}},}}&{{\qquad\mathcal{A}_{p_{\tau}^{\mathcal{F}}\gets v_{\tau}}=\mathrm{id}.}}\end{array}$$

Use Proposition 6.7(b) to get a new copy e 2στ of the edge eστ with the maps multiplied by ι F
τ. Use this edge with Proposition 6.5 to move the edge r DL
στ to an edge between vτ and vστ, then using the edge r LD
στ with Proposition 6.5 move this edge between vτ and vστ to an edge between vσ and vτ which has maps ισ and ιτ respectively. Call this edge pστ. Using Proposition 6.7(b) can remove both eστ and e 2στ since π F
τis the left inverse of ι F
τ. Finally, we can remove the edge r LD
στ with Proposition 6.9 as (ι F
σ
)
∗ι F
σ = id. Now choose some vertex σ0. As the nerve is connected, and each edge from each vertex has the same restriction maps to that vertex we can keep applying Proposition 6.5 until all edges have σ0 as a boundary. There might be double edges, but these can be removed with Proposition 6.7(b). Then we apply Proposition 6.9 to reduce to just the vertex σ0.

The Laplacian is now

$$\sum_{\tau\in Q_{0}^{\mathcal{H}}}\left[\mathrm{id}_{\sigma_{0}}-\pi_{\sigma_{0}}^{\mathcal{F}}\iota_{\tau}^{\mathcal{F}}\pi_{\tau}^{\mathcal{F}}\iota_{\sigma_{0}}^{\mathcal{F}}\right]$$

and the eigenvalue relationship follows by tracking all the uses of Propositions 6.7(a),
6.7(b), 6.5, 6.9. □
THEOREM 7.2. Let S be a feature selector on a set X equipped with a cover U *. For each subset* F ⊂ X
∗, here exists a sheaf A ′over a quiver Q′ *with Laplacian*

$$(L_{\mathcal{A}^{\prime}})_{\sigma,\tau}=\begin{cases}\sum_{\tau\subset\sigma}\left(2\mathrm{id}_{\sigma}-\pi_{\sigma}^{\mathcal{F}}t_{\tau}^{\mathcal{F}}\pi_{\tau}^{\mathcal{F}}t_{\sigma}^{\mathcal{F}}\right)+\sum_{\sigma\subset\gamma}\pi_{\sigma}^{\mathcal{F}}t_{\gamma}^{\mathcal{F}}\pi_{\tau}^{\mathcal{F}}t_{\sigma}^{\mathcal{F}}&\text{if$\sigma=\tau$,}\\ -\pi_{\sigma}^{\mathcal{F}}t_{\tau}^{\mathcal{F}}&\text{if$\tau\subset\sigma$or$\sigma\subset\tau$,}\\ 0&\text{otherwise.}\end{cases}$$

30 OTTO SUMRAY, HEATHER A. HARRINGTON, VIDIT NANDA
such that there is an isomorphism Γ(A ′
•
) ∼= Γ(MS,F
•)*; and moreover, we have*

$$\lambda_{i}({\bf M_{\bullet}^{S,\mathcal{F}}})\leq\lambda_{i}(\mathcal{A}_{\bullet}^{\prime})\leq\lambda_{i+k}({\bf N_{\bullet}^{S,\mathcal{F}}})$$

for all i ∈ {1, . . . , n − k}*. Here* MS,F
•is the mixed representation of Definition 3.9, while n is its total dimension and k := n − ∑σ∈Q0 dim A
S,F
σ .

PROOF. Consider the representation (A
S,F
- )
∗ ⊔R Ab S,F
- as defined in Definition 3.9, and view it as a sheaf A• over a quiver Q. We can immediately remove identity self-loops using Proposition 6.7(a). The quiver Q is as follows:

$$\begin{array}{l}{{Q_{0}=\left\{v_{\sigma}:\sigma\in Q_{0}^{\mathcal{U}}\right\}\cup\left\{v_{\sigma\tau}:(\sigma\to\tau)\in Q_{1}^{\mathcal{U}}\right\},}}\\ {{Q_{1}=\left\{e_{\sigma\tau},r_{\sigma\tau}^{D L},r_{\sigma\tau}^{L D}:(\sigma\to\tau)\in Q_{1}^{\mathcal{U}}\right\},}}\\ {{s(e_{\sigma\tau})=v_{\tau},\quad t(e_{\sigma\tau})=v_{\sigma},}}\\ {{s(r_{\sigma\tau}^{D L})=s(r_{\sigma\tau}^{L D})=v_{\sigma},\quad t(r_{\sigma\tau}^{D L})=t(r_{\sigma\tau}^{L D})=v_{\sigma\tau}.}}\end{array}$$
$$\in Q^{\mathcal{U}}.$$

The sheaf A• consists of the following for each σ ∈ QU :

$$\begin{array}{l l}{{\mathcal{A}_{v_{\tau}\to e_{\sigma\tau}}=\pi_{\sigma}^{\mathcal{F}}\circ\iota_{\tau}^{\mathcal{F}},}}&{{\mathcal{A}_{e_{\sigma\tau}\gets v_{\sigma}}=\mathrm{id},}}\\ {{\mathcal{A}_{v_{\sigma}\to r_{\sigma}^{D L}}=\iota_{\tau}^{\mathcal{F}}\circ\pi_{\tau}^{\mathcal{F}}\circ\iota_{\sigma}^{\mathcal{F}},}}&{{\mathcal{A}_{r_{\sigma}^{D L}\gets v_{\sigma}}=\mathrm{id},}}\\ {{\mathcal{A}_{v_{\sigma}\to r_{\tau}^{L D}}=\iota_{\sigma}^{\mathcal{F}},}}&{{\mathcal{A}_{r_{\sigma}^{D L}\gets v_{\sigma}}=\mathrm{id}.}}\end{array}$$

We can use Proposition 6.9 to remove each vστ. In doing so, we add three new self-loops to vσ; two identities and a self loop with maps ι F
σ and ι F
τ ◦ π F
τ ◦ ι F
σ. The two identity self loops can be removed with Proposition 6.7(a). □
7.1. Remarks on computation. In Theorems 7.1 and 7.2, we have assumed that L is Hermitian with respect to some orthonormal basis. Often, however, the bases we would prefer to use are not orthogonal with respect to our chosen inner product. We will see such an example in §8, where computing inner products is straightforward whilst finding an orthonormal basis is computationally infeasible. It is then advantageous then to compute eigenvectors of a Laplacian without such a change of basis. Suppose, for each σ ∈ U , we have some basis Bσ of S
F
|σ| and a Hermitian positive definite matrix MS,F
σ representing the inner product in this basis. As MS,F
σ is positive definite there exists an invertible Wσ such that MS,F
σ = W∗
σWσ. Then, in this basis, we now have for σ, τ ∈ U

$$\begin{array}{l}{{\pi_{\sigma}^{\mathcal{F}}\iota_{\tau}^{\mathcal{F}}=W_{\sigma}^{-\ast}M_{\sigma\tau}^{\mathbf{S},\mathcal{F}}W_{\tau}^{-1},}}\\ {{\pi_{\sigma}^{\mathcal{F}}\iota_{\tau}^{\mathcal{F}}\pi_{\tau}^{\mathcal{F}}\iota_{\sigma}^{\mathcal{F}}=W_{\sigma}^{-\ast}M_{\sigma\tau}^{\mathbf{S},\mathcal{F}}(M_{\tau}^{\mathbf{S},\mathcal{F}})^{-1}M_{\tau\sigma}^{\mathbf{S},\mathcal{F}}W_{\sigma}^{-1}}}\end{array}$$

where MS,F
στ is the matrix of inner products between Bσ and Bτ. Now computing eigenvectors of a Laplacian L in this basis can be realised as the generalised eigenvector problem Lx = λMS,F
Ux where MS,F
Uis the block diagonal matrix with blocks MS,F
σ for σ ∈ U .

As the matrices MS,F
τ are Hermitian and positive-definite, the products

$$M_{\sigma\tau}^{\bf S,\mathcal{F}}(M_{\tau}^{\bf S,\mathcal{F}})^{-1}M_{\tau\sigma}^{\bf S,\mathcal{F}}$$

can be quickly computed using the Cholesky decomposition of MS,F
τ . Furthermore, as L is Hermitian and usually sparse, there exist computationally efficient methods for calculating its smallest eigenvalues and their eigenvectors, e.g. variations on the Lanczos method [21], combined with the Cholesky decomposition (see e.g. [18]) of L + αI for some small α > 0.

## 8. Single-Cell Chromatin Accessibility

Chromatin is a macromolecule consisting of DNA and certain proteins, primarily histones [4]. Histones facilitate the dense compaction of DNA, which allows it to fit inside limited space within the cell nucleus. The fundamental unit of chromatin is a *nucleosome*,
which consists of approximately 147 *base-pairs* (namely, the usual A, C, G and T nucleotides) wound around histone molecules. The density of nucleosomes varies considerably across the genome; low density regions are more accessible to transcription factors and other binding proteins. Thus, understanding the relative accessibility of various parts of the genome is important in the study of gene regulation and its variation across different cell types.

Among the most promising experimental frameworks for measuring chromatin accessibility is **ATAC-seq** [1], which has been extended to single cell sequencing **scATACseq** (see e.g. [28]). The output of scATAC-seq may be viewed from a mathematical perspective as follows. Consider a set X of cells {x1, . . . , xN}, with N being on the order of thousands. Each cell xi has a genome consisting of M base pairs, where M is approximately three billion. The output of ATAC-seq on X is an N × M integer matrix. For each 1 ≤ i ≤ N and 1 ≤ j ≤ M, the entry αi,jis a number in {0, 1, 2} representing the accessibility (for cell xi at the j-th genomic position). Such data is high-dimensional, noisy and sparse, and hence warrants feature selection. This is accomplished via a class of techniques called **peak-calling** algorithms [36]. The goal of these methods is to identify specific locations along the genome, called *summits*, which are significantly accessible across the cells in X - see for instance the MACS2 algorithm [39].

REMARK 8.1. We are often interested in quantifying accessibility when one restricts to various sub-populations Y ⊂ X of cell types. However, the peaks of various Y may be lost when calling peaks on X, particularly when the cardinalities of the X under consideration are unbalanced. The standard remedy is to first cluster the data and then call peaks on each cluster [28]. Subsequently, peaks from all the clusters are combined, with various rules beings applied for grouping and extending peaks which overlap. We show below how the quiver Laplacian provides a different mechanism for achieving similar results.

8.1. Pre-processing the data. We use the single-cell ATAC-seq data of [28], which consist of 28,274 tumour-infiltrating T cells. The pre-processing steps are the same as those of ibid:
(1) We align fragments to the GRCH37/HG19 assembly.

(2) We filter sample profiles to keep those with at least 1,000 fragments and a transcription start site (TSS) enrichment score of 8.

(3) We create a count matrix by tiling the genome with 2,500 base-pair windows and counting overlaps of endpoints of fragments with the windows.

(4) Next, we binarise this matrix and retain only the top 20,000 most accessible sites; call the resulting 28, 724 × 20, 000 boolean matrix B.

(5) We then create a frequency-inverse document frequency matrix, apply truncated singular value decomposition to obtain the 2nd to 25th singular vectors. This results in a reduced matrix E of size 28724 × 24.

8.2. Generating the quiver. We build an undirected graph G from the reduced matrix E as follows. Its vertices are the cells Ci, which correspond to rows of E. Treating each such row as a vector in R24, let δi,j ≥ 0 be the Euclidean distance between rows i and j for each i < j. We construct the 15 nearest neighbour graph generated by the δi,j distances.

Our analysis now deviates from [28]. Using the Leiden algorithm [33] the vertex set V of G
is partitioned into finitely many communities, V = ⨿i Vi. As in ibid, communities of size
< 200 are excluded. We then generate a cover U of X from the surviving communities as follows: each cover element Ui ∈ U has the form Vi ∪ Wi, where Wi ⊂ (V − Vi) consists of those vertices which share an edge with some vertex of Vi. The resulting quiver QU
has 87 vertices, and is depicted in Figure 6A. Similarly, Figure 6B displays the contents of each vertex relative to the overall distribution, using the cell types identified in [28].

8.3. Building the representation. Having constructed QU , we apply our feature selector S - which in this case is the MACS2 peak-calling algorithm [39] - to the fragment profiles of cells corresponding to each individual vertex. In the notation of Section 2, the input F is given by the columns of the binarised matrix B; explicitly, the map fj: X → R associated to the j-th column of E sends each xito the entry Bij ∈ {0, 1}. Calling peaks on this set of features produces a vector space S|σ| ⊂ V(F ) for every vertex σ of QU .

We used the same parameters as in [28], and obtained several hundred thousand summits for each vertex as a result. For the purposes of this demonstration, we retained only the most significant 1,000 summits per vertex. Thus the total dimension of the selected vector spaces is 87,000. Since peak-calling on different sub-populations may change the true summit location on the genome slightly, we follow [38] and use a Gaussian kernel between summits (with bandwidth equal to 1,000 base-pairs) as the inner product on V(F ). This allows us to build the mixed representation MS,F
•(see Definition 3.9).

8.4. Results. We computed the first 3,000 eigenvectors of the Laplacian of MS,F
•. Since the total space admits a distinguished basis whose vectors correspond to summits (i.e.,
certain genomic positions {pk}), we may associate to each eigenvector v = ∑k αkpkthe subset of supported genomic positions Pv := {k | αk ̸= 0}
5. Figure 6D shows that for an overwhelming majority of eigenvectors v, the diameter of Pv for most v approximately equals 147 base-pairs, which is the average length of DNA around a nucleosome. A
small fraction of the eigenspaces had dimension > 1; this resulted in a mixing of genomic positions, as shown by the blue outliers in Figure 6D. Nevertheless, in almost all cases, we observed that **the genomic supports of eigenvectors are tightly aligned across the**
vertices of QU .

We then performed a more detailed analysis of the sparsity pattern of the 3,000 eigenvectors. The outcome of this analysis has been summarised in Figure 6E, which plots the 3,000 eigenvectors against all 87 vertices of QU and highlights those vertices along which a given eigenvector has a non-zero component. We observe that the eigenvectors fall broadly into two classes. The first class, which is considerably larger, consists of those **eigenvectors whose genomic support contains summits which are shared by most, if not**
all vertices: see, for instance, the components of eigenvector 11 in Figure 7. The second class contains **eigenvectors whose genomic support contains summits which are shared** by a small fraction of the vertices. A prime example of this type is eigenvector 2702, which has nonzero components along only 3 of the 87 vertices, and has also been depicted in Figure 7.

Finally, we note that (at least for these two examples) **the size of the support of the**
eigenvector relates to biological function. Eigenvector 11, for instance, is concentrated in a regulatory region a few hundred base pairs downstream of the gene *FAM72D*. This gene is involved in the cell cycle [9], and is therefore relevant to most subpopulations of cells. On the other hand, eigenvector 2702 lies just downstream of the gene *STAT3*,
which is a transcription factor known to be an important regulator for differentiation and proliferation in Th1, Th17, and Treg cells [27]. We also note that this eigenvector was only supported on the vertices 8, (8, 11), and 11 (Figure 7). These vertices are particularly enriched in Th1, Th17 and Treg cells (see Figure 6B). Indeed, Figure 6E reveals that many other eigenvectors are also uniquely supported on the vertices 8, (8, 11), 11 and (1, 11).

Since vertex 11 is relatively disconnected from the other vertices, our analysis highlights it as an unusual sub-population of X.

## Code And Data Availability

Code produced for the analysis will be available at https://github.com/osumray/harmonic_feature_selection.

The data from [28] is available from the Gene Expression Omnibus with accession number GSE129785.

## Appendix A. Removing Edges And Vertices

The following extends known results from graphs, e.g. see [34] and [35] respectively.

PROPOSITION A.1. Let A• be a sheaf over a quiver Q, and let n be its total dimension.

A.1(a) Let R ⊂ Q1 be a subset of edges of Q. Let Q′be the quiver with edges Q1 \ R and A ′the restriction of A to Q′*. Then* λk+i(A•) ≤ λk+i(A
′
•
) ≤ λk+r+i(A•)

for i = 1, . . . , n − k − *r where k* = dim Γ(A•) *and r* = ∑e∈R dim Ae.
A.1(b) Suppose V ⊂ Q0 is a subset of vertices of Q. Let Q′be the quiver with vertices Q0 \ V
and all edges e ∈ Q1 such that either s(e) ∈ V or t(e) ∈ *V, and* A ′
•*the restriction of* A•
to Q′*. Then*
$$\lambda_{i}(\mathcal{A}_{\bullet})-w_{1}\leq\lambda_{i}(\mathcal{A}_{\bullet}^{\prime})\leq\lambda_{k+i}(\mathcal{A}_{\bullet})-w_{2}$$
for i = 1, . . . , n − *k where k* = ∑u∈Q0\V dim Au and
$$f o r\,i=1,\ldots,n$$
w1 = max v∈V n∑ s(e)=v t(e)∈/V σmax(Av→e) 2 + ∑ t(e)=v s(e)∈/V σmax(Ae←v) 2o, w2 = min v∈V n∑ s(e)=v t(e)∈/V σmin(Av→e) 2 + ∑ t(e)=v s(e)∈/V σmin(Ae←v) 2o.
PROOF OF PROPOSITION A.1(A). Define LA ,op = BA B
∗
A
. Let k = dim ker LA and c = dim ker LA ,op. Then for i = 1, . . . , n − k, we have that λk+i(LA ) = λc+i(LA ,op).

Now, removing the set of edges R ⊂ Q1 corresponds to the r × r principal submatrix of LA ,op, where r := ∑e∈R dim Ae. By Theorem B.3 we have where i ∈ {1, . . . , m − r} thus

$$\lambda_{i}(L_{\mathcal{A},\mathrm{op}})\leq\lambda_{i}(L_{\mathcal{A}^{\prime},\mathrm{op}})\leq\lambda_{i+r}(L_{\mathcal{A},\mathrm{op}})$$  thus
$$\lambda_{k+i}({\mathcal{A}}_{\bullet})\leq\lambda_{k+i}({\mathcal{A}}_{\bullet}^{\prime})\leq\lambda_{k+r+i}({\mathcal{A}}_{\bullet})$$
$${\mathrm{for}}\;i\in\{1,\ldots,n-k-r\}.$$
for i ∈ {1, . . . , n − k − r}. □
PROOF OF PROPOSITION A.1(B). The boundary matrix BA has block form

$$\begin{bmatrix}B_{11}&0\\ B_{21}&B_{22}\end{bmatrix}$$

where B11 = BA ′ . Here, BA has row blocks indexed by edges between vertices in V and column blocks indexed by vertices in V. Then Laplacian LA = B
∗
A
BA has block form

$$\begin{array}{r l}{{\left[B_{11}^{*}B_{11}+B_{21}^{*}B_{21}\right.}}&{{\left.B_{21}^{*}B_{22}\right]}}\\ {{\left.B_{22}^{*}B_{21}\right.}}&{{\left.B_{22}^{*}B_{22}\right].}}\end{array}$$

Define LQ0\V = B
∗
11B11 + B
∗
21B21 which is a principal submatrix of LA . Note that B
∗
21B21 is a diagonal matrix: The v, v block is

$$\sum_{\begin{array}{l}{{s(e)=v}}\\ {{t(e)\neq V}}\end{array}}\mathcal{A}_{v\to e}^{*}\mathcal{A}_{v\to e}+\sum_{\begin{array}{l}{{t(e)=v}}\\ {{s(e)\neq V}}\end{array}}\mathcal{A}_{e\gets v}^{*}\mathcal{A}_{e\gets v}.$$

We now have that

λi(A ′ - ) = λi(B ∗ 11B11) = λi(LQ0\V − B ∗ 21B21) ≤ λi(LQ0\V) + λn−k(−B ∗ 21B21) = λi(LQ0\V) − λ1(B ∗ 21B21) = λi(LQ0\V) − min v∈V λ1 ∑ s(e)=v t(e)̸=V A ∗ v→eAv→e + ∑ t(e)=v s(e)̸=V A ∗ e←vAe←v  ≤ λi(LQ0\V) − min v∈V n∑ s(e)=v t(e)̸=V λ1(A ∗ v→eAv→e) + ∑ t(e)=v s(e)̸=V A ∗ e←vAe←v o = λi(LQ0\V) − min v∈V n∑ s(e)=v t(e)̸=V σmin(Av→e) 2 + ∑ t(e)=v s(e)̸=V σmin(Ae←v) 2o ≤ λi+k(LA ) − min v∈V n∑ s(e)=v t(e)̸=V σmin(Av→e) 2 + ∑ t(e)=v s(e)̸=V σmin(Ae←v) 2o.
The first two inequalities are from Theorem B.4 and the final inequality is due to Theorem B.3. The right inequality is proven similarly. □

## Appendix B. Classical Results On Eigenvalues Of Hermitian Matrices

In the following, for an n × n Hermitian matrix A, let λ1(A), . . . , λn(A) be the eigenvalues ordered in increasing fashion.

THEOREM B.1 (Rayleigh, see [18] Theorem 4.2.2). *Let A be a Hermitian matrix. Then for* integers 1 ≤ i1, . . . , ik ≤ *n let x*i1
, . . . , xik be orthonormal, where xij is an eigenvector corresponding to λij
(A)*. Define S* = span xi1
, . . . , xik
	*. Then for any x* ∈ S

$$\lambda_{i_{1}}(A)\leq\frac{x^{*}A x}{\|x\|^{2}}\leq\lambda_{i_{k}}(A).$$

THEOREM B.2 (Courant-Fischer, see [18] Theorem 4.2.6). *Let A be Hermitian matrix.*
Then

$$\lambda_{k}(A)=\operatorname*{min}_{\dim V=k}\left[\operatorname*{max}_{x\in V\setminus0}{\frac{\langle x,A x\rangle}{\langle x,x\rangle}}\right].$$

THEOREM B.3 (Cauchy's interlacing theorem, see [18] Theorem 4.3.17). Let A be a Hermitian matrix of size n × n and B an m × *m principal submatrix of A. Then*

$$\lambda_{i}(A)\leq\lambda_{i}(B)\leq\lambda_{i+n-m}(A)$$

for i = 1, . . . , m.

THEOREM B.4 (Weyl's inequalities, see [18] Theorem 4.3.1). For A, B Hermitian matrices of size n × *n the following inequalities hold:*

$$\lambda_{i}(A+B)\leq\lambda_{i+j}(A)+\lambda_{n-j}(B)$$
$$s\,f o r\,j=0,\ldots,n-1\,a n d$$
$$f o r\,j=1,\ldots,i.$$
$$\lambda_{i}(A+B)\geq\lambda_{i-j+1}(A)+\lambda_{j}(B)$$

THEOREM B.5 (See [31] Theorem 5). *For H a Hermitian matrix of dimension n given in* block form as

$$H={\begin{bmatrix}A&B^{*}\\ B&D\end{bmatrix}}$$

where D is non-singular let H/D = A − BD−1B
∗*be the Schur complement of D. Then the* eigenvalues of H and H/D are interlaced:

$$\lambda_{i}(H)\leq\lambda_{i}(H/D)\leq\lambda_{i+r}(H)$$
_for $i=1,...,n-r$ where $r$ is the rank of $D$._

## References

[1] J. D. Buenrostro, P. G. Giresi, L. C. Zaba, H. Y. Chang, and W. J. Greenleaf. Transposition of native chromatin for fast and sensitive epigenomic profiling of open chromatin, DNA-binding proteins and nucleosome position. *Nature methods*, 10(12):1213–1218, 2013.

[2] F. R. Chung. The Laplacian of a hypergraph. *Expanding graphs*, 10:21–36, 1992. [3] F. R. Chung. *Spectral graph theory*, volume 92. American Mathematical Soc., 1997. [4] G. Cooper and K. Adams. *The cell: a molecular approach*. Oxford University Press, 2022.

[5] J. Curry, R. Ghrist, and V. Nanda. Discrete Morse theory for computing cellular sheaf cohomology.

Foundations of Computational Mathematics, 16:875–897, 2016.

[6] J. M. Curry. *Sheaves, cosheaves and applications*. University of Pennsylvania, 2014.

[7] F. Dorfler and F. Bullo. Synchronization of power networks: Network reduction and effective resistance. *IFAC Proceedings Volumes*, 43(19):197–202, 2010.

[8] S. Eilenberg and N. Steenrod. *Foundations of algebraic topology*, volume 2193. Princeton University Press, 2015.

[9] M. Fischer, P. Grossmann, M. Padi, and J. A. DeCaprio. Integration of TP53, DREAM, MMB-FOXM1 and RB-E2F target gene analyses identifies cell cycle gene regulatory networks. *Nucleic acids research*,
44(13):6070–6086, 2016.

[10] T. Gao, J. Brodzki, and S. Mukherjee. The geometry of synchronization problems and learning group actions. *Discrete & Computational Geometry*, 65(1):150–211, 2021.

[11] R. Ghrist and H. Riess. Cellular sheaves of lattices and the Tarski Laplacian. *arXiv preprint* arXiv:2007.04099, 2020.

[12] T. E. Goldberg. *Combinatorial Laplacians of Simplicial Complexes*. Senior thesis, Bard College, 2002. [13] G. H. Golub and C. F. Van Loan. *Matrix Computations*. Johns Hopkins Studies in the Mathematical Sciences. Johns Hopkins University Press, 3rd ed edition, 1996.

[14] J. Gu, B. Hua, and S. Liu. Spectral distances on graphs. *Discrete Applied Mathematics*, 190:56–74, 2015.

[15] I. Guyon, J. Weston, S. Barnhill, and V. Vapnik. Gene selection for cancer classification using support vector machines. *Machine learning*, 46:389–422, 2002.

QUIVER LAPLACIANS AND FEATURE SELECTION 37
[16] J. Hansen and R. Ghrist. Toward a Spectral Theory of Cellular Sheaves. *Journal of Applied and Computational Topology*, 3(4), 2019.

[17] A. N. Hirani. *Discrete exterior calculus*. California Institute of Technology, 2003. [18] R. A. Horn and C. R. Johnson. *Matrix Analysis*. Cambridge University Press, second edition, corrected reprint edition, 2017.

[19] I. T. Jolliffe. *Principal Components Analysis, 2nd Ed.* Springer, 2002.

[20] C. A. Joslyn, L. Charles, C. DePerno, N. Gould, K. Nowak, B. Praggastis, E. Purvine, M. Robinson, J. Strules, and P. Whitney. A sheaf theoretical approach to uncertainty quantification of heterogeneous geolocation information. *Sensors*, 20(12):3418, 2020.

[21] C. Lanczos. An iteration method for the solution of the eigenvalue problem of linear differential and integral operators. *United States Governm. Press Office Los Angeles, CA*, 1950.

[22] R. Lehoucq, K. Maschhoff, D. Sorensen, C. Yang, F. Houssen, S. Ledru, et al. ARPACK-NG: Large scale eigenvalue problem solver. *Astrophysics Source Code Library*, pages ascl–2306, 2023.

[23] T. Mikolov, K. Chen, G. Corrado, and J. Dean. Efficient estimation of word representations in vector space. *arXiv preprint arXiv:1301.3781*, 2013.

[24] T. Muller, A. Seigal, and V. Nanda. Multilinear hyperquiver representations. arXiv:2305.05622v2
[math.AG], 2023.

[25] A. Parada-Mayorga, H. Riess, A. Ribeiro, and R. Ghrist. Quiver signal processing (QSP). arXiv preprint arXiv:2010.11525, 2020.

[26] K. Pearson F.R.S. On lines and planes of closest fit to systems of points in space. *The London, Edinburgh,*
and Dublin Philosophical Magazine and Journal of Science, 2(11):559–572, 1901.

[27] C. Rébé and F. Ghiringhelli. STAT3, a master regulator of anti-tumor immune response. *Cancers*,
11(9):1280, 2019.

[28] A. T. Satpathy, J. M. Granja, K. E. Yost, Y. Qi, F. Meschi, G. P. McDermott, B. N. Olsen, M. R. Mumbach, S. E. Pierce, M. R. Corces, P. Shah, J. C. Bell, D. Jhutty, C. M. Nemec, J. Wang, L. Wang, Y. Yin, P. G.

Giresi, A. L. S. Chang, G. X. Y. Zheng, W. J. Greenleaf, and H. Y. Chang. Massively parallel single-cell chromatin landscapes of human immune cell development and intratumoral T cell exhaustion. *Nature* Biotechnology, 37(8):925–936, 2019.

[29] R. Schiffler. *Quiver Representations*. Number 184 in CMS Books in Mathematics. Springer, 2014.

[30] A. Seigal, H. A. Harrington, and V. Nanda. Principal components along quiver representations. *Foundations of Computational Mathematics*, 23(4):1129–1165, 2023.

[31] R. L. Smith. Some interlacing properties of the Schur complement of a Hermitian matrix. *Linear Algebra* and its Applications, 177:137–144, 1992.

[32] R. Tibshirani. Regression shrinkage and selection via the lasso. Journal of the Royal Statistical Society Series B: Statistical Methodology, 58(1):267–288, 1996.

[33] V. A. Traag, L. Waltman, and N. J. Van Eck. From Louvain to Leiden: guaranteeing well-connected communities. *Scientific reports*, 9(1):5233, 2019.

[34] J. Van Den Heuvel. Hamilton cycles and eigenvalues of graphs. *Linear algebra and its applications*,
226:723–730, 1995.

[35] B. Wu, J. Shao, and X. Yuan. Deleting vertices and interlacing Laplacian eigenvalues. *Chinese Annals of* Mathematics, Series B, 31(2):231–236, 2010.

[36] F. Yan, D. R. Powell, D. J. Curtis, and N. C. Wong. From reads to insight: a hitchhiker's guide to ATAC-seq data analysis. *Genome biology*, 21:1–16, 2020.

[37] K. Ye and L.-H. Lim. Schubert varieties and distances between subspaces of different dimensions.

SIAM Journal on Matrix Analysis and Applications, 37(3):1176–1197, 2016.

[38] J. Yu, D. Sun, Z. Hou, and L.-Y. Wu. Single-cell ATAC-seq analysis via network refinement with peaks location information. *bioRxiv*, page 2022.11.18.517159, 2022.

38 OTTO SUMRAY, HEATHER A. HARRINGTON, VIDIT NANDA

[39] Y. Zhang, T. Liu, C. A. Meyer, J. Eeckhoute, D. S. Johnson, B. E. Bernstein, C. Nusbaum, R. M. Myers, M. Brown, W. Li, et al. Model-based analysis of ChIP-Seq (MACS). *Genome biology*, 9(9):1–9, 2008.
FIGURE 6. Overview of Laplacian from 7.2 applied to tumour-infiltrating T



cells. (A) Quiver constructed from cover, with vertex size corresponding to the cardinality of the covering set. (B) Log likelihood of each cell type label within each vertex. (C) First 3,000 eigenvalues. (D) Range of genomic positions on each chromosome corresponding to non-zero components of the first 3,000 eigenvectors. Blue points correspond to positions across multiple chromosomes. (E) Binary matrix corresponding to the existence of a nonzero component in each vertex for the first 3,000 eigenvectors.

Figure 7.  Examples of eigenvectors. Eigenvector \#11 has a non-zero component at each vertex, whilst eigenvector \#2702 has only non-zero components in vertices (8,), (11,) and (8, 11).



