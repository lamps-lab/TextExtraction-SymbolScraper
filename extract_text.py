import xml.etree.ElementTree as ET
import argparse
import os
import html
import re

"""This module uses SymbolScraper to extract all text from a PDF file"""

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--xml", required = True, help = "path to the xml file")
    parser.add_argument("-i", "new_xml", required = True, help = "path to the corrected xml file")
    parser.add_argument("--outputDirectory", help = "path to save the result of each page")
    parser.add_argument("--textName", help = "name of output .txt file ")
    return parser

# TODO
def remove_invalidCharacter():
    parser = get_args()
    args = parser.parse_args()
    xml_path = args.xml
    file = open(xml_path)
    text = file.read()
    file.close()
    text = re.sub("(&#)[0-9]?;?", "", text)

    # get the relative path of the xml directory and join with "_corrected.xml"
    file2 = open(os.path.join(xml_path[:4], "_corrected.xml", 'w'))
    file2.write(text)
    file2.close()

def getRoot():
    try:

        parser = get_args()
        args = parser.parse_args()
        #TODO: open the corrected xml 
        xml_path = args.xml
        tree = ET.parse(xml_path)
        root = tree.getroot()
        return root
    except Exception as error:
        print(error)
    


# def getText(root):
#     result = []
#     try:

#         for tags in root[0]:
#             #word = []
#             for child in tags:
#                 word = []
#                 numElement = len(list(child))
#                 for i in range(numElement):
#                 # char = tags[0][i].text
#                     char = child[i].text
#                     word.append(char)
#                 words = "".join(word)
#                 result.append(words)
#             #result.append(" ")
#     except Exception as error:
#         print(error)
#     return result

def getText():
    root = getRoot()
    result = []
    try:

        for page in root:
            page_result = []
            for tags in page:

                line = []
                for child in tags:
                    word = []
                    numElement = len(list(child))
                    for i in range(numElement):
                    # char = tags[0][i].text
                        char = child[i].text
                        word.append(char)
                    words = "".join(word)
                    # page_result.append(words)
                    line.append(words)    # added code
                sentence = " ".join(line)  # added code
                page_result.append(sentence) # added code
            result.append(page_result)
    except Exception as error:
        print(error)
    return result

def createPageText():
    parser = get_args()
    args = parser.parse_args()
    output_dir = args.outputDirectory
    textFile = args.textName
    result = getText()
    fp = open(os.path.join(output_dir, textFile + ".txt"), 'w')
    for i, pageText in enumerate(result):
        fp.write(f"======================================== Page {i + 1}================================================")
        for line in pageText:

            #text = " ".join(pageText)
            line = line.replace("\n", "")
            #fp.write("\n")
            fp.write("\n")
            #fp.write(text)
            fp.write(line)
            fp.write("\n")
    fp.close()


if __name__ == '__main__':
    createPageText()