 <p align="center"><img src="Resources\logo_blue.png"  height="85px" width="200px"></p>
 <br>

# Sea-Land_Segmentation-Tracking Using AI 🌍📡


<p align="center">
     <img src="Resources\home_page.jpg">
      <p align="center">
       <b>HOME PAGE</b>
     </p>
 </p>
 
![](https://img.shields.io/badge/License-MIT-blue)![](https://img.shields.io/badge/Version-v1-blue)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## ***Project Aims:*** 
- This project aims to solve the issue of sea level rise affecting the land in Egypt. Its objective is to analyze and 
quantify the erosion and differences occurring over time in a specific region between the sea and the land. 
Additionally, it can predict potential events such as Reducing the expected problems on military ports, floods, 
droughts, and other related problems. This will be achieved through the use of AI for Satellite Image Segmentation 
and Tracking, employing the U-Net algorithm.

 ## System Architecture ⚙
- ***Data Collection and Preparation:***
  ##### 1. Google Earth Dataset: 210 images and masks.
  ##### 2. Images: 3-band, 1000×1000, 3~5m resolution.
  ##### 3. Random sampling: 256×256 patches, 13,563 per dataset.
  <p align="center">
   <img src="Resources\Picture1.jpg"  height="210px" width="385px">
  </p>
  
 - ***Model Selection and Evaluation:***
   ##### 1. U-Net: Robust, boundary-focused sea-land segmentation.
   ##### 2. Versatile: Handles variations, limited data requirements.
   ##### 3. Evaluate Model for deployment and improvement.
   
   <p align="center">
    <img src="Resources\u-net-architecture.png"  height="550px" width="600px">
   </p>
   <p align="center">
     <b>U-NET ARCHITECTURE</b>
   </p>

   <br>
   
   <p align="center">
    <img src="Resources\acc.jpg" width="365px">
   </p>
   <p align="center">
     <b>ACCURACY</b>
   </p>

   <br>
   
## System Analysis 📊
   <p align="center">
     <p>
       - <b>Data Flow Diagram</b>
     </p>
     <img src="Resources\Picture3.png" height="580px" width="670px">
   </p>
   
   <p align="center">   
     <p>
       - <b>Use Case</b>
     </p>
     <img src="Resources\use_case.jpg" height="580px" width="650px">
   </p>
   
   <p align="center">  
     <p>
       - <b>Activity Diagram</b>
     </p>
     <img src="Resources\activity_diagram.jpg" height="580px" width="720px">   
   </p>
   

## Implementation and Design 🎬💻
- A project consisting of three pages on the main where the map and image capture are located, the analysis page through which the mask for the image and the proportion of sea and land can be obtained, and the tracking page through which the difference between places can be tracked at certain time periods.
<br>
 <p align="center">
     <p>
       <b>ANALSIS RESULT</b>
     </p>
     <img src="Resources\Analysis_result.png">
 </p>
 <p align="center">    
     <p>
       <b>TRACKING RESULT</b>
     </p>
     <img src="Resources\Trace_result.png">
 </p>
 
<br>

## Packages and Technologies 🔍💻
- [Xd (Adobe XD)](https://helpx.adobe.com/support/xd.html) 🎨: Adobe XD is a powerful design and prototyping tool. It's crucial for designing the graphical user interface (GUI) of your application, allowing you to create visually appealing and user-friendly interfaces. You can design and prototype the layout of your application screens before implementing them.
- [PyCharm](https://www.jetbrains.com/pycharm/) 🐍: is an Integrated Development Environment (IDE) for Python. It provides a development environment for coding, debugging, and running Python applications, including GUIs. PyCharm's code editor and debugging tools make the development process more efficient.
- [Jupyter Notebook](https://jupyter.org/) 📓: is an interactive web-based environment for writing and running code, especially beneficial for data analysis and machine learning model development. You can use Jupyter Notebook to experiment with code, visualize data, and document your workflow.
- [PyTkinter](https://docs.python.org/3/library/tkinter.html) 🖼️: is a standard Python library for creating GUI applications. It's essential for building the graphical user interface of your "sea-land segmentation" application. You can design windows, dialogs, buttons, and other GUI elements using Tkinter.
- [Matplotlib](https://matplotlib.org/) 📊: is a popular Python library for creating static, animated, and interactive plots and graphs. In your GUI, you might use Matplotlib to display visualizations or image previews related to your sea-land segmentation.
- [Google Maps](https://developers.google.com/maps/documentation/javascript/overview) and [Geopy](https://geopy.readthedocs.io/en/stable/) 🗺️: If your project involves geographic data or mapping, integrating Google Maps and using the Geopy library can help you display maps, geocode addresses, and calculate distances between locations.
- [scikit-learn](https://scikit-learn.org/stable/) 🧠: is a machine learning library for Python. It provides tools for data preprocessing, model selection, and evaluation, making it a valuable resource for building machine learning models related to sea-land segmentation.
- [OpenCV](https://opencv.org/) 📸: is an open-source computer vision library. It's essential for image processing and manipulation tasks, such as pre-processing satellite or aerial images before using them for segmentation.
- [NumPy](https://numpy.org/) 🔢:  is a fundamental library for numerical computing in Python. It provides support for arrays and matrices, which are often used in machine learning and image processing tasks.
- [Segmentation Models Library](https://github.com/qubvel/segmentation_models) 🖼️🧠: This library provides pre-built deep learning models for image segmentation tasks. You can use these models as a starting point for your sea-land segmentation model.
- [TensorFlow](https://www.tensorflow.org/) and [Keras](https://keras.io/) 🧠🤖:TensorFlow is an open-source deep learning framework, and Keras is an API that runs on top of it. Together, they provide a powerful platform for building and training neural networks, including image segmentation models.

<br>

  <p align="center">    
     <img src="Resources\tools.jpg">
 </p>

<br>

## [Video (Demo)](https://youtu.be/qlQtsoNzOb4?si=cnnTt9TGYMMf5o7O) 📽️
 <p align="center">
    <img src="Resources\qr_demo.png"  height="500px" width="500px">
 </p>
 
 <br>

## Project Team 👨‍🎓💪
- [**Abdelrhman Elshafey**](https://github.com/AbdelrhmanElshafey)
  [<img src="Resources\facebook.png" align="center" height="20" width="20"  >](https://www.facebook.com/AbdalrhmanElshafey)
  [<img src="Resources\linkedin.png" align="center" height="20" width="20"  >](https://www.linkedin.com/in/abdelrhman-elshafey-3342951b3/)
  
- [**Diaa Rozik**](https://github.com/diaarozik)
  [<img src="Resources\facebook.png" align="center" height="20" width="20"  >](https://www.facebook.com/diaa.salah.982982)
  [<img src="Resources\linkedin.png" align="center" height="20" width="20"  >](https://www.linkedin.com/in/diaa-rozik-979ba3214/)
  
- [**Omar Khaled**](https://github.com/okhaled11)
  [<img src="Resources\facebook.png" align="center" height="20" width="20"  >](https://www.facebook.com/profile.php?id=100010977722514)
  [<img src="Resources\linkedin.png" align="center" height="20" width="20"  >](https://www.linkedin.com/in/omar-khaled-097552226/)
  
- [**Ziad Elshal**](https://github.com/zizo100)
  [<img src="Resources\facebook.png" align="center" height="20" width="20"  >](https://www.facebook.com/zizo.elshaluwk)
  [<img src="Resources\linkedin.png" align="center" height="20" width="20"  >](https://www.linkedin.com/in/ziad-elshal-9aa006226/)
  
- [**Mohamed Essam**](https://github.com/MohamedEssam17)
  [<img src="Resources\facebook.png" align="center" height="20" width="20"  >](https://www.facebook.com/Mohammed.Elbahnasy.18)
  [<img src="Resources\linkedin.png" align="center" height="20" width="20"  >](https://www.linkedin.com/in/mohamedessam14/)
