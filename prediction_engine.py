import os
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans

class PredEngine:
    def __init__(self):
        print("[PredEngine] Loading models...")
        self.y_mdl = LinearRegression()
        self.c_mdl = KMeans(n_clusters=3, random_state=42, n_init='auto')
        self.train_mdls()

    def train_mdls(self):
        csv_path = os.path.join(os.path.dirname(__file__), 'data', 'Crop_recommendation.csv')
        df = pd.read_csv(csv_path)
        
        X_reg = df[['rainfall', 'ph']].values
        np.random.seed(42)
        y_reg = df['rainfall'] * 0.05 + df['ph'] * 1.2 + np.random.normal(0, 1, len(df))
        self.y_mdl.fit(X_reg, y_reg)
        
        X_cl = df[['N', 'P', 'K']].values
        self.c_mdl.fit(X_cl)
        
    def pred_yld(self, rf, ph):
        x_in = np.array([[rf, ph]])
        p_yld = self.y_mdl.predict(x_in)[0]
        print(f"[PredEngine] Yield predicted: {p_yld:.2f}t/a")
        return p_yld

    def get_zone(self, n, p, k):
        x_in = np.array([[n, p, k]])
        cl = self.c_mdl.predict(x_in)[0]
        z_map = {0: 'Zone A', 1: 'Zone B', 2: 'Zone C'}
        z = z_map.get(cl, "Unknown")
        print(f"[PredEngine] NPK Zone: {z}")
        return z

    def get_risk(self, hum):
        p_p = 0.30 
        is_hi = hum > 75.0
        
        if is_hi:
            r = (0.80 * p_p) / 0.40
        else:
            r = (0.20 * p_p) / 0.60
            
        print(f"[PredEngine] Pest Risk: {r:.2%}")
        return r
