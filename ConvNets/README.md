Convolutional Neural Networks:

This is a repo to all beginner-friendly convolutional neural networks for different use cases, mainly image tasks. Although these are mainly for reference purpose, the notebooks can be downloaded to run in Google Colab.

How to use:
1. Download the notebook.
2. Upload notebook to your Google Drive to utilize Google Colab that provides a free GPU.
3. Connect to a hosted runtime to start using their GPU.
4. Go to "Edit -> Notebook settings" and change "Hardware Accelerator" to GPU.
5. Start by running each cell to see the results.

Content:
1. Beginner Convolutional Neural Network 
  - How to code a basic CNN that takes in as input a set of images and classify them accordingly
  
2. Cats and Dogs Classifier
  - Using a basic convolutional neural network to classify cats and dogs images
  - Perform data augmentation to increase data size and prevent overfitting
  
3. AlexNet
  - Using a modified version of AlexNet that takes in images of shape (224, 224, 3) instead of (150, 150, 3)
  
4. VGG16
  - Using a modified version of VGG16 that reached a higher accuracy than AlexNet with less overfitting
  
5. Transfer learning based on VGG-16
  - Using transfer learning based on VGG-16, a cats and dogs classifier can be trained with shorter duration and higher accuracy/less overfitting
