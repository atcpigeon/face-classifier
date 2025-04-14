import os
from facenet_pytorch import MTCNN
from PIL import Image
from tqdm import tqdm

# 初始化 MTCNN，关闭预处理
mtcnn = MTCNN(keep_all=False)

RAW_DIR = 'data/raw'
CROP_DIR = 'data/cropped'

for person in os.listdir(RAW_DIR):
    person_raw_path = os.path.join(RAW_DIR, person)
    person_crop_path = os.path.join(CROP_DIR, person)
    os.makedirs(person_crop_path, exist_ok=True)

    for img_name in tqdm(os.listdir(person_raw_path), desc=f'Processing {person}'):
        img_path = os.path.join(person_raw_path, img_name)

        try:
            img = Image.open(img_path).convert("RGB")

            boxes, _ = mtcnn.detect(img)

            if boxes is not None:
                box = boxes[0]
                left, top, right, bottom = [int(b) for b in box]
                face_crop = img.crop((left, top, right, bottom))
                face_crop = face_crop.resize((160, 160))

                save_path = os.path.join(person_crop_path, img_name)
                face_crop.save(save_path)
            else:
                print(f"No face detected in {img_path}.")

        except Exception as e:
            print(f"Failed to process {img_path} due to: {e}")
