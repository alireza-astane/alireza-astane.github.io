---
title: Digital_Holographi_Image_Processing
date: 2025-05-04 15:09:15 +0000
categories: [GitHub, Repositories]
tags: [github, digital_holographi_image_processing]
---

---
description: No description available.
---
---
toc: false
---

# Digital Holography Project

This repository contains the work carried out under the supervision of Dr Nader Reyhani at Sharif University of Technology. The project focuses on digital holography, a technique that reconstructs three-dimensional images by recording the interference patterns generated when two light sources intersect.

## Overview

Digital holography uses the intersection of two images produced by different light sources. The interference pattern that results encodes the phase and amplitude information of the light scattered by the object. In this project, such techniques have been applied to extract detailed data on the shape of red blood cells.

## Key Techniques

- **Interference Imaging:**  
  Two images with different light sources are combined so that their intersection (the interference pattern) reveals more detailed structural information about the object.

- **Noise Reduction:**  
  Various filtering and processing techniques have been applied to reduce the noise inherent in holographic data. Techniques include:  
  - Converting the input images to high-resolution arrays (using numpy with the `int64` datatype as seen in process.ipynb).  
  - Applying spatial filtering to suppress random noise.  
  - Utilizing phase mapping (phase_map.png) to enhance the identification of key features.

- **Shape Extraction:**  
  Image processing methods have been implemented to isolate and extract the shape of red blood cells. This includes converting the raw image data (from signal.bmp, signalb1.bmp, and signalb2.bmp) into quantifiable information, making it possible to analyze morphological characteristics.

## Project Artifacts

- **Notebooks and Scripts:**  
  The main processing is performed in the process.ipynb notebook which demonstrates:
  - Image file reading
  - Application of noise reduction
  - Visualization of intermediary steps using `matplotlib` and `plotly`

- **Result Representation:**  
  The final results are visualized in HTML files, such as result.html, which integrate interactive plots (via Plotly) and static analyses.

- **Figures & Images:**  
  - **Raw and Processed Images:**  
    -  – Shows the detected lines in the image used for alignment or interference pattern formation.
    -  – The final processed output after noise reduction and phase mapping.
  - **Holographic Reconstructions:**  
    - , h_res2.png, h_res3.png – Different stages of the holographic reconstruction process.
  - **Additional Data:**  
    -  – Provides the size reference used during image processing.

- **Interactive HTML Files:**  
  The HTML files (fig.html, fig1.html, fig2.html) include embedded Plotly configurations (see the script tag in each file) allowing dynamic visualization of the holography data, matching the chosen interference and reconstruction schemes.

## Conclusion

This project demonstrates the effectiveness of digital holography in extracting detailed information about the shape of red blood cells by intersecting images from different light sources. The combined techniques of noise reduction, phase mapping, and image processing result in high-quality reconstructions that aid in biomedical analysis.

For more detailed insights and step-by-step processing, please refer to the process.ipynb notebook.
