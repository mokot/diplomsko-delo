from evaluate import load

################################################################################
# GRAMMAR ERROR DETECTION METRICS:
################################################################################
# Accuracy is the proportion of correct predictions among the total number of
# cases processed. It can be computed with:
# Accuracy = (TP + TN) / (TP + TN + FP + FN)
metric_accuracy = load("accuracy")

# Precision is the fraction of correctly labeled positive examples out of all of
# the examples that were labeled as positive. It is computed via the equation:
# Precision = TP / (TP + FP)
metric_precision = load("precision")

# Recall is the fraction of the positive examples that were correctly labeled by
# the model as positive. It can be computed with the equation:
# Recall = TP / (TP + FN)
metric_recall = load("recall")

# The F1 score is the harmonic mean of the precision and recall. It can be
# computed with the equation:
# F1 = 2 * (precision * recall) / (precision + recall)
metric_f1 = load("f1")

# The Matthews correlation coefficient is used in machine learning as a measure
# of the quality of binary and multiclass classifications. It takes into account
# true and false positives and negatives and is generally regarded as a balanced
# measure which can be used even if the classes are of very different sizes. The
# MCC is in essence a correlation coefficient value between -1 and +1. A
# coefficient of +1 represents a perfect prediction, 0 an average random
# prediction and -1 an inverse prediction
metric_matthews_correlation = load("matthews_correlation")

################################################################################
# GRAMMAR ERROR RECOGNITION METRICS:
################################################################################
# seqeval is a Python framework for sequence labeling evaluation. seqeval can
# evaluate the performance of chunking tasks such as named-entity recognition,
# part-of-speech tagging, semantic role labeling and so on.
metric_seqeval = load("seqeval")

# The Matthews correlation coefficient is used in machine learning as a measure
# of the quality of binary and multiclass classifications. It takes into account
# true and false positives and negatives and is generally regarded as a balanced
# measure which can be used even if the classes are of very different sizes. The
# MCC is in essence a correlation coefficient value between -1 and +1. A
# coefficient of +1 represents a perfect prediction, 0 an average random
# prediction and -1 an inverse prediction
metric_matthews_correlation = load("matthews_correlation")

# Returns the rate at which the input predicted strings exactly match their
# references, ignoring any strings input as part of the regexes_to_ignore list.
metric_exact_match = load("exact_match")

################################################################################
# GRAMMAR ERROR CORRECTION METRICS:
################################################################################
# BLEU (Bilingual Evaluation Understudy) is an algorithm for evaluating the
# quality of text which has been machine-translated from one natural language to
# another. Quality is considered to be the correspondence between a machine's
# output and that of a human: "the closer a machine translation is to a
# professional human translation, the better it is"
metric_bleu = load("bleu")

# SacreBLEU provides hassle-free computation of shareable, comparable, and
# reproducible BLEU scores. Inspired by Rico Sennrich’s multi-bleu-detok.perl,
# it produces the official Workshop on Machine Translation (WMT) scores but
# works with plain text. It also knows all the standard test sets and handles
# downloading, processing, and tokenization.
metric_sacrebleu = load("sacrebleu")

# The BLEU score has some undesirable properties when used for single sentences,
# as it was designed to be a corpus measure. We therefore use a slightly
# different score for our RL experiments which we call the ‘GLEU score’. For the
# GLEU score, we record all sub-sequences of 1, 2, 3 or 4 tokens in output and
# target sequence (n-grams). We then compute a recall, which is the ratio of the
# number of matching n-grams to the number of total n-grams in the target
# (ground truth) sequence, and a precision, which is the ratio of the number of
# matching n-grams to the number of total n-grams in the generated output
# sequence. Then GLEU score is simply the minimum of recall and precision. This
# GLEU score’s range is always between 0 (no matches) and 1 (all match) and it
# is symmetrical when switching output and target. According to our experiments,
# GLEU score correlates quite well with the BLEU metric on a corpus level but
# does not have its drawbacks for our per sentence reward objective.
metric_gleu = load("google_bleu")

# ChrF and ChrF++ are two MT evaluation metrics that use the F-score statistic
# for character n-gram matches. ChrF++ additionally includes word n-grams, which
# correlate more strongly with direct assessment. We use the implementation that
# is already present in sacrebleu.
metric_chrf = load("chrf")

# METEOR, an automatic metric for machine translation evaluation that is based
# on a generalized concept of unigram matching between the machine-produced
# translation and human-produced reference translations. Unigrams can be matched
# based on their surface forms, stemmed forms, and meanings; furthermore, METEOR
# can be easily extended to include more advanced matching strategies. Once all
# generalized unigram matches between the two strings have been found, METEOR
# computes a score for this matching using a combination of unigram-precision,
# unigram-recall, and a measure of fragmentation that is designed to directly
# capture how well-ordered the matched words in the machine translation are in
# relation to the reference.
metric_meteor = load("meteor")

# TER (Translation Edit Rate, also called Translation Error Rate) is a metric to
# quantify the edit operations that a hypothesis requires to match a reference
# translation. We use the implementation that is already present in sacrebleu.
metric_ter = load("ter")

# Character error rate (CER) is a common metric of the performance of an
# automatic speech recognition system. CER is similar to Word Error Rate (WER),
# but operates on character instead of word. Please refer to docs of WER for
# further information. Character error rate can be computed as:
# CER = (S + D + I) / N = (S + D + I) / (S + D + C) where S is the number of
# substitutions, D is the number of deletions, I is the number of insertions,
# C is the number of correct characters, N is the number of characters in the
# reference (N=S+D+C). CER’s output is not always a number between 0 and 1, in
# particular when there is a high number of insertions. This value is often
# associated to the percentage of characters that were incorrectly predicted.
# The lower the value, the better the performance of the ASR system with a CER
# of 0 being a perfect score.
metric_cer = load("cer")

# Word error rate (WER) is a common metric of the performance of an automatic
# speech recognition system. The general difficulty of measuring performance
# lies in the fact that the recognized word sequence can have a different length
# from the reference word sequence (supposedly the correct one). The WER is
# derived from the Levenshtein distance, working at the word level instead of
# the phoneme level. The WER is a valuable tool for comparing different systems
# as well as for evaluating improvements within one system. This kind of
# measurement, however, provides no details on the nature of translation errors
# and further work is therefore required to identify the main source(s) of error
# and to focus any research effort. This problem is solved by first aligning the
# recognized word sequence with the reference (spoken) word sequence using
# dynamic string alignment. Examination of this issue is seen through a theory
# called the power law that states the correlation between perplexity and word
# error rate. Word error rate can then be computed as:
# WER = (S + D + I) / N = (S + D + I) / (S + D + C) where S is the number of
# substitutions, D is the number of deletions, I is the number of insertions, C
# is the number of correct words, N is the number of words in the reference
# (N=S+D+C). This value indicates the average number of errors per reference
# word. The lower the value, the better the performance of the ASR system with a
# WER of 0 being a perfect score.
metric_wer = load("wer")
