## Extraction Rate 

The Extraction Rate (ER) is the ratio of the number of Markdown (.md) files successfully generated from PDF files to the total number of PDF files. 

$$ \text{ER} = \frac{\text{hypothesiscnt}}{\text{referencecnt}} $$

Where:
- hypothesiscnt: The count of Markdown files that have been successfully created.
- referencecnt: The overall count of PDF files that were subjected to the conversion process.

## Similarity Score

- **Overlap Score**

For a set of hypothesis text chunks `H` and a set of reference text chunks `R`, the maximum similarity score between each hypothesis text chunk and the reference text chunks is calculated using the function $F(H_{\text{chunk}}, R_{\text{chunk}}$, which returns a value between 0 and 1.

$${maxscore}(H_{\text{chunk}}, R) = \max_{R_{\text{chunk}} \in R} \left[ F(H_{\text{chunk}}, R_{\text{chunk}}) \right]$$


- **Mean Score**

The mean score `Mean_score` is calculated for the set of maximum scores `maxscore` of all hypothesis text chunks:

$$\text{Mean\\_score} = \text{mean}(maxscore)$$

If `maxscore` is empty, the mean score is 0.

- **Final Score**

The final score is the average alignment score between the set of hypothesis text chunks and the set of reference text chunks, denoted as $Score(T_H, T_R)$:

$${Score}(T_H, T_R) = \text{Mean}\left(\max_{R_{\text{chunk}} \in R} \left[F(H_{\text{chunk}}, R_{\text{chunk}}) \right]\right)$$
Where:
- $T_H$ is the hypothesis text.
- $T_R$ is the reference text.
- $C(T, chunk_len)$ is the function that segments text `T` into chunks of length `chunk_len`.
- $H_{\text{chunk}}, R_{\text{chunk}}$ is the function that calculates the similarity score between two text chunks, which calculated by edit distance, score_cutoff is 30.
- $max$ indicates finding the most similar chunk in the set of reference text chunks `R` for each hypothesis text chunk.
- $Mean$ is the function that calculates the average value.

## Edit Distance

- **Description:**

It is a method for measuring the differences between two strings. It is defined as the minimum number of single-character editing operations required to transform one string into another. These editing operations include insertions, deletions, and substitutions of characters.

- **Usage:**
  
To mitigate the impact of line breaks and spaces on the score, we calculate the edit distance between two strings after preprocessing.

- **Reference:**
  
[Levenshtein, V.I., et al.: Binary codes capable of correcting deletions, insertions,
and reversals. In: Soviet physics doklady. vol. 10, pp. 707–710. Soviet Union (1966)]
https://nymity.ch/sybilhunting/pdf/Levenshtein1966a.pdf

## BLEU

- **Description:**

The BLEU score is a value that ranges from 0 to 1, with higher BLEU scores typically indicating better translation quality.

- **Usage:**
  
We calculate the sentence_bleu of two strings after tokenization with nltk, using method1 as the smoothing_function.

- **Reference:**
  
[Papineni, K., Roukos, S., Ward, T., Zhu, W.J.: Bleu: a method for automatic
evaluation of machine translation. In: Proceedings of the 40th annual meeting of
the Association for Computational Linguistics. pp. 311–318 (2002)]
https://aclanthology.org/P02-1040.pdf 
