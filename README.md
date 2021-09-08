

# SuperCaustics
 **Official Repository for [SuperCaustics: Real-time, open-source simulation of transparent objects for deep learning applications](https://arxiv.org/abs/2107.11008)**
    
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
  

Transparent objects are a very challenging problem in computer vision. They are hard to segment or classify due to their lack of precise boundaries, and there is limited data available for training deep neural networks. As such, current solutions for this problem employ rigid synthetic datasets, which lack flexibility and lead to severe performance degradation when deployed on real-world scenarios. In particular, these synthetic datasets omit features such as refraction, dispersion and caustics due to limitations in the rendering pipeline. To address this issue, we present SuperCaustics, a real-time, open-source simulation of transparent objects designed for deep learning applications. SuperCaustics features extensive modules for stochastic environment creation; uses hardware ray-tracing to support caustics, dispersion, and refraction; and enables generating massive datasets with multi-modal, pixel-perfect ground truth annotations. To validate our proposed system, we trained a deep neural network from scratch to segment transparent objects in difficult lighting scenarios. Our neural network achieved performance comparable to the state-of-the-art on a real-world dataset using only 10% of the training data and in a fraction of the training time. Further experiments show that a model trained with SuperCaustics can segment different types of caustics, even in images with multiple overlapping transparent objects.   To the best of our knowledge, this is the first such result for a model trained on synthetic data.
  
 
<p align="center">
**System Overview:**
</p>
<p align="center">
<img src="Assets/Diagram.png" alt="drawing" width="600"/>
</p>



Contact: 
If you have questions or comments (or bugs!) please open a github issue or contact me at:
mehdimousavi.redcap[at]gmail[dot]com

# Installation

  This repository is tested with Unreal Engine 4.26 on Windows 10 (SuperCaustics Simulations) and Ubuntu 16.04 (Neural Networks), Python 3.7, Pytorch 1.7.1 and Easytorch 2.8.3  
    
   **Hardware Requirements:**

    - nvidia geforce rtx 2060 for real-time ray-tracing (or higher)
    - intel core i5 7600K (or better)
    - 8 GB RAM (preferred 16 GB)
    - 4 GB disk space
    - ample disk space for raw dataset to occupy

**Software Requirements:**

    - (neural networks):
    pip install easytorch pytorch torchvision pillow numpy imageio shutil opencv-python
    
    - (supercaustics editor):
     NVRTX Unreal Engine 4.26 - Caustics branch
     
    - (probe data gatherer) 
    pip install pykeyboard


# Using SuperCaustics
SuperCaustics features a fully-fledged automatic scene generation system with compatibility and user-friendliness in mind.  Using SuperCaustics to generate your own data is very easy. Heres how:

## **Unreal Engine**

To use SuperCaustics Editor, you need a compatible version of Unreal Engine 4.26x or higher.  To download Unreal Engine, follow step-by-step instructions to be added to Epic Games Github [here](https://www.unrealengine.com/en-US/ue4-on-github), and afterwards you can access and build UE4 from source [here](https://github.com/NvRTX/UnrealEngine/tree/NvRTX_Caustics-4.26).

## **Importing your own 3D Meshes**

 To import your 3D meshes, follow these steps: 

 1. Export 3D mesh into `.FBX` or any other format accepted by Unreal
    Engine. 
 2. Drag `.FBX` file and drop into a folder inside the UE4 Content browser. 
 3. Go to `Content>Logic>Glass_Actors>Master>Actor.bp` 
 4. Right-click on `Actor.bp`, and `Create a child blueprint` from `Actor.bp` 
 5. Open the child blueprint you just created. go to viewport, and drag-drop your 3D mesh into `static mesh component`. 
 6. Repeat from (1) to create as many Glass actors as you wish.

you really dont have to do this since SuperCaustics comes with free 3D meshes made for transparent object detection (curated for Cleargrasp dataset).

 <p align="left">
<img src="Assets/Tutorial_Images/static_mesh.jpg" alt="drawing" width="250"/>
</p>

## **Generating Scenes**

Using a template scene `content>maps>template>realistic.map` We can easily set up a simulation exactly how we like it. You can **create a duplicate of this scene**, or make your own scene and bring in the components we're about to discuss into the scene yourself.

   <p align="left">
<img src="Assets/Tutorial_Images/Generator_settings.jpg" alt="drawing" width="250"/>
</p>

Set the bounds of your simulation by adjusting these settings:

****1.1 Objects:****

 - `Object Range From, To` determine a range of objects to be spawned at each generated scenario.
 - `Objects to spawn` takes an `int` and spawns n number of objects.
 - `Glass Array` consists of objects within the reach of the Generator. To remove/add items from this array click on the `x` or `+` button.
 - `Add Force?` Determines if a physics impulse is added to each spawned object upon generation.
 - `Max Impulse Modifier`  sets the intensity of the impulse added in the beginning of the simulation.
 - `Spawn Offset Distance` sets the minimum distance between random spawning points.

****1.2 Camera:****

 - `Camera Space Normals?` switches between Camera-space and world-space surface normals.
 - `Intel Realsense Camera?` switches between SuperCaustics custom camera and a simulated Intel Realsense camera.

## Adding or Modifying Props

**Prop Manager Module:** 
This module manages the visibility and position of props in each generated scene. You can click on each prop and change its properties however you wish, and it will be placed randomly in each iteration of the simulation. Out of the box, prop manager supports up to 6 unique props, and It can generate and output unique colors for uni-material objects at runtime. (note the tiger has a different color every time I reset the simulation.)

<p align="left">
  <img src="Assets/colors.gif" alt="drawing" width="600"/>
</p>

**Setting up props:** 
To set up your own props, you can create your `object` inside unreal engine (or elsewhere and import it), find prop manager in `world outliner` (top right of the screen), select Prop manager components and drag and drop your `object` into `static mesh` and `material` components.

<p align="left">
  <img src="Assets/Tutorial_Images/propman.jpg" alt="drawing" width="250"/>
</p>

## **Light Manager **

Light Manager is a small system that stores lighting information (colors, rotations) and handles its runtime operations. 
Light Manager has a `SuperCaustics` Category where you can change the color of the main light source along with its rotations whenever the `l` control event is pressed.

<p align="left">
  <img src="Assets/Tutorial_Images/lightman.jpg" alt="drawing" width="250"/>
</p>

## ** Blueprint Contoller and Control Events**
 Events, cameras and Data Ablation events are handled by the `level blueprint`. Level blueprint can handle every present object inside the scene. Events are triggered by keyboard control signals (keystrokes). To view and edit the level blueprint, click on `Blueprints` at the top middle of the screen, and click on `Open level blueprint`.
 
<p align="left">
  <img src="Assets/Tutorial_Images/levelbp.jpg" alt="drawing" width="250"/>
</p>
 
 Scene Control Signals:
 - `m` : changing backdrop material 
 - `d`: toggle raytracing and DLSS 
 -   `l`: lights - rotates the primary light source in `LightManager`
 - `q`: fast restart simulation
 - `c`: Take screenshot at current resolution. `(to change your resolution, run the command r.setres 1920x1080w)` *
 -  `v`: Switch views (cameras)
 
Ground-truth Control Signals:
 - `g`: show transparent object masks
 - `e`: Toggle mesh caustics
 - `t`: show depth ground-truth. 
 - `r`: show surface normals ground-truth.   
 - `o`: show outlines ground-truth
 
Notes: 
 - To save system resources during fast restarts, RTX and DLSS are set to disabled by default, so you need to press `D` everytime before taking screenshots.
 - Due to the nature of real-time ray tracing (raytracing at lower resolution, upscale and denoise) screenshots `c` made at non-native resolutions will appear noisy, since there is no denoise at the upper levels where screenshots are captured. 
 - If you wish to, you can edit these key events inside the `level blueprint`.
 - surface normals ground truth `r` only shows the surface normal modality you choose in `Generator module`.


## Probe Data Gatherer  
![Probe is named after the Protoss Resource gatherers in Starcraft. Yes, I am a game nerd.](Assets/Probe.jpg) 
Probe is a data gathering script that sends control signals to the data-ablation module inside the SuperCaustics simulation. Probe works by sending specific keyboard commands to the supercaustics window. 
How to use Probe:

**Set arguments:** 

 - `setsize`: `int` determines how many scenarios would you like
   collected.
 - `moves_file`: `address` save your moves/scenarios, for later recreation if needed.

 Run [Probe.py](https://github.com/MMehdiMousavi/SuperCaustics/blob/main/Probe/Probe.py) & Wait until data is fully collected.


<p align="center">
  <img src="Assets/Probe.gif" alt="drawing" width="600"/>
  
  Probe works with any window/application, this is probe running on another project.
</p>


## Training Neural Networks
After setting up your data, copy it somewhere accessible to the python code. Then, run: 

    python segmentation_main.py -ph train  -ms 1 -data /path/to/dataset -nw 32 -ep 35 -b 8 -gi 4 -log experiments_supercaustics

**Arguments:**  

 - `-ms` : model scale (`double`) 
 -   `-nw`: number of worker threads, usually, keep it at half of your available cpu threads (`int`)
 - `-b`: batch size. (`int`) 
 - `-gi`: gradient accumulation.  use to increase effective batch size. (`int`)
 -    `-ep`: number of epochs to train. (`int`)
 -  `-ph`: phase. (`train` or `test`)   
 - `-data`: path to your dataset. use absolute path for percision. (example: `./home/data/folder/`)
 -  `-spl`: split ratio - easytorch will split the data for train/val/test randomly. (example: `-spl  0.7 0.2 0.1`)


## Citation:
If you end up using SuperCaustics or The Neural Networks, please cite our paper: 

    @misc{mousavi2021supercaustics,
      title={SuperCaustics: Real-time, open-source simulation of transparent objects for deep learning applications}, 
      author={Mehdi Mousavi and Rolando Estrada},
      year={2021},
      eprint={2107.11008},
      archivePrefix={arXiv},
      primaryClass={cs.GR}}
