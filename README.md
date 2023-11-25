# Emotify

Emotify is a unique "Music Recommendation System” that seamlessly integrates emotion detection through facial recognition. The model used in this project achieves an accuracy of approximately 72% on the provided dataset.

Click on the image to see the demo video:
[![Emotify Prototype Demo](https://img.youtube.com/vi/qTglMz0Ef_w/maxresdefault.jpg)](https://youtu.be/qTglMz0Ef_w)

The system adapts music recommendations from Spotify based on users’ emotions, identified from 7 distinctive moods:

- Angry
- Disgust
- Fear
- Happy
- Neutral
- Sad
- Surprise

## Features

- **Facial Emotion Detection**: Utilizes OpenCV and Keras for real-time emotion detection through webcam input.
- **Integration with Spotify**: Seamlessly integrates with Spotify API to play songs based on detected emotions.
- **Frontend**: React app with a 'Try Emotify' button that initiates the emotion detection process.

## Folder Structure

- `Emotify_ANKH-master`: Contains the React frontend code.
- `emotionDetection`: Backend 1 responsible for facial emotion detection.
- `songRecommender`: Backend 2 that interacts with Spotify for song recommendations.
- `certificate`: Proof of participation in the Arithemania hackathon.
- `prototype`: Demo video demonstrating the model.
- `.cache`, `.git`, `node_modules`, `package`, `package-lock`: Standard project files and dependencies.
- `me`: Image demonstrating the project to judges.
- `venue`: Picture of the first hackathon venue.
- `new.txt`: Backend-related file.

## Getting Started

1. Clone the repository:

   ```
   git clone https://github.com/urvashii-b/Emotify-Arithemania.git
   ```

2. Navigate to the respective folders for frontend and backend setups.

3. Follow the README files in each folder for specific setup instructions.

## Training Your Own Model

If you want to train your own emotion recognition model using a different dataset or architecture, you can modify the `main.py` script and use the dataset of your choice. Be sure to update the `model.h5` file with your new model.
