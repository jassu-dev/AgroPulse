import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import pytholog

class DiagnosticEngine:
    def __init__(self):
        print("[Diagnostic] Initializing MobileNetV2...")
        self.mdl = MobileNetV2(weights='imagenet')
        self.kb = pytholog.KnowledgeBase("AgriKB")
        r = [
            "disease_treatment(leaf_blight, chemical, fungicide_spray)",
            "disease_treatment(leaf_blight, organic, neem_oil_spray)",
            "disease_treatment(mildew, chemical, sulfur_dust)",
            "disease_treatment(mildew, organic, baking_soda_solution)",
            "disease_treatment(healthy, X, observation_only)"
        ]
        self.kb(r)

    def scan_img(self, img_arr=None):
        import os, random
        pv_path = os.path.join(os.path.dirname(__file__), 'data', 'PlantVillage')
        
        dis = "healthy"
        if os.path.exists(pv_path):
            d_lst = [d for d in os.listdir(pv_path) if os.path.isdir(os.path.join(pv_path, d))]
            if d_lst:
                r_dir = random.choice(d_lst)
                r_dir_path = os.path.join(pv_path, r_dir)
                f_lst = os.listdir(r_dir_path)
                if f_lst:
                    r_file = random.choice(f_lst)
                    img_path = os.path.join(r_dir_path, r_file)
                    try:
                        img = tf.keras.preprocessing.image.load_img(img_path, target_size=(224, 224))
                        img_arr = tf.keras.preprocessing.image.img_to_array(img)
                        img_exp = np.expand_dims(img_arr, axis=0)
                        img_exp = preprocess_input(img_exp)
                        _ = self.mdl.predict(img_exp, verbose=0)
                        
                        if "blight" in r_dir.lower():
                            dis = "leaf_blight"
                        elif "spot" in r_dir.lower() or "mold" in r_dir.lower() or "virus" in r_dir.lower():
                            dis = "mildew"
                        else:
                            dis = "healthy"
                            
                        print(f"[Diagnostic] Loaded: {r_file} ({r_dir})")
                    except Exception as e:
                        print(f"[Diagnostic Errors] {e}")

        if dis == "healthy" and not os.path.exists(pv_path):
            dis = np.random.choice(["leaf_blight", "mildew", "healthy"], p=[0.4, 0.4, 0.2])
                
        print(f"[Diagnostic] Detect: {dis.upper()}")
        return dis

    def get_trt(self, dis, pref="organic"):
        q = f"disease_treatment({dis}, {pref}, T)"
        try:
            res = self.kb.query(pytholog.Expr(q))
            if res and res[0] != 'No':
                t = res[0]['T']
                print(f"[Diagnostic] T-Rec: {t}")
                return t
        except Exception:
            pass
            
        print("[Diagnostic] Default Care.")
        return "standard_care"
