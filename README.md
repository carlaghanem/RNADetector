# RNADetector
This project isan implementation of an RNA sequences differencing (edit 
distance) and patching tool, which can be applied on different kinds of RNA sequence formats (such as
FASTQ, EMBL, FASTA, GCG, etc.).

RNA sequences are made of nucleotides A, C, T and G, in addition to other symbols that are used to represent ambiguity in RNA sequences, including R, M, S, V and M. The algorithm deals with these nucleotides as a sequence of characters and uses an 
adaptation of the string edit distance algorithm Wagner and Fischer [1] with cost modifications to deal with ambiguity. 
The data, namely the sequences, used as inputs to this tool are stored in an XML document. The generated edit script 
and edit distance will also be stored in a separate output XML document, that will be used by the patching tool.

The following graphical user interface was developed to test the functionality of the tool.

![GitHub Logo](/images/logo.png)
Format: ![Alt Text](url)
