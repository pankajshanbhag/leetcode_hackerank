

def validatesubseq(array,seq):
  arridx = 0
  seqidx = 0
  while arridx < len(array) and seqidx < len(seq):
    if arra[arridx] == seq[seqidx]:
      seqidx += 1
    arridx += 1
   return len(seq) == seqidx
