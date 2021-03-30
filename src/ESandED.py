import numpy as np
import xml.etree.ElementTree as ET

def wagner_fischer(seq1, seq2):
    # Finding dimensions of matrix to be filled, add 1 since we start from zero
    n = len(seq1) + 1
    m = len(seq2) + 1

    # initialize EDMatrix matrix

    # deleting all characters and inserting all characters
    EDMatrix = np.zeros(shape=(n, m), dtype=np.float)  # fill the matrix with zeros
    EDMatrix[:, 0] = range(n)  # filling first column from 0 till n i.e. deleting all chars
    EDMatrix[0, :] = range(m)  # filling first row from 0 till m i.e. inserting all chars

    # BMatrix is the backtrack matrix. At each index, we have 3 boolean values used as flags.
    # if BMatrix(i,j) = (1, 0, 0), the distance computed in EDMatrix(i,j) came from a deletion.
    # we will use it to compute backtracking later
    BMatrix = np.zeros(shape=(n, m), dtype=[("del", 'b'), ("upd", 'b'), ("ins", 'b')])
    BMatrix[1:, 0] = (1, 0, 0)  # first column resulting from deletions
    BMatrix[0, 1:] = (0, 0, 1)  # first row resulting from insertions

    # Wagner and Fisher algorithm to calculate edit distance
    for i, l_1 in enumerate(seq1, start=1):
        for j, l_2 in enumerate(seq2, start=1):
            deletion = EDMatrix[i-1, j] + 1  # cost of deletion is 1 + cost of previous cell
            insertion = EDMatrix[i, j-1] + 1  # cost of insertion is 1 + cost of previous cell
            # cost of previous cell + calculated cost (to take ambiguity into consideration)
            substitution = EDMatrix[i-1, j-1] + (calculate_update_cost(l_1, l_2))
            # minimum distance between three operations
            minimum_op = np.min([deletion, insertion, substitution])
            # put 1 if the operation cost equal to min (operation completed) and 0 otherwise
            BMatrix[i, j] = (deletion == minimum_op, substitution == minimum_op, insertion == minimum_op)
            # adding cost to the edit distance matrix
            EDMatrix[i, j] = minimum_op
    ED = EDMatrix[n-1][m-1]
    Sim = 1/(1+ED)
    bt=naive_backtrace(BMatrix)
    storeES(seq1,seq2,bt,ED,Sim)
    return EDMatrix,ED,Sim


def calculate_update_cost(char1, char2):
    ambiguous = ["R", "S", "M", "V", "N"]  # ambiguous characters
    unambiguous = ["A", "C", "T", "G"]  # Unambiguous characters
    if char1 in unambiguous and char2 in unambiguous:  # if both chars are not ambiguous
        # if they are equal, update cost is zero, else cost is 1
        if char1 == char2:
            return 0
        else:
            return 1
    else:  # one of them is ambiguous
        if char2 in ambiguous:
            temp = char1
            char1 = char2
            char2 = temp
        if char1 == "R":
            if char2 in ["A", "R", "G"]:
                return 0.5  # if char2 is one of 'R; possibilities, avg cost is 0.5
            elif char2 in unambiguous:
                return 1
            else:
                if char2 in ["M", "S", "N"]:
                    return 0.75
                elif char2 == "V":
                    return 0.67
        if char1 == "S":
            if char2 in ["C", "S", "G"]:
                return 0.5
            elif char2 in unambiguous:
                return 1
            else:
                if char2 in ["M", "R", "N"]:
                    return 0.75
                elif char2 == "V":
                    return 0.67
        if char1 == "M":
            if char2 in ["C", "M", "A"]:
                return 0.5
            elif char2 in unambiguous:
                return 1
            else:
                if char2 in ["S", "R", "N"]:
                    return 0.75
                elif char2 == "V":
                    return 0.67
        if char1 == "V":
            if char2 in ["G", "C", "V", "A"]:
                return 0.33
            elif char2 in unambiguous:
                return 1
            else:
                if char2 in ["S", "R", "M"]:
                    return 0.67
                elif char2 == "N":
                    return 0.75
        if char1 == "N":
            if char2 in ["G", "C", "N", "A", "U"]:
                return 0.25
            elif char2 in unambiguous:
                return 1
            else:
                return 0.75
    return 0


def naive_backtrace(B_matrix):
    i, j = B_matrix.shape[0]-1, B_matrix.shape[1]-1
    backtrace_idxs = [(i, j)]

    while (i, j) != (0, 0):
        # if there is an update decrement both i and j (move up diagonally to the left)
        if B_matrix[i, j][1]:
            i, j = i-1, j-1
        # if there is a deletion decrement i (move up vertically)
        elif B_matrix[i, j][0]:
            i, j = i-1, j
        # if there is insertion decrement j (go to the left)
        elif B_matrix[i, j][2]:
            i, j = i, j-1
        # add index  moved to each time we loop
        backtrace_idxs.append((i, j))

    return backtrace_idxs

# we can create XML file from this

def storeES(word_1, word_2, bt,dist,sim):
    operations = []
    ES = []
    root = ET.Element('root')
    es = ET.SubElement(root,'ES')
    ed=ET.SubElement(root,'ED')
    distance=ET.SubElement(ed,'distance')
    distance.text=str(dist)
    similarity=ET.SubElement(ed,'Sim')
    similarity.text=str(sim)
    backtrace = bt[::-1]  # make it a forward trace: flip the list
    for k in range(len(backtrace) - 1):
        i_0, j_0 = backtrace[k]
        i_1, j_1 = backtrace[k+1]

        if i_1 > i_0 and j_1 > j_0:  # either update or no-op
            if word_1[i_0] == word_2[j_0]:  # no-op, same symbol
                op = " "
            else:  # cost increased: update
                op = "u"
                ES.append("Update <A"+str(i_1)+",B"+str(j_1)+">")
                u = ET.SubElement(es, 'u')
                index = ET.SubElement(u, 'index')
                oldData = ET.SubElement(u, 'oldData')
                newData = ET.SubElement(u, 'newData')
                index.text = str(i_0)
                newData.text = (str(word_2[j_0]))
                oldData.text = str(word_1[i_0])
        elif i_0 == i_1:  # insertion since same row
            op = "i"
            ES.append("Insert <B"+str(j_1)+">")
            i = ET.SubElement(es, 'i')
            index = ET.SubElement(i, 'index')
            data = ET.SubElement(i, 'data')
            index.text = str(i_0)
            data.text = (str(word_2[j_0]))
        else:  # j_0 == j_1,  deletion
            op = "d"
            ES.append("Delete <A"+str(i_1)+">")
            d = ET.SubElement(es, 'd')
            index = ET.SubElement(d, 'index')
            oldData = ET.SubElement(d, 'oldData')
            oldData.text = word_1[i_0]
            index.text = str(i_0)
        operations.append(op)
    # write this edit script into an xml file for later use
    b_xml = ET.tostring(root)
    with open("EditScript.xml", "wb") as f:
        f.write(b_xml)
    return operations, ES

def parseEditScript(path):

    script = ET.parse(path)
    es=script.find('ES')
    updateElements = es.findall('u')
    insertElements = es.findall('i')
    deleteElements = es.findall('d')
    updates = []
    insertions = []
    deletions = []

    for update in updateElements:
        u = [int(update[0].text), update[1].text, update[2].text]
        updates.append(u)

    for insertion in insertElements:
        i = [int(insertion[0].text), insertion[1].text]
        insertions.append(i)

    for deletion in deleteElements:
        d = [int(deletion[0].text), deletion[1].text]
        deletions.append(d)
    print(updates)
    print(deletions)
    print(insertions)
    return updates, deletions, insertions


def patchtoTarget(initial, path):
    updates, deletions, insertions = parseEditScript(path)
    print(insertions)
    sList = list(initial)
    for update in updates:
        sList[int(update[0])] = update[2]
    for deletion in deletions:
        sList[deletion[0]] = ''  # To avoid decrementing the deletion indexes: used instead of pop
    for insertion in insertions:
        sList.insert(int(insertion[0]), insertion[1])
        for insertion1 in insertions:
            insertion1[0] = int(insertion1[0])+1
    target = "".join(sList)
    return target


def patchtoInitial(target, path):
    updates, insertions, deletions = parseEditScript(path)
    sList = list(target)
    for deletion in deletions:
        sList.pop(deletion[0])
    for insertion in insertions:
        sList.insert(int(insertion[0]), insertion[1])
    for update in updates:
        sList[int(update[0])] = update[1]
    print(updates)
    initial = "".join(sList)
    return initial

def parseSequences(path):
    tree = ET.parse(path)
    sequence = []

    RNAS = tree.findall('RNA')
    for RNA in RNAS:
        sequence.append(RNA[3].text)

    print("Parsed successfully")
    return sequence
