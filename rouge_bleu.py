def rouge_bleu(out,ref):
    """
    Input:
        out is the machine-outputted summary as list of words
        ref is the gold_standard as a list of words
    Output:
        rouge = number_of_overlappting_words / total_words_in_reference_summary
        bleu = number_of_overlappting_words / total_words_in_system_summary
    """

    out_i = [0] * len(out)
    ref_i = [0] * len(ref)
    for o, olem in enumerate(out):
        for r, rlem in enumerate(ref):
            if olem == rlem:
                if out_i[o] == 0:
                    if ref_i[r] == 0:
                        out_i[o] = 1
                        ref_i[r] = 1

    if len(ref) > 0:
        rouge = sum(out_i) / len(ref)
    else:
        rouge = 0

    if len(out) > 0:
        bleu = sum(out_i) / len(out)
    else:
        bleu = 0

    return rouge, bleu
