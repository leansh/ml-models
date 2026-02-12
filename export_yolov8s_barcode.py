#!/usr/bin/env python3
"""
Download the YOLOv8s Barcode Detection model from HuggingFace and export it
to ONNX format.

Source: https://huggingface.co/Piero2411/YOLOV8s-Barcode-Detection
  - Architecture: YOLOv8s (11.2M params)
  - Input: 640x640
  - Classes: barcode, qrcode

Usage:
    pip install ultralytics huggingface_hub
    python export_yolov8s_barcode.py

Output:
    yolov8s-barcode.onnx
"""

import sys
from pathlib import Path

HF_REPO = "Piero2411/YOLOV8s-Barcode-Detection"
HF_FILENAME = "YOLOV8s_Barcode_Detection.pt"
INPUT_SIZE = 640
OUTPUT_PATH = Path(__file__).resolve().parent / "yolov8s-barcode.onnx"


def main():
    try:
        from huggingface_hub import hf_hub_download
    except ImportError:
        print("ERROR: huggingface_hub not installed. Run: pip install huggingface_hub")
        sys.exit(1)

    try:
        from ultralytics import YOLO
    except ImportError:
        print("ERROR: ultralytics not installed. Run: pip install ultralytics")
        sys.exit(1)

    # Step 1: Download .pt from HuggingFace
    print(f"Downloading {HF_FILENAME} from {HF_REPO}...")
    pt_path = hf_hub_download(repo_id=HF_REPO, filename=HF_FILENAME)
    print(f"Downloaded to: {pt_path}")

    # Step 2: Load model and export to ONNX
    print(f"Loading model and exporting to ONNX (imgsz={INPUT_SIZE})...")
    model = YOLO(pt_path)
    onnx_path = model.export(format="onnx", imgsz=INPUT_SIZE, simplify=True)
    print(f"Exported to: {onnx_path}")

    # Step 3: Copy to output location
    import shutil
    shutil.copy2(onnx_path, OUTPUT_PATH)
    print(f"Copied to: {OUTPUT_PATH}")

    # Step 4: Verify
    size_mb = OUTPUT_PATH.stat().st_size / (1024 * 1024)
    print(f"Done. Model size: {size_mb:.1f} MB")


if __name__ == "__main__":
    main()
