
# SuperCaustics
Caustics Enabled Real-time Simulation using Hardware Raytracing (NvRTX Unreal Engine 4)


SuperCaustics uses nVRTX branch of Unreal Engine to generate Photorealistic images of Transparent objects for use in Deep Learning. 
SC is designed to be plug-and-play user friendly. Run the application/open the project files, enter your parameters/3D files, Use Probe to gather images, process the data using the notebook, and train your model using the data.

The images can be processed into [ClearGrasp's](https://github.com/Shreeyak/cleargrasp "ClearGrasp") style of data, and can be used after processing with their code. 

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
