# Running on Kaggle
Note: Using Kaggle will let you implement code for the CS 361 final project through your browser instead of having to install torchvision on your computer.

1. Download/git clone the project code. The code contains the ```kaggle/``` and ```local/``` folder. You will only need the ```kaggle/``` folder.

2. Create an account on Kaggle (any email works).

3. On Kaggle, click on Notebooks on the left side of the screen. Click ``` + New Notebook ```. Select language: Python. Select type: Notebook. Ignore advanced settings. Click Create.

5. Go to File -> Upload Notebook. Then upload the Python notebook for part 1 from the ```kaggle/``` folder. Save this notebook by clicking Save Version in the upper right hand corner. Please use the code in the kaggle/ folder, not the local/ folder.

6. Repeat steps 3-4 for the Python notebook for part 2. You should now have 2 separate notebooks on Kaggle.

7. Open the part 2 notebook on Kaggle. Click ``` + Add Data``` on the top right. Then click ```Search by URL```. Enter this URL ```https://www.kaggle.com/brianyangcoder/cs-361-mnist-data``` into the search box. Click ```Add``` for the dataset that says ```CS 361 MNIST Data```. 
    - **If you are having issues with adding the data or the page says ```Draft Session Fatal```, you may need to enable phone verification on the panel on the right. Once you've verified your phone number, you should enable Internet and then retry this step again.**

8. To save a file, click ```Save Version``` on the top. Select either ```Quick Save``` or ```Save & Run All```. Kaggle will autosave every few seconds, but in case you lose connection, you should click ```Save Version``` to save multiple versions of your code.

9. Optional: Click the title of your notebook on the top and rename it so that you can find it later. The title usually looks like ```kernel<random characters>```, but rename it so that you can find the notebook more easily next time.


# Running Locally
1. Download/git clone the project code. The code contains the ```kaggle/``` and ```local/``` folder. You will only need the ```local/``` folder.

2. Run ```pip install torch torchvision``` on the terminal. This may take a long time.

3. Open either `.ipynb` file in Jupyter/Anaconda to start writing code.

# Other Things to Note
- You only need the MNIST_data/ folder for part 2 of the coding portion.

- If you’d like to move the MNIST_data/ folder to reorganize your folders or simply move it out of the way, note that the Python notebook for part 2 will need to be able to find this folder.
To change where the notebook should look for the MNIST_data/ folder, replace:
```python
trainset = datasets.MNIST('./MNIST_data', download=False, train=True, transform=transform)
valset = datasets.MNIST('./MNIST_data', download=False, train=False, transform=transform)
```
with
```python
trainset = datasets.MNIST('<path to MNIST_data/ folder>', download=False, train=True, transform=transform)
valset = datasets.MNIST('<path to MNIST_data/ folder>', download=False, train=False, transform=transform)
```

- If you are using Kaggle, please use the code in the ```kaggle/``` folder, not the code in ```local/```. The Python notebooks in both ```local/``` and ```kaggle/``` are mostly the same except that the part 2 notebooks in ```kaggle/``` need the datasets to be uploaded to kaggle.
