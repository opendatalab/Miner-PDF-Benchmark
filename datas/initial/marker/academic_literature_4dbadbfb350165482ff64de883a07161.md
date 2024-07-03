# On Weighted Failure Rate, Its Means And Associated Quantile Version

Subarna Bhattacharjee1 ∗
, S.M. Sunoj2**, Sabana Anwar**3 1,3 **Department of Mathematics, Ravenshaw University, Cuttack, Odisha, India**
2 Department of Statistics, Cochin University of Science and **Technology, Cochin, Kerala, India**
April 11, 2024

## Abstract

In this paper, we define weighted failure rate and their different means from the stand point of an application. We begin by emphasizing that the formation of n **independent component** series system having weighted failure rates with sum of weight functions being unity is same as a mixture of n **distributions. We derive some parametric and non-parametric characterization**
results. We discuss on the form invariance property of baseline failure rate for a specific choice of weight function. Some bounds on means of aging functions are obtained. Here, we establish that weighted IFRA class is not closed under formation of coherent **systems unlike the IFRA** class. An interesting application of the present work is credited to the fact that the quantile version of means of failure rate is obtained as a special case of weighted means of failure rate.

Keywords and Phrases: **Weighted distribution, weighted failure rate, weighted arithmetic**
mean failure rate, weighted geometric mean failure rate, weighted harmonic mean failure rate.

AMS 2020 Subject Classification: **Primary 60E15, Secondary 62N05, 60E05**

## 1 Introduction

The notion of ageing plays an important role in reliability theory and in the study of lifetime data analysis. Ageing of a mechanical or biological component based on a lifetime distributions is generally studied using the residual lifetime of the unit that is affected its age. Abundant literature is available on various ageing concepts and their patterns of ageing, comparison of life distributions and to explain their data generating mechanism. Reliability ageing classes based on the monotonicity of the failure rate, such as increasing (decreasing) failure rate (IFR (DFR)) and its average, increasing (decreasing) failure rate average (IFRA (DFRA)) have been found great interest among researchers as it easily give an indication on the manner in which ageing can be described, life
∗**Corresponding author: E-mail: subarna.bhatt@gmail.com**
distributions can be classified and distinguished, and appropriate models can be chosen when observations are available (cf. Barlow and Proschan (1975)).

Let X be a non-negative random variable representing the lifetime of an event or living mechanism with absolutely continuous distribution function F(·**) and probability density function (pdf),**
f(·). Then F is said to be IFR (DFR), if the conditional survival function F¯(x|t) = F¯(x+t)
F¯(x)is decreasing (increasing) in 0 ≤ t < ∞, where F¯ = 1 − F **is the survival (reliability) function; or**
equivalently the failure rate h(t) = f(t)
F¯(t)
is increasing (decreasing) in t ≥ 0, provided f(t**) exists.**
Further, F **is said to IFRA (DFRA), if** −1 t log F¯(t) is increasing (decreasing) in t ≥ **0. However,**
in many real situations, h(x) is not always monotonic. In such cases, the monotonicity of **IFRA**
class condition in terms of the failure rate, 1 t R x 0 h(t)dt**, known as the arithmetic mean failure rate**
(AFR) is a useful measure (Roy and Mukherjee (1992)) in identifying the monotonicity of classes of life distributions. Along with arithmetic mean failure rate, Roy and Mukherjee (1992) have also studied classes of distributions through the monotonic behaviour of geometric failure rate (GFR) and harmonic failure rate (HFR), and the characterizations **and ageing classes based on it. They** pointed out until then no work has been done on GFR and HFR. The **following definition is cited** from Roy and Mukherjee (1992).

Definition 1.1 Let X **be a non-negative random variable with absolutely continuous CDF** F(·),
PDF f(·) and failure rate h(·)**. Then the arithmetic mean failure rate (AFR), geometric mean** failure rate (GFR) and harmonic failure rate (HFR), denoted by A(·), G(·) and H(·) **respectively are**
defined as A(x) = 1x R x 0 h(u)du, x > 0; G(x**) = exp** 1x R x 0 ln h(u)du; H(x) = 1x R x 0 1 h(u)
du−1. ✷
Recently, Bhattacharjee et al. (2022) further studied the usefulness of the three measures based on the notion of ageing intensity (AI) function proposed by Jiang et al. (2003).

When sample observations are not equally likely, we use the weighted measures to capture the significance of their relative importance. Choosing appropriate weights, we can then compute various measures in a better way by giving appropriate weights based on the sample mechanism. Such biased sampling schemes are usually employed in observational studies either due to its convenience or its cost-effectiveness. Based on this, Rao (1965) identified the concept of weighted distributions in connection with the modeling statistical data, in situations where the usual practice of employing standard distributions for the purpose was not found appropriate. These distributions occur frequently in the studies related to reliability, analysis **of family data, meta analysis and analysis**
of intervention data, biomedicine, ecology, etc, for more details, see Patil and Rao (1978), Gupta and Kirmani (1990), and the references therein. If X **is a non-negative random variable with a**
probability density function (pdf) f(x), then the pdf of the weighted random variable Xw **is given**
by, fw(x) = w(x)f(x)
Ew(X)
, x > 0, where w(·**) is a non-negative weight function (cf. Rao (1965)). There**
are many weight functions used by different authors, however, the weight functions w(x) = x and w(x) = x α, α > 0 are found to be more popular due to its adaptibility in terms **of identifying the**
observed distribution in various applied problems wherein **the probability of selecting the sample**
units are proportional to the length or size of the population units, the respective random variables are known as the length-biased and size-biased random **variables. Motivated by these, in the**
present study, we propose weighted mean failure rates based **on the measures of AFR, GFR and**
HFR.

The paper is organized as follows. In Section 2, we introduce **the definitions of weighted means of**
failure rate along with citing an application. As an application of weighted failure rates as proposed in this paper, we note that formation of an n **component series system having complementary** weight functions is actually a mixture of n **distributions and vice-versa. We give some parametric**
and non-parametric characterization results. Section 2 gives a note on form invariance property of the baseline failure rate and its transformation from one aging class to another depending upon the choice of the weight function. Section 2 also highlights **on some bounds of means of aging** functions. We focus on some new non-parametric aging classes based on means of failure rate and discuss their inclusive properties. Some illustrative **examples are given for ready reference.** Some equivalent conditions of aging classes based on geometric and harmonic means are obtained. We prove our claim that weighted IFRA class is not closed under formation of coherent systems unlike IFRA class by giving an easy counterexample. In Section 4, we derive the quantile version of means of failure rate as special case from weighted means of failure rate. We study the proportional quantile hazards model and compare it with conventional proportional hazards model. Concluding remarks are listed in Section 5.

## 2 Weighted Means Of Failure Rate

In this paper, we introduce a generalized versions of AFR, GFR and HFR involving a suitable choice of a non-negative weight function as defined below.

Definition 2.1 Let X **be a non-negative random variable with absolutely continuous distribution**
function F(·), probability density function f(·) and failure rate h(·). **The weighted arithmetic mean** failure rate (w-AFR), weighted geometric mean failure rate **(w-GFR) and weighted harmonic failure**
rate (w-HFR) denoted by Aw(·), Gw(·) and Hw(·) **respectively, with a suitable non-negative weight**
function w(·)**, are defined as**

$(i)$$A^{w}(x)=\frac{\int_{0}^{x}w(u)h(u)du}{\int_{0}^{x}w(u)du},x>0;$  $(ii)$$G^{w}(x)=\exp\left(\frac{\int_{0}^{x}w(u)\ln h(u)du}{\int_{0}^{x}w(u)du}\right),x>0;$  $(iii)$$H^{w}(x)=\left(\int_{0}^{x}w(u)du\right)\left(\int_{0}^{x}\frac{w(u)}{h(u)}du\right)^{-1},x>0.$
du−1**, x >** 0. ✷
$\square$  . 
Clearly, if w(x) = 1 for all x ≥ **0 then above definition reduces to that of AFR, GFR and HFR**
given in Definition 1.1 due to Roy and Mukherjee (1992).

In the pretext, of above, we shall define the other reliability functions of the weighted random variable as given in the following definition.

Definition 2.2 The weighted survival function of X, or survival function of weighted random variable Xw, **denoted by** F
w(·) **is defined as** F
w(x**) = exp** −R x 0 w(u)h(u)du, x > 0. **The density and**
failure rate function of Xw are f w(x) = w(x)h(x**) exp** −R x 0 w(u)h(u)duand h w(x) = w(x)h(x)
for all x > 0, **respectively.**
The fact that h w(x) = w(x)h(x) reminds us of proportional hazard models (PHR) where h(x**) is**
the baseline failure rate and w(x) is the proportionality function giving rise to a new hazard **rate**
h w(·).

Referring to the related literature, one can notice that corresponding to the baseline survival function G having failure rate rG, **Marshall and Olkin (1997) proposed a cumulative distribution**
function F such that its hazard rate hF (·) is given by hF (x, α) = 1 1−αG(x)
hG(x) where **x, α** ∈ R+
and α = 1 − α, ( the parameter α **termed as tilt parameter by Marshall and Olkin (2007)) and this**
is a special case of Definition 2.2 if one assumes w(x) = 1 1−αG(x)
. **Furthermore, Balakrishnan et al.**
(2018) defined modified proportional hazard rates (MPHR) of n **independent components having**
lifetimes X1, X2, . . . , Xn **with respective survival functions** Fiif

$$F_{i}(x,\lambda_{i})=\frac{1-\left(\overline{{{F}}}(x)\right)^{\lambda_{i}}}{1-\overline{{{\alpha}}}\big(\overline{{{F}}}(x)\big)^{\lambda_{i}}},\alpha>0,\overline{{{\alpha}}}=1-\alpha,\lambda_{i}>0$$

for i = 1, 2, . . . , n where F **is the corresponding baseline survival function. They considered it**
(MPHR model) to be the generalization of PHR model because if α **= 1 then PHR is a special**
case of MPHR. However, one shall observe that this is based on the notion that Xi**'s with survival**
functions Fi(x) follow PHR model if there exits positive constants λi's such that Fi(x) = F
λi(x).

It is worthwhile to note that the definition of MPHR proposed by Balakrishnan et al. (2018) is not based on the fact that hi(x) = h(x)w(x) where h(x**) is considered to be the baseline failure**
rate. The present work, in other words, is an attempt to define **PHR model in a more general sense.**
We now give a necessary and sufficient condition that weight function w(x**), and hazard rate**
h(x) must satisfy so that F¯w(x**) represents a (weighted) survival function. One can refer to Marshall**
and Olkin (2007) to look into the postulates for hazard rate (non-weighted).

(i) w(x) ≥ 0, h(x) ≥ 0.

(ii) For x > 0,R x 0 w(u)h(u)**du <** ∞

## (Iii) R ∞ 0 W(U)H(U)Du = ∞

(iv) If R x 0 w(u)h(u)du = ∞ for some x then h(y) = ∞ for every **y > x.**
Now, we look into some uses of weighted failure rate arising in practical field. Let us consider a series system formed by n components having failure rates hi(x**) with respective weights** wi(x),
for i = 1, 2, . . . , n and x > **0 such that** Pn i=1 wi(x) = 1. The failure rate h(x**) of the resultant** n component series system is h(x) = Pn i=1 hi(x)wi(x). This form of h(x**) is similar to the failure rate**
of the mixture of n distributions, with cumulative distributions, Fi(·) having failure rates, hi(·**) for**
i = 1, 2, . . . , n. The failure rate of mixture of n distributions is given by F(x) = Pn i=1 πiFi(x), **with**
Pn i=1 πi **= 1 is**

$$\begin{array}{r c l}{{h(x)}}&{{=}}&{{\frac{\sum_{i=1}^{n}\pi_{i}f_{i}(x)}{1-\sum_{i=1}^{n}\pi_{i}F_{i}(x)}}}\\ {{}}&{{=}}&{{\frac{\sum_{i=1}^{n}\pi_{i}h_{i}(x)\overline{{{F}}}_{i}(x)}{\sum_{i=1}^{n}\pi_{i}\overline{{{F}}}_{i}(x)}=\sum_{i=1}^{n}p_{i}(x)h_{i}(x)}}\end{array}$$
where $p_i(x)=\frac{\pi_i\overline{F}_i(x)}{\sum_{i=1}^n\pi_i F_i(x)}$ wh? 
which in turn satisfies $\sum_{i=1}^{n}p_{i}(x)=1$.  
Unlike the log-exponential family (cf. Patil G. P. and Ord, J. K. (1976)) which possesses the form-invariance property among the weighted distributions defined by Rao (1965) under size based sampling of order c > 0, (i.e., w(x) = x c**), in the present work Weibull distribution bear the said**
property. If a given Weibull distribution with failure rate h(x) = αβxβ−1 **belongs to positive aging**
classes, namely IFR, then the resultant size biased distribution also fall in the same aging class, but this may not be true for DFR negative aging class, i.e., if β + c > **1 then the baseline DFR** Weibull distribution is shifted to IFR positive aging class **under size based sampling.**
Additive Weibull distribution with failure rate h(x) = αθxθ−1 + βγxγ−1 with **α, β, θ, γ >** 0 has form-invariance property under size biased sampling. However, the weight function w(x) = x c drags the additive Weibull distribution from DFR class to IFR class if c + θ > and c + γ > 1.

If X **follows four-parameter Weibull distribution (cf. Kies (1958)) with survival function**

$${\overline{{F}}}(t)=\exp\big(-\lambda\big({\frac{t-a}{b-t}}\big)^{\beta}\big),0\leq a<t<b,\lambda,\beta>0$$

then w(t) = t−a b−t is a form-invariance weight function for the distribution. We know that X has bathtub failure rate if 0 < β < 1, and IFR if β > 1 but the weighted random variable Xw **is always**
IFR independent of β **under the aforementioned weighted transformation.**

## 2.1 Characterization Results

Now, we prove that the equality of any two of w-AFR, w-GFR and w-HFR characterize exponential distribution. The following proposition gives some light on this. We continue with the same notations as discussed in previous sections of the paper.

Proposition 2.1 A non-negative random variable X, **follows exponential distribution if and only**
if for x > 0, **any one of the following hold**
(i) Aw(x) = Gw(x)
(ii) Gw(x) = Hw(x)
(iii) Aw(x) = Hw(x).

Proof. If X **follows exponential distribution then it is easy to prove that (i), (ii) and (iii) hold.**
Conversely, if (i) holds then

$${\frac{\int_{0}^{x}w(u)h(u)d u}{\int_{0}^{x}w(u)d u}}=\exp\Big({\frac{\int_{0}^{x}w(u)\ln h(u)d u}{\int_{0}^{x}w(u)d u}}\Big),$$

gives

$$\big{(}\int_{0}^{x}w(u)du\big{)}\big{\{}\ln\big{(}\int_{0}^{x}h(u)w(u)du\big{)}\big{\}}=\big{(}\int_{0}^{x}w(u)du\big{)}\big{(}\ln\int_{0}^{x}w(u)du\big{)}+\int_{0}^{x}w(u)\ln h(u)du.\tag{2.1}$$  Differentiating (2.1) with respect to $u$ we get $h(u)=u$ ($u$) where 
Differentiating (2.1) with respect to x, we get ln(ez1(x)) = z1(x**) where**

$$z_{1}(x)={\frac{h(x)\int_{0}^{x}w(u)d u}{\int_{0}^{x}w(u)\ln w(u)h(u)d u}}.$$
.
Thus, z1(x) = 1, for all x ≥ 0, **gives** d dx h(x)
 R x 0 w(u)du= 0, **and since** R x 0 w(u)du 6**= 0, we**
conclude that h(x) is constant for all x ≥ 0. This proves that X **has exponential distribution.**
Similarly, if (ii**) holds then**

$$\exp\Big(\frac{\int_{0}^{x}w(u)\ln h(u)d u}{\int_{0}^{x}w(u)d u}\Big)=\Big(\int_{0}^{x}w(u)d u\Big)\Big(\int_{0}^{x}\frac{w(u)}{h(u)}d u\Big)^{-1},$$

or equivalently

$$\int_{0}^{x}w(u)h(u)du+\Big{(}\int_{0}^{x}w(u)du\Big{)}\ln\Big{(}\int_{0}^{x}\frac{w(u)}{r(u)}du\Big{)}=\Big{(}\int_{0}^{x}w(u)du\Big{)}\ln\Big{(}\int_{0}^{x}w(u)du\Big{)}.\tag{2.2}$$

After differentiating (2.2), we get ln(ez2(x)) = z2(x**) where**

$$z_{2}(x)={\frac{\int_{0}^{x}w(u)d u}{h(x){\Big(}\int_{0}^{x}{\frac{w(u)}{h(u)}}d u{\Big)}}}.$$

6 Hence, z2(x**) = 1 which in turn gives** d dx r(x)
 R x 0 w(u)
h(u)
du= 0. **Since** w(u)
R x 0 h(u)
du6= 0, **it follows**
that h(x) = constant. This proves that if (ii) holds then X **has exponential distribution.**
Note that if (iii**) holds then it is equivalent to the fact that**

$$\Big(\int_{0}^{x}w(u)h(u)d u\Big)\Big(\int_{0}^{x}{\frac{w(v)}{h(v)}}d v\Big)=\Big(\int_{0}^{x}w(u)d u\Big)^{2}.$$
$$(2.3)$$
$$(2.4)$$

Taking logarithm on both sides and then differentiating both sides with respect to x, **we get**

$${\frac{h(x)\int_{0}^{x}w(u)d u}{\int_{0}^{x}w(u)h(u)d u}}+\Big({\frac{1}{h(x)}}\Big)\Big({\frac{\int_{0}^{x}w(u)d u}{\int_{0}^{x}{\frac{w(v)}{h(v)}}d v}}\Big)=2.$$

Since w-HFR=w-AFR, replacing w-HFR by w-AFR in the second term of (2.4), we get

$${\frac{h(x)\int_{0}^{x}w(u)d u}{\int_{0}^{x}w(u)h(u)d u}}+\Big({\frac{1}{h(x)}}\Big)\Big({\frac{\int_{0}^{x}w(u)h(u)d u}{\int_{0}^{x}w(u)d u}}\Big)=2.$$
Hence,
Hence, $$\left(h(x)\int_0^x w(u)du-\int_0^x w(u)h(u)du\right)^2=0,$$ and this gives $\frac{d}{dx}h(x)=0$ as $\int_0^x w(u)du\neq0.$ This completes the proof.
0 w(u)du 6= 0. **This completes the proof.** ✷
Note that Aw(x) = c for all x > **0 characterizes exponential distribution, and so is true for** Gw(·)
and Hw(·). **If we simultaneously peep into the lines in the proof of Proposition 2.1, we conclude**
that (i), (ii) and (iii) get reduced to Aw(x) = Gw(x) = Hw(x) = c for all x > 0.

In the next proposition we obtain simple relationships between w-AFR, w-GFR and w-HFR
functions and hazard rate, that characterize the underlying distributions through their hazard rates. The proof is omitted.

Proposition 2.2 Let h(x) be differentiable for all x ≥ 0. **Then for any non-negative weight function**
w(x), and for suitable positive values of constants, a, b, c, k **we have**

 $(i)\;\;A^{w}(x)=ah(x)\;for\;all\;x\;if\;and\;only\;if\;h(x)=k\Big(\int_{0}^{x}w(u)du\Big)^{(1-a)/a}$ . 
_(ii) $G^{w}(x)=bh(x)$ for all $x$ if and only if $h(x)=k\Big{(}\int_{0}^{x}w(u)du\Big{)}^{\ln(e/b)-1}$._
 *(iii) $H^w(x)=ch(x)$ for all $x$ if and only if $h(x)=\left(\frac{1}{kc}\int_0^x w(u)du\right)^{1-c}$, where $c$ constant. 
0 w(u)du1−c, where k **is an arbitrary**
7 One can wonder whether for any particular class of well known **probability distribution, weighted**
means are proportional to their respective hazard rates. If we choose weight function as w(x) = x n, then the corresponding failure rate is that of two-parameter Weibull distribution with shape parameter (n − an + 1)/a and scale parameter ka/(n − an + 1)(n **+ 1)** 1−a a, **provided** 1+n−an a
> 0.

Intuitively, it follows that (ii) and (iii**) are also satisfied for two-parameter Weibull distribution**
having a different sets of scale and shape parameters. We summarize this discussion by claiming that w(x) = x nfor suitable n, and x > **0 is a proper choice of weight function as it results in**
a legitimate probability distribution. A little work out will show that if we choose w(x) = e nx, then the resultant failure rate function is h(x**) does not correspond to a well defined probability** distribution, underlying the fact that proportionality of **weighted means and hazard rate do not** hold good.

We end this subsection by stating some crucial observations **in the upcoming remark.**
Remark 2.1 **An essence of introducing the weighted version of means of failure rate lies in the**
aforementioned Proposition 2.2, where a suitable choice of **weight function characterizes some well**
known distributions. The readers may also note that, proportionality of each of Aw(·), Gw(·) and Hw(·) with h(·) imply that h(x) is increasing (decreasing) in x if and only if a ≤ (≥)1, b ≤ (≥)1, and c ≤ (≥)1 **respectively. It is clear that, under the aforementioned conditions, monotonicity of**
h(·) **is independent of the choice of weight function.**

## 2.2 Bounds And Limiting Behavior Of Aging Means

We state a result from Wijsman (1985) in the form of a lemma.

Lemma 2.1 Let fi, gi are non-negative functions, such that the integrals Rfigi **are positive for**
i, j = 1, 2. **Then**
$${\frac{\int f_{1}g_{1}d\mu}{\int f_{1}g_{2}d\mu}}\geq{\frac{\int f_{2}g_{1}d\mu}{\int f_{2}g_{2}d\mu}},$$
provided f1/f2 and g1/g2 **are monotonic in same direction. The inequality in (2.5) is reversed if**
f1/f2 and g1/g2 **are monotonic in opposite direction. Equality holds if and only if either** f1/f2 or
g1/g2 is a constant. Here µ **is Lebesgue measure on a subset of the real line or counting measure**
on a subset of the integers.

The following proposition decides bounds of the aging means **on the basis of monotonicity of**
weight function and hazard rate (as the case may be). An interpretation of the result is Proposition 2.3 (i) Aw(x) ≥ (≤)A(x) according as w(x) and h(x) **are monotonic in same**
(opposite) direction.

(ii) If the hazard rate function h(x) ≥ 1 for all x ≥ 0 then Gw(x) ≥ (≤)G(x) **according as** w(x)
and h(x) **are monotonic in same (opposite) direction.**
(iii) Hw(x) ≥ (≤)H(x) according as w(x) and h(x) **are monotonic in same (opposite) direction.**
Proof. We choose f1(x) = w(x), g1(x) = h(x), f2(x) = g2(x) = 1, to prove (i). **By choosing**
f1(x) = w(x), g1(x) = ln h(x), f2(x) = g2(x) = 1, and assuming ln h(x) ≥ 0 (since h(x) ≥ **1 for all**
x ≥ **0), Lemma 2.1 gives** R x 0 w(u) ln h(u)du R x 0 w(u)du ≥ (≤)
1 x R x 0 ln h(u)duaccording as w(x) and h(x**) are**
monotonic in same (opposite) direction. This proves (ii). Similarly, taking f1(x) = w(x), g1(x) =
1, f2(x) = 1, g2(x) = 1/h(x), we prove (iii). ✷
The readers may arrive at the following remark by looking at the Proposition 2.3 and the fact that Aw(x) ≥ Gw(x) ≥ Hw(x**) for all** x ≥ 0.

Remark 2.2 If w(x) and h(x) **are monotonic in same direction then the lower and upper bounds**
of the aging means of failure rate are H(x) and Aw(x) respectively. On the other hand, w(x) and h(x) are monotonic in opposite direction then the lower and upper **bounds of the aging means of**
failure rate are Hw(x) and A(x) **respectively. The lower and upper bounds of the aging means of**
failure rate discussed in this article are min(H(x), Hw(x)) and max(A(x), Aw(x)) **respectively.**
In the following theorem, we obtain bounds for the ratio of the weighted hazard means by associating weights in sequence.

  **Theorem 2.1**: _Let $h_{k}(x)=w(x)h_{k-1}(x)=(w(x))^{k}h(x),k\geq1,h_{0}(x)=h(x),$ for $x>0$. We define $A_{h_{k}}^{w}(x)=\left(\frac{L^{w}w(x)h_{k}(x)h_{0}}{L^{w}w(x)h}\right),$$G_{h_{k}}^{w}(x)=\exp\left(\frac{L^{w}w(x)h_{0}(x)h_{0}(x)}{L^{w}_{0}\ w(x)h}\right)$, and $H_{h_{k}}^{w}(x)=\left(\frac{L^{w}w(x)h_{0}}{L^{w}\frac{w(x)}{h_{k}(x)}h}\right)$. For $x>0$, the following statements hold._
(i) If h(x) and w(x) **are monotonic in opposite (same) direction then**

$$\frac{A_{h_{k}}^{w}(x)}{A_{h}^{w}(x)}\geq(\leq)\frac{\int_{0}^{x}w(u)d u}{\int_{0}^{x}(w(u))^{n+1}d u}.$$
$$(i i)\,\,\,I f\,w(x)>1,\,\,t h e n$$
$$\frac{G_{h_{k}}^{w}(x)}{G_{h}^{w}(x)}\geq\exp\left(\frac{k}{x}\int_{0}^{x}\ln w(u)d u\right).$$

(iii) If h(x) and w(x) **are monotonic in same (opposite) direction then**

$$\frac{H_{h_{k}}^{w}(x)}{H_{h}^{w}(x)}\geq(\leq)\frac{\int_{0}^{x}w(u)d u}{\int_{0}^{x}\frac{1}{(w(u))^{k-1}}d u}.$$

(iv) If w(x) and h(x) **are monotonic in same (opposite) direction then** Aw hk
(x) ≥ (≤)A(x), and Hw hk
(x) ≥ (≤)H(x), **according as** w(x) ≤ (≥)1.

(v) If h(x) ≥ 1, w(x) ≥ 1 **then** Gw hk
(x) ≥ G(x), provided w(x) and h(x) **are monotonic in same**
direction.
Proof. The proofs of (i),(ii) and (iii**) follow by applying Lemma 2.1 on the ratios, viz.,**

$$\frac{A_{h_{k}}^{w}(x)}{A_{h}^{w}(x)}=\frac{\int_{0}^{x}(w(u))^{k+1}h(u)d u}{\int_{0}^{x}w(u)h(u)d u},\frac{G_{h_{k}}^{w}(x)}{G_{h}^{w}(x)}=\exp\Big(\frac{k\int_{0}^{x}w(u)\ln w(u)d u}{\int_{0}^{x}w(u)d u}\Big),$$  $$\frac{H_{h_{k}}^{w}(x)}{H_{h}^{w}(x)}=\Big(\frac{\int_{0}^{x}\frac{w(u)}{h(u)}d u}{\int_{0}^{x}\frac{1}{w^{k-1}(u)h(u)}d u}\Big),x>0.$$
$$\operatorname{and}$$

The proof of (iv) follows from (i) and (iii) of Proposition 2.3. The proof of (v**) follows from (**ii)
of Proposition 2.3. If w(x) and h(x**) are monotonic in same (opposite) direction then** Aw hk
(x) ≥ (≤
)Aw h
(x), and Hw hk
(x) ≥ (≤)Hw h
(x), **according as** w(x) ≥ (≤)1. ✷
The above theorem can be interpreted by saying that one can keep minimizing the means of failure rate (AFR and HFR) of a component, having increasing **failure rate by associating weights** in sequence which are monotonically decreasing with time. However, GFR increases rapidly with the increase in number of weight functions and is independent of the nature of monotonicity of weight and hazard rate. Theorem 2.1 (ii) reveals that if k → ∞ and w(x) > **1 then** Gw hk
(x) → ∞.

## 3 Non-Parametric Classes Of Distributions Based On Weighted Means Of Failure Rates

We define non-parametric classes of distributions on the basis of monotonicity of w-AFR,
w-GFR and w-HFR.

Definition 3.1 A random variable X **is said to belong to the class of**
(i) Increasing (resp. Decreasing) weighted arithmetic mean failure rate Iw − AF R **(resp.** Dw −
AF R)) distributions if Aw(x) is increasing (resp. decreasing) in x > 0.

(ii) Increasing (resp. Decreasing) weighted geometric mean failure rate Iw − GF R **(resp. (**Dw −
GF R)) distributions if Gw(x) is increasing (resp. decreasing) in x > 0.

(iii) Increasing (resp. Decreasing) weighted harmonic mean failure rate Iw − HF R **(resp.** Dw −
HF R)) distributions if Hw(x) is increasing (resp. decreasing) in x > 0. ✷
The next theorem emphasises on the fact that the monotonic behaviour of h(x**) is possessed**
by Aw(x), Gw(x**) and** Hw(x).

Theorem 3.1 If h(x) is increasing (decreasing) in x ≥ 0 **then**
(i) Aw(x) **is increasing (decreasing) in** x ≥ 0;
(ii) Gw(x) **is increasing (decreasing) in** x ≥ 0;
(iii) Hw(x) **is increasing (decreasing) in** x ≥ 0.

  **Proof.** To prove (i), we note that $\Big{(}\int_{0}^{\pi}w(u)du\Big{)}\Big{(}\frac{d}{du}A^{w}(x)\Big{)}=w(x)(h(x)-A^{w}(x))$, and thus $\Big{(}\begin{smallmatrix}d&A^{w}(x)\end{smallmatrix}\Big{)}>(c)\ 0$ according as $h(x)\geq(c)\ A^{w}(x)$ for all $x\geq0$. If $h(x)$ is increasing (decreasing)
dxAw(x)
≥ (≤) 0 according as h(x) ≥ (≤)Aw(x) for all x ≥ 0. If h(x**) is increasing (decreasing)**
in x then h(x) ≥ (≤) Aw(x) for x ≥ 0. This proves (i). Similarly, to prove (ii), **we first note that**
$$\left(\frac{d}{d x}G^{w}(x)\right)=\frac{G^{w}(x)}{\left(\int_{0}^{x}w(u)d u\right)}w(x)\ln\Big(\frac{h(x)}{G^{w}(x)}\Big),$$
and this implies that d dxGw(x) ≥ (≤) 0 according as h(x) ≥ (≤)Gw(x). One can note that if h(x**) is**
increasing (decreasing) in x then h(x) ≥ (≤) Gw(x) for all x ≥ 0, thus proving (ii). To prove (iii),

we first note that
$$\Big(\frac{d}{d x}H^{w}(x)\Big)\Big(\int_{0}^{x}\frac{w(p)}{h(p)}d p\Big)=w(x)\Big\{1-\frac{H^{w}(x)}{h(x)}\Big\},$$
and hence we find that d dxHw(x)
≥ (≤) 0 according as h(x) ≥ (≤)Hw(x) for all x ≥ 0. **Also, if**
h(x) is increasing (decreasing) in x then h(x) ≥ (≤)Hw(x) for all x ≥ 0. **This completes the proof.**✷
The next example highlights the importance of choosing weight functions in generating new distributions. It is also cited in upcoming counterexample **3.1 for establishing that w-IFRA class**
is not closed under formation of coherent systems.

Example 3.1 Let X **follows two parameter Weibull distribution with scale and shape parameter** α and β respectively. If we take w(x) = e nx for all x > 0, then the weighted random variable Xw has failure rate h w(x) = αβenxx β−1. Here, taking n = −m with m > 0,

$$\int_{0}^{x}w(u)h(u)u=\alpha\beta\int_{0}^{x}e^{-mt}t^{\beta-1}dt\tag{3.5}$$ $$=\alpha\beta(-n)^{-\beta}\gamma(\beta,-nx)$$ $$=\alpha\beta(-n)^{-\beta}\Big{(}\Gamma(\beta)-\Gamma(\beta,-nx)\Big{)},$$

where the incomplete Gamma function γ(z, a) and its complement Γ(z, α) **(also known as Prym's** function) are

$$\begin{array}{l}{{\gamma(a,x)=\int_{0}^{x}t^{a-1}e^{-t}d t,\Gamma(a,x)=\int_{x}^{\infty}t^{a-1}e^{-t}d t,\,\,R e a l(a)>0),}}\\ {{\mathrm{}}}\\ {{z)+\Gamma(a,x)=\Gamma(a).\,\,I f\,n<0\,\,w e\,\,h a v e\,\,r a e l\,\,v a l a u e s\,\,f o r\,\,\bar{F}^{w}(t),\,\,a s}}\end{array}$$

satisfying γ(a, x) + Γ(a, x) = Γ(a). If n < 0 **we have real values for** F¯w(t), as

$$\bar{F}^{w}(x)=\exp\Big\{-\alpha\beta(-n)^{-\beta}\Big(\Gamma(\beta)-\Gamma(\beta,-n x)\Big)\Big\},x>0,\beta>0.$$

Also, considering m = −n, **we get**

$${\frac{d}{d x}}h^{w}(x)={\frac{d}{d x}}{\Big(}\alpha\beta e^{n x}x^{\beta-1}{\Big)}=\alpha\beta e^{n x}x^{\beta-2}(\beta-1-m x)\leq0$$

if (β − 1 − mx) ≤ 0, **i.e.,** d dx h w(x) ≤ 0 if x ≥
β−1 m
. If β < 1 **then** d dx h w(x) ≤ 0 for all x > 0.

Thus, Xw is DFR if β < 1. On the other hand if β > 1, **then** d dx h w(x) ≥ 0 for x ∈ (0, β−1 m ) and d dx h w(x) ≤ 0 for x ≥
β−1 n
. Thus Xw is DFR if β < 1, whereas Xw **has upside-down bathtub shaped**
failure rate if β > 1. **Using (3.5) and the fact that** R x 0 w(u)du = 1n e nx − 1
**we get**

$$A^{w}(x)={\frac{n(-n)^{-\beta}\alpha\beta\left(\Gamma[\beta]-\Gamma[\beta,-n x]\right)}{\left(e^{n x}-1\right)}}$$

Here, for β < 1, hw(x) is decreasing in x, and so is Aw(x) **as evident from Theorem 3.1. Similarly,**
for β > 1, Aw(x) **is upside-upside-down bathtub. Using (3.6), we note that,**

d dxA w(x) = n(−n) −βαβ d dx  Γ[β] − Γ[β, −nx]  e nx − 1  = n(−n) −βαβ((e nx − 1)e nx(−nx) β−1(−n) − Γ[β] − Γ[β, −nx] e nxn ) (e nx − 1)2 = n(−n) −βαβ((e nx − 1)e nx(−nx) β(−n) −(nx) − Γ[β] − Γ[β, −nx] e nxn ) (e nx − 1)2 =n(−n) −βαβenx x(e nx − 1)2 n(e nx − 1)(−nx) β + nxΓ[β, −nx] − Γ[β] o =n 2x(−n) −βαβenx x(e nx − 1)2 nΓ[β, −nx] − Γ[β] − (e nx − 1)(−nx) β−1o =n 2x(−n) −βαβenx x(e nx − 1)2 n− γ[β, −nx] − P(x) o, (say), P(x) = (e nx − 1)(−nx) β−1 ≤ 0, x > 0.
$$w h e r e$$
The change point of monotonicity of Aw(x) is determined by the root of equation γ[β, −nx]+P(x) =
0. **Similarly, we obtain**

0. _Similarly, we obtain_ $$G^w(x)=\alpha\beta t^{\beta-1}(-nt)^{\frac{\beta-1}{n-1}}e^{\frac{(\beta-1)(E_1(-nt)+\gamma)}{n^{\beta-1}}}$$ $$H^w(x)=\frac{\alpha\beta(e^{nt}-1)nt^{\beta}(-nt)^{-\beta}}{\Gamma[2-\beta]-\Gamma[2-\beta,-nt]},$$ *where $\gamma\sim0.577216$ is Euler's constant and $E_n(z)$ is the exponential integral function. 
Below, we state two theorems highlighting the inclusion property of the non-parametric aging classes given in Definition 3.1. The proof follows due to Theorem 3.1, line of the proof therein and the fact that Aw(x) ≥ Gw(x) ≥ Hw(x) for all x > 0.

Theorem 3.2 IF R ⊆ Iw − AF R ⊆ Iw − GF R ⊆ Iw − **HF R**
Theorem 3.3 DF R ⊆ Dw − HF R ⊆ Dw − GF R ⊆ Dw − **AF R**

## 3.1 Characterization Results For W-Afr, And W-Gfr

We introduce the concept of weighted star-shaped (anti-star) function which is a generalization of star-shaped (anti-star) function to give an equivalent condition of Iw − AF R and Dw − **AF R**
classes of distributions.

Definition 3.2 A function g(x) defined on [0,∞) is said to be weighted star-shaped (weighted antistar shaped) with respect to a non-negative weight function w(x) if −1 R x 0 w(u)dug(x) **is increasing**
in x > 0. Equivalently, for 0 ≤ α ≤ 1 and x ≥ 0,

$$g(\alpha x)\leq\Big(\frac{\int_{0}^{\alpha x}w(u)d u}{\int_{0}^{x}w(u)d u}\Big)g(x)$$

The next theorem gives a necessary and sufficient condition of **a increasing (decreasing)**
weighted arithmetic failure rate or weighted failure rate average class of distributions, denoted by w-AFR. We omit the proof for the sake of brevity.

Theorem 3.4 Let X has increasing (decreasing) w-AFR. Then the following conditions are equivalent.

_(i)_ $\Big{(}-\frac{1}{\int_{0}^{\cdot}w(u)du}\Big{)}\ln F^{w}(x)$ _is increasing (decreasing) in_ $x>0$_._  _(ii)_ $-\ln F^{w}(x)$ _is weighted star-shaped (weighted anti-star shaped) with respect to_ $c(\cdot)$_._
_(iii) $\left(\bar{F}^{w}(x)\right)^{\frac{1}{\int_{0}^{x}w(u)du}}$ is decreasing (increasing) in $x>0$._
(iv) For α ∈ [0, 1], and x > 0, F¯w(αx) ≥ (≤)
$$\bar{F}^{w}(\alpha x)\geq(\leq)\Big(\bar{F}^{w}(x)\Big)^{\frac{\int_{0}^{\alpha x}w(u)d u}{\int_{0}^{x}w(u)d u}}.$$
0 w(u)du. ✷
$${\mathrm{ons~for~}}w-G F R.$$
The following theorem gives equivalent conditions for w − **GF R**.

Theorem 3.5 Let X has increasing (decreasing) w-GFR.Then the following conditions are equivalent.

1. $\left(\frac{1}{f_{0}^{x}\,w(u)du}\right)\!\!\left(\int_{0}^{x}w(u)\ln h(u)du\right)$ _is increasing (decreasing) in_ $x>0$_._ 2. $\left(\int_{0}^{x}w(u)\ln h(u)du\right)$ _is weighted star-shaped (weighted anti-star shaped) with respect to_ $c(\cdot)$_._
(iii) For α ∈ [0, 1], and x > 0,R αx
0 w(u**) ln** h(u)du ≤ (≥)
$$u\leq(\geq){\frac{\int_{0}^{\alpha x}w(u)d u}{\int_{0}^{x}w(u)d u}}{\bigg(}\int_{0}^{x}w(u)\ln h(u)d u{\bigg)}.\qquad\qquad\Box$$
We note that, 0 ≤
R αx
$${\frac{w(u)d u}{w(u)d u}}\leq1\,\sin\,$$
R x
0 w(u)du ≤ 1 since w(x) ≥ 0 for all x ≥ **0 and 0** ≤ α ≤ 1.
$$\square$$

$${\textrm{d}}0\leq\alpha\leq1.$$

## 3.2 Results On Coherent System

In this section, we primarily focus on Iw-AFR class and its closure properties. We know that IFRA
class is closed under the formation of coherent system. Naturally, a question ponders, whether the same result is true for increasing weighted AFR class (Iw-AFR). Let us consider a coherent system with n **components having weighted survival functions** F¯w i
(x) for i = 1, 2, . . . , n. **The survival**
function F¯w(x**) of the resultant coherent system satisfies**

$$\bar{F}^{w}(\alpha x)=h(\bar{F}_{1}^{w}(\alpha x),\bar{F}_{2}^{w}(\alpha x),\ldots,\bar{F}_{n}^{w}(\alpha x)),$$
$$(3.6)$$
(αx)), **(3.6)**
where h **represents the survival function of the coherent system. Further, if we assume that each**
Xi **has increasing w-AFR, then we explore what would be the survival function of the resultant**
coherent system. Since F¯w i
(αx) ≥
F¯w i
(x)

R αx 0 w(u)du R x 0 w(u)du for i = 1, 2, . . . , n, α ∈ [0, 1], x > 0, and h is increasing in each argument, (3.6) reduces to

$$\bar{F}^{w}(\alpha t)\geq h\Big{(}\big{(}\bar{F}_{1}^{w}(x)\big{)}^{\frac{\int_{0}^{\alpha x}w(u)du}{\int_{0}^{\alpha}w(u)du}},\big{(}\bar{F}_{2}^{w}(x)\big{)}^{\frac{\int_{0}^{\alpha x}w(u)du}{\int_{0}^{\alpha}w(u)du}},\ldots,\big{(}\bar{F}_{n}^{w}(x)\big{)}^{\frac{\int_{0}^{\alpha x}w(u)du}{\int_{0}^{\alpha}w(u)du}}\big{)}$$

The following counterexample shows that Iw-AFR is not closed under the formation of coherent system.

Counterexample 3.1 Let us consider a series system with lifetime X **formed by two components**
with lifetimes Xw 1and Xw 2respectively. Let the failure rates be h1(t), and h2(t) **with corresponding**
weights w1(t) and w2(t) respectively. Let h1(t) = αβtβ−1, w1(t) = e nt, and h2(t) = abtb−1, w2(t) =
(1 − e nt) where α, a > 0; β, b > 1; n < 0. Since, β, b > 1; h1(t) and h2(t) **are increasing in** t. By Theorem 3.1, it follows that Aw 1
(t) and Aw 2
(t) are increasing in t as h1(t) and h2(t) **are increasing**
in t. Then the hazard rate of the series system is given by hX (t) = h1(t)w1(t) + h2(t)w2(t) for all t > 0. **From Example 3.1, it follows that each of** h w 1
(t) = h1(t)w1(t) and h w 2
(t) = h2(t)w2(t)
are non-monotonic in t > 0. **(upside-down bathtub curve). Thus,** Xw 1and Xw 2**are Iw-AFR but**
not IFR. Here, X is not Iw-AFR since h(t) **is non-monotonic (as noted in Example 3.1) and**
non-monotonicity of h(t) is transmitted to A(t) **(by Theorem 3.1).**
We end this section by the following remark which once again emphasizes the importance of the concepts introduced in this article which in turn engenders the upcoming section.

Remark 3.1 **In particular, if in the definition 2.2 discussed above, we replace failure rate** h(·) by hazard quantile function hq(·) and w(·) by density quantile function q(·) **respectively, with support**
restricted to [0, 1], **we get quantile version of AFR, GFR and HFR as mentioned in upcoming**
section.

## 4 Quantile Version Of Afr, Gfr And Hfr

The Remark 3.1 is the genesis of this section. The readers would be interested to see how the act of replacing failure rate by hazard quantile function and weight function by density quantile function respectively will differ the rest of the analysis and **is taken up in the present section.** For a random variable X**, quantile function (QF) is defined as**

$$Q(u)=F^{-1}(u)=\operatorname*{inf}{\Big\{}x:F(x)\geq u{\Big\}},0\leq u\leq1$$
$$\quad(4.7)$$. 
o, 0 ≤ u ≤ **1 (4.7)**
gives F Q(u) = u. Differentiating with respect to u, we get f(Q(u))q(u) = 1 or f(Q(u**)) =** 1 q(u)
,
where f(Q(u)) and q(u) = d duQ(u**) are respectively known as the density quantile function and**
quantile density function of X**. From the definition of hazard rate, the corresponding hazard** quantile function is given by

$$h_{q}(u)=h(Q(u))=\frac{f(Q(u))}{F(Q(u))}=\frac{1}{(1-u)q(u)}.$$

This implies q(u) = 1
(1−u)hq(u)
. Integrating, we get Q(u) = R u 0 1
(1−p)hq(p)
dp**. The quantile approach**
is an alternative to the traditional distribution function **method as it can also used to specify a**
probability distribution. As the quantile approach possess some interesting properties not shared by its distribution function counterpart and in many situations, quantile measures provide simple expressions that are easily amenable to many computational **analysis. Abundant literature are now**
available on various properties of quantile functions and different measures based on it and their applications, for details see Gilchrist (2000), Nair et al. **(2013), Nair et al. (2023) and Aswin et al.**
(2023) and references therein.

Note that, the quantile version of AFR, GFR and HFR, denoted by QA(·), QG(·), QH(·) respectively, can be independently derived using quantile approach. Alternatively, we can obtain the same by applying the Remark 3.1 (ii) in Definition 2.2, i.e., replacing the failure rate h(·**) by**
hazard quantile function hq(·) and w(·) by density quantile function q(·**) respectively, with support**
restricted to [0, 1].

$$QA(u)=QA(Q(u))=\frac{-\ln(1-F(Q(u)))}{Q(u)}\tag{4.8}$$ $$=\frac{-\ln(1-u)}{Q(u)}=-\Big{(}\ln(1-u)\Big{)}\Big{\{}\int_{0}^{u}\frac{1}{(1-p)h_{q}(p)}dp\Big{\}}^{-1}.$$
$$\begin{array}{r c l}{{Q G(u)=Q G(Q(u))}}&{{=}}&{{\exp\left(\frac{1}{Q(u)}\int_{0}^{u}\ln\left(\frac{1}{(1-p)q(p)}\right)d Q(p)\right)}}\\ {{}}&{{=}}&{{\exp\left(-\,\frac{1}{Q(u)}\int_{0}^{u}q(p)\ln\left((1-p)q(p)d p\right)\right),}}\end{array}$$

or equivalently,

$$\begin{array}{r c l}{{Q(u)\ln Q G(u)}}&{{=}}&{{-\int_{0}^{u}(\ln(1-p))q(p)d p-\int_{0}^{u}(\ln q(p))q(p)d p}}\\ {{}}&{{=}}&{{-\int_{0}^{u}q(p)\ln\left\{(1-p)q(p)\right\}d p=\int_{0}^{u}q(p)\ln h_{q}(p)d p}}\end{array}$$
$$(4.9)$$

and

$$QH(u)=QH(Q(u))=\left(\frac{1}{Q(u)}\int_{0}^{u}\frac{1}{h(Q(p))}dQ(p)\right)^{-1}\tag{4.10}$$ $$=Q(u)\Big{(}\int_{0}^{u}(1-p)(q(p))^{2}dp\Big{)}^{-1}$$ $$=Q(u)\Big{(}\int_{0}^{u}\frac{q(p)}{h_{q}(p)}dp\Big{)}^{-1}.$$

Differentiating (4.8) with respect to u**, we obtain**

$$Q A^{\prime}(u)Q(u)+Q A(u)q(u)={\frac{1}{1-u}}$$

When quantile AFR is increasing (decreasing), we get

$$Q A(u)\leq(\geq)\ h_{q}(u).$$
From (4.10), we have
$${\frac{Q(u)}{Q H(u)}}=\int_{0}^{u}(1-p)(q(p))^{2}d p.$$ we got. 
Differentiating with respect to u**, we get**

$$Q H(u)q(u)-Q(u)Q H^{\prime}(u)=(1-u)(q(u))^{2}\,(Q H(u))^{2}\,.$$

Now when the quantile HFR is increasing (decreasing), yield

$$Q H(u)\leq(\geq)h_{q}(u).$$

A similar arguement as given in Theorem 3.1 depicts that monotonicity of hazard quantile function hq(·) is transmitted to quantile version of AFR, GFR and HFR, i.e., QA(·), QG(·**) and** QH(·). In continuation to the Proposition 2.2 of previous section, if we replace w(·) by q(·) and h(·**) by** hq(·),
we find that proportionality of weighted means of quantile hazard functions with quantile hazard function characterizes some quantile function. To the best of our knowledge, Q(x**) as obtained in** Proposition 4.1 represents a new generalized version of quantile function where Q(0) 6= 0.

The next example gives the quantile function of AFR, GFR and HFR of Pareto-I distribution.

Example 4.1 For Pareto I distribution, with quantile function Q(u) = α(1 − u)
−1/α, **we have**

$$QA(u)=-\frac{(1-u)^{1/\alpha}\log(1-u)}{\alpha},QG(u)=e^{1-(1-u)^{1/\alpha}}(1-u)^{1/\alpha},\text{and}\text{}QH(u)=-\frac{2(1-u)^{1/\alpha}}{(1-u)^{2/\alpha}-1},$$  _for $0<u<1$._
$$\mathbb{D}$$

Proposition 4.1 Let hazard quantile function hq(u) be differentiable for all u ∈ [0, 1]. **Then for**
the non-negative weight function q(u), called as density quantile function and for a, b, c > 0 **we have**

_(i) $QA(u)=a\ h_{q}(u)$ for all $u\in[0,1]$ if and only if $Q(u)=\left(\frac{1}{ak}\right)^{a}\left\{\ln(\frac{A}{1-u})\right\}^{a}$._
_(ii)_: $QG(u)=b\ h_{q}(u)$ _for all_ $u$ _if and only if_ $Q(u)=\left(\frac{\ln(e/b)}{k}\right)^{\frac{1}{\ln(e/b)}}\left\{\ln(\frac{A}{1-u})\right\}^{\frac{1}{\ln(e/b)}}$_._ 3. $QH(u)=c\ h_{q}(u)$ _for all_ $u$ _if and only if_ $Q(x)=\left(\frac{\ln(e/b)}{k}\right)^{\frac{1}{\ln(e/b)}}\left\{\ln(\frac{A}{1-u})\right\}^{\frac{1}{\ln(e/b)}}$ _where_ $k$ _is an arbitrary constant._
Proof. From Theorem 2.2 (i), it follows that QA(u) = a hq(u**) is equivalent to**

$$h_{q}(u)=k{\bigg(}\int_{0}^{u}q(p)d p{\bigg)}^{(1-a)/a}$$

and since $h_{q}(u)=\frac{1}{(1-u)q(u)}$, we prove $(i)$. Proofs of $(ii)$ and $(iii)$ are similar.  
, we prove (i). Proofs of (ii) and (iii**) are similar.** ✷
Transformation on a random variable is generally employed to find the best model for a given set of observations. A simple alternative method to this is to keep the original data as it is and transform the QF to find the best model, using the following property of quantile functions which is not shared by the distribution function. If TX(x**) is a continuous non-decreasing function then**
TX (QX(u)) is the QF of TX (X**) or in symbols**

$$Q_{T(X)}(u)=T\left(Q_{X}(u)\right).$$

Theorem 4.1 Let T(·) **be a continuous non-decreasing and invertible transformation. Then the**
quantile versions of AFR, GFR and HFR takes the form

1. $QA_{T(X)}(u)=\frac{-\log(1-u)}{T(Q_{X}(u))}$, 2. $QG_{T(X)}(u)=\exp\Big{(}-\frac{1}{T(Q_{X}(u))}\int_{0}^{u}T^{\prime}\left(Q_{X}(p)\right)q(p)\left[\log(1-p)T^{\prime}\left(Q_{X}(p)\right)q(p)\right]dp\Big{)}$, and 3. $QH_{T(X)}(u)=T\left(Q_{X}(u)\right)\Big{(}\int_{0}^{u}(1-p)\left(T^{\prime}\left(Q_{X}(p)\right)q(p)\right)^{2}dp\Big{)}^{-1}$.  
Theorem 4.2 The following statements are equivalent: (i) X **follows Exponential distribution with**
shape parameter c, (ii) QA(u) = c, (iii) QG(u) = c, and (iv) QH(u) = c. ✷
Remark 4.1 **The quantile version is not always equivalent to its distribution function approach.**
Theorem 4.3 QA(u) = (Q(u))C−1, where C > 0 holds if and only X **follows Weibull distribution**
with quantile function Q(u) = (− **log(1** − u))
1 λ , 0 < u < 1**, λ >** 0. ✷
For many models, the distribution function and quantile approches yield similar properties as we have seen in Theorem 4.2, while for certain other cases, it **gives different results. For example,**
when X and Y **satisfy proportional hazard rate model (PHM), we have** hqY
(u) = θhqX
(u), or equivalently, we have F¯Y (u) = F¯X (u)θ. **We look at the corresponding AFR, GFR and HFR of** Y .

It is easy to note that AY (x) = θ AX (x), GY (x) = θ GX (x) and HY (x) = θ HX(x**). To obtain the**
quantile version of AFR, GFR and HFR under PHM, it is easy to obtain the QF of Y **, as**

$$Q_{Y}(u)=\operatorname*{inf}\left\{x:F_{Y}(x)\geq u\right\}=Q_{X}(1-(1-u)^{1/\theta}),$$

which in turn obtain the quantile version of AFR for PHM as

$$Q A_{Y}(u)=-{\frac{\ln(1-u)}{Q_{Y}(u)}}={\frac{-\ln(1-u)}{Q_{X}(1-(1-u)^{1/\theta})}}=\theta Q A_{X}(1-(1-u)^{1/\theta})\neq\ \ \theta Q A_{X}(u),$$

since

$$QA_{X}(1-(1-u)^{1/\theta})=\frac{-\ln\left\{\left\{1-(1-(1-u)^{1/\theta})\right\}\right\}}{Q_{X}(1-(1-u)^{1/\theta})}=-\frac{1}{\theta}\frac{\ln(1-u)}{Q_{X}(1-(1-u)^{1/\theta})}.\tag{4.12}$$  The quantile GFR of PHM will be 
$$Q G_{Y}(u)=\exp\Bigg[-\frac{1}{Q_{X}\left(1-(1-u)^{\frac{1}{\theta}}\right)}\int_{0}^{u}\!\!\frac{1}{\theta}q_{X}\left(1-(1-p)^{\frac{1}{\theta}}\right)(1-p)^{\frac{1}{\theta}-1}$$ $$\ln\left(\frac{1}{\theta}q_{X}\left(1-(1-p)^{\frac{1}{\theta}}\right)(1-p)^{\frac{1}{\theta}}\right)d p\Bigg],$$

or equivalently

$$Q G_{Y}(u)=\exp\left[-\frac{1}{Q_{X}(u)}\int_{0}^{1-(1-u)^{\frac{1}{\theta}}}\frac{1}{\theta}q_{X}(p)(1-p)^{1-\theta}\ln\left((1-p)\frac{1}{\theta}q_{X}(p)\right)\right]\neq\theta\ \mathcal{Q G}_{X}(u).$$

Also, the quantile version of HFR becomes

$$QH_{Y}(u)=\left(\frac{1}{Q_{X}\left(1-(1-u)^{\frac{1}{\theta}}\right)}\int_{0}^{u}\frac{1}{\theta}(1-p)^{\frac{\theta}{2}-1}q_{X}\left(1-(1-u)^{\frac{1}{\theta}}\right)^{2}\right)^{-1}\neq\theta\ QH_{X}(u).$$  Clearly illustrates that quantile version of the AEP, CEP and HEP for the PHM not satisfied.  
This clearly illustrates that quantile version of the AFR, GFR and HFR for the PHM not satifying the properties those hold in the distribution function approach.

## 5 Conclusion

At the long last, for readers we reiterate that mixture of n distributions is a special case of formation of n **independent component series system having weighted failure rates with the sum of** weight functions being unity. However, the latter system having arbitrary weights is also not a generalization of the former. The idea of relating the said concepts deserves some credit because the existing literature on mixture of distributions can be extended to the formation of coherent systems (in particular, series system) so far as non-preservation properties of reliability operations are concerned. One can generate new distributions using weighted version of arithmetic, geometric and harmonic means of failure rate. Since, the quantile version of means of hazard rate is a special case of weighted means of failure rate, the properties studied for weighted means is put forth for the prior.

## Acknowledgement

Subarna Bhattacharjee would like to thank Odisha State Higher Education Council for providing support to carry out the research project under OURIIP, Odisha, India (Grant No. 22-SF-MT-073).

## References

[1] Aswin, I. C., Sankaran, P. G., and Sunoj, S. M. (2023). Some reliabiility aspects of record values using quantile functions, Communications in Statistics-Theory and Methods**, DOI:** 10.1080/03610926.2023.2189499.

[2] Balakrishnan, N., Barmalzan, G. and Haidari, A. (2018). Modified proportional hazard rates and proportional reversed hazard rates models via **Marshall-Olkin distribution**
and some stochastic comparisons, Journal of the Korean Statistical Society**, 47, 127–138.**
https://doi.org/10.1016/j.jkss.2017.10.003
[3] Barlow, R. E. and Proschan, F., (1975). **Statistical Theory of Reliability and Life Testing:**
Probability Models**. Holt, Rinehart and Winston, New York.**
[4] Bhattacharjee, S., Mohanty, I., Szymkowiak, M. and Nanda, A. K. (2022). Properties of aging functions and their means, **Communication in Statistics- Simulation and Computation**, Available Online. DOI: 10.1080/03610918.2022.2141257.

[5] Gilchrist, W. (2000). Statistical Modelling with Quantile Functions**. Boca Raton, Florida:**
Chapman and Hall/CRC.

[6] Gupta, R. C., and Kirmani, S. N. (1990). The role of weighted distributions in stochastic modeling. Communication in Statistics - Theory and Methods**, 19, 3147-3162.**
https://doi.org/10.1080/03610929008830371
[7] Jiang, R., Ji, P., Xiao, X., 2003. Aging property of univariate failure rate models. Reliability Engineering and System Safety 39, 113–116. https://doi.org/https://doi.org/10.1016/S09518320(02)00175-8
[8] Kies, J.A., 1958. The strength of glass. Naval Research Lab., Washington DC. Report No.

5093.

[9] Marshall, A. W., and Olkin, I. (1997). A new method for adding a parameter to a family of distributions with application to the exponential and Weibull families.

https://www.jstor.org/stable/2337585 Biometrika**, 84, 641–652.**
[10] Marshall, A.W., Olkin, I. (2007). Life Distributions**. Springer, New York.**
[11] Nair, N.U., Sankaran, P.G., and Balakrishnan, N. (2013). **Quantile-Based Reliability Analysis**.

Statistics for Industry and Technology, New York, NY: Birkhauser.

[12] Nair, N.U., Sunoj, S.M., and Suresh, N. (2023). Additive hazards quantile model, **Metrika**,
DOI: 10.1007/s00184-023-00924-2.

[13] Patil G. P. and Ord, J. K. (1976). On Size-Biased Sampling and Related Form-Invariant Weighted Distributions, Sankhy¯a: The Indian Journal of Statistics**, Series B (1960-2002),**
38(1), 48-61.

[14] Patil, G. P., and Rao, G. R. (1978). Weighted distributions and size biased sampling with applications to wildlife populations and human families. Biometrics**, 34, 179-189.**
https://doi.org/10.2307/2530008
[15] Rao, C. R. (1965). On discrete distributions arising out of methods of ascertainment. In Classical and Contagious Discrete Distributions**. Patil, G. P. ed. Pergamon Press and Statistical** Publishing Society, Calcutta, 320-332. http://www.jstor.org/stable/25049375
[16] Roy, D. and Mukherjee, S.P. (1992). Characterizations **based on arithmetic, geometric and**
harmonic means of failure rates, In: Contributions to Stochastics**, Venugopal N. (ed.), Wiley,** 178-185.

[17] Wijsman, R. A. (1985). A useful inequality on ratios of integrals, with application to maximum likelihood estimation, Journal of the American Statistical Association**, 80 (390), 472- 475.** https://doi.org/10.2307/2287917