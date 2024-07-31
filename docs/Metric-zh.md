## 提取率
提取率（ER）是从PDF文件成功生成Markdown（.md）文件的数量与PDF文件总数的比率。

$$ \text{ER} = \frac{\text{hypothesiscnt}}{\text{referencecnt}} $$

## 相似度得分

### 相似得分
对于一组假设文本块 `H` 和一组参考文本块 `R`，使用函数 $F(H_{\text{chunk}}, R_{\text{chunk}})$ 计算每个假设文本块与参考文本块之间的最大相似度得分，该函数返回0到1之间的值。

$${maxscore}(H_{\text{chunk}}, R) = \max_{R_{\text{chunk}} \in R} \left[ F(H_{\text{chunk}}, R_{\text{chunk}}) \right]$$

### 平均得分
对于所有假设文本块的最大得分集合 `maxscore`，计算平均得分 $ \text{Mean\_score} $：

$$\text{Mean\\_score} = \text{mean}(maxscore)$$

### 最终得分
最终得分是假设文本块集合与参考文本块集合之间的平均对齐得分，表示为 $ \text{Score}(T_H, T_R) $：

$$ \text{Score}(T_H, T_R) = \text{Mean}\left(\max_{R_{\text{chunk}} \in R} \left[F(H_{\text{chunk}}, R_{\text{chunk}}) \right]\right) $$

## 编辑距离

### 描述
它是一种测量两个字符串之间差异的方法。它定义为将一个字符串转换为另一个字符串所需的最少单字符编辑操作次数。这些编辑操作包括插入、删除和替换字符。

### 用途
为了减少换行和空格对得分的影响，我们在预处理后计算两个字符串之间的编辑距离。

### 引用
[Levenshtein, V.I., et al.: Binary codes capable of correcting deletions, insertions,
and reversals. In: Soviet physics doklady. vol. 10, pp. 707–710. Soviet Union (1966)]
http://www.lrec-conf.org/proceedings/lrec2006/pdf/168_pdf.pdf


## BLEU

### 描述
BLEU分数是一个介于0到1之间的值，较高的BLEU分数通常表示更好的翻译质量。

### 用途
我们在nltk分词后计算两个字符串的sentence_bleu，使用method1作为平滑函数。

### 引用
[Papineni, K., Roukos, S., Ward, T., Zhu, W.J.: Bleu: a method for automatic
evaluation of machine translation. In: Proceedings of the 40th annual meeting of
the Association for Computational Linguistics. pp. 311–318 (2002)]
https://aclanthology.org/P02-1040.pdf
