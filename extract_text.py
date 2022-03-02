import xml.etree.ElementTree as ET
import argparse
import os
import html
import re

"""This module uses SymbolScraper to extract all text from a PDF file"""

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--xml", required = True, help = "path to the xml file")
    parser.add_argument("--outputDirectory", help = "path to save the result of each page")
    parser.add_argument("--textName", help = "name of output .txt file ")
    return parser


def getRoot():
    try:

        parser = get_args()
        args = parser.parse_args()
        xml_path = args.xml
        tree = ET.parse(xml_path)
        root = tree.getroot()
        return root
    except Exception as error:
        print(error)
    


def getText():
    root = getRoot()
    result = []
    try:
        # loop through each page
        for page in root:
            page_result = []
            # loop through each line in a page
            for tags in page:

                line = []
                # loop through word in a line
                for child in tags:
                    word = []
                    numElement = len(list(child))
                    # each character in a word
                    for i in range(numElement):
                        char = child[i].text
                        word.append(char)
                    words = "".join(word)
                    line.append(words)   
                sentence = " ".join(line) 
                page_result.append(sentence)
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
