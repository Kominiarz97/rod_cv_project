import numpy as np
import cv2
import os
import imutils


def anomaly_classification(orginal_img):
    """
        Wykrywanie i klasyfikacja zagrożeń
    """

    CONFIDENCE = 0.2
    THRESHHOLD = 0.3

    # WSKAZANAIE ŚCIEŻEK DO PLIKÓW
    labels_path = os.path.join('yolo', 'classes.names')
    LABELS = open(labels_path).read().strip().split('\n')
    weights_path = os.path.join('yolo', 'yolov3.weights')
    custom_cfg_path = os.path.join('yolo', 'yolov3.cfg')

    # WYKONANIE KOPI OBRAZU , POBRANIE ROZMIARU ORAZ NAZW WARST WYJŚCIOWYCH
    net = cv2.dnn.readNetFromDarknet(custom_cfg_path, weights_path)
    image = orginal_img.copy()
    image = imutils.resize(image, 400, 600)
    (h, w) = image.shape[:2]
    layer_names = net.getLayerNames()

    layer_names = [layer_names[i[0]-1] for i in net.getUnconnectedOutLayers()]
    blob = cv2.dnn.blobFromImage(image, 1/255., (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    layer_outputs = net.forward(layer_names)

    # INICJALIZACJA LIST DLA WYKRYTYCH OBIEKTÓW, DOKLADNOSCI ORAZ ETYKIET
    my_boxes = []
    confidences = []
    class_ids = []

    # DETEKCJA
    for output in layer_outputs:
        for detection in output:
            all_scores = detection[5:]
            class_id = np.argmax(all_scores)
            confidence = all_scores[class_id]
            if confidence > CONFIDENCE:
                box = detection[0:4] * np.array([w, h, w, h])
                (x_center, y_center, width, height) = box.astype('int')

                x = int(x_center - (width/2))
                y = int(y_center - (height/2))
                my_boxes.append([x, y, int(width), int(height)])
                confidences.append(float(confidence))
                class_ids.append(class_id)

            # TLUMNIENIE SLABYCH, NAKLADAJACYCH SIE RAMEK
            idxs = cv2.dnn.NMSBoxes(my_boxes, confidences, CONFIDENCE, THRESHHOLD)

    # JEŻELI ISTNIEJE CHOCIAZ JEDNA DETEKCJA OBIEKTU TO:
    # NARYSUJ PROSTOKĄT SYMBOLIZUJACY GRANICE OBIEKTU
    if len(idxs) > 0:
        for i in idxs.flatten():
            (x, y) = (my_boxes[i][0], my_boxes[i][1])
            (w, h) = (my_boxes[i][2], my_boxes[i][3])

            color = (0, 0, 255)
            cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
            text = f'{LABELS[class_ids[i]]}'
            cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    else:
        cv2.putText(image, "Niesklasyfikowane", (30, 500), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, cv2.LINE_AA)
    return image