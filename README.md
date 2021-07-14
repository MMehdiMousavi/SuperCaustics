
# SuperCaustics
Caustics Enabled Real-time Simulation using Hardware Raytracing (NvRTX Unreal Engine 4)
**Official Repository for SuperCaustics: Real-time,  open-source simulation of transparent objects for deep learning applications**

SuperCaustics is a simulation tool made in Unreal Engine for generating massive computer vision datasets that include transparent objects.
SuperCaustics is specifically compatible with [ClearGrasp](https://github.com/Shreeyak/cleargrasp "ClearGrasp").  You can process the data you collect using the [Dataset Creator](https://github.com/MMehdiMousavi/SuperCaustics/blob/main/Dataset%20Creator.ipynb "Dataset Creator Script") into their style of data, though you dont specifically have to use that pipeline. You can also use the [Neural Networks](https://github.com/MMehdiMousavi/SuperCaustics/tree/main/Neural%20Networks "neural networks") provided in this repository.

<p align="center">
  <img src="Assets/SuperCaustics.gif" alt="drawing" width="600"/>
</p>

<p align="center">
  <img src="Assets/Showcase.png" alt="drawing" width="600"/>
</p>
<p align="center">

**Software Requirements for Neural Networks and Image Processing:**

    pip install easytorch pytorch torchvision pillow numpy imageio shutil opencv-python

  **Requirements for running SuperCaustics Simulation:**

    Geforce RTX 2060 (or higher), Intel core i5 7600K (or better), Unreal Engine 4.26 (for editing)


  
  This repo is a work in progress. 
