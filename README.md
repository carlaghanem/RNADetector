# RNADetector
This project isan implementation of an RNA sequences differencing (edit 
distance) and patching tool, which can be applied on different kinds of RNA sequence formats (such as
FASTQ, EMBL, FASTA, GCG, etc.).

RNA sequences are made of nucleotides A, C, T and G, in addition to other symbols that are used to represent ambiguity in RNA sequences, including R, M, S, V and M. The algorithm deals with these nucleotides as a sequence of characters and uses an adaptation of the string edit distance algorithm Wagner and Fischer [1] with cost modifications to deal with ambiguity. 
The data, namely the sequences, used as inputs to this tool are stored in an XML document. The generated edit script and edit distance will also be stored in a separate output XML document, that will be used by the patching tool.

The following graphical user interface was developed to test the functionality of the tool.

This is the differencing tool. It takes as input the XML document containing the sewuences to be compared and generates an XML file that contains the edit script and edit distance. It also displays the distance and similarity.
![GitHub Logo](https://github.com/carlaghanem/RNADetector/blob/main/images/Differencing%20Tool.png)

This is the patching tool which takes as input either the target or initial sequence, and the user chooses whether he/she are converting from initial to target or vice versa, and gives it the ES XML document. It also displays the patched sequence. 
Note that the patching tool is independent of the differencing tool and the user can enter a sequence of his own in addition to an edit script of his own on conidition that it matches the format of our XML document structure.

![GitHub Logo](https://github.com/carlaghanem/RNADetector/blob/main/images/Patching%20Tool.png)


Credits to my colleagues Ahmad Houmany and Khaled Baghdadi who worked with me on this project.
