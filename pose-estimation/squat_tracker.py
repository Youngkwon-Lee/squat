import cv2
import torch
import torchvision
from torchvision.transforms import functional as F

# Keypoint R-CNN 모델 로드
model = torchvision.models.detection.keypointrcnn_resnet50_fpn(pretrained=True)
model.eval()

# 웹캠 활성화
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # 이미지 변환 및 모델 입력
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image_tensor = F.to_tensor(image).unsqueeze(0)
    
    with torch.no_grad():
        prediction = model(image_tensor)
    
    # 예측된 keypoints 시각화
    for box, keypoints in zip(prediction[0]['boxes'], prediction[0]['keypoints']):
        x1, y1, x2, y2 = map(int, box.tolist())
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
        for kp in keypoints:
            x, y, confidence = map(int, kp.tolist())
            if confidence > 0.5:  # 신뢰도 필터링
                cv2.circle(frame, (x, y), 3, (0, 0, 255), -1)
    
    cv2.imshow('Keypoint-RCNN Pose Estimation', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()