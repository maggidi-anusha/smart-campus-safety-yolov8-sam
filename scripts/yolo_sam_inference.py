import os
import cv2
import torch
import numpy as np
from ultralytics import YOLO
from segment_anything import sam_model_registry, SamPredictor

# Paths
YOLO_MODEL_PATH = "saved_models/best_v1.pt"
SAM_CHECKPOINT = "sam_models/sam_vit_b_01ec64.pth"
INPUT_DIR = "data/images/val"
OUTPUT_DIR = "runs/yolo_sam"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load YOLO model
yolo_model = YOLO(YOLO_MODEL_PATH)

# Load SAM model
sam = sam_model_registry["vit_b"](checkpoint=SAM_CHECKPOINT)
sam.to(device="cuda" if torch.cuda.is_available() else "cpu")
predictor = SamPredictor(sam)

for img_name in os.listdir(INPUT_DIR):
    img_path = os.path.join(INPUT_DIR, img_name)
    image = cv2.imread(img_path)
    if image is None:
        continue

    # YOLO detection
    results = yolo_model(image, conf=0.4)[0]

    if results.boxes is None:
        continue

    # Prepare SAM
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    predictor.set_image(image_rgb)

    for box in results.boxes.xyxy:
        box = box.cpu().numpy().astype(int)

        masks, _, _ = predictor.predict(
            box=box,
            multimask_output=False
        )

        mask = masks[0]

        # Overlay mask
        color_mask = np.zeros_like(image)
        color_mask[mask] = (0, 255, 0)
        image = cv2.addWeighted(image, 1, color_mask, 0.5, 0)

    cv2.imwrite(os.path.join(OUTPUT_DIR, img_name), image)

print("✅ YOLOv8 + SAM inference completed successfully!")
print("📁 Results saved in runs/yolo_sam/")

