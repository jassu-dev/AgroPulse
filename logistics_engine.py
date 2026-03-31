import heapq

class LogEngine:
    def __init__(self):
        print("[LogEngine] Init A*...")
        self.g = {
            'Farm': [('C1', 10), ('H_A', 25)],
            'C1': [('Farm', 10), ('M1', 30), ('M2', 40)],
            'H_A': [('Farm', 25), ('M3', 35)],
            'M1': [('C1', 30)],
            'M2': [('C1', 40)],
            'M3': [('H_A', 35)]
        }
        self.h = {
            'M1': {'Farm': 35, 'C1': 25, 'H_A': 40, 'M1': 0, 'M2': 20, 'M3': 50},
            'M2': {'Farm': 45, 'C1': 35, 'H_A': 50, 'M1': 20, 'M2': 0, 'M3': 60},
            'M3': {'Farm': 55, 'C1': 60, 'H_A': 30, 'M1': 50, 'M2': 60, 'M3': 0}
        }
        
    def a_star(self, st, end):
        q = []
        heapq.heappush(q, (0, st, [st]))
        
        g_s = {n: float('inf') for n in self.g}
        g_s[st] = 0
        
        while q:
            f, c, p = heapq.heappop(q)
            if c == end: return p, g_s[c]
                
            for n, cst in self.g.get(c, []):
                t_g = g_s[c] + cst
                if t_g < g_s[n]:
                    g_s[n] = t_g
                    f_c = t_g + self.h[end].get(n, float('inf'))
                    heapq.heappush(q, (f_c, n, p + [n]))
                    
        return None, float('inf')

    def get_rt(self, st='Farm'):
        mds = ['M1', 'M2', 'M3']
        b_rt = None
        min_c = float('inf')
        
        for m in mds:
            rt, c = self.a_star(st, m)
            if c < min_c:
                min_c = c
                b_rt = rt
                
        print(f"[LogEngine] Best Route: {'->'.join(b_rt)} (Cost: {min_c})")
        return b_rt, min_c
