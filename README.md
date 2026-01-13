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
├── scripts/          #Training and inference scripts
├── data/             #Dataset configuration
├── saved_models/     #Trained YOLOv8 model (not pushed)
├── sam_models/       #SAM checkpoint (not pushed)
├── final_results/    #Output images (not pushed)
├── requirements.txt
├── .gitignore
└── README.md
```

  

## YOLOv8 Training

YOLOv8 was trained on a custom dataset containing safety-related classes.  
The trained model (`best_v1.pt`) is stored locally and is not included in this repository due to file size constraints.

## YOLOv8 + SAM Integration

After object detection using YOLOv8, the detected bounding boxes are passed to the Segment Anything Model. SAM generates accurate segmentation masks for each detected object, resulting in improved object boundary representation.

This integration enhances the interpretability of safety violations and protective equipment detection.

## Results

- YOLOv8 provides fast and reliable object detection.
- SAM improves spatial accuracy through segmentation.
- The combined approach produces clearer and more informative outputs compared to detection alone.

Sample results are used for evaluation and demonstration purposes.

The system demonstrates effective detection and segmentation under controlled conditions and serves as a strong baseline for further real-time deployment.


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