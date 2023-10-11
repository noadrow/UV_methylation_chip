import re
from Bio import SeqIO
from Bio.Blast import NCBIWWW
import xml.etree.ElementTree as ET
from Bio.Blast import NCBIXML
from Bio.Blast.Applications import NcbiblastnCommandline
import subprocess

string_this = """CATTCAATGTTACCTTCCAA
AGCCACTCATTTTTAACACC
AATGTACAAACTGGAAACC
TTTCTCTCTCACAGGAATAA
TTCTCCTTAAGCTGGTTTAA
GGAAAACTGGTTCAGTAGAC
TTATCTCTTGCCTTCTTTTC
AGACAATAGACTGCAAATCC
CCTACCACCTTGTGAAGA
GCACTGTACACTGAAAATTG
CCAAGATGCTTAGAAAAATG
GGCATCAAATCTCTGGTT
AGCTTCAGGTAAGTTTTTGG
ACACAGAAGCATCTGTTCTT
TTACTCCCAAAGTCTATTGC
TGTAACCAGTGAGATAAGGC
GGTTGTGGGTTTACATTCAA
AAGGGTGACCTAGAGCACA
GAATCTGAAGACAGTCCAGT
TTTAACAACCCTTCACTTC
GAACTCAGTGCATGAACAAG
TCTGAGGACAGAGCTGTATC
GCTGTTCTCCAAACACTAAT
TTACATCGAGCTAACCTGTC
TTCATTCAAGAGCACAGAAA
ACAAACTAGGGCAAAACAG
GTCATTTAAATTTTCTTGGC
TAATCTAGGTGGTGGTTACC
CAGAAGCTCTTTGGTTTAAT
GCTGCTTTACAAAATACTGC
CCTTGGGTTCAATGAAACCT
GGCACAGAAGAAAGGGACAG
GAGCCCACCCTATAAACATT
CAGATCTTGGCAAGACTCAG
CCTTTAGGAATTACCCAGTA
TTAGGAAGCAGTAATGAGG
GTTGACATGCTGGGAAATC
TGCCCATACAGCTGTTCTCT
AGTTGTTTCAGAAGGCCTCT
AGTGACAGGAATGAGGCTG
GATGTGCACACATGGACC
AGACATCTGCTCAGGGAGTT
CAATCTAAAATCAAGGAAAT
ATACAATGTGACAGATGCTA
TTGTTTGCCTAGAAAACAGG
TCACTTTTTCAATCCCACTT
GGATATTTCTGTCCATTGAT
CACAGTGGTATTAAACAAGG
GGCATTGTCTCTTCTTGCTA
TAACAGAACCCAAACTCGTG
TCATAATTACCATCATAGCA
AAATCAGCGATATTAATAGC
GGCAAAAGAGTGAGACTC
CCTTCCCTTAATAGCCTAAG
AGATAGCCTGCTAGGATTTG
GTGATGGATACCCCATTTAC
CCATTACTTCATTTCTGCCT
TTGGTCACAGAACATTGAAT
TTATTTCCTTGCTATAGTGG
GAAACAACTCAGAAAGCTAG
TGGAACAAGAACTTGTGAGC
GCCAAAATGCATAATTTCA
TCTCTGTGCATCACCCTATT
GGCAAAGTTCAAGTCTCTGG
GATTCCCGTCTGTGTGGTCT
TCTTATTTTTGACTCTGAGATTGTGG
TGGTGCCTAAGAAAGACATTCA
TTCCTTCCCAAAGTGGCTTA
TCCCAAAGAATTGTCAATGG
TTTGGTTTCCCATCAAGGTC
AACATTGAGGATGGAGCAG
CAAAAATGGGGTCTTATCTG
TGTCAATGTAAAAATGCAAG
ACAGCAAAGGTCTTCTATTC
GTAACAGAGGGCTAGTCTTG
AGTTTGAGTGGTGACTGATT
GCCTTTATTGATTCCTGCTT
TGGGGCTCACCTAAAAGTT
GGTGTCTCATCAGCAGGG
GATTCCTATTTTGCTCAGGC
CCTTAGGTCCACATGACATG
GTGCAGTCAAGCTTGAAGTC
AAGTTTCCTTTTGATTAGGT
ACTAGGAGAAAATATTTGCC
AACAAACAAACAAAAAACGC
CACAGCTTCTTCATCTGACC
GAAGAGGTCACATATGTGAG
ATTACCAAACAAGATTGTTG
GCATTCCAGCTTAAAGGA
ACATTTAAAAGATGGTGCAA
GCATAGCCTTGAAAAAATCC
TGTGGAATGGATAAATTGCC
TTCATGGACTCAATAGTCCC
TGAGCTTGAAGAGGAAAGAG
CCTGTCAGCAGGTAGAAGGA
TCTCATGAAGTAGGCAGAGGAA
TTTTGCAAGTAAAGCAATTTTAGG
GCTCTGCTGGACACCTTGAT
CAAATTGATGAAATCCTTATTTGC
AAACCATCAAATACAGGAAAAGAAA
"""

def filter_strings_with_no_numbers(strings):
    pattern = re.compile(r'^[^\d]+$')
    filtered_strings = [s for s in strings if pattern.match(s)]
    return filtered_strings

to_parse = """CATTCAATGTTACCTTCCAA AGCCACTCATTTTTAACACC 487
A_16_P15405423 AATGTACAAACTGGAAACC TTTCTCTCTCACAGGAATAA 433
A_16_P15405605 TTCTCCTTAAGCTGGTTTAA GGAAAACTGGTTCAGTAGAC 500
2q31.3 A_18_P13533801 TTATCTCTTGCCTTCTTTTC AGACAATAGACTGCAAATCC 503
A_16_P15950347 CCTACCACCTTGTGAAGA GCACTGTACACTGAAAATTG 425
3q13.32 A_16_P16375641 CCAAGATGCTTAGAAAAATG GGCATCAAATCTCTGGTT 444
A_16_P16375863 AGCTTCAGGTAAGTTTTTGG ACACAGAAGCATCTGTTCTT 451
A_18_P14352811 TTACTCCCAAAGTCTATTGC TGTAACCAGTGAGATAAGGC 475
4q21.22 A_18_P14767506 GGTTGTGGGTTTACATTCAA AAGGGTGACCTAGAGCACA 428
A_18_P14771686 GAATCTGAAGACAGTCCAGT TTTAACAACCCTTCACTTC 516
A_16_P36800196 GAACTCAGTGCATGAACAAG TCTGAGGACAGAGCTGTATC 333
5q14.2 A_18_P15262957 GCTGTTCTCCAAACACTAAT TTACATCGAGCTAACCTGTC 431
A_18_P15267322 TTCATTCAAGAGCACAGAAA ACAAACTAGGGCAAAACAG 429
A_16_P37250366 GTCATTTAAATTTTCTTGGC TAATCTAGGTGGTGGTTACC 487
6q14.3 A_18_P15726331 CAGAAGCTCTTTGGTTTAAT GCTGCTTTACAAAATACTGC 413
A_18_P15730616 CCTTGGGTTCAATGAAACCT GGCACAGAAGAAAGGGACAG 395
A_14_P101769 GAGCCCACCCTATAAACATT CAGATCTTGGCAAGACTCAG 434
8q23.3 A_16_P18442814 CCTTTAGGAATTACCCAGTA TTAGGAAGCAGTAATGAGG 465
A_16_P18442955 GTTGACATGCTGGGAAATC TGCCCATACAGCTGTTCTCT 364
A_16_P01996624 AGTTGTTTCAGAAGGCCTCT AGTGACAGGAATGAGGCTG 366
9q31.2 A_18_P16960445 GATGTGCACACATGGACC AGACATCTGCTCAGGGAGTT 473
A_16_P02153618 CAATCTAAAATCAAGGAAAT ATACAATGTGACAGATGCTA 355
A_16_P18730465 TTGTTTGCCTAGAAAACAGG TCACTTTTTCAATCCCACTT 453
10q25.1 A_16_P19058209 GGATATTTCTGTCCATTGAT CACAGTGGTATTAAACAAGG 472
A_18_P10889615 GGCATTGTCTCTTCTTGCTA TAACAGAACCCAAACTCGTG 473
A_16_P19058540 TCATAATTACCATCATAGCA AAATCAGCGATATTAATAGC 416
11q22.1 A_16_P19340901 GGCAAAAGAGTGAGACTC CCTTCCCTTAATAGCCTAAG 468
A_16_P19341057 AGATAGCCTGCTAGGATTTG GTGATGGATACCCCATTTAC 413
A_18_P11204159 CCATTACTTCATTTCTGCCT TTGGTCACAGAACATTGAAT 411
14q21.3 A_16_P20035587 TTATTTCCTTGCTATAGTGG GAAACAACTCAGAAAGCTAG 364
A_16_P40178245 TGGAACAAGAACTTGTGAGC GCCAAAATGCATAATTTCA 471
A_18_P11991646 TCTCTGTGCATCACCCTATT GGCAAAGTTCAAGTCTCTGG 404
15q21.1 A_18_P12205990 GATTCCCGTCTGTGTGGTCT TCTTATTTTTGACTCTGAGATTGTGG 251
A_18_P12206420 TGGTGCCTAAGAAAGACATTCA TTCCTTCCCAAAGTGGCTTA 287
A_16_P40388779 TCCCAAAGAATTGTCAATGG TTTGGTTTCCCATCAAGGTC 300
16q21 A_18_P12484550 AACATTGAGGATGGAGCAG CAAAAATGGGGTCTTATCTG 431
A_18_P12480335 TGTCAATGTAAAAATGCAAG ACAGCAAAGGTCTTCTATTC 436
A_16_P20492408 GTAACAGAGGGCTAGTCTTG AGTTTGAGTGGTGACTGATT 445
18q12.2 A_18_P12842528 GCCTTTATTGATTCCTGCTT TGGGGCTCACCTAAAAGTT 522
A_18_P12844310 GGTGTCTCATCAGCAGGG GATTCCTATTTTGCTCAGGC 459
A_18_P12846883 CCTTAGGTCCACATGACATG GTGCAGTCAAGCTTGAAGTC 452
19q12 A_16_P20991672 AAGTTTCCTTTTGATTAGGT ACTAGGAGAAAATATTTGCC 422
A_16_P03441288 AACAAACAAACAAAAAACGC CACAGCTTCTTCATCTGACC 412
A_18_P13021425 GAAGAGGTCACATATGTGAG ATTACCAAACAAGATTGTTG 397
20q12 A_18_P13795069 GCATTCCAGCTTAAAGGA ACATTTAAAAGATGGTGCAA 408
A_18_P13792864 GCATAGCCTTGAAAAAATCC TGTGGAATGGATAAATTGCC 438
A_16_P21129167 TTCATGGACTCAATAGTCCC TGAGCTTGAAGAGGAAAGAG 433
21q21.2 A_16_P41413387 CCTGTCAGCAGGTAGAAGGA TCTCATGAAGTAGGCAGAGGAA 256
A_16_P21216858 TTTTGCAAGTAAAGCAATTTTAGG GCTCTGCTGGACACCTTGAT 299
  A_18_P13889716 CAAATTGATGAAATCCTTATTTGC AAACCATCAAATACAGGAAAAGAAA """


def string_this_to_fasta(string_this):
    lines = string_this.splitlines()  # Split into individual lines
    indexed_lines = []  # Create a new list for indexed lines

    for i, line in enumerate(lines, start=1):
        indexed_lines.append(f">{i}\n{line}")  # Append indexed line to the list

    indexed_string = '\n'.join(indexed_lines)  # Join lines with newline characters

    return indexed_lines

def prep_fasta_sites():
    parse_list = to_parse.split(" ")
    output_strings = filter_strings_with_no_numbers(parse_list)
    string_this = '\n'.join(output_strings)  # Join lines with newline characters
    output_str = string_this_to_fasta(string_this)

    open('arigent_sites.txt', 'w').close()
    with open('arigent_sites.txt', 'w') as fp:
        for item in output_str:
            # write each item on a new line
            fp.write("%s\n" % item)
        print('Done')

def blast_to_xml():
    open('results.xml', 'w').close()

    sequence_data = "CATTCAATGTTACCTTCCAA"
    #command = f"blastn -qseqid {sequence_data} -db refseq_genomic -outfmt 5 -perc_identity 100"
    #result = subprocess.run(command, shell=True, capture_output=True)

    #sequence_data = open("arigent_sites.txt").read()
    result_handle = NCBIWWW.qblast(program="blastn", database="refseq_genomic", sequence=sequence_data, entrez_query="9606[taxid] AND grch38",perc_ident=100,word_size=len(sequence_data))

    with open('results.xml', 'w') as save_file:
        blast_results = result_handle.read()
        save_file.write(blast_results)

def parse_xml_to_bed():
    result=open("results.xml","r")
    records= NCBIXML.parse(result)
    item=next(records)
    for alignment in item.alignments:
        if "chromosome" in alignment.title:
            chrnum = alignment.title.split("chromosome: ")[1] if "chromosome: " in alignment.title else alignment.title.split("chromosome ")[1]
            chrnum = chrnum if (chrnum=='Z' or chrnum=='X') else int(re.search(r'\d+', chrnum).group())

            for hsp in alignment.hsps:
                print(f"{hsp.query=}")
                print(f"{hsp.score=}")
                start = hsp.sbjct_end
                end = hsp.sbjct_start
                print(f"chr{chrnum}",start,end)

#prep_fasta_sites()
blast_to_xml()
parse_xml_to_bed()