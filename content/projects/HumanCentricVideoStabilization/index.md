---
title: Human Centric Video Stabilization
description: Pipeline that isolates a person from the background and stabilizes their position across every frame.
date: 2025-09-02
github: https://github.com/IndraReddy5/Human_Centric_Video_Stabilization
tags: [Python, OpenCV, MediaPipe, PyTorch, Kalman Filter]
showDate: false
---

A complete three-pass pipeline to process a video of a person, isolate them from the background, and stabilize their position on screen. Output includes a stabilized video and a side-by-side comparison with the original.

## How It Works

The pipeline runs in three passes:

**Pass 1 — Data Collection:** MediaPipe detects human pose in every frame. The midpoint between the hip/shoulder keypoints is used as a stable anchor point, and its raw shaky coordinates are stored per frame.

**Pass 2 — Trajectory Smoothing:** The raw anchor trajectory is passed through a Kalman Filter, which predicts and corrects the person's position — producing a smooth path that removes high-frequency camera shake.

**Pass 3 — Rendering:** For each frame, a warp transform moves the person from their original position to the smoothed position via `cv2.warpAffine`. Optionally, DeepLabv3 removes the background before warping.

## Stack

- **PyTorch (DeepLabv3)** — background removal
- **MediaPipe** — human pose detection
- **Kalman Filter** — trajectory smoothing
- **OpenCV** — video processing and rendering

## Results

Benchmarked on a 13s video at 25 fps (328 frames, 1080×1920):

| Time Taken | Device | Background Removal |
|:----------:|:------:|:------------------:|
| 24s        | CPU    | No                 |
| 1h 15m     | CPU    | Yes                |
| 3m 27s     | GPU    | Yes                |

## Demo

<video src="https://github.com/user-attachments/assets/105b6802-b996-4243-b734-87b756bb55e3" controls style="width:100%;border-radius:8px;margin-bottom:1rem;"></video>

<video src="https://github.com/user-attachments/assets/f47aebf1-1be0-449c-ab72-b9cf622f47e0" controls style="width:100%;border-radius:8px;margin-bottom:1rem;"></video>

<video src="https://github.com/user-attachments/assets/d1893dd2-87c5-4e8a-88cd-6ca7cd3a4a87" controls style="width:100%;border-radius:8px;margin-bottom:1rem;"></video>

## Limitations

- If MediaPipe fails on a frame, the last known position is reused; prolonged failures cause drift
- Tracks a single person — anchors on the first detected pose
