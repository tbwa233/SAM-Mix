# SAM-Mix

This repository contains the implementation of SAM-Mix. The associated publication for this project is listed below:

["Annotation-Efficient Task Guidance for Medical Segment Anything,"](https://arxiv.org/pdf/2412.08575) by Tyler Ward and Abdullah-Al-Zubaer Imran. In [ISBI](https://biomedicalimaging.org/2025/), 2025.

Our proposed model performs joint semi-supervised classification and segmentation by employing a dual-branch architecture consisting of a ResNet-38 classifier and a segmenatation branch based on the Segment Anything Model (SAM). We use GradCAMs produced by the classification branch to produce bounding box prompts to guide the SAM segmentation.

## Abstract
Medical image segmentation is a key task in the imaging workflow, influencing many image-based decisions. Traditional, fully-supervised segmentation models rely on large amounts of labeled training data, typically obtained through manual annotation, which can be an expensive, time-consuming, and error-prone process. This signals a need for accurate, automatic, and annotation-efficient methods of training these models. We propose SAM-Mix, a novel multitask learning framework for medical image segmentation that uses class activation maps produced by an auxiliary classifier to guide the predictions of the semi-supervised segmentation branch, which is based on the SAM framework. Experimental evaluations on the public LiTS dataset confirm the effectiveness of SAM-Mix for simultaneous classification and segmentation of the liver from abdominal computed tomography (CT) scans. When trained for 90% fewer epochs on only 50 labeled 2D slices, representing just 0.04% of the available labeled training data, SAM-Mix achieves a Dice improvement of 5.1% over the best baseline model. The generalization results for SAM-Mix are even more impressive, with the same model configuration yielding a 25.4% Dice improvement on a cross-domain segmentation task.

## Model
![Figure](https://github.com/tbwa233/SAM-Mix/blob/main/images/arxivarch(1).png)

## Results
A brief summary of our results are shown below. Our model SAM-Mix is compared to various baselines. In the table, the best scores are bolded and the second-best scores are underlined.

## Data
In this project, we evaluate on two segmentation tasks, in-domain and cross-domain. For the in-domain task, we use the full [Liver Tumor Segmentation Benchmark (LiTS)](https://competitions.codalab.org/competitions/17094#learn_the_details-overview) for binary liver segmentation. For the cross-domain task, we use 20 CT scans from the [TotalSegmentator](https://zenodo.org/records/10047292) training dataset, again for binary liver segmentation.

## Code
The code has been written in Python using the Pytorch framework. Training requries a GPU. We provide a Jupyter Notebook, which can be run in Google Colab, containing the algorithm in a usable version. The notebook includes annotations to follow along.

## Citation
If you find this repo or the paper useful, please cite: 

**arXiv preprint**
```
@article{ward2024annotation,
  title={Annotation-Efficient Task Guidance for Medical Segment Anything},
  author={Ward, Tyler and Imran, Abdullah-Al-Zubaer},
  journal={arXiv preprint arXiv:2412.08575},
  year={2024}
}
```
