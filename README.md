

# SuperCaustics
 **Official Repository for SuperCaustics: Real-time,  open-source simulation of transparent objects for deep learning applications**
    
  This repo is a work in progress. 

SuperCaustics is a simulation tool made in Unreal Engine for generating massive computer vision datasets that include transparent objects.
SuperCaustics is specifically compatible with [ClearGrasp](https://github.com/Shreeyak/cleargrasp "ClearGrasp").  You can process the data you collect using the [Dataset Creator](https://github.com/MMehdiMousavi/SuperCaustics/blob/main/Dataset%20Creator.ipynb "Dataset Creator Script") into their style of data, though you dont specifically have to use that pipeline. You can also use the [Neural Networks](https://github.com/MMehdiMousavi/SuperCaustics/tree/main/Neural%20Networks "neural networks") provided in this repository.

<p align="center">
  <img src="Assets/SuperCaustics.gif" alt="drawing" width="600"/>
</p>

<p align="center">
  <img src="Assets/Showcase.png" alt="drawing" width="600"/>
</p>
<p align="center">
  

Transparent objects are a very challenging problem in computer vision. They are hard to segment or classify due to their lack of precise boundaries, and there is limited data available for training deep neural networks. As such, current solutions for this problem employ rigid synthetic datasets, which lack flexibility and lead to severe performance degradation when deployed on real-world scenarios. In particular, these synthetic datasets omit features such as refraction, dispersion and caustics due to limitations in the rendering pipeline. To address this issue, we present SuperCaustics, a real-time, open-source simulation of transparent objects designed for deep learning applications. SuperCaustics features extensive modules for stochastic environment creation; uses hardware ray-tracing to support caustics, dispersion, and refraction; and enables generating massive datasets with multi-modal, pixel-perfect ground truth annotations. To validate our proposed system, we trained a deep neural network from scratch to segment transparent objects in difficult lighting scenarios. Our neural network achieved performance comparable to the state-of-the-art on a real-world dataset using only 10% of the training data and in a fraction of the training time. Further experiments show that a model trained with SuperCaustics can segment different types of caustics, even in images with multiple overlapping transparent objects. To the best of our knowledge, this is the first such result for a model trained on synthetic data.
  
 
<p align="center">
**System Overview:**
</p>
<p align="center">
<img src="Assets/Diagram.png" alt="drawing" width="600"/>
</p>



Contact: 
If you have questions or comments (or bugs!) please open a github issue or contact me at:
mehdimousavi.redcap[at]gmail[dot]com

  ## Installation
  This repository is tested with Unreal Engine 4.26 on Windows 10 (SuperCaustics Simulations) and Ubuntu 16.04 (Neural Networks), Python 3.7, Pytorch 1.7.1 and Easytorch 2.8.3  
    
   **Hardware Requirements:**

    - nvidia geforce rtx 2060 (or higher) for real-time ray-tracing 
    - intel core i5 7600K (or better)
    - 8 GB RAM (preferred 16 GB)
    - 4 GB disk space
    - ample disk space for raw dataset to occupy

**Software Requirements:**

    pip install easytorch pytorch torchvision pillow numpy imageio shutil opencv-python
    (not required but recomeneded for editing) Unreal Engine 4.26





