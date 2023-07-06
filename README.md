# Disease-Diagnosis-Using-Nail-Images

This project was done as a part of Externship program in Artificial Intelligence from SmartInternz.

NOTE: DiseaseDiagnosisUsingNailImages is the main directory of the project. The other three folders contains the team members individual assignments that were given as a part of the Externship program.

1.	Introduction

  	Human nails have special characteristics that make early illness detection always possible. Physical changes in the patient's nails are the earliest signs of disorders affecting the liver, lungs, heart, kidneys, and several other organs. Examples of diseases whose initial symptoms can be seen through the patient's nails include anemia, diabetes, and arthritis. It has been noted that this built-in protection system of the human body is frequently disregarded and seen in a humorous way. Our goal is to create an AI-based-automatic nail image classifier that can examine an image and identify a patient's vulnerable disease. 

2. Dataset Collection

   We have used two datasets to build the models. We have trained four models using the dataset provided by SmartInternz. We have also trained a model using our own dataset. The datasets can be accessed using the link : https://drive.google.com/drive/folders/1puw4t__ZZmXjFf4dEdKE7CjEUt_8QLu0?usp=sharing

3. Proposed Method

   We have trained 5 models and the details are as follows:
   
   ![image](https://github.com/Varshinits/Disease-Diagnosis-Using-Nail-Images/assets/83009058/10a72b2e-a5e3-40e8-9711-ced4f856e7b4)

    All the trained model weights can also be found in the same link as that of the dataset.

     This model has been integrated with a web app usig Flask that can be deployed locally.
  
5. Conclusion

   This research has used Five pre-trained Transfer Learning models on two different dataset. The first dataset – Dataset1 is a multiclass dataset with 17 classes. The Dataset2 is a multiclass dataset with 12 classes. Among all the models used in this research four model were trained on Dataset1 and one model was trained with Dataset2. The four Transfer Learning models that were trained on Dataset1 are: VGG16, ResNet121-ResNet50 hybrid, DenseNet121, DenseNet121-VGG16. The first two models were trained used Adam optimizer and the next two models were trained using RMSProp optimizer. The last model that was trained on Dataset2 uses a Transfer Learning model combining DenseNet121 and ResNet50 with Adam optimizer. Among the five transfer learning model used in this research, the model performing with a concatenation of DenseNet121-VGG16 and RMSProp optimizer on Dataset1 (Dataset given by SmartBridge) gave better results with an accuracy of 98.72% and an average minimum loss of about 0.0543. 

6. Future Scope

   The user interface used does not store the data of the user, where they can refer it for their future consultations. The approach can be implemented on a big scale using a variety of web applications and enough database systems. We can also integrate an interactive medical-voice assistant to the user interface which can enable them interact and clear their doubts on their disease. Also the web result can give a description about the predicted disease.

# Method to run the project

1. Download DiseaseDiagnosisUsingNailImages folder and unzip the folder.
2. Download the models from the drive link unzip the folder and move the contents. Ensure the DiseaseDiagnosisUsingNailImages folder looks like that in below image:
   
   ![image](https://github.com/Varshinits/Disease-Diagnosis-Using-Nail-Images/assets/83009058/5aeec454-fcfd-4271-b1b7-88f4f6a3efa8)

3. Open DiseaseDiagnosisUsingNailImages folder using VSCode or any preferred ide and run app.py
4. NOTE: replace the .h5 file name with other models or any other trained model in app.py to try working of other models. Also PNG file shown in the image is not added in the repository as those images were used just to check the working of the web app and model. The images can be used according to personal preferrence.
