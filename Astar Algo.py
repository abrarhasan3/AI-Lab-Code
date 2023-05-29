
import heapq as hp

graph = {'Oradea':{'Zerind':71,'Sibiu':151},'Zerind':{'Oradea':71,'Arad':75},
          'Arad':{'Timisoara':118,'Sibiu':140,'Zerind':75},
          'Timisoara':{'Arad':118,'Lugoj':111},
          'Lugoj':{'Timisoara':111,'Mehadia':70},
          'Mehadia':{'Lugoj':70,'Dobreta':70},
          'Dobreta':{'Mehadia':75,'Craiova':120},
          'Craiova':{'Dobreta':120,'Rimnicu Vilcea':146,'Pitesti':138},
          'Sibiu':{'Arad':140,'Oradea':151,'Rimnicu Vilcea':80,'Fagaras':99},
          'Rimnicu Vilcea':{'Sibiu':80,'Craiova':146,'Pitesti':97},
          'Fagaras':{'Sibiu':99,'Bucharest':221},
          'Pitesti':{'Bucharest':101,'Rimnicu Vilcea':97,'Craiova':138},
          'Bucharest':{'Fagaras':211,'Pitesti':101,'Giurgiu':90,'Urziceni':85},
          'Giurgiu':{'Bucharest':90},
          'Urziceni':{'Bucharest':85,'Hirsova':98,'Vaslui':142},
          'Hirsova':{'Urziceni':98,'Eforie':86},
          'Eforie':{'Hirsova':86},
          'Vaslui':{'Urziceni':142,'Iasi':92},
          'Iasi':{'Neamt':87,'Vaslui':92},
          'Neamt':{'Iasi':87}}
hsld = {'Arad':366, 'Bucharest':0, 'Craiova':160, 'Dobreta':242, 'Eforie':161, 'Fagaras':176, 'Giurgiu':77, 'Hirsova':151, 'Iasi':226, 'Lugoj':244, 'Mehadia':241, 'Neamt':234, 'Oradea':380, 'Pitesti':100, 'Rimnicu Vilcea':193, 'Sibiu':253, 'Timisoara':329, 'Urziceni':80, 'Vaslui':199, 'Zerind':374}

heap = []
hp.heapify(heap)
visited =[]
start = 'Arad'
current = (hsld.get(start),0,start,[])

goal = 'Bucharest'
visited+=[current[2]]

path1 = {}


while current[2]!=goal:
    #print(current)
    temp = []
    for item in graph[current[2]]:
        if (item in visited)==False:
            
            cost = graph[current[2]].get(item)
            h_x = hsld.get(item)
            f = cost + h_x + current[1]
            t_cost = current[1]+cost
            path = current[3][:]
            path1[item]=[]+[current[2]]
            if (current[2] in path)==False:
                path+=[current[2]]
            hp.heappush(heap, (f,t_cost,item,path))
        
    visited+=[current[2]]
    current=heap[0]
    
    hp.heappop(heap)
    

a,f_cost,c,f_path = current
f_path+=[goal]


print(f_cost)
print(f_path)
