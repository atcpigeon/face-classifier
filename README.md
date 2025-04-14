# Face Classifier - Lightweight Face Recognition for Small Datasets

This is a lightweight face classification project that uses PyTorch and pre-trained face embedding models (FaceNet) to recognize people in personal photo collections. The project was developed as a fun and educational exercise based on a small set of group travel photos (not publicly shared).


## Project Goals

- Build a simple face recognition pipeline using a small number of personal photos.
- Detect and crop faces using MTCNN.
- Extract face embeddings via pre-trained FaceNet.
- Train a classifier (SVM or MLP) to recognize individuals.
- Predict and annotate who is in a new image.

## How to Use

1. Clone this repository.
2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Prepare training data: 
    - Place labeled images under `data/raw/{person_name}/image.jpg`.
4. Run scripts in the following order:
    - `01_crop_faces.py` – face detection and cropping
    - `02_extract_embeddings.py` – generate face embeddings
    - `03_train_classifier.py` – train an SVM or MLP
    - `04_predict.py` – test the model on new images

Example results (annotated images) will be saved in `results/`.

