from ultralytics import YOLO
import cv2
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# load yolov8 model
model = YOLO('yolov8n.pt')

# load video
video_path = './cars.mp4'
cap = cv2.VideoCapture(0)

ret = True
# read frames
while True:
    try:
    
        ret, frame = cap.read()
        results = model.track(frame, persist=False)
        frame_ = results[0].plot()
        cv2.imshow('frame', frame_)
        k=cv2.waitKey(100)
        if k==27:
            break
        result=results[0]
        box = result.boxes[0]
        class_id = result.names[box.cls[0].item()]
        print(f"{class_id}")

        if class_id=="tv":
            engine.say("tv detected,You are in living area")

        elif class_id=="scissors":
            engine.say("scissors detected,harmful object")

        elif class_id=="knife":
            engine.say("knife detected,harmful object")

        elif class_id=="bench":
            engine.say("bench detected,you are in classroom")

        elif class_id=="chair":
            engine.say("chair detected,You are in office")
        
        
        else:
            engine.say(class_id)
        engine.runAndWait()
        
    except Exception as e:
        pass
cap.release()
