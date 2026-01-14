# Smart Campus Safety Detection Using YOLOv8 & SAM

This project focuses on improving safety compliance in campus environments such as laboratories and workshops through automated visual monitoring. The system is designed to detect commonly used safety equipment, including helmets, gloves, and masks, and to highlight these objects in real time using computer vision techniques.

The system combines:
- **YOLOv8** for real-time object detection
- **Segment Anything Model (SAM)** for precise object segmentation

YOLOv8 is responsible for locating objects in an image, while SAM refines those detections by producing pixel-level segmentation masks. This combination helps in achieving more accurate visual understanding compared to bounding boxes alone.

## Objectives

- To identify campus safety equipment in live video streams using a deep learning–based object detection model  
- To generate precise, pixel-level segmentation for detected safety objects  
- To visualize detection and segmentation results for analysis and evaluation
  

## Technology Stack

- **Programming Language:** Python (version 3.9 or above)
- **Deep Learning Framework:** PyTorch
- **Object Detection:** YOLOv8 (Ultralytics)  
- **Segmentation:** Segment Anything Model (SAM)  
- **Computer Vision:** OpenCV

## Project Structure
```
smart-campus-safety-yolov8-sam/

scripts/
- train.py               : used to train the YOLOv8 model
- test.py                : used to test the trained model
- yolo_inference.py      : runs YOLOv8 detection only
- yolo_sam_inference.py  : runs YOLOv8 with SAM segmentation

data/
- images/
  - train/               : training images
  - val/                 : validation images
- labels/
  - train/               : training label files
  - val/                 : validation label files

samples/
- sample_construction_site.jpg
- sample_factory_worker.jpg
- sample_helmet.jpg
- sample_helmet_gloves.jpg
- sample_indoor_safety.jpg
- sample_multiple_people.jpg

saved_models/
- best.pt                : trained YOLOv8 model (not pushed to GitHub)

sam_models/
- sam_vit_b_01ec64.pth   : SAM checkpoint (not pushed to GitHub)

final_results/
- val_outputs/           : output images after YOLOv8 + SAM inference

requirements.txt         : list of required Python packages
data.yaml                : dataset configuration file
.gitignore               : files and folders ignored by Git
README.md                : project documentation
```

  

## YOLOv8 Training

YOLOv8 was trained on a custom dataset containing safety-related classes.  
The trained model (`best.pt`) is stored locally and is not included in this repository due to file size constraints.

## YOLOv8 + SAM Integration

After object detection using YOLOv8, the detected bounding boxes are passed to the Segment Anything Model. SAM generates accurate segmentation masks for each detected object, resulting in improved object boundary representation.

This integration enhances the interpretability of safety violations and protective equipment detection.

## Results

- YOLOv8 provides fast and reliable object detection.
- SAM improves spatial accuracy through segmentation.
- The combined approach produces clearer and more informative outputs compared to detection alone.

Sample results are used for evaluation and demonstration purposes.

The system demonstrates effective detection and segmentation under controlled conditions and serves as a strong baseline for further real-time deployment.

## Sample Inference

Raw images placed in the `samples/` folder were used as input for
YOLOv8 and SAM inference. The generated output images with bounding
boxes and segmentation masks are saved in `final_results/val_outputs`.



## How to Run

> Python version: 3.9+

1. Create a virtual environment
2. Install dependencies from `requirements.txt`
3. Download the SAM checkpoint manually
4. Place trained YOLO model in `saved_models/`
5. Run `scripts/yolo_sam_inference.py`

## Note

Large files such as trained models, checkpoints, and output images are excluded from the repository and should be added manually before execution.

## Future Scope

- Integration of live webcam feeds across multiple locations  
- Automated alert generation for safety violations  
- Expansion of the dataset to include additional safety equipment  
- Deployment on edge devices for real-world campus use