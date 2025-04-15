import os
from PIL import Image
import pillow_heif
from tqdm import tqdm

ARW_DIR = 'data/HEIF'
RAW_OUT_DIR = 'data/raw'

for person in os.listdir(ARW_DIR):
    person_arw_dir = os.path.join(ARW_DIR, person)
    person_raw_dir = os.path.join(RAW_OUT_DIR, person)
    os.makedirs(person_raw_dir, exist_ok=True)

    for file in tqdm(os.listdir(person_arw_dir), desc=f'Converting {person}'):
        if file.lower().endswith(('.heic', '.heif', '.hif')):
            heif_path = os.path.join(person_arw_dir, file)
            jpg_name = os.path.splitext(file)[0] + '.jpg'
            jpg_path = os.path.join(person_raw_dir, jpg_name)

            try:
                image = pillow_heif.read_heif(heif_path)
                pil_image = Image.frombytes(
                    image.mode, image.size, image.data, "raw"
                )
                pil_image.save(jpg_path, format="JPEG", quality=95)
            except Exception as e:
                print(f"Failed to convert {heif_path}: {e}")
