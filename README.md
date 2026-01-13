# Smart Campus Safety Detection Using YOLOv8 & SAM

This project focuses on improving safety compliance in campus environments such as laboratories and workshops through automated visual monitoring. The system is designed to detect commonly used safety equipment, including helmets, gloves, and masks, and to highlight these objects in real time using computer vision techniques.

By combining object detection and segmentation models, the project reduces the need for continuous manual supervision and provides a practical approach to real-time safety monitoring.

## Objectives

- To identify campus safety equipment in live video streams using a deep learning–based object detection model  
- To generate precise, pixel-level segmentation for detected safety objects  
- To present detection and segmentation results through an interactive web-based interface  

## Technology Stack

- **Programming Language:** Python (version 3.9 or above)  
- **Object Detection:** YOLOv8 (Ultralytics)  
- **Segmentation:** Segment Anything Model (SAM)  
- **Computer Vision:** OpenCV  
- **Web Interface:** Streamlit 

## Project Progress

- Phase 1: Project planning and environment setup – Completed  
- Phase 2: Dataset collection and preparation – Completed  
- Phase 3: YOLOv8 model training and evaluation – Completed  
- Phase 4: YOLOv8 and SAM integration – In progress  

## YOLOv8 Model Training and Results

The object detection model was trained using a custom dataset created specifically for campus safety scenarios. The dataset includes multiple safety-related classes such as helmets, gloves, masks, and apron-based protective equipment. Training was performed on annotated images collected from diverse environments to improve generalization.

After training, the YOLOv8 model demonstrated consistent detection accuracy and stable performance during inference. The model is suitable for real-time usage and can effectively identify safety compliance as well as violations. Training visualizations, evaluation metrics, and selected prediction samples have been organized and stored in the results directory for further analysis.

## Future Scope

- Integration of live webcam feeds across multiple locations  
- Automated alert generation for safety violations  
- Expansion of the dataset to include additional safety equipment  
- Deployment on edge devices for real-world campus use  