import cv2
import numpy as np

# 读入图片
mask＿img = cv2.imread('../configs/animated_drawing/characters/tempchar/mask_ori.png')
parse_img = cv2.imread('../outputs/segment/parse.png')
pose_img = cv2.imread('../configs/animated_drawing/characters/tempchar/pose.png')
rgb_img = cv2.imread('../configs/animated_drawing/characters/tempchar/texture.png')
# 转换为灰度图像
gray_pose = cv2.cvtColor(pose_img, cv2.COLOR_BGR2GRAY)
kernel = np.ones((10,10),np.uint8)
gray_pose = cv2.dilate(gray_pose,kernel,iterations = 1)
# pose_mask = cv2.threshold(pose, 1, 255, cv2.THRESH_BINARY)

# 边缘检测
edge_parse = cv2.Canny(parse_img, 10, 150)

# 膨胀边缘
kernel = np.ones((20,20),np.uint8)
dilation = cv2.dilate(edge_parse,kernel,iterations = 1)


# 创建一个空白图像
output = mask_img

# 将边缘部分复制到空白图像上
dilation = cv2.resize(dilation, (output.shape[1], output.shape[0]))

# dilation[pose!=0] = 0
print(dilation.shape)
print(output.shape)
output[dilation != 0] = 0
output[gray_pose != 0] = 255

# 显示结果
cv2.imwrite('temp_results/mask.png', mask_img)
cv2.imwrite('temp_results/parse.png', parse_img)
cv2.imwrite('temp_results/edge.png', dilation)
cv2.imwrite('temp_results/edge_mask.png', output)
cv2.imwrite('temp_results/pose.png', gray_pose)
