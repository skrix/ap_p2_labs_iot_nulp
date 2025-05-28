from collections import deque

class MaxFlow:
    def __init__(self):
        self.nodes_map = {}
        self.total_nodes_count = 0
        self.capacity_matrix = []
        self.source = 0
        self.sink = 0

    def _bfs(self, parent_map):
        visited = [False] * self.total_nodes_count
        queue = deque()

        queue.append(self.source)
        visited[self.source] = True
        parent_map[self.source] = 0

        while queue:
            u = queue.popleft()
            for v_idx in range(self.total_nodes_count):
                if not visited[v_idx] and self.capacity_matrix[u][v_idx] > 0:
                    queue.append(v_idx)
                    visited[v_idx] = True
                    parent_map[v_idx] = u
                    if v_idx == self.sink:
                        return True
        return False

    def _build_source(self, nodes):
        for node in nodes:
            if node in self.nodes_map:
                node_id = self.nodes_map[node]
                self.capacity_matrix[self.source][node_id] = float('inf')

    def _build_sink(self, nodes):
        for node in nodes:
            if node in self.nodes_map:
                node_id = self.nodes_map[node]
                self.capacity_matrix[node_id][self.sink] = float('inf')

    def _build_roads(self, roads):
        for u_name, v_name, capacity_value in roads:
            if u_name in self.nodes_map and v_name in self.nodes_map:
                u_id = self.nodes_map[u_name]
                v_id = self.nodes_map[v_name]
                self.capacity_matrix[u_id][v_id] = capacity_value

    def _assign_source(self, nodes):
        self.source = len(nodes)

    def _assign_sink(self, nodes):
        self.sink = len(nodes) + 1

    def _update_nodes_count(self, nodes):
        # nodes count + source + sink nodes
        self.total_nodes_count = len(nodes) + 2

    def _build_capacity_matrix(self, size):
        self.capacity_matrix = [[0] * size for _ in range(size)]

    def _build_nodes_map(self, nodes):
        self.nodes_map = { name: i for i, name in enumerate(nodes) }

    def calculate_max_flow(self, farms, shops, roads, nodes):
        self._build_nodes_map(nodes)
        self._assign_source(nodes)
        self._assign_sink(nodes)
        self._update_nodes_count(nodes)
        self._build_capacity_matrix(self.total_nodes_count)
        self._build_source(farms)
        self._build_sink(shops)
        self._build_roads(roads)

        max_flow_value = 0
        parent_map = [0] * self.total_nodes_count

        while self._bfs(parent_map):
            path_flow = float('inf')
            s_node = self.sink

            while s_node != self.source:
                path_flow = min(path_flow, self.capacity_matrix[parent_map[s_node]][s_node])
                s_node = parent_map[s_node]

            max_flow_value += path_flow

            v_node = self.sink
            while v_node != self.source:
                u_node = parent_map[v_node]
                self.capacity_matrix[u_node][v_node] -= path_flow
                self.capacity_matrix[v_node][u_node] += path_flow
                v_node = u_node

        return max_flow_value

