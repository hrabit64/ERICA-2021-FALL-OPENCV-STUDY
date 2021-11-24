from feature_extraction.feature_extractor import FeatureExtractor
import os
import cv2
import tqdm
import numpy as np
import shutil
from tensorflow.keras.preprocessing.image import load_img

def classifier(input_dir="", output_dir="", rep_img=[]):
    extractor = FeatureExtractor()
    target_files = os.listdir(input_dir)
    rep_features = dict()

    with tqdm.tqdm(total=len(rep_img)) as tqdm.pbar:
        print("<< Auto classifier >> Extract features from rep images.")
        for label_name,img_name in rep_img:

            img = load_img(os.path.join(input_dir,img_name))
            feature = extractor.run(src=img)
            rep_features[label_name] = feature
            if not os.path.exists(os.path.join(output_dir,label_name)):
                os.makedirs(os.path.join(output_dir,label_name))
            tqdm.pbar.update(1)

    with tqdm.tqdm(total=len(target_files)) as tqdm.pbar:
        print("<< Auto classifier >> Classifying images")
        for img_name in target_files:

            img = load_img(os.path.join(input_dir,img_name))
            target_feature = extractor.run(src=img)
            len_list = dict()

            for rep in rep_features.keys():
                # len_list[rep] = (np.linalg.norm(target_feature - rep_features[rep]))
                len_list[rep] = (np.linalg.norm(rep_features[rep] - target_feature))
            print(f"name // {img_name} : {len_list}")
            feature_name = min(len_list,key=len_list.get)
            shutil.copy(os.path.join(input_dir,img_name),os.path.join(output_dir,feature_name,img_name))
            tqdm.pbar.update(1)
