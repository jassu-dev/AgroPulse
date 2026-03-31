import time
import random
from diagnostic_engine import DiagnosticEngine
from prediction_engine import PredEngine
from logistics_engine import LogEngine
from feedback_engine import FbkEngine

class AgriAgent:
    def __init__(self):
        print("[Agent] Booting Core...")
        self.diag = DiagnosticEngine()
        self.pred = PredEngine()
        self.log = LogEngine()
        self.fbk = FbkEngine()
        
        self.prof = 1000  
        self.pref = "organic" 

    def act(self, env):
        print(f"\n[Agent] Parsing environment percepts...")
        
        st, pol = self.fbk.get_sent(env['voice'])
        r_tol = "low" if st == "Stressed" else "high"
        print(f"[Agent] Risk tolerance set to {r_tol}")
            
        p_risk = self.pred.get_risk(env['hum'])
        p_yld = self.pred.pred_yld(env['rain'], env['ph'])
        z = self.pred.get_zone(*env['npk'])
        
        dis = self.diag.scan_img(env.get('img', None))
        
        trt = None
        if dis != "healthy":
            trt = self.diag.get_trt(dis, pref=self.pref)
            self.prof -= 50
            
        rt, f_cst = self.log.get_rt()
        self.prof -= f_cst  
        
        m_prc = 200 
        rev = p_yld * m_prc
        
        if p_risk > 0.5 and trt is None and r_tol == "high":
            print("[Agent] Pest damage incurred.")
            rev *= 0.7 
            
        self.prof += rev

        print("\n--- FINAL ACTIONS ---")
        print(f"1. Mode: {r_tol} risk.")
        print(f"2. Zone: {z}.")
        print(f"3. Treatment: {trt if trt else 'None'}.")
        print(f"4. Route: {'->'.join(rt)}.")
        print(f"-> Net Profit: ${self.prof:.2f}")
        return self.prof

if __name__ == "__main__":
    env = {
        'voice': "erratic weather and bugs.",
        'hum': 80.5,
        'rain': 120.0,
        'ph': 6.2,
        'npk': (45, 30, 60), 
        'img': None 
    }
    a = AgriAgent()
    a.act(env)
