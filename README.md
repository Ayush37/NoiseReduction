# Noise Reduction Spatial
## Demo of implementing CICD pipeline for image noise reduction algos, conducting few sample test cases on CircleCI to test the resulting image reduction

Here I am trying to run few basic Spatial denoise algos over a with 4 differnt types of noises added.

Filters that are implemented:
1. Mean Filter
2. Median Filter
3. Guassian Filter
4. Conservative Filter

First we try to add 4 different type of noise to our image

1. Guassian Noise
2. Poission Noise
3. Sath and Pepper
4. Speckle

``` 
python addnoise.py 

```
This will create 4 distorted images in the images/ directory
Now we run our filters on top of these images

### To verify the efficacy, we will convert the images to Grayscale and run a noise calculation function before and after applying the filter

```
python MeanFilter.py 

```

## Output

### Mean Filter
```
##### Running MEAN filter on different noises ####
Estimating quality for guassian image before mean filter   0.6361
Estimating quality for guassian image after mean filter   0.1604

```
![image](https://user-images.githubusercontent.com/19201225/129359257-8ce6e98a-b8c9-4574-a6e7-0f4b87ecd63d.png)

```

Estimating quality for poisson image before mean filter    0.6416
Estimating quality for poisson image after mean filter    0.1614

```
![image](https://user-images.githubusercontent.com/19201225/129359298-805a7c58-46bd-4958-b550-2a5715add269.png)

```
Estimating quality for S&P image before mean filter   11.9353
Estimating quality for S&P image after mean filter    0.2798
```
![image](https://user-images.githubusercontent.com/19201225/129359320-4cbadc45-a26d-4576-9cec-27d2a9bfc505.png)

```
Estimating quality for speckle image before mean filter   61.4482
Estimating quality for speckle image after mean filter    0.5790
```
![image](https://user-images.githubusercontent.com/19201225/129359381-29cb4b8d-b962-499a-995a-08548d580d8f.png)


### Median Filter

```

##### Running MEDIAN filter on different noises ####
Estimating quality for guassian image before median filter   0.6361
Estimating quality for guassian image after median filter   0.1981

```
![image](https://user-images.githubusercontent.com/19201225/129360259-12e6a5f0-9e13-46aa-af00-695bec5cc6d7.png)

```
Estimating quality for poisson image before median filter    0.6416
Estimating quality for poisson image after median filter    0.1995
```

![image](https://user-images.githubusercontent.com/19201225/129360329-d54acfc4-38a2-4f66-b967-802ebe7b10d6.png)

```
Estimating quality for S&P image before median filter   11.9353
Estimating quality for S&P image after median filter    0.2358
```
![image](https://user-images.githubusercontent.com/19201225/129360392-a00f03b7-a6e1-415d-9712-5562490059bb.png)

```
Estimating quality for speckle image before median filter   61.4482
Estimating quality for speckle image after median filter    1.6339

```
![image](https://user-images.githubusercontent.com/19201225/129360465-34557a80-dd44-40a2-b455-c67593cef33f.png)

### Guassian Filter

```
python GuassianBlur.py

##### Running GAUSSIAN filter on different noises ####
Estimating quality for guassian image before Gaussian filter   0.6361
Estimating quality for guassian image after Gaussian filter   0.1825
```
![image](https://user-images.githubusercontent.com/19201225/129360835-55a0044f-dbd9-4b64-8a1c-f03db6716e3e.png)


```
Estimating quality for poisson image before Gaussian filter    0.6416
Estimating quality for poisson image after Gaussian filter    0.1836
```
![image](https://user-images.githubusercontent.com/19201225/129360901-6581c648-a318-4227-8e57-800594ed7ad1.png)


```
Estimating quality for S&P image before Gaussian filter   11.9353
Estimating quality for S&P image after Gaussian filter    0.2732
```
![image](https://user-images.githubusercontent.com/19201225/129360925-bb76629c-d5ea-4660-b4b7-3ba839c33792.png)

```
Estimating quality for speckle image before Gaussian filter   61.4482
Estimating quality for speckle image after Gaussian filter    0.3154

```
![image](https://user-images.githubusercontent.com/19201225/129360982-ffa79db8-fc8e-4cb0-8d64-fa8bf12123f4.png)

We can also run UnitTest on these algos

```
python -m unittest

(DJ) ag841k@US-00010509:~/AG/TopazLabs$ python -m unittest test.py
....
----------------------------------------------------------------------
Ran 4 tests in 13.222s

```

