from torchvision import datasets, transforms
import shutil

transform = transforms.Compose([transforms.ToTensor(),
                                transforms.Normalize((0.5,), (0.5,)),
                                ])

trainset = datasets.MNIST('drive/My Drive/mnist/MNIST_data', download=True, train=True, transform=transform)
valset = datasets.MNIST('drive/My Drive/mnist/MNIST_data', download=True, train=False, transform=transform)

# Extract the MNIST_data folder
try:
    shutil.copytree("drive/My Drive/mnist/MNIST_data/", "./MNIST_data/")
except shutil.Error as e:
    print('Directory not copied. Error: %s' % e)
except OSError as e:
    print('Directory not copied. Error: %s' % e)

# Delete the drive/ folder since the MNIST_data folder has been extracted
try:
    shutil.rmtree("drive/")
except OSError as e:
    print('drive/ folder not found. Error: %s' % e)