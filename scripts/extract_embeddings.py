import os
import torch
from PIL import Image
from tqdm import tqdm
import json
from torchvision import transforms
from facenet_pytorch import InceptionResnetV1

model = InceptionResnetV1(pretrained='vggface2').eval()

transform = transforms.Compose([
    transforms.Resize((160, 160)),
    transforms.ToTensor(),
    transforms.Normalize([0.5], [0.5])
])

CROPPED_DIR = 'data/cropped'
embeddings = []
labels = []

for person in os.listdir(CROPPED_DIR):
    person_dir = os.path.join(CROPPED_DIR, person)
    for img_name in tqdm(os.listdir(person_dir), desc=f'Extracting {person}'):
        img_path = os.path.join(person_dir, img_name)
        try:
            img = Image.open(img_path).convert('RGB')
            img_tensor = transform(img).unsqueeze(0)  # shape: (1, 3, 160, 160)

            with torch.no_grad():
                embedding = model(img_tensor)  # shape: (1, 512)
                embeddings.append(embedding.squeeze(0))  # shape: (512,)
                labels.append(person)
        except Exception as e:
            print(f"Failed to process {img_path}: {e}")

embeddings_tensor = torch.stack(embeddings)

os.makedirs('data/embeddings', exist_ok=True)

torch.save(embeddings_tensor, 'data/embeddings/embeddings.pt')

with open('data/embeddings/labels.json', 'w') as f:
    json.dump(labels, f)

print("Embedding extraction completed.")
