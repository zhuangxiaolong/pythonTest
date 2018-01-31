#pip install opencv-python
import cv2 as cv
#读取图像，支持 bmp、jpg、png、tiff 等常用格式
img=cv.imread("c:/img/test.jpg")
print(img.shape)
print(img.size)
# 获取训练好的人脸的参数数据，这里直接从GitHub上使用默认值
face_cascade = cv2.CascadeClassifier(r'./haarcascade_frontalface_default.xml')
#创建窗口并显示图像
cv.namedWindow("Image")
cv.imshow("Image",img)
cv.waitKey(0)
#释放窗口
cv2.destroyAllWindows() 