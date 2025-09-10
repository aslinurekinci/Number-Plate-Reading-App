#library
import cv2
import numpy as np
from ultralytics import YOLO

#detection function
def detect_plate(image ,model_path):

    color=(0,255,0)
    font=cv2.FONT_HERSHEY_SIMPLEX

    print("[INFO].. Image is loading!")
    image_array=np.asarray(image,copy=True)

    print("[INFO].. Processing is started!")
    model=YOLO(model_path)
    results=model(image_array)[0]

    is_detected =len(results.boxes.data.tolist())

    if is_detected is not 0:
        threshold=0.5
        for result in results.boxes.data.tolist():
            x1,y1,x2,y2,score,class_id=result
            x1,y1,x2,y2=int(x1),int(y1),int(x2),int(y2)

            if score>threshold:
                cropped_image=image_array[y1:y2,x1:x2]
                cv2.rectangle(image_array,(x1,y1),(x2,y2),color,2)

                score=score*100
                class_name=results.names[int(class_id)]
                
                text=f"{class_name}: %{score:.2f}"
                cv2.putText(image_array,text,(x1,y1-10),font,0.5,color,1,cv2.LINE_AA)
    else:
        text="No Detection"
        cv2.putText(image_array,text,(10,30),font,0.5,color,1,cv2.LINE_AA)
    


    return image_array,cropped_image,is_detected