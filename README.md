English | [简体中文](README-zh.md)

# Introduction
   MPB (Miner-PDF-Benchmark) is an end-to-end PDF document comprehension evaluation suite designed for large-scale model data scenarios. It ensures human readability at the file granularity and provides PDF categorization tags. The total dataset comprises 350 PDF files and 8410 pages of PDFs, including 11 types of datasets such as books, textbooks, academic literature, PPT to PDF conversions, and examination papers. It serves as a reference for evaluating PDF document comprehension capabilities for developers of large-scale model data and tool developers.
   
# Dataset Source
The MPB dataset is sourced from a variety of origins, including arXiv, Sci-Hub, textbooks, examination papers, historical documents, etc., with reference to the corpus proportion of Llama. The sources and composition of different subsets are as follows:

| Category                  | Tag                 | File Count | Total Pages | Description                                                                                    |
|---------------------------|---------------------|-------------|--------------|------------------------------------------------------------------------------------------------|
| Research Reports           | research_report     | 70          | 875          | Contains rich tabular information with single-column, double-column, and complex layouts.       |
| Ordinary Textbooks        | ordinary_textbook   | 40          | 388          | Single-column layout, black and white, includes a wealth of formulas.                         |
| Academic Literature        | academic_literature | 183         | 3323         | Data sourced from arXiv and Sci-Hub, includes single-column, double-column, charts, formulas, and other complex formats. |
| Atlas                     | atlas               | 3           | 269          | Characterized by a single page containing large area images.                                 |
| Courseware (PPT to PDF)   | courseware         | 7           | 383          | Includes subjects such as Biology, Chinese, English, and Physics.                              |
| Special Exam Papers       | special_exam_paper  | 3           | 80           | Includes watermarks, text within graphics, primary school Pinyin, and math problems.         |
| Historical Documents       | historical_documents | 1           | 3            | The Layout is vertical, and the reading order is from right to left.                                     |
| Notes                      | notes               | 3           | 293          | Includes handwritten notes from three junior high school students.                            |
| Ordinary Exam Papers       | ordinary_exam_paper | 27          | 372          | Includes subjects such as Computer Science, Mathematics, and Chinese, covering primary school, junior high school, high school, and industry question banks, mainly in black and white. |
| Colorful Textbooks        | colorful_textbook   | 3           | 144          | Includes subjects such as English, Mathematics, and Chinese (including Pinyin), containing colorful graphic information. |
| Ordinary Books             | ordinary_books      | 10          | 2280         | Single-column layout, black and white background books.                                       |

# Statistics of MPB

<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/43176747-4f03-42ad-b48b-a4448fc0dc0e" width="350" height="200" alt="The distribution of pages">  

<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/fb06f784-f22f-4897-9b7e-00cf7f622e38" width="350" height="200" alt="The distribution of PDF file"> 

<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/d233a4ca-c54a-41f3-be96-8b80b1b0b740" width="350" height="200" alt="The distribution of md language">  
<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/5ff056a7-6094-420b-8a93-a31585da9451" width="350" height="200" alt="The distribution of PDF  Type">  

# Metrics

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


# Results
### Overall Average Score
| Solution               | Extraction Rate (↑) | Similarity Score (↑) | Edit Distance (↓) | BLEU Score (↑) |
|------------------------|----------------------|----------------------|------------------|------------------|
| nogout (Open-Source Tool)                 | 100%                 | 0.35                 | 0.57             | 0.33             |
| marker (Open-Source Tool)                 | 99.4%                | 0.47                 | 0.42             | 0.386            |
| doc2x (Commercial Tool)| 99%                  | 0.67                 | 0.189            | 0.611            |
| ocrmath (Commercial Tool) | 92%                 | 0.56                 | 0.38             | 0.39             |
| **mathpix (Commercial Tool)** | **100%**                | **0.83**                 | **0.08**             | **0.91**         |

### Scores of 11 Types
<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/473223d0-fee9-4158-8b79-52c09066d8e1" width="350" height="200" alt="The distribution of sim_socre">  

<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/eb537cf8-f8d0-4815-b1c4-0494d72aa9ae" width="350" height="200" alt="The distribution of edit distance">  

<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/f358d113-72fd-4cea-9f68-d46f01249219" width="350" height="200" alt="The distribution of bleu">  

notes:
- marker's test version is v0.2.8;
- nogout's test version is v0.1.0 small;
  
# Get Data
Datasets can be downloaded from [OpenDataLab](https://opendatalab.com/OpenDataLab/Miner-PDF-Benchmark/tree/main);

# Usage
- **step1**
  
Clone the project into your environment.

```
git clone https://github.com/opendatalab/Miner-PDF-Benchmark
cd Miner-PDF-Benchmark
```
- **step2**
  
Installtion

```
python -m pip install -r requirements.txt
```

- **step3**

Evaluation Set Preparation

Download the evaluation set from [OpenDataLab](https://opendatalab.com/OpenDataLab/Miner-PDF-Benchmark/tree/main), and unzip the evaluation set into the `datasets` directory, ensuring the datasets directory contains `pdf` and `annotations`.

- **step4**

Preprocess the evaluation set

Since the images in the evaluation set have not been evaluated yet, you need to execute the following command to preprocess the images:

```
cd evaluate_tool
python clean_photo.py --tool_type annotations --download_dir ../datasets/
```

- **step5**

Preparation of datasets for tools to be evaluated

Please copy the `Markdown` file generated by the evaluation tool you need to evaluate to the `datasets/tool_type/tool_name` directory according to the type. `too_type` is the label corresponding to the 11 categories, and `tool_name` is the name of your tool.
The directory structure after copying is as follows:
```
- Miner-PDF-Benchmark/
  - datasets/
    - academic_literature/
      - annotations/
        - academic_literature_xx.md
      - tool_name/
        - academic_literature_xx.md
      - pdf/ 
    - atlas/
      - tool_name/
        - atlas_xx.md
    - ...
```

Execute the following command to preprocess the dataset generated by the tool you want to evaluate:
```
cd evaluate_tool
python clean_photo.py --tool_type tool_name --download_dir ../datasets/
```

- **step6**

Calculate the score

Please execute the following command to calculate the score, where `--tool_type` is the name of the tool you want to evaluate, `--file_types` is the optional 11 types of corresponding labels, which includes all types by default. You can also specify one or more types to be evaluated, please separate multiple types with spaces; `--download_dir` specifies the path where the json file is saved.

```
cd evaluate_tool
python markdown_calculate.py --tool_type tool_name --download_dir ../datasets/ --results xx.json
```

# Contact
For any questions about the dataset, please contact the authors by wechat opendatalab_yunying.
