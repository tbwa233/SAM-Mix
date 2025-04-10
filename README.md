# SAM-Mix

This repository contains the implementation of SAM-Mix. The associated publication for this project is listed below:

["Annotation-Efficient Task Guidance for Medical Segment Anything,"](https://arxiv.org/pdf/2412.08575) by Tyler Ward and Abdullahh-Al-Zubaer Imran. In [ISBI](https://2025.midl.io/), 2025.

Our proposed model performs joint semi-supervised classification and segmentation by employing a dual-branch architecture consisting of a ResNet-38 classifier and a segmenatation branch based on the Segment Anything Model (SAM). We use GradCAMs produced by the classification branch to produce bounding box prompts to guide the SAM segmentation.
