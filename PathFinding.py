import networkx as nx
class metroNamma:
    def __init__(self, starting, ending):
        self.starting = starting
        self.ending = ending

    def findrouteandfare(starting, ending):
        green_line = {1:'Madavara', 2:'Chikkabidirakallu', 3:'Manjunath Nagar', 4:'Nagasandra', 5:'Dasarahalli', 6:'Jalahalli', 7:'Peenya Industry', 8:'Peenya', 9:'Goraguntepalya', 10:'Yeshwantpur', 11:'Sandal Soap Factory', 12:'Mahalaxmi', 13:'Rajajinagar', 14:'Kuvempu Road', 15:'Srirampura', 16:'Mantri Square Sampige Road', 17:'Nadaprabhu Kempe Gowda Majestic', 18:'Chickpete', 19:'Krishna Rajendra Market', 20:'National College', 21:'Lalbagh', 22:'South End Circle', 23:'Jayanagar', 24: 'Rashtriya Vidhyalaya Road', 25:'Banashankari', 26:'Jayaprakash Nagar', 27:'Yelachenahalli', 28:'Konanakunte Cross', 29:'Doddakallasandra', 30:'Vajrahalli', 31:'Thalaghattapura', 32:'Anjanapura'}
        purple_line = {33: 'Challaghatta', 34: 'Kengeri Bus Terminal', 35: 'Mailasandra', 36: 'Pattanagere', 37: 'Jnanabharathi', 38: 'Rajarajeshwari Nagar', 39: 'Nayandahalli', 40: 'Mysuru Road', 41: 'Deepanjali Nagar', 42: 'Attiguppe', 43: 'Vijayanagar', 44: 'BSG Hosahalli', 45: 'Magadi Road', 46: 'KSR City Railway Station', 17: 'Nadaprabhu Kempe Gowda Majestic', 48: 'Sir M Visveswaraya Central College', 49: 'Dr. B R Ambedkar Vidhana Soudha', 50: 'Cubbon Park', 51: 'Mahatma Gandhi Road', 52: 'Trinity', 53: 'Halasuru', 54: 'Indiranagar', 55: 'Swami Vivekananda Road', 56: 'Baiyyappanahalli', 57: 'Benniganahalli', 58: 'Krishnaraja Puram', 59: 'Mahadevpura', 60: 'Garudacharpalya', 61: 'Hoodi Junction', 62: 'Sitarama Palya', 63: 'Kunalahalli', 64: 'Nallurahalli', 65: 'Sadaramangala', 66: 'Pattanduru Agrahara', 67: 'Kadugodi Industrial Area', 68: 'Channasandra', 69: 'Whitefield'}
        blue_line = {70: 'KIA Terminals', 71: 'Airport City', 72: 'Doddaljala', 73: 'Bettahalasuru', 74: 'Bagalur Cross', 75: 'Yelahanka', 76: 'Jakkuru Cross', 77: 'Kodigehalli', 78: 'Hebbal', 79: 'Kempapura', 80: 'Veeranna Palya', 81: 'Nagawara (intersection)', 82: 'HBR Layout', 83: 'Kalyan Nagar', 84: 'HRBR Layout', 85: 'Horamavu', 86: 'Kasturi Nagar', 58: 'Krishnaraja Puram ', 88: 'Saraswathi Nagar', 89: 'DRDO - Sports Complex', 90: 'Doddanekkundi', 91: 'ISRO', 92: 'Marathahalli', 93: 'Kadubeesanahalli', 94: 'Devarabeesanahalli', 95: 'Bellandur', 96: 'Ibblur', 97: 'Agara Lake', 98: 'Venkatapura', 99:'Central Silk Board'}
        yellow_line = {24: 'Rashtriya Vidhyalaya Road', 100: 'Ragigudda', 101: 'Jayadeva', 102: 'BTM Layout', 99: 'Central Silk Board', 104: 'Bommanahalli', 105: 'Hongasandra', 106: 'Kudlu gate', 107: 'Singasandra', 108: 'Hosa Road', 109: 'Beratena Agrahara', 110: 'Electronic City', 111: 'Infosys Foundation Konappana Agrahara', 112: 'Huskur Road', 113: 'Hebbagodi', 114: 'Bommasandra'}
        pink_line = {81: 'Nagawara', 116: 'Kadugondanahalli', 117: 'Venkateshapura', 118: 'Tannery Road', 119: 'Pottery Town', 120: 'Cantonment', 121: 'Shivajinagar', 51: 'Mahatma Gandhi Road', 123: 'Rashtriya Military School', 124: 'Langford Town', 125: 'Lakkasandra', 126: 'Dairy Circle', 127: 'Tavarekere', 101: 'Jayadeva', 129: 'JP Nagar 4th Phase', 130: 'IIMB', 131: 'Hulimavu', 132: 'Kalena Agrahara'}

        allstations=green_line.copy()
        allstations.update(purple_line)
        allstations.update(blue_line)
        allstations.update(yellow_line)
        allstations.update(pink_line)

        intersection = {17:'Nadaprabhu Kempe Gowda Majestic', 24: 'Rashtriya Vidhyalaya Road', 51: 'Mahatma Gandhi Road', 58: 'Krishnaraja Puram', 81: 'Nagawara', 99:'Central Silk Board', 101: 'Jayadeva'}

        greenlist = list(green_line.keys())
        purplelist = list(purple_line.keys())
        bluelist = list(blue_line.keys())
        yellowlist = list(yellow_line.keys())
        pinklist = list(pink_line.keys())
        pathlist = [greenlist, purplelist, bluelist, yellowlist, pinklist]

        intersectionlist = list(intersection.keys())

        def findStation(starting):
            for index, value in green_line.items():
                if value == starting:
                    return index, greenlist

            for index, value in purple_line.items():
                if value == starting:
                    return index, purplelist

            for index, value in blue_line.items():
                if value == starting:
                    return index, bluelist

            for index, value in yellow_line.items():
                if value == starting:
                    return index, yellowlist

            for index, value in pink_line.items():
                if value == starting:
                    return index, pinklist
            return 0,''

        def findIntercetion(startingIndex, path):
            shortestDist = len(path)
            #print('findinter', path)
            #print('start', startingIndex)
            startingIndex = path.index(startingIndex)
            for i in intersectionlist:
                if i in path:
                    #print('test1',i,startingIndex, path.index(i))
                    a = abs(startingIndex - path.index(i))
                    #print(a)
                    if a < shortestDist:
                        shortestDist = a
                        shortInter = i
                        return shortInter, shortestDist
                    return 0,0

        def findroute(a,b, list1):
            route = []
            #print(a,b)
            startingpoint = list1.index(a)
            endingpoint = list1.index(b)
            #print("inside findroute", list1)
            #print(a, startingpoint)
            #print(b, endingpoint)
            #print(startingpoint)
            #print(endingpoint)
            #print(startingpoint,endingpoint)
            i = startingpoint
            limit = endingpoint+1 if endingpoint>startingpoint else endingpoint-1
            while i != limit:
                route = route + [i]
                #print(a,b)
                i=i+1 if startingpoint < endingpoint else i-1
                #print("i",i)
            #print(route)
            return route

        def ConnectInter(sourceinter, destinter):
            G = nx.Graph()
            graph = [(17, 24, 16), (17, 51, 3), (24, 101, 1), (51, 81, 6), (51, 101, 5), (51, 58, 6), (58, 81, 5), (58, 99, 10),
                     (101, 99, 1)]
            G.add_weighted_edges_from(graph)
            return nx.dijkstra_path(G, sourceinter, destinter)

        def removeduplicates(testlist):
            res = []
            for i in testlist:
                if i not in res:
                    res.append(i)
            return res

        def calclutatefare(list1):
            cntr = 0
            for i in intersection.values():
                if i in list1:
                    cntr+=1
            #print(cntr)
            return 9.5 + (2.8 * cntr) + ((len(list1)-cntr) * 1.9)

        global finalshortestpath
        finalshortestpath = []

        startingIndex, startingpath = findStation(starting)
        shortInter1, shortestDist1= findIntercetion(startingIndex, startingpath)
        #print('starting',startingIndex,shortInter1)


        endingIndex, endingpath = findStation(ending)
        shortInter2, shortestDist2 = findIntercetion(endingIndex, endingpath)
        #print('ending', endingIndex, shortInter2,endingpath)


        #print(startingIndex in startingpath, endingIndex in startingpath)

        if startingIndex in startingpath and endingIndex in startingpath:
            #print('First cae success')
            for i in findroute(startingIndex, endingIndex, startingpath):
                finalshortestpath = finalshortestpath + [allstations[startingpath[i]]]
            #print('final path', finalshortestpath)

        else:
            if startingIndex in endingpath and endingIndex in endingpath:
                #print('Second Case')
                for i in findroute(startingIndex, endingIndex, endingpath):
                    finalshortestpath = finalshortestpath + [allstations[endingpath[i]]]
                #print('final path', finalshortestpath)
            else:
                if shortInter1 == shortInter2:
                    #print('case 3 success')
                    for i in findroute(startingIndex,shortInter2,startingpath):
                        finalshortestpath = finalshortestpath + [allstations[startingpath[i]]]
                    #print(finalshortestpath)
                    k = 1
                    #print('ending index',shortInter2,endingIndex)
                    for j in findroute(shortInter2,endingIndex,endingpath):
                        if k != 1:
                            finalshortestpath = finalshortestpath + [allstations[endingpath[j]]]
                        k+=1
                        #print('case 3',finalshortestpath)

                else:
                    for i in findroute(startingIndex,shortInter1,startingpath):
                        finalshortestpath = finalshortestpath + [allstations[startingpath[i]]]

                    connectedpath = ConnectInter(shortInter1,shortInter2)
                    i = 0
                    while(i < len(connectedpath)- 1):
                        start=connectedpath[i]
                        end=connectedpath[i+1]
                        for j in pathlist:
                            if start in j and end in j:
                                k = 0
                                for i in findroute(start, end, j):
                                        finalshortestpath = finalshortestpath + [allstations[j[i]]]
                        i=+1
                    for i in findroute(shortInter2,endingIndex,endingpath):
                        #print('ending path',shortInter2, endingIndex, endingpath, i)
                        finalshortestpath = finalshortestpath + [allstations[endingpath[i]]]
                        #print(finalshortestpath)

        finalshortestpath=removeduplicates(finalshortestpath)
        #print(finalshortestpath)

        totalfare = calclutatefare(finalshortestpath)
        #print(totalfare)
        return totalfare, finalshortestpath
