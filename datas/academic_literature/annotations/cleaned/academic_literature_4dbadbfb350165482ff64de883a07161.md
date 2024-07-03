# On weighted failure rate, its means and associated quantile version 

Subarna Bhattacharjee ${ }^{1 *}$, S.M. Sunoj ${ }^{2}$, Sabana Anwar ${ }^{3}$<br>1,3 Department of Mathematics, Ravenshaw University, Cuttack, Odisha, India<br>${ }^{2}$ Department of Statistics, Cochin University of Science and Technology, Cochin, Kerala, India

April 11, 2024


#### Abstract

In this paper, we define weighted failure rate and their different means from the stand point of an application. We begin by emphasizing that the formation of $n$ independent component series system having weighted failure rates with sum of weight functions being unity is same as a mixture of $n$ distributions. We derive some parametric and non-parametric characterization results. We discuss on the form invariance property of baseline failure rate for a specific choice of weight function. Some bounds on means of aging functions are obtained. Here, we establish that weighted IFRA class is not closed under formation of coherent systems unlike the IFRA class. An interesting application of the present work is credited to the fact that the quantile version of means of failure rate is obtained as a special case of weighted means of failure rate.


Keywords and Phrases: Weighted distribution, weighted failure rate, weighted arithmetic mean failure rate, weighted geometric mean failure rate, weighted harmonic mean failure rate.

AMS 2020 Subject Classification: Primary 60E15, Secondary 62N05, 60E05

## 1 Introduction

The notion of ageing plays an important role in reliability theory and in the study of lifetime data analysis. Ageing of a mechanical or biological component based on a lifetime distributions is generally studied using the residual lifetime of the unit that is affected its age. Abundant literature is available on various ageing concepts and their patterns of ageing, comparison of life distributions and to explain their data generating mechanism. Reliability ageing classes based on the monotonicity of the failure rate, such as increasing (decreasing) failure rate (IFR (DFR)) and its average, increasing (decreasing) failure rate average (IFRA (DFRA)) have been found great interest among researchers as it easily give an indication on the manner in which ageing can be described, life[^0]distributions can be classified and distinguished, and appropriate models can be chosen when observations are available (cf. Barlow and Proschan (1975)).

Let $X$ be a non-negative random variable representing the lifetime of an event or living mechanism with absolutely continuous distribution function $F(\cdot)$ and probability density function (pdf), $f(\cdot)$. Then $F$ is said to be IFR (DFR), if the conditional survival function $\bar{F}(x \mid t)=\frac{\bar{F}(x+t)}{F(x)}$ is decreasing (increasing) in $0 \leq t<\infty$, where $\bar{F}=1-F$ is the survival (reliability) function; or equivalently the failure rate $h(t)=\frac{f(t)}{F(t)}$ is increasing (decreasing) in $t \geq 0$, provided $f(t)$ exists. Further, $F$ is said to IFRA (DFRA), if $-\left(\frac{1}{t}\right) \log \bar{F}(t)$ is increasing (decreasing) in $t \geq 0$. However, in many real situations, $h(x)$ is not always monotonic. In such cases, the monotonicity of IFRA class condition in terms of the failure rate, $\frac{1}{t} \int_{0}^{x} h(t) d t$, known as the arithmetic mean failure rate (AFR) is a useful measure (Roy and Mukherjee (1992)) in identifying the monotonicity of classes of life distributions. Along with arithmetic mean failure rate, Roy and Mukherjee (1992) have also studied classes of distributions through the monotonic behaviour of geometric failure rate (GFR) and harmonic failure rate (HFR), and the characterizations and ageing classes based on it. They pointed out until then no work has been done on GFR and HFR. The following definition is cited from Roy and Mukherjee (1992).

Definition 1.1 Let $X$ be a non-negative random variable with absolutely continuous $C D F F(\cdot)$, PDF $f(\cdot)$ and failure rate $h(\cdot)$. Then the arithmetic mean failure rate (AFR), geometric mean failure rate (GFR) and harmonic failure rate (HFR), denoted by $A(\cdot), G(\cdot)$ and $H(\cdot)$ respectively are defined as $A(x)=\frac{1}{x} \int_{0}^{x} h(u) d u, x>0 ; G(x)=\exp \left(\frac{1}{x} \int_{0}^{x} \ln h(u) d u\right) ; H(x)=\left(\frac{1}{x} \int_{0}^{x} \frac{1}{h(u)} d u\right)^{-1}$.

Recently, Bhattacharjee et al. (2022) further studied the usefulness of the three measures based on the notion of ageing intensity (AI) function proposed by Jiang et al. (2003).

When sample observations are not equally likely, we use the weighted measures to capture the significance of their relative importance. Choosing appropriate weights, we can then compute various measures in a better way by giving appropriate weights based on the sample mechanism. Such biased sampling schemes are usually employed in observational studies either due to its convenience or its cost-effectiveness. Based on this, Rao (1965) identified the concept of weighted distributions in connection with the modeling statistical data, in situations where the usual practice of employing standard distributions for the purpose was not found appropriate. These distributions occur frequently in the studies related to reliability, analysis of family data, meta analysis and analysis of intervention data, biomedicine, ecology, etc, for more details, see Patil and Rao (1978), Gupta and Kirmani (1990), and the references therein. If $X$ is a non-negative random variable with a probability density function (pdf) $f(x)$, then the pdf of the weighted random variable $X^{w}$ is given by, $f_{w}(x)=\frac{w(x) f(x)}{E w(X)}, x>0$, where $w(\cdot)$ is a non-negative weight function (cf. Rao (1965)). There are many weight functions used by different authors, however, the weight functions $w(x)=x$ and
$w(x)=x^{\alpha}, \alpha>0$ are found to be more popular due to its adaptibility in terms of identifying the observed distribution in various applied problems wherein the probability of selecting the sample units are proportional to the length or size of the population units, the respective random variables are known as the length-biased and size-biased random variables. Motivated by these, in the present study, we propose weighted mean failure rates based on the measures of AFR, GFR and HFR.

The paper is organized as follows. In Section 2, we introduce the definitions of weighted means of failure rate along with citing an application. As an application of weighted failure rates as proposed in this paper, we note that formation of an $n$ component series system having complementary weight functions is actually a mixture of $n$ distributions and vice-versa. We give some parametric and non-parametric characterization results. Section 2 gives a note on form invariance property of the baseline failure rate and its transformation from one aging class to another depending upon the choice of the weight function. Section 2 also highlights on some bounds of means of aging functions. We focus on some new non-parametric aging classes based on means of failure rate and discuss their inclusive properties. Some illustrative examples are given for ready reference. Some equivalent conditions of aging classes based on geometric and harmonic means are obtained. We prove our claim that weighted IFRA class is not closed under formation of coherent systems unlike IFRA class by giving an easy counterexample. In Section 4, we derive the quantile version of means of failure rate as special case from weighted means of failure rate. We study the proportional quantile hazards model and compare it with conventional proportional hazards model. Concluding remarks are listed in Section 5.

## 2 Weighted means of failure rate

In this paper, we introduce a generalized versions of AFR, GFR and HFR involving a suitable choice of a non-negative weight function as defined below.

Definition 2.1 Let $X$ be a non-negative random variable with absolutely continuous distribution function $F(\cdot)$, probability density function $f(\cdot)$ and failure rate $h(\cdot)$. The weighted arithmetic mean failure rate ( $w-A F R$ ), weighted geometric mean failure rate ( $w$-GFR) and weighted harmonic failure rate (w-HFR) denoted by $A^{w}(\cdot), G^{w}(\cdot)$ and $H^{w}(\cdot)$ respectively, with a suitable non-negative weight function $w(\cdot)$, are defined as

(i) $A^{w}(x)=\frac{\int_{0}^{x} w(u) h(u) d u}{\int_{0}^{x} w(u) d u}, x>0$;

(ii) $G^{w}(x)=\exp \left(\frac{\int_{0}^{x} w(u) \ln h(u) d u}{\int_{0}^{x} w(u) d u}\right), x>0$;

(iii) $H^{w}(x)=\left(\int_{0}^{x} w(u) d u\right)\left(\int_{0}^{x} \frac{w(u)}{h(u)} d u\right)^{-1}, x>0$.

Clearly, if $w(x)=1$ for all $x \geq 0$ then above definition reduces to that of AFR, GFR and HFR given in Definition 1.1 due to Roy and Mukherjee (1992).

In the pretext, of above, we shall define the other reliability functions of the weighted random variable as given in the following definition.

Definition 2.2 The weighted survival function of $X$, or survival function of weighted random variable $X^{w}$, denoted by $\bar{F}^{w}(\cdot)$ is defined as $\bar{F}^{w}(x)=\exp \left(-\int_{0}^{x} w(u) h(u) d u\right), x>0$. The density and failure rate function of $X^{w}$ are $f^{w}(x)=w(x) h(x) \exp \left(-\int_{0}^{x} w(u) h(u) d u\right)$ and $h^{w}(x)=w(x) h(x)$ for all $x>0$, respectively.

The fact that $h^{w}(x)=w(x) h(x)$ reminds us of proportional hazard models (PHR) where $h(x)$ is the baseline failure rate and $w(x)$ is the proportionality function giving rise to a new hazard rate $h^{w}(\cdot)$.

Referring to the related literature, one can notice that corresponding to the baseline survival function $\bar{G}$ having failure rate $r_{G}$, Marshall and Olkin (1997) proposed a cumulative distribution function $F$ such that its hazard rate $h_{F}(\cdot)$ is given by $h_{F}(x, \alpha)=\frac{1}{1-\bar{\alpha} \bar{G}(x)} h_{G}(x)$ where $x, \alpha \in R^{+}$ and $\bar{\alpha}=1-\alpha$, ( the parameter $\alpha$ termed as tilt parameter by Marshall and Olkin (2007)) and this is a special case of Definition 2.2 if one assumes $w(x)=\frac{1}{1-\bar{\alpha} \bar{G}(x)}$. Furthermore, Balakrishnan et al. (2018) defined modified proportional hazard rates (MPHR) of $n$ independent components having lifetimes $X_{1}, X_{2}, \ldots, X_{n}$ with respective survival functions $\bar{F}_{i}$ if

$$
F_{i}\left(x, \lambda_{i}\right)=\frac{1-(\bar{F}(x))^{\lambda_{i}}}{1-\bar{\alpha}(\bar{F}(x))^{\lambda_{i}}}, \alpha>0, \bar{\alpha}=1-\alpha, \lambda_{i}>0
$$

for $i=1,2, \ldots, n$ where $\bar{F}$ is the corresponding baseline survival function. They considered it (MPHR model) to be the generalization of PHR model because if $\alpha=1$ then PHR is a special case of MPHR. However, one shall observe that this is based on the notion that $X_{i}$ 's with survival functions $\bar{F}_{i}(x)$ follow PHR model if there exits positive constants $\lambda_{i}$ 's such that $\bar{F}_{i}(x)=\bar{F}^{\lambda_{i}}(x)$. It is worthwhile to note that the definition of MPHR proposed by Balakrishnan et al. (2018) is not based on the fact that $h_{i}(x)=h(x) w(x)$ where $h(x)$ is considered to be the baseline failure rate. The present work, in other words, is an attempt to define PHR model in a more general sense.

We now give a necessary and sufficient condition that weight function $w(x)$, and hazard rate $h(x)$ must satisfy so that $\bar{F}^{w}(x)$ represents a (weighted) survival function. One can refer to Marshall and Olkin (2007) to look into the postulates for hazard rate (non-weighted).

(i) $w(x) \geq 0, h(x) \geq 0$.

(ii) For $x>0, \int_{0}^{x} w(u) h(u) d u<\infty$
(iii) $\int_{0}^{\infty} w(u) h(u) d u=\infty$

(iv) If $\int_{0}^{x} w(u) h(u) d u=\infty$ for some $x$ then $h(y)=\infty$ for every $y>x$.

Now, we look into some uses of weighted failure rate arising in practical field. Let us consider a series system formed by $n$ components having failure rates $h_{i}(x)$ with respective weights $w_{i}(x)$, for $i=1,2, \ldots, n$ and $x>0$ such that $\sum_{i=1}^{n} w_{i}(x)=1$. The failure rate $h(x)$ of the resultant $n$ component series system is $h(x)=\sum_{i=1}^{n} h_{i}(x) w_{i}(x)$. This form of $h(x)$ is similar to the failure rate of the mixture of $n$ distributions, with cumulative distributions, $F_{i}(\cdot)$ having failure rates, $h_{i}(\cdot)$ for $i=1,2, \ldots, n$. The failure rate of mixture of $n$ distributions is given by $F(x)=\sum_{i=1}^{n} \pi_{i} F_{i}(x)$, with $\sum_{i=1}^{n} \pi_{i}=1$ is

$$
\begin{aligned}
h(x) & =\frac{\sum_{i=1}^{n} \pi_{i} f_{i}(x)}{1-\sum_{i=1}^{n} \pi_{i} F_{i}(x)} \\
& =\frac{\sum_{i=1}^{n} \pi_{i} h_{i}(x) \bar{F}_{i}(x)}{\sum_{i=1}^{n} \pi_{i} \bar{F}_{i}(x)}=\sum_{i=1}^{n} p_{i}(x) h_{i}(x)
\end{aligned}
$$

where $p_{i}(x)=\frac{\pi_{i} \bar{F}_{i}(x)}{\sum_{i=1}^{n} \pi_{i} \overline{F_{i}}(x)}$ which in turn satisfies $\sum_{i=1}^{n} p_{i}(x)=1$.

Unlike the log-exponential family (cf. Patil G. P. and Ord, J. K. (1976)) which possesses the form-invariance property among the weighted distributions defined by Rao (1965) under size based sampling of order $c>0$, (i.e., $w(x)=x^{c}$ ), in the present work Weibull distribution bear the said property. If a given Weibull distribution with failure rate $h(x)=\alpha \beta x^{\beta-1}$ belongs to positive aging classes, namely IFR, then the resultant size biased distribution also fall in the same aging class, but this may not be true for DFR negative aging class, i.e., if $\beta+c>1$ then the baseline DFR Weibull distribution is shifted to IFR positive aging class under size based sampling.

Additive Weibull distribution with failure rate $h(x)=\alpha \theta x^{\theta-1}+\beta \gamma x^{\gamma-1}$ with $\alpha, \beta, \theta, \gamma>0$ has form-invariance property under size biased sampling. However, the weight function $w(x)=x^{c}$ drags the additive Weibull distribution from DFR class to IFR class if $c+\theta>$ and $c+\gamma>1$.

If $X$ follows four-parameter Weibull distribution (cf. Kies (1958)) with survival function

$$
\bar{F}(t)=\exp \left(-\lambda\left(\frac{t-a}{b-t}\right)^{\beta}\right), 0 \leq a<t<b, \lambda, \beta>0
$$

then $w(t)=\left(\frac{t-a}{b-t}\right)$ is a form-invariance weight function for the distribution. We know that $X$ has bathtub failure rate if $0<\beta<1$, and IFR if $\beta>1$ but the weighted random variable $X^{w}$ is always IFR independent of $\beta$ under the aforementioned weighted transformation.

### 2.1 Characterization results

Now, we prove that the equality of any two of w-AFR, w-GFR and w-HFR characterize exponential distribution. The following proposition gives some light on this. We continue with the same notations as discussed in previous sections of the paper.

Proposition 2.1 A non-negative random variable $X$, follows exponential distribution if and only if for $x>0$, any one of the following hold

(i) $A^{w}(x)=G^{w}(x)$

(ii) $G^{w}(x)=H^{w}(x)$

(iii) $A^{w}(x)=H^{w}(x)$.

Proof. If $X$ follows exponential distribution then it is easy to prove that (i), (ii) and (iii) hold. Conversely, if (i) holds then

$$
\frac{\int_{0}^{x} w(u) h(u) d u}{\int_{0}^{x} w(u) d u}=\exp \left(\frac{\int_{0}^{x} w(u) \ln h(u) d u}{\int_{0}^{x} w(u) d u}\right)
$$

gives

$$
\left(\int_{0}^{x} w(u) d u\right)\left\{\ln \left(\int_{0}^{x} h(u) w(u) d u\right)\right\}=\left(\int_{0}^{x} w(u) d u\right)\left(\ln \int_{0}^{x} w(u) d u\right)+\int_{0}^{x} w(u) \ln h(u) d u
$$

Differentiating (2.1) with respect to $x$, we get $\ln \left(e z_{1}(x)\right)=z_{1}(x)$ where

$$
z_{1}(x)=\frac{h(x) \int_{0}^{x} w(u) d u}{\int_{0}^{x} w(u) \ln w(u) h(u) d u}
$$

Thus, $z_{1}(x)=1$, for all $x \geq 0$, gives $\left(\frac{d}{d x} h(x)\left(\int_{0}^{x} w(u) d u\right)=0\right.$, and since $\int_{0}^{x} w(u) d u \neq 0$, we conclude that $h(x)$ is constant for all $x \geq 0$. This proves that $X$ has exponential distribution. Similarly, if (ii) holds then

$$
\exp \left(\frac{\int_{0}^{x} w(u) \ln h(u) d u}{\int_{0}^{x} w(u) d u}\right)=\left(\int_{0}^{x} w(u) d u\right)\left(\int_{0}^{x} \frac{w(u)}{h(u)} d u\right)^{-1}
$$

or equivalently

$$
\int_{0}^{x} w(u) h(u) d u+\left(\int_{0}^{x} w(u) d u\right) \ln \left(\int_{0}^{x} \frac{w(u)}{r(u)} d u\right)=\left(\int_{0}^{x} w(u) d u\right) \ln \left(\int_{0}^{x} w(u) d u\right)
$$

After differentiating (2.2), we get $\ln \left(e z_{2}(x)\right)=z_{2}(x)$ where

$$
z_{2}(x)=\frac{\int_{0}^{x} w(u) d u}{h(x)\left(\int_{0}^{x} \frac{w(u)}{h(u)} d u\right)}
$$

Hence, $z_{2}(x)=1$ which in turn gives $\frac{d}{d x} r(x)\left(\int_{0}^{x} \frac{w(u)}{h(u)} d u\right)=0$. Since $\left(\frac{w(u)}{J_{0}^{x} h(u)} d u\right) \neq 0$, it follows that $h(x)=$ constant. This proves that if $(i i)$ holds then $X$ has exponential distribution.

Note that if (iii) holds then it is equivalent to the fact that

$$
\left(\int_{0}^{x} w(u) h(u) d u\right)\left(\int_{0}^{x} \frac{w(v)}{h(v)} d v\right)=\left(\int_{0}^{x} w(u) d u\right)^{2}
$$

Taking logarithm on both sides and then differentiating both sides with respect to $x$, we get

$$
\frac{h(x) \int_{0}^{x} w(u) d u}{\int_{0}^{x} w(u) h(u) d u}+\left(\frac{1}{h(x)}\right)\left(\frac{\int_{0}^{x} w(u) d u}{\int_{0}^{x} \frac{w(v)}{h(v)} d v}\right)=2
$$

Since $\mathrm{w}-\mathrm{HFR}=\mathrm{w}-\mathrm{AFR}$, replacing w-HFR by w-AFR in the second term of (2.4), we get

$$
\frac{h(x) \int_{0}^{x} w(u) d u}{\int_{0}^{x} w(u) h(u) d u}+\left(\frac{1}{h(x)}\right)\left(\frac{\int_{0}^{x} w(u) h(u) d u}{\int_{0}^{x} w(u) d u}\right)=2
$$

Hence,

$$
\left(h(x) \int_{0}^{x} w(u) d u-\int_{0}^{x} w(u) h(u) d u\right)^{2}=0
$$

and this gives $\frac{d}{d x} h(x)=0$ as $\int_{0}^{x} w(u) d u \neq 0$. This completes the proof.

Note that $A^{w}(x)=c$ for all $x>0$ characterizes exponential distribution, and so is true for $G^{w}(\cdot)$ and $H^{w}(\cdot)$. If we simultaneously peep into the lines in the proof of Proposition 2.1, we conclude that (i), (ii) and (iii) get reduced to $A^{w}(x)=G^{w}(x)=H^{w}(x)=c$ for all $x>0$.

In the next proposition we obtain simple relationships between w-AFR, w-GFR and w-HFR functions and hazard rate, that characterize the underlying distributions through their hazard rates. The proof is omitted.

Proposition 2.2 Let $h(x)$ be differentiable for all $x \geq 0$. Then for any non-negative weight function $w(x)$, and for suitable positive values of constants, $a, b, c, k$ we have

(i) $A^{w}(x)=a h(x)$ for all $x$ if and only if $h(x)=k\left(\int_{0}^{x} w(u) d u\right)^{(1-a) / a}$

(ii) $G^{w}(x)=b h(x)$ for all $x$ if and only if $h(x)=k\left(\int_{0}^{x} w(u) d u\right)^{\ln (e / b)-1}$

(iii) $H^{w}(x)=\operatorname{ch}(x)$ for all $x$ if and only if $h(x)=\left(\frac{1}{k c} \int_{0}^{x} w(u) d u\right)^{1-c}$, where $k$ is an arbitrary constant.

One can wonder whether for any particular class of well known probability distribution, weighted means are proportional to their respective hazard rates. If we choose weight function as $w(x)=x^{n}$, then the corresponding failure rate is that of two-parameter Weibull distribution with shape parameter $(n-a n+1) / a$ and scale parameter $k a /\left((n-a n+1)(n+1)^{\frac{1-a}{a}}\right)$, provided $\left(\frac{1+n-a n}{a}\right)>0$. Intuitively, it follows that (ii) and (iii) are also satisfied for two-parameter Weibull distribution having a different sets of scale and shape parameters. We summarize this discussion by claiming that $w(x)=x^{n}$ for suitable $n$, and $x>0$ is a proper choice of weight function as it results in a legitimate probability distribution. A little work out will show that if we choose $w(x)=e^{n x}$, then the resultant failure rate function is $h(x)$ does not correspond to a well defined probability distribution, underlying the fact that proportionality of weighted means and hazard rate do not hold good.

We end this subsection by stating some crucial observations in the upcoming remark.

Remark 2.1 An essence of introducing the weighted version of means of failure rate lies in the aforementioned Proposition 2.2. where a suitable choice of weight function characterizes some well known distributions. The readers may also note that, proportionality of each of $A^{w}(\cdot), G^{w}(\cdot)$ and $H^{w}(\cdot)$ with $h(\cdot)$ imply that $h(x)$ is increasing (decreasing) in $x$ if and only if $a \leq(\geq) 1, b \leq(\geq) 1$, and $c \leq(\geq) 1$ respectively. It is clear that, under the aforementioned conditions, monotonicity of $h(\cdot)$ is independent of the choice of weight function.

### 2.2 Bounds and Limiting behavior of aging means

We state a result from Wijsman (1985) in the form of a lemma.

Lemma 2.1 Let $f_{i}, g_{i}$ are non-negative functions, such that the integrals $\int f_{i} g_{i}$ are positive for $i, j=1,2$. Then

$$
\frac{\int f_{1} g_{1} d \mu}{\int f_{1} g_{2} d \mu} \geq \frac{\int f_{2} g_{1} d \mu}{\int f_{2} g_{2} d \mu}
$$

provided $f_{1} / f_{2}$ and $g_{1} / g_{2}$ are monotonic in same direction. The inequality in (2.5) is reversed if $f_{1} / f_{2}$ and $g_{1} / g_{2}$ are monotonic in opposite direction. Equality holds if and only if either $f_{1} / f_{2}$ or $g_{1} / g_{2}$ is a constant. Here $\mu$ is Lebesgue measure on a subset of the real line or counting measure on a subset of the integers.

The following proposition decides bounds of the aging means on the basis of monotonicity of weight function and hazard rate (as the case may be). An interpretation of the result is

Proposition 2.3 (i) $A^{w}(x) \geq(\leq) A(x)$ according as $w(x)$ and $h(x)$ are monotonic in same (opposite) direction.

(ii) If the hazard rate function $h(x) \geq 1$ for all $x \geq 0$ then $G^{w}(x) \geq(\leq) G(x)$ according as $w(x)$ and $h(x)$ are monotonic in same (opposite) direction.
(iii) $H^{w}(x) \geq(\leq) H(x)$ according as $w(x)$ and $h(x)$ are monotonic in same (opposite) direction.

Proof. We choose $f_{1}(x)=w(x), g_{1}(x)=h(x), f_{2}(x)=g_{2}(x)=1$, to prove $(i)$. By choosing $f_{1}(x)=w(x), g_{1}(x)=\ln h(x), f_{2}(x)=g_{2}(x)=1$, and assuming $\ln h(x) \geq 0$ (since $h(x) \geq 1$ for all $x \geq 0$ ), Lemma 2.1 gives $\left(\frac{\int_{0}^{x} w(u) \ln h(u) d u}{\int_{0}^{x} w(u) d u}\right) \geq(\leq)\left(\frac{1}{x} \int_{0}^{x} \ln h(u) d u\right)$ according as $w(x)$ and $h(x)$ are monotonic in same (opposite) direction. This proves (ii). Similarly, taking $f_{1}(x)=w(x), g_{1}(x)=$ $1, f_{2}(x)=1, g_{2}(x)=1 / h(x)$, we prove $(i i i)$.

The readers may arrive at the following remark by looking at the Proposition 2.3 and the fact that $A^{w}(x) \geq G^{w}(x) \geq H^{w}(x)$ for all $x \geq 0$.

Remark 2.2 If $w(x)$ and $h(x)$ are monotonic in same direction then the lower and upper bounds of the aging means of failure rate are $H(x)$ and $A^{w}(x)$ respectively. On the other hand, $w(x)$ and $h(x)$ are monotonic in opposite direction then the lower and upper bounds of the aging means of failure rate are $H^{w}(x)$ and $A(x)$ respectively. The lower and upper bounds of the aging means of failure rate discussed in this article are $\min \left(H(x), H^{w}(x)\right)$ and $\max \left(A(x), A^{w}(x)\right)$ respectively.

In the following theorem, we obtain bounds for the ratio of the weighted hazard means by associating weights in sequence.

Theorem 2.1 Let $h_{k}(x)=w(x) h_{k-1}(x)=(w(x))^{k} h(x), k \geq 1, h_{0}(x)=h(x)$, for $x>0$. We define $A_{h_{k}}^{w}(x)=\left(\frac{\int_{0}^{x} w(u) h_{k}(u) d u}{\int_{0}^{x} w(u) d u}\right), G_{h_{k}}^{w}(x)=\exp \left(\frac{\int_{0}^{x} w(u) \ln h_{k}(u) d u}{\int_{0}^{x} w(u) d u}\right)$, and $H_{h_{k}}^{w}(x)=\left(\frac{\int_{0}^{x} w(u) d u}{\int_{0}^{x} \frac{w}{h_{k}(u)}(u)}\right)$. For $x>0$, the following statements hold.

(i) If $h(x)$ and $w(x)$ are monotonic in opposite (same) direction then

$$
\frac{A_{h_{k}}^{w}(x)}{A_{h}^{w}(x)} \geq(\leq) \frac{\int_{0}^{x} w(u) d u}{\int_{0}^{x}(w(u))^{n+1} d u}
$$

(ii) If $w(x)>1$, then

$$
\frac{G_{h_{k}}^{w}(x)}{G_{h}^{w}(x)} \geq \exp \left(\frac{k}{x} \int_{0}^{x} \ln w(u) d u\right)
$$

(iii) If $h(x)$ and $w(x)$ are monotonic in same (opposite) direction then

$$
\frac{H_{h_{k}}^{w}(x)}{H_{h}^{w}(x)} \geq(\leq) \frac{\int_{0}^{x} w(u) d u}{\int_{0}^{x} \frac{1}{(w(u))^{k-1}} d u}
$$

(iv) If $w(x)$ and $h(x)$ are monotonic in same (opposite) direction then $A_{h_{k}}^{w}(x) \geq(\leq) A(x)$, and $H_{h_{k}}^{w}(x) \geq(\leq) H(x)$, according as $w(x) \leq(\geq) 1$.

(v) If $h(x) \geq 1, w(x) \geq 1$ then $G_{h_{k}}^{w}(x) \geq G(x)$, provided $w(x)$ and $h(x)$ are monotonic in same direction.

Proof. The proofs of $(i),(i i)$ and (iii) follow by applying Lemma 2.1 on the ratios, viz.,

$$
\frac{A_{h_{k}}^{w}(x)}{A_{h}^{w}(x)}=\frac{\int_{0}^{x}(w(u))^{k+1} h(u) d u}{\int_{0}^{x} w(u) h(u) d u}, \frac{G_{h_{k}}^{w}(x)}{G_{h}^{w}(x)}=\exp \left(\frac{k \int_{0}^{x} w(u) \ln w(u) d u}{\int_{0}^{x} w(u) d u}\right)
$$

and

$$
\frac{H_{h_{k}}^{w}(x)}{H_{h}^{w}(x)}=\left(\frac{\int_{0}^{x} \frac{w(u)}{h(u)} d u}{\int_{0}^{x} \frac{1}{w^{k-1}(u) h(u)} d u}\right), x>0
$$

The proof of (iv) follows from (i) and (iii) of Proposition 2.3. The proof of $(v)$ follows from (ii) of Proposition 2.3. If $w(x)$ and $h(x)$ are monotonic in same (opposite) direction then $A_{h_{k}}^{w}(x) \geq(\leq$ $A_{h}^{w}(x)$, and $H_{h_{k}}^{w}(x) \geq(\leq) H_{h}^{w}(x)$, according as $w(x) \geq(\leq) 1$.

The above theorem can be interpreted by saying that one can keep minimizing the means of failure rate (AFR and HFR) of a component, having increasing failure rate by associating weights in sequence which are monotonically decreasing with time. However, GFR increases rapidly with the increase in number of weight functions and is independent of the nature of monotonicity of weight and hazard rate. Theorem 2.1 (ii) reveals that if $k \rightarrow \infty$ and $w(x)>1$ then $G_{h_{k}}^{w}(x) \rightarrow \infty$.

## 3 Non-parametric classes of distributions based on weighted means of failure rates

We define non-parametric classes of distributions on the basis of monotonicity of w-AFR, w-GFR and w-HFR.

Definition 3.1 $A$ random variable $X$ is said to belong to the class of

(i) Increasing (resp. Decreasing) weighted arithmetic mean failure rate $I w-A F R$ (resp. Dw$A F R)$ ) distributions if $A^{w}(x)$ is increasing (resp. decreasing) in $x>0$.

(ii) Increasing (resp. Decreasing) weighted geometric mean failure rate Iw-GFR (resp. (Dw$G F R)$ ) distributions if $G^{w}(x)$ is increasing (resp. decreasing) in $x>0$.

(iii) Increasing (resp. Decreasing) weighted harmonic mean failure rate Iw-HFR (resp. DwHFR)) distributions if $H^{w}(x)$ is increasing (resp. decreasing) in $x>0$.

The next theorem emphasises on the fact that the monotonic behaviour of $h(x)$ is possessed by $A^{w}(x), G^{w}(x)$ and $H^{w}(x)$.

Theorem 3.1 If $h(x)$ is increasing (decreasing) in $x \geq 0$ then

(i) $A^{w}(x)$ is increasing (decreasing) in $x \geq 0$;

(ii) $G^{w}(x)$ is increasing (decreasing) in $x \geq 0$;
(iii) $H^{w}(x)$ is increasing (decreasing) in $x \geq 0$.

Proof. To prove (i), we note that $\left(\int_{0}^{x} w(u) d u\right)\left(\frac{d}{d u} A^{w}(x)\right)=w(x)\left(h(x)-A^{w}(x)\right)$, and thus $\left(\frac{d}{d x} A^{w}(x)\right) \geq(\leq) 0$ according as $h(x) \geq(\leq) A^{w}(x)$ for all $x \geq 0$. If $h(x)$ is increasing (decreasing) in $x$ then $h(x) \geq(\leq) A^{w}(x)$ for $x \geq 0$. This proves $(i)$. Similarly, to prove (ii), we first note that

$$
\left(\frac{d}{d x} G^{w}(x)\right)=\frac{G^{w}(x)}{\left(\int_{0}^{x} w(u) d u\right)} w(x) \ln \left(\frac{h(x)}{G^{w}(x)}\right)
$$

and this implies that $\frac{d}{d x} G^{w}(x) \geq(\leq) 0$ according as $h(x) \geq(\leq) G^{w}(x)$. One can note that if $h(x)$ is increasing (decreasing) in $x$ then $h(x) \geq(\leq) G^{w}(x)$ for all $x \geq 0$, thus proving (ii). To prove (iii), we first note that

$$
\left(\frac{d}{d x} H^{w}(x)\right)\left(\int_{0}^{x} \frac{w(p)}{h(p)} d p\right)=w(x)\left\{1-\frac{H^{w}(x)}{h(x)}\right\}
$$

and hence we find that $\left(\frac{d}{d x} H^{w}(x)\right) \geq(\leq) 0$ according as $h(x) \geq(\leq) H^{w}(x)$ for all $x \geq 0$. Also, if $h(x)$ is increasing (decreasing) in $x$ then $h(x) \geq(\leq) H^{w}(x)$ for all $x \geq 0$. This completes the proof. $\square$

The next example highlights the importance of choosing weight functions in generating new distributions. It is also cited in upcoming counterexample 3.1 for establishing that w-IFRA class is not closed under formation of coherent systems.

Example 3.1 Let $X$ follows two parameter Weibull distribution with scale and shape parameter $\alpha$ and $\beta$ respectively. If we take $w(x)=e^{n x}$ for all $x>0$, then the weighted random variable $X^{w}$ has failure rate $h^{w}(x)=\alpha \beta e^{n x} x^{\beta-1}$. Here, taking $n=-m$ with $m>0$,

$$
\begin{aligned}
\int_{0}^{x} w(u) h(u) u & =\alpha \beta \int_{0}^{x} e^{-m t} t^{\beta-1} d t \\
& =\alpha \beta(-n)^{-\beta} \gamma(\beta,-n x) \\
& =\alpha \beta(-n)^{-\beta}(\Gamma(\beta)-\Gamma(\beta,-n x))
\end{aligned}
$$

where the incomplete Gamma function $\gamma(z, a)$ and its complement $\Gamma(z, \alpha)$ (also known as Prym's function) are

$$
\left.\gamma(a, x)=\int_{0}^{x} t^{a-1} e^{-t} d t, \Gamma(a, x)=\int_{x}^{\infty} t^{a-1} e^{-t} d t, \quad \operatorname{Real}(a)>0\right)
$$

satisfying $\gamma(a, x)+\Gamma(a, x)=\Gamma(a)$. If $n<0$ we have real values for $\bar{F}^{w}(t)$, as

$$
\bar{F}^{w}(x)=\exp \left\{-\alpha \beta(-n)^{-\beta}(\Gamma(\beta)-\Gamma(\beta,-n x))\right\}, x>0, \beta>0
$$

Also, considering $m=-n$, we get

$$
\frac{d}{d x} h^{w}(x)=\frac{d}{d x}\left(\alpha \beta e^{n x} x^{\beta-1}\right)=\alpha \beta e^{n x} x^{\beta-2}(\beta-1-m x) \leq 0
$$

if $(\beta-1-m x) \leq 0$, i.e., $\frac{d}{d x} h^{w}(x) \leq 0$ if $x \geq \frac{\beta-1}{m}$. If $\beta<1$ then $\frac{d}{d x} h^{w}(x) \leq 0$ for all $x>0$. Thus, $X^{w}$ is DFR if $\beta<1$. On the other hand if $\beta>1$, then $\frac{d}{d x} h^{w}(x) \geq 0$ for $x \in\left(0, \frac{\beta-1}{m}\right)$ and $\frac{d}{d x} h^{w}(x) \leq 0$ for $x \geq \frac{\beta-1}{n}$. Thus $X^{w}$ is DFR if $\beta<1$, whereas $X^{w}$ has upside-down bathtub shaped failure rate if $\beta>1$. Using (3.5) and the fact that $\int_{0}^{x} w(u) d u=\frac{1}{n}\left(e^{n x}-1\right)$ we get

$$
A^{w}(x)=\frac{n(-n)^{-\beta} \alpha \beta(\Gamma[\beta]-\Gamma[\beta,-n x])}{\left(e^{n x}-1\right)}
$$

Here, for $\beta<1, h^{w}(x)$ is decreasing in $x$, and so is $A^{w}(x)$ as evident from Theorem 3.1. Similarly, for $\beta>1, A^{w}(x)$ is upside-upside-down bathtub. Using (3.6), we note that,

$$
\begin{aligned}
\frac{d}{d x} A^{w}(x) & =n(-n)^{-\beta} \alpha \beta \frac{d}{d x}\left(\frac{(\Gamma[\beta]-\Gamma[\beta,-n x])}{e^{n x}-1}\right) \\
& =n(-n)^{-\beta} \alpha \beta\left\{\frac{\left(e^{n x}-1\right) e^{n x}(-n x)^{\beta-1}(-n)-(\Gamma[\beta]-\Gamma[\beta,-n x]) e^{n x} n}{\left(e^{n x}-1\right)^{2}}\right\} \\
& =n(-n)^{-\beta} \alpha \beta\left\{\frac{\left(e^{n x}-1\right) e^{n x}(-n x)^{\beta}\left(\frac{(-n)}{-(n x)}\right)-(\Gamma[\beta]-\Gamma[\beta,-n x]) e^{n x} n}{\left(e^{n x}-1\right)^{2}}\right\} \\
& =\frac{n(-n)^{-\beta} \alpha \beta e^{n x}}{x\left(e^{n x}-1\right)^{2}}\left\{\left(e^{n x}-1\right)(-n x)^{\beta}+n x(\Gamma[\beta,-n x]-\Gamma[\beta])\right\} \\
& =\frac{n^{2} x(-n)^{-\beta} \alpha \beta e^{n x}}{x\left(e^{n x}-1\right)^{2}}\left\{\Gamma[\beta,-n x]-\Gamma[\beta]-\left(e^{n x}-1\right)(-n x)^{\beta-1}\right\} \\
& =\frac{n^{2} x(-n)^{-\beta} \alpha \beta e^{n x}}{x\left(e^{n x}-1\right)^{2}}\{-\gamma[\beta,-n x]-P(x)\},(\text { say })
\end{aligned}
$$

where

$$
P(x)=\left(e^{n x}-1\right)(-n x)^{\beta-1} \leq 0, x>0
$$

The change point of monotonicity of $A^{w}(x)$ is determined by the root of equation $\gamma[\beta,-n x]+P(x)=$ 0. Similarly, we obtain

$$
\begin{gathered}
G^{w}(x)=\alpha \beta t^{\beta-1}(-n t)^{\frac{\beta-1}{e^{n t}-1}} e^{\frac{(\beta-1)\left(E_{1}(-n t)+\gamma\right)}{e^{n t}-1}} \\
H^{w}(x)=\frac{\alpha \beta\left(e^{n t}-1\right) n t^{\beta}(-n t)^{-\beta}}{\Gamma[2-\beta]-\Gamma[2-\beta,-n t]}
\end{gathered}
$$

where $\gamma \sim 0.577216$ is Euler's constant and $E_{n}(z)$ is the exponential integral function.

Below, we state two theorems highlighting the inclusion property of the non-parametric aging classes given in Definition 3.1. The proof follows due to Theorem 3.1, line of the proof therein and the fact that $A^{w}(x) \geq G^{w}(x) \geq H^{w}(x)$ for all $x>0$.

Theorem 3.2 IFR $\subseteq I w-A F R \subseteq I w-G F R \subseteq I w-H F R$

Theorem 3.3 $D F R \subseteq D w-H F R \subseteq D w-G F R \subseteq D w-A F R$

### 3.1 Characterization results for w-AFR, and w-GFR

We introduce the concept of weighted star-shaped (anti-star) function which is a generalization of star-shaped (anti-star) function to give an equivalent condition of $I w-A F R$ and $D w-A F R$ classes of distributions.

Definition 3.2 A function $g(x)$ defined on $[0, \infty)$ is said to be weighted star-shaped (weighted antistar shaped) with respect to a non-negative weight function $w(x)$ if $\left(-\frac{1}{\int_{0}^{x} w(u) d u}\right) g(x)$ is increasing in $x>0$. Equivalently, for $0 \leq \alpha \leq 1$ and $x \geq 0$,

$$
g(\alpha x) \leq\left(\frac{\int_{0}^{\alpha x} w(u) d u}{\int_{0}^{x} w(u) d u}\right) g(x)
$$

The next theorem gives a necessary and sufficient condition of a increasing (decreasing) weighted arithmetic failure rate or weighted failure rate average class of distributions, denoted by w-AFR. We omit the proof for the sake of brevity.

Theorem 3.4 Let $X$ has increasing (decreasing) $w-A F R$. Then the following conditions are equivalent.

(i) $\left(-\frac{1}{\int_{0}^{x} w(u) d u}\right) \ln \bar{F}^{w}(x)$ is increasing (decreasing) in $x>0$.

(ii) $-\ln \bar{F}^{w}(x)$ is weighted star-shaped (weighted anti-star shaped) with respect to $c(\cdot)$.

(iii) $\left(\bar{F}^{w}(x)\right)^{\frac{1}{J_{0}^{x} w(u) d u}}$ is decreasing (increasing) in $x>0$.

(iv) For $\alpha \in[0,1]$, and $x>0, \bar{F}^{w}(\alpha x) \geq(\leq)\left(\bar{F}^{w}(x)\right)^{\frac{\int_{0}^{\alpha x} w(u) d u}{\rho_{0}^{x} w(u) d u}}$.

The following theorem gives equivalent conditions for $w-G F R$.

Theorem 3.5 Let $X$ has increasing (decreasing) w-GFR. Then the following conditions are equivalent.

(i) $\left(\frac{1}{\int_{0}^{x} w(u) d u}\right)\left(\int_{0}^{x} w(u) \ln h(u) d u\right)$ is increasing (decreasing) in $x>0$.

(ii) $\left(\int_{0}^{x} w(u) \ln h(u) d u\right)$ is weighted star-shaped (weighted anti-star shaped) with respect to $c(\cdot)$.

(iii) For $\alpha \in[0,1]$, and $x>0, \int_{0}^{\alpha x} w(u) \ln h(u) d u \leq(\geq) \frac{\int_{0}^{\alpha x} w(u) d u}{\int_{0}^{x} w(u) d u}\left(\int_{0}^{x} w(u) \ln h(u) d u\right)$.

We note that, $0 \leq \frac{\int_{0}^{\alpha x} w(u) d u}{\int_{0}^{x} w(u) d u} \leq 1$ since $w(x) \geq 0$ for all $x \geq 0$ and $0 \leq \alpha \leq 1$.

### 3.2 Results on coherent system

In this section, we primarily focus on Iw-AFR class and its closure properties. We know that IFRA class is closed under the formation of coherent system. Naturally, a question ponders, whether the same result is true for increasing weighted AFR class (Iw-AFR). Let us consider a coherent system with $n$ components having weighted survival functions $\bar{F}_{i}^{w}(x)$ for $i=1,2, \ldots, n$. The survival function $\bar{F}^{w}(x)$ of the resultant coherent system satisfies

$$
\bar{F}^{w}(\alpha x)=h\left(\bar{F}_{1}^{w}(\alpha x), \bar{F}_{2}^{w}(\alpha x), \ldots, \bar{F}_{n}^{w}(\alpha x)\right)
$$

where $h$ represents the survival function of the coherent system. Further, if we assume that each $X_{i}$ has increasing w-AFR, then we explore what would be the survival function of the resultant coherent system. Since $\bar{F}_{i}^{w}(\alpha x) \geq\left(\bar{F}_{i}^{w}(x)\right)^{\frac{\int_{0}^{\alpha x} w(u) d u}{\int_{0}^{w} w(u) d u}}$ for $i=1,2, \ldots, n, \alpha \in[0,1], x>0$, and $h$ is increasing in each argument, (3.6) reduces to

$$
\bar{F}^{w}(\alpha t) \geq h\left(\left(\bar{F}_{1}^{w}(x)\right)^{\frac{\int_{0}^{\alpha x} w(u) d u}{\int_{0}^{x} w(u) d u}},\left(\bar{F}_{2}^{w}(x)\right)^{\frac{\int_{0}^{\alpha x} w(u) d u}{J_{0}^{x} w(u) d u}}, \ldots,\left(\bar{F}_{n}^{w}(x)\right)^{\frac{\int_{0}^{\alpha x} w(u) d u}{\int_{0}^{x} w(u) d u}}\right)
$$

The following counterexample shows that Iw-AFR is not closed under the formation of coherent system.

Counterexample 3.1 Let us consider a series system with lifetime $X$ formed by two components with lifetimes $X_{1}^{w}$ and $X_{2}^{w}$ respectively. Let the failure rates be $h_{1}(t)$, and $h_{2}(t)$ with corresponding weights $w_{1}(t)$ and $w_{2}(t)$ respectively. Let $h_{1}(t)=\alpha \beta t^{\beta-1}, w_{1}(t)=e^{n t}$, and $h_{2}(t)=a b t^{b-1}, w_{2}(t)=$ $\left(1-e^{n t}\right)$ where $\alpha, a>0 ; \beta, b>1 ; n<0$. Since, $\beta, b>1 ; h_{1}(t)$ and $h_{2}(t)$ are increasing in $t$. By Theorem 3.1, it follows that $A_{1}^{w}(t)$ and $A_{2}^{w}(t)$ are increasing in $t$ as $h_{1}(t)$ and $h_{2}(t)$ are increasing in $t$. Then the hazard rate of the series system is given by $h_{X}(t)=h_{1}(t) w_{1}(t)+h_{2}(t) w_{2}(t)$ for all $t>0$. From Example 3.1, it follows that each of $h_{1}^{w}(t)=h_{1}(t) w_{1}(t)$ and $h_{2}^{w}(t)=h_{2}(t) w_{2}(t)$ are non-monotonic in $t>0$. (upside-down bathtub curve). Thus, $X_{1}^{w}$ and $X_{2}^{w}$ are Iw-AFR but not IFR. Here, $X$ is not Iw-AFR since $h(t)$ is non-monotonic (as noted in Example 3.1) and non-monotonicity of $h(t)$ is transmitted to $A(t)$ (by Theorem 3.1).

We end this section by the following remark which once again emphasizes the importance of the concepts introduced in this article which in turn engenders the upcoming section.

Remark 3.1 In particular, if in the definition 2.2 discussed above, we replace failure rate $h(\cdot)$ by hazard quantile function $h_{q}(\cdot)$ and $w(\cdot)$ by density quantile function $q(\cdot)$ respectively, with support restricted to $[0,1]$, we get quantile version of $A F R, G F R$ and HFR as mentioned in upcoming section.

## 4 Quantile version of AFR, GFR and HFR

The Remark 3.1 is the genesis of this section. The readers would be interested to see how the act of replacing failure rate by hazard quantile function and weight function by density quantile function respectively will differ the rest of the analysis and is taken up in the present section. For a random variable $X$, quantile function $(\mathrm{QF})$ is defined as

$$
Q(u)=F^{-1}(u)=\inf \{x: F(x) \geq u\}, 0 \leq u \leq 1
$$

gives $F Q(u)=u$. Differentiating with respect to $u$, we get $f(Q(u)) q(u)=1$ or $f(Q(u))=\frac{1}{q(u)}$, where $f(Q(u))$ and $q(u)=\frac{d}{d u} Q(u)$ are respectively known as the density quantile function and quantile density function of $X$. From the definition of hazard rate, the corresponding hazard quantile function is given by

$$
h_{q}(u)=h(Q(u))=\frac{f(Q(u))}{\bar{F}(Q(u))}=\frac{1}{(1-u) q(u)}
$$

This implies $q(u)=\frac{1}{(1-u) h_{q}(u)}$. Integrating, we get $Q(u)=\int_{0}^{u} \frac{1}{(1-p) h_{q}(p)} d p$. The quantile approach is an alternative to the traditional distribution function method as it can also used to specify a probability distribution. As the quantile approach possess some interesting properties not shared by its distribution function counterpart and in many situations, quantile measures provide simple expressions that are easily amenable to many computational analysis. Abundant literature are now available on various properties of quantile functions and different measures based on it and their applications, for details see Gilchrist (2000), Nair et al. (2013), Nair et al. (2023) and Aswin et al. (2023) and references therein.

Note that, the quantile version of AFR, GFR and HFR, denoted by $Q A(\cdot), Q G(\cdot), Q H(\cdot)$ respectively, can be independently derived using quantile approach. Alternatively, we can obtain the same by applying the Remark 3.1 (ii) in Definition [2.2, i.e., replacing the failure rate $h(\cdot)$ by hazard quantile function $h_{q}(\cdot)$ and $w(\cdot)$ by density quantile function $q(\cdot)$ respectively, with support restricted to $[0,1]$.

$$
\begin{aligned}
& Q A(u)=Q A(Q(u))=\frac{-\ln (1-F(Q(u)))}{Q(u)} \\
& =\frac{-\ln (1-u)}{Q(u)}=-(\ln (1-u))\left\{\int_{0}^{u} \frac{1}{(1-p) h_{q}(p)} d p\right\}^{-1} . \\
& Q G(u)=Q G(Q(u))=\exp \left(\frac{1}{Q(u)} \int_{0}^{u} \ln \left(\frac{1}{(1-p) q(p)}\right) d Q(p)\right) \\
& =\exp \left(-\frac{1}{Q(u)} \int_{0}^{u} q(p) \ln ((1-p) q(p) d p)\right)
\end{aligned}
$$

or equivalently,

$$
\begin{aligned}
Q(u) \ln Q G(u) & =-\int_{0}^{u}(\ln (1-p)) q(p) d p-\int_{0}^{u}(\ln q(p)) q(p) d p \\
& =-\int_{0}^{u} q(p) \ln \{(1-p) q(p)\} d p=\int_{0}^{u} q(p) \ln h_{q}(p) d p
\end{aligned}
$$

and

$$
\begin{aligned}
Q H(u)=Q H(Q(u)) & =\left(\frac{1}{Q(u)} \int_{0}^{u} \frac{1}{h(Q(p))} d Q(p)\right)^{-1} \\
& =Q(u)\left(\int_{0}^{u}(1-p)(q(p))^{2} d p\right)^{-1} \\
& =Q(u)\left(\int_{0}^{u} \frac{q(p)}{h_{q}(p)} d p\right)^{-1}
\end{aligned}
$$

Differentiating (4.8) with respect to $u$, we obtain

$$
Q A^{\prime}(u) Q(u)+Q A(u) q(u)=\frac{1}{1-u}
$$

When quantile AFR is increasing (decreasing), we get

$$
Q A(u) \leq(\geq) h_{q}(u)
$$

From (4.10), we have

$$
\frac{Q(u)}{Q H(u)}=\int_{0}^{u}(1-p)(q(p))^{2} d p
$$

Differentiating with respect to $u$, we get

$$
Q H(u) q(u)-Q(u) Q H^{\prime}(u)=(1-u)(q(u))^{2}(Q H(u))^{2}
$$

Now when the quantile HFR is increasing (decreasing), yield

$$
Q H(u) \leq(\geq) h_{q}(u)
$$

A similar arguement as given in Theorem 3.1]depicts that monotonicity of hazard quantile function $h_{q}(\cdot)$ is transmitted to quantile version of AFR, GFR and HFR, i.e., $Q A(\cdot), Q G(\cdot)$ and $Q H(\cdot)$. In continuation to the Proposition 2.2 of previous section, if we replace $w(\cdot)$ by $q(\cdot)$ and $h(\cdot)$ by $h_{q}(\cdot)$, we find that proportionality of weighted means of quantile hazard functions with quantile hazard function characterizes some quantile function. To the best of our knowledge, $Q(x)$ as obtained in Proposition 4.1 represents a new generalized version of quantile function where $Q(0) \neq 0$.

The next example gives the quantile function of AFR, GFR and HFR of Pareto-I distribution.

Example 4.1 For Pareto I distribution, with quantile function $Q(u)=\alpha(1-u)^{-1 / \alpha}$, we have $Q A(u)=-\frac{(1-u)^{1 / \alpha} \log (1-u)}{\alpha}, Q G(u)=e^{1-(1-u)^{1 / \alpha}}(1-u)^{1 / \alpha}$, and $Q H(u)=-\frac{2(1-u)^{1 / \alpha}}{(1-u)^{2 / \alpha}-1}$, for $0<u<1$.

Proposition 4.1 Let hazard quantile function $h_{q}(u)$ be differentiable for all $u \in[0,1]$. Then for the non-negative weight function $q(u)$, called as density quantile function and for $a, b, c>0$ we have

(i) $Q A(u)=a h_{q}(u)$ for all $u \in[0,1]$ if and only if $Q(u)=\left(\frac{1}{a k}\right)^{a}\left\{\ln \left(\frac{A}{1-u}\right)\right\}^{a}$.

(ii) $Q G(u)=b h_{q}(u)$ for all $u$ if and only if $Q(u)=\left(\frac{\ln (e / b)}{k}\right)^{\frac{1}{\ln (e / b)}}\left\{\ln \left(\frac{A}{1-u}\right)\right\}^{\frac{1}{\ln (e / b)}}$.

(iii) $Q H(u)=c h_{q}(u)$ for all $u$ if and only if $Q(x)=\left(\frac{\ln (e / b)}{k}\right)^{\frac{1}{\ln (e / b)}}\left\{\ln \left(\frac{A}{1-u}\right)\right\}^{\frac{1}{\ln (e / b)}}$ where $k$ is an arbitrary constant.

Proof. From Theorem $2.2(i)$, it follows that $Q A(u)=a h_{q}(u)$ is equivalent to

$$
h_{q}(u)=k\left(\int_{0}^{u} q(p) d p\right)^{(1-a) / a}
$$

and since $h_{q}(u)=\frac{1}{(1-u) q(u)}$, we prove (i). Proofs of (ii) and (iii) are similar.

Transformation on a random variable is generally employed to find the best model for a given set of observations. A simple alternative method to this is to keep the original data as it is and transform the QF to find the best model, using the following property of quantile functions which is not shared by the distribution function. If $T_{X}(x)$ is a continuous non-decreasing function then $T_{X}\left(Q_{X}(u)\right)$ is the $\mathrm{QF}$ of $T_{X}(X)$ or in symbols

$$
Q_{T(X)}(u)=T\left(Q_{X}(u)\right)
$$

Theorem 4.1 Let $T(\cdot)$ be a continuous non-decreasing and invertible transformation. Then the quantile versions of $A F R, G F R$ and HFR takes the form

(i) $Q A_{T(X)}(u)=\frac{-\log (1-u)}{T\left(Q_{X}(u)\right)}$,

(ii) $Q G_{T(X)}(u)=\exp \left(-\frac{1}{T\left(Q_{X}(u)\right)} \int_{0}^{u} T^{\prime}\left(Q_{X}(p)\right) q(p)\left[\log (1-p) T^{\prime}\left(Q_{X}(p)\right) q(p)\right] d p\right)$, and

(iii) $Q H_{T(X)}(u)=T\left(Q_{X}(u)\right)\left(\int_{0}^{u}(1-p)\left(T^{\prime}\left(Q_{X}(p)\right) q(p)\right)^{2} d p\right)^{-1}$.

Theorem 4.2 The following statements are equivalent: (i) $X$ follows Exponential distribution with shape parameter $c$, (ii) $Q A(u)=c$, (iii) $Q G(u)=c$, and (iv) $Q H(u)=c$.

Remark 4.1 The quantile version is not always equivalent to its distribution function approach.

Theorem 4.3 $Q A(u)=(Q(u))^{C-1}$, where $C>0$ holds if and only $X$ follows Weibull distribution with quantile function $Q(u)=(-\log (1-u))^{\frac{1}{\lambda}}, 0<u<1, \lambda>0$.

For many models, the distribution function and quantile approches yield similar properties as we have seen in Theorem 4.2, while for certain other cases, it gives different results. For example, when $X$ and $Y$ satisfy proportional hazard rate model (PHM), we have $h_{q_{Y}}(u)=\theta h_{q_{X}}(u)$, or equivalently, we have $\bar{F}_{Y}(u)=\left(\bar{F}_{X}(u)\right)^{\theta}$. We look at the corresponding AFR, GFR and HFR of $Y$. It is easy to note that $A_{Y}(x)=\theta A_{X}(x), G_{Y}(x)=\theta G_{X}(x)$ and $H_{Y}(x)=\theta H_{X}(x)$. To obtain the quantile version of AFR, GFR and HFR under PHM, it is easy to obtain the QF of $Y$, as

$$
Q_{Y}(u)=\inf \left\{x: F_{Y}(x) \geq u\right\}=Q_{X}\left(1-(1-u)^{1 / \theta}\right)
$$

which in turn obtain the quantile version of AFR for PHM as

$$
Q A_{Y}(u)=-\frac{\ln (1-u)}{Q_{Y}(u)}=\frac{-\ln (1-u)}{Q_{X}\left(1-(1-u)^{1 / \theta}\right)}=\theta Q A_{X}\left(1-(1-u)^{1 / \theta}\right) \neq \theta Q A_{X}(u)
$$

since

$$
Q A_{X}\left(1-(1-u)^{1 / \theta}\right)=\frac{-\ln \left\{\left\{1-\left(1-(1-u)^{1 / \theta}\right\}\right\}\right.}{Q_{X}\left(1-(1-u)^{1 / \theta}\right)}=-\frac{1}{\theta} \frac{\ln (1-u)}{Q_{X}\left(1-(1-u)^{1 / \theta}\right)}
$$

The quantile GFR of PHM will be

$$
\begin{aligned}
& Q G_{Y}(u)=\exp \left[-\frac{1}{Q_{X}\left(1-(1-u)^{\frac{1}{\theta}}\right)} \int_{0}^{u} \frac{1}{\theta} q_{X}\left(1-(1-p)^{\frac{1}{\theta}}\right)(1-p)^{\frac{1}{\theta}-1}\right. \\
&\left.\ln \left(\frac{1}{\theta} q_{X}\left(1-(1-p)^{\frac{1}{\theta}}\right)(1-p)^{\frac{1}{\theta}}\right) d p\right]
\end{aligned}
$$

or equivalently

$$
Q G_{Y}(u)=\exp \left[-\frac{1}{Q_{X}(u)} \int_{0}^{1-(1-u)^{\frac{1}{\theta}}} \frac{1}{\theta} q_{X}(p)(1-p)^{1-\theta} \ln \left((1-p) \frac{1}{\theta} q_{X}(p)\right)\right] \neq \theta \mathcal{Q \mathcal { G } _ { X } ( u )}
$$

Also, the quantile version of HFR becomes

$$
Q H_{Y}(u)=\left(\frac{1}{Q_{X}\left(1-(1-u)^{\frac{1}{\theta}}\right)} \int_{0}^{u} \frac{1}{\theta}(1-p)^{\frac{2}{\theta}-1} q_{X}\left(1-(1-u)^{\frac{1}{\theta}}\right)^{2}\right)^{-1} \neq \theta Q H_{X}(u)
$$

This clearly illustrates that quantile version of the AFR, GFR and HFR for the PHM not satifying the properties those hold in the distribution function approach.

## 5 Conclusion

At the long last, for readers we reiterate that mixture of $n$ distributions is a special case of formation of $n$ independent component series system having weighted failure rates with the sum of weight functions being unity. However, the latter system having arbitrary weights is also not a generalization of the former. The idea of relating the said concepts deserves some credit because the existing literature on mixture of distributions can be extended to the formation of coherent systems (in particular, series system) so far as non-preservation properties of reliability operations are concerned. One can generate new distributions using weighted version of arithmetic, geometric and harmonic means of failure rate. Since, the quantile version of means of hazard rate is a special case of weighted means of failure rate, the properties studied for weighted means is put forth for the prior.

## Acknowledgement

Subarna Bhattacharjee would like to thank Odisha State Higher Education Council for providing support to carry out the research project under OURIIP, Odisha, India (Grant No. 22-SF-MT-073).

## References

[1] Aswin, I. C., Sankaran, P. G., and Sunoj, S. M. (2023). Some reliabiility aspects of record values using quantile functions, Communications in Statistics-Theory and Methods, DOI: 10.1080/03610926.2023.2189499.

[2] Balakrishnan, N., Barmalzan, G. and Haidari, A. (2018). Modified proportional hazard rates and proportional reversed hazard rates models via Marshall-Olkin distribution and some stochastic comparisons, Journal of the Korean Statistical Society, 47, 127-138. https://doi.org/10.1016/j.jkss.2017.10.003

[3] Barlow, R. E. and Proschan, F., (1975). Statistical Theory of Reliability and Life Testing: Probability Models. Holt, Rinehart and Winston, New York.

[4] Bhattacharjee, S., Mohanty, I., Szymkowiak, M. and Nanda, A. K. (2022). Properties of aging functions and their means, Communication in Statistics- Simulation and Computation, Available Online. DOI: 10.1080/03610918.2022.2141257.

[5] Gilchrist, W. (2000). Statistical Modelling with Quantile Functions. Boca Raton, Florida: Chapman and Hall/CRC.

[6] Gupta, R. C., and Kirmani, S. N. (1990). The role of weighted distributions in stochastic modeling. Communication in Statistics - Theory and Methods, 19, 3147-3162. https://doi.org/10.1080/03610929008830371

[7] Jiang, R., Ji, P., Xiao, X., 2003. Aging property of univariate failure rate models. Reliability Engineering and System Safety 39, 113-116. https://doi.org/https://doi.org/10.1016/S09518320(02)00175-8

[8] Kies, J.A., 1958. The strength of glass. Naval Research Lab., Washington DC. Report No. 5093.

[9] Marshall, A. W., and Olkin, I. (1997). A new method for adding a parameter to a family of distributions with application to the exponential and Weibull families. https://www.jstor.org/stable/2337585 Biometrika, 84, 641-652.

[10] Marshall, A.W., Olkin, I. (2007). Life Distributions. Springer, New York.

[11] Nair, N.U., Sankaran, P.G., and Balakrishnan, N. (2013). Quantile-Based Reliability Analysis. Statistics for Industry and Technology, New York, NY: Birkhauser.

[12] Nair, N.U., Sunoj, S.M., and Suresh, N. (2023). Additive hazards quantile model, Metrika, DOI: $10.1007 / \mathrm{s00184-023-00924-2 \text {. }}$

[13] Patil G. P. and Ord, J. K. (1976). On Size-Biased Sampling and Related Form-Invariant Weighted Distributions, Sankhyā: The Indian Journal of Statistics, Series B (1960-2002), $38(1), 48-61$.

[14] Patil, G. P., and Rao, G. R. (1978). Weighted distributions and size biased sampling with applications to wildlife populations and human families. Biometrics, 34, 179-189. https://doi.org/10.2307/2530008

[15] Rao, C. R. (1965). On discrete distributions arising out of methods of ascertainment. In Classical and Contagious Discrete Distributions. Patil, G. P. ed. Pergamon Press and Statistical Publishing Society, Calcutta, 320-332. http://www.jstor.org/stable/25049375

[16] Roy, D. and Mukherjee, S.P. (1992). Characterizations based on arithmetic, geometric and harmonic means of failure rates, In: Contributions to Stochastics, Venugopal N. (ed.), Wiley, $178-185$.

[17] Wijsman, R. A. (1985). A useful inequality on ratios of integrals, with application to maximum likelihood estimation, Journal of the American Statistical Association, 80 (390), 472- 475. https://doi.org/10.2307/2287917


[^0]:    ${ }^{*}$ Corresponding author: E-mail: subarna.bhatt@gmail.com

