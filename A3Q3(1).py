import sys
import heapq

def compute_transit_time(use_walking):
    vertex_map = {}
    station_to_vertex = []
    graph = []
    vertex_count = 0
    
    for station in range(n):
        vertex_map[(station, None)] = vertex_count
        station_to_vertex.append(station)
        graph.append([])
        vertex_count += 1
    
    for line_id in range(m):
        for station in station_list[line_id]:
            if (station, line_id) not in vertex_map:
                vertex_map[(station, line_id)] = vertex_count
                station_to_vertex.append(station)
                graph.append([])
                vertex_count += 1
    
    for station in range(n):
        base_vertex = vertex_map[(station, None)]
        for line_id in range(m):
            if station in station_list[line_id]:
                line_vertex = vertex_map[(station, line_id)]
                graph[base_vertex].append((line_vertex, waiting[line_id]))
    
    for line_id in range(m):
        stations = station_list[line_id]
        times = traveling[line_id]
        for i, station in enumerate(stations):
            curr_vertex = vertex_map[(station, line_id)]
            
            if i < len(stations) - 1:
                next_station = stations[i + 1]
                next_vertex = vertex_map[(next_station, line_id)]
                graph[curr_vertex].append((next_vertex, times[i]))
            
            if i > 0:
                prev_station = stations[i - 1]
                prev_vertex = vertex_map[(prev_station, line_id)]
                graph[curr_vertex].append((prev_vertex, times[i - 1]))
    
    for station, trans_info in transfer.items():
        for (from_line, to_line), trans_time in trans_info.items():
            from_vertex = vertex_map[(station, from_line)]
            to_vertex = vertex_map[(station, to_line)]
            total_time = trans_time + waiting[to_line]
            graph[from_vertex].append((to_vertex, total_time))
    
    if use_walking:
        for (s1, s2), walk_time in walking.items():
   
            v1 = vertex_map[(s1, None)]
            v2 = vertex_map[(s2, None)]
            graph[v1].append((v2, walk_time))
            graph[v2].append((v1, walk_time))
            
            for line_id in range(m):
                if s1 in station_list[line_id]:
                    v1_line = vertex_map[(s1, line_id)]
                    graph[v1_line].append((v2, walk_time))
                if s2 in station_list[line_id]:
                    v2_line = vertex_map[(s2, line_id)]
                    graph[v2_line].append((v1, walk_time))
    

    result = []
    for start in range(n):
        distances = [float('inf')] * vertex_count
        min_station_time = [float('inf')] * n
        start_vertex = vertex_map[(start, None)]
        distances[start_vertex] = 0
        
        pq = [(0, start_vertex)]
        while pq:
            curr_time, curr_vertex = heapq.heappop(pq)
            if curr_time > distances[curr_vertex]:
                continue
            
            curr_station = station_to_vertex[curr_vertex]
            min_station_time[curr_station] = min(
                min_station_time[curr_station],
                curr_time
            )
            
            for next_vertex, edge_time in graph[curr_vertex]:
                new_time = curr_time + edge_time
                if new_time < distances[next_vertex]:
                    distances[next_vertex] = new_time
                    heapq.heappush(pq, (new_time, next_vertex))
        
        result.append(min_station_time)
    
    return result

def compare_transit_time():
    res1 = compute_transit_time(False)
    res2 = compute_transit_time(True)
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[i][j] = res1[i][j] - res2[i][j]
    return res

s = sys.stdin.readline().split()
n, m = int(s[0]), int(s[1])
waiting = []
station_list = []
traveling = []
for _ in range(m):
    s = sys.stdin.readline().split()
    waiting.append(int(s[0]))
    st, tr = [], []
    for i in range(1, len(s), 2):
        st.append(int(s[i][1:]))
        if i + 1 < len(s):
            tr.append(int(s[i+1]))
    station_list.append(st)
    traveling.append(tr)
nn = int(sys.stdin.readline())
transfer = {}
for _ in range(nn):
    s = sys.stdin.readline().split()
    st = int(s[0][1:])
    transfer[st] = {}
    for i in range(1, len(s)):
        ss = s[i].split(':')
        l1, l2, t = int(ss[0][1:]), int(ss[1][1:]), int(ss[2])
        transfer[st][l1, l2], transfer[st][l2, l1] = t, t
mm = int(sys.stdin.readline())
walking = {}
for _ in range(mm):
    s = sys.stdin.readline().split()
    s1, s2, t = int(s[0][1:]), int(s[1][1:]), int(s[2])
    walking[s1, s2], walking[s2, s1] = t, t
transit_time = compare_transit_time()
for i in range(n):
    print(' '.join([str(j) for j in transit_time[i]]))