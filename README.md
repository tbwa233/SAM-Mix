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

| Model         | DS (LiTS)         | HD (LiTS)         | DS (TotalSegmentator) | HD (TotalSegmentator) |
|---------------|:-----------------:|:-----------------:|:----------------------:|:----------------------:|
| U-Net         | 0.897 ± 0.010     | 13.496 ± 1.272     | 0.669 ± 0.055          | 29.588 ± 0.052         |
| nnU-Net       | 0.863 ± 0.034     | 21.407 ± 1.391     | 0.645 ± 0.013          | 38.497 ± 0.043         |
| TransU-Net    | 0.889 ± 0.005     | _12.68 ± 2.109_    | 0.642 ± 0.024          | 42.796 ± 0.038         | 
| MultiMix      | 0.627 ± 0.007     | 21.470 ± 1.901     | 0.159 ± 0.196          | 97.982 ± 0.057         |
| SAM-PP-0*     | 0.441 ± 0.012     | 67.565 ± 1.477     | 0.334 ± 0.011          | 72.150 ± 1.250         |
| SAM-PP-5      | 0.754 ± 0.006     | 36.521 ± 0.528     | 0.593 ± 0.007          | 54.784 ± 0.545         |
| SAM-PP-50     | 0.726 ± 0.005     | 30.993 ± 0.010     | 0.579 ± 0.008          | 46.513 ± 0.035         |
| SAM-PP-100    | 0.763 ± 0.003     | 26.535 ± 0.069     | 0.605 ± 0.004          | 40.328 ± 0.068         |
| SAM-Mix-5     | 0.919 ± 0.002     | 15.141 ± 0.250     | 0.807 ± 0.002          | 17.568 ± 0.086         |
| SAM-Mix-50    | **0.948 ± 0.002** | **9.842 ± 0.046**  | **0.923 ± 0.004**      | **11.164 ± 0.021**     |
| SAM-Mix-100   | _0.941 ± 0.001_   | 14.671 ± 0.052     | _0.921 ± 0.001_        | _12.926 ± 0.023_       |

\* _No segmentation training_

## Data
In this project, we evaluate on two segmentation tasks, in-domain and cross-domain. For the in-domain task, we use the full [Liver Tumor Segmentation Benchmark (LiTS)](https://competitions.codalab.org/competitions/17094#learn_the_details-overview) for binary liver segmentation. For the cross-domain task, we use 20 CT scans from the [TotalSegmentator](https://zenodo.org/records/10047292) training dataset, again for binary liver segmentation. In our open-sourced SAM-Mix implementation, we assume your datasets are stored in [HDF5](https://www.hdfgroup.org/solutions/hdf5/) format. We have provided a script to convert from the raw Nifti files of LiTS and TotalSegmentator to HDF5 format, which also applies the pre-processing techniques we used to your dataset.

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
