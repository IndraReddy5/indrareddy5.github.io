---
title: About
showDate: false
---

I am a perception engineer working at the intersection of classical 3D vision and embodied AI. My current focus is SLAM, Gaussian splatting, and VLA baselines for manipulation — problems where 3D scene understanding meets policy learning on real robotic platforms. I have built scene reconstruction pipelines using COLMAP and 3DGS, deployed VR-based teleoperation on the Unitree G1 humanoid, and trained SmolVLA on contact-rich manipulation tasks. Earlier work covered LiDAR-based perception for autonomous systems — point cloud segmentation, dynamic obstacle tracking, and sensor occlusion detection. I enjoy working close to the hardware, bridging research and deployment across the full stack. Outside of work, cricket and anime keep me sane — one for the strategy, the other for the stories. Coming from the historic city of Kurnool, I bring curiosity and a bias toward building things that actually work in the real world.

## Work Experience

**Engineer - Robotics Perception**
Virya Autonomous Technologies | Aug 2026 - Present

> Working on perception systems for autonomous robotic platforms, building on prior experience in SLAM, 3D reconstruction, and sensor based scene understanding. Early days here, with plenty more to share as things ramp up on front.

**SLAM Engineer**  
Merai Newage Pvt Ltd. (A Meril Group Company) | Dec 2025 – Aug 2026

> My current work sits at the intersection of 3D scene reconstruction and embodied AI. I built an end-to-end outdoor reconstruction pipeline using 30 FPS monocular captures, COLMAP-based structure-from-motion, and 3D Gaussian Splatting with MCMC-based densification — producing scene substrates used for downstream model behaviour analysis. On the robot side, I deployed a VR-based teleoperation pipeline on the Unitree G1 humanoid using Unitree's xr-teleop package, working through dependency conflicts and network latency issues to achieve stable real-time control. I also trained a SmolVLA baseline on the LeHome dataset for cloth folding, reaching 60% / 28% task-success on train / held-out test, and built EDA pipelines and a public Gradio tool for episode inspection and joint-range analysis. Additionally, I adapted the AWS RoboMaker Hospital Gazebo world into a multi-floor simulation testbed by converting static elevator assets into dynamic, ROS-controllable models and integrating a mobile robot platform.

**Software Engineer**  
Proliant Infotech | Sep 2024 – Jul 2025

> In my role, I focused on building intelligent perception modules for autonomous systems using ROS and LiDAR data. On a daily basis, I worked on developing ROS nodes for point cloud segmentation, temporal tracking, and dynamic obstacle state estimation—achieving reliable detection of people and vehicles up to 35 meters. I also optimized data handling by converting Ouster sensor range images into compact point clouds, reducing storage needs by 80%. To improve system safety, I designed occlusion detection nodes that flagged partial or full sensor blockages in real time. Alongside this, I trained and deployed an optical flow–based ego-vehicle velocity predictor, further strengthening the overall perception stack. These contributions combined research-driven methods with practical engineering to deliver robust, real-world performance.

**Computer Vision Intern**  
Proliant Infotech | Dec 2023 - Sep 2024

> In this role, my day-to-day work revolved around developing and deploying advanced computer vision and reinforcement learning solutions. I worked with a mix of proprietary, open-source, and simulator datasets to design robust vision algorithms and integrated spatial-temporal relationships into existing models, optimizing data input and cutting training time by 50%. I also gained hands-on deployment experience by porting models to the NVIDIA Jetson Xavier NX, ensuring efficient performance on embedded hardware. Additionally, I implemented DQN-based reinforcement learning models in the CARLA simulator, exploring both urban and off-road driving scenarios to advance autonomous decision-making. This combination of research, optimization, and real-world deployment shaped a strong end-to-end workflow in AI-driven autonomy.


## Education

<div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem; margin-top:1rem;">
  <div style="padding:1.25rem; border:1px solid var(--ed-color-border); border-radius:8px;">
    <div style="font-weight:700; color:var(--ed-color-heading);">BS · Data Science & Applications </div>
    <div style="font-size:0.875rem; color:var(--ed-color-text-muted); margin-top:0.25rem;">Minor in Generative AI <br> IIT Madras</div>
    <div style="font-size:0.8125rem; color:var(--ed-color-text-faint); margin-top:0.25rem;">Nov 2025</div>
  </div>
  <div style="padding:1.25rem; border:1px solid var(--ed-color-border); border-radius:8px;">
    <div style="font-weight:700; color:var(--ed-color-heading);">B.Tech · Electrical & Electronics </div>
    <div style="font-size:0.875rem; color:var(--ed-color-text-muted); margin-top:0.25rem;">G. Pulla Reddy Engineering College</div>
    <div style="font-size:0.8125rem; color:var(--ed-color-text-faint); margin-top:0.25rem;">Feb 2022</div>
  </div>
</div>
