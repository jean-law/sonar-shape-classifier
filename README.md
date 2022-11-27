# sonar-shape-classifier
Deep learning project done for PHY473O Electronics Modal - Sound and Speech. Developed in Python (Tensorflow) a convolutional neural network that permits the use of a HC-SR04 Arduino SONAR, despite its low lateral precision, to collect data on an object and determine whether it has a cylindrical or a flat contour. The SONAR emits an ultrasound pulse every 0.5 seconds to measure the distance between the SONAR and the object in front of it, and we displace the SONAR manually along an axis in order to measure the contour of an object. Full details can be found in the "sonar-ppt.pptx" and "sonar-report.pdf" (in French). Final accuracy of 80% on 10 highly-noised datasets.

This repository consists of two python scripts and one Jupyter notebook:
- 1_data_to_txtfile.py: Saves distances measured by SONAR to a text file.
- 2_txtfile_to_graphique_txtinput.py: Plots the distances in the text file in a graph, so as to create an image representing the contour of the object.
- 3_CNN.ipynb: A CNN that trains on artificially generated SONAR data and classifies whether the contour of the object is cylindrical or flat.
