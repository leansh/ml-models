# ml-models

ML model artifacts for [mining-orchestrator](https://github.com/unblock-computing/mining-orchestrator). Models are stored as GitHub release assets to keep them out of git history.

## Models

| Model | Description | Used by |
|-------|-------------|---------|
| `yolov8s-barcode.onnx` | YOLOv8s barcode detection (43MB) | barcode-scanner |

## Downloading

Models are downloaded automatically during build via Gradle's `downloadModel` task. To download manually:

```bash
gh release download v1 --repo unblock-computing/ml-models --pattern "yolov8s-barcode.onnx"
```

## Adding a new model

1. Create a release tag (e.g., `yolov8s-barcode-v2`)
2. Upload the model as a release asset:
   ```bash
   gh release create yolov8s-barcode-v2 ./model.onnx --repo unblock-computing/ml-models --title "yolov8s-barcode v2"
   ```
3. Update the download URL in the consuming project's `build.gradle.kts`
