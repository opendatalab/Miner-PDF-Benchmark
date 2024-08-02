"""
Calculate simscore, refer to (https://github.com/VikParuchuri/marker?tab=readme-ov-file)
"""
from statistics import mean
from typing import List

from rapidfuzz import fuzz

CHUNK_MIN_CHARS = 25


def chunk_text(text: str, chunk_len=500) -> List[str]:
    """
    Chunk text into chunks of a given length.
    """
    chunks = [text[i : i + chunk_len] for i in range(0, len(text), chunk_len)]
    chunks = [c for c in chunks if c.strip() and len(c) > CHUNK_MIN_CHARS]
    return chunks


def overlap_score(hypothesis_chunks: List[str], reference_chunks: List[str]) -> List[float]:
    """
    Compute an overlap score for each chunk in the hypothesis.
    """
    if len(reference_chunks) > 0:
        length_modifier = len(hypothesis_chunks) / len(reference_chunks)
    else:
        length_modifier = 0
    search_distance = max(len(reference_chunks) // 5, 10)
    chunk_scores = []
    for i, hyp_chunk in enumerate(hypothesis_chunks):
        max_score = 0
        i_offset = int(i * length_modifier)
        chunk_range = range(max(0, i_offset - search_distance), min(len(reference_chunks), i_offset + search_distance))
        for j in chunk_range:
            ref_chunk = reference_chunks[j]
            score = fuzz.ratio(hyp_chunk, ref_chunk, score_cutoff=30) / 100
            if score > max_score:
                max_score = score
        chunk_scores.append(max_score)
    return chunk_scores


def score_text(hypothesis: str, reference: str) -> float:
    """
    Compute a score for the hypothesis text compared to the reference text.
    """
    hypothesis_chunks = chunk_text(hypothesis)
    reference_chunks = chunk_text(reference)
    chunk_scores = overlap_score(hypothesis_chunks, reference_chunks)
    if len(chunk_scores) > 0:
        mean_score = mean(chunk_scores)
        return mean_score
    else:
        return 0
