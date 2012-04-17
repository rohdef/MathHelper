

def parseListOfList(data, var=None):
    if var:
        listOfLists = var + ": ["
    else:
        listOfLists = "["
    
    listOfLists += parseLinesIntoLists(data)
    
    listOfLists += "]"
    return listOfLists

def parseMatrix(data, var=None):
    if var:
        matrix = var + ": matrix("
    else:
        matrix = "matrix("
    
    matrix += parseLinesIntoLists(data)
    
    matrix += ")"
    return matrix
    
def parseLinesIntoLists(data):
    dataAsLines = data.splitlines()
    
    lists = ""
    for line in dataAsLines:
        lists += "[" + line.replace(" ", ",") + "],\n"
    
    lists = lists[:-2]
    
    return lists

def main():
    pass
    

if __name__ == '__main__':
    main()
