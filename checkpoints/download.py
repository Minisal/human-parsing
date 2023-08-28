import gdown

output = 'checkpoints/lip.pth'
url = 'https://drive.google.com/uc?id=1k4dllHpu0bdx38J7H28rVVLpU-kOHmnH'
gdown.download(url, output, quiet=False)
output = 'checkpoints/atr.pth'
url = 'https://drive.google.com/uc?id=1ruJg4lqR_jgQPj-9K0PP-L2vJERYOxLP'
gdown.download(url, output, quiet=False)
output = 'checkpoints/pascal.pth'
url = 'https://drive.google.com/uc?id=1E5YwNKW2VOEayK9mWCS3Kpsxf-3z04ZE'
gdown.download(url, output, quiet=False)


