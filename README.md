This project is introducing the details of implementing a real-time streaming a binary sentiment analysis (positive, negative, neutral) pipeline using Spark Apache for English comments in Twitter including some keywords. I have implemented my sentiment analysis model and trained it using open-source dataset. After that, I have tested it with tweets from Twitter APIs to measure the accuracy of the implemented model. 

# This project has three main parts:

## **Part 1: Get tweets from the Twitter API**

In this part, I applied for Twitter developer account and  used its credentials to authenticate and connect to the Twitter API. After that, I have created a TCP socket between Twitter’s API and Spark. In order to implement this, I used Python’s **Tweepy** library for connecting and retrieving the tweets from the Twitter APIs.

## **Part 2: Tweet pre-preprocessing and ready-made sentiment analysis model**

In this part, After receiving the data from the TCP socket and preprocess it with the **pyspark** library. I have applied sentiment analysis using **textblob**, which is Python’s library for processing textual data. After sentiment analysis, we save the tweet and the sentiment analysis scores in a CSV file. This will be used later as testing data to my trained model.

## **Part 3: Building my sentiment analysis model:**

In this part, I have implemented my own sentiment analysis model. The given dataset was only positive or negative, so I have tested the Tweets to be only positive or negative (no neutral) as it was an extra feature that I have not taken into consideration during the mode. I have used **CNN** to train my model.


# For part 1 and 2:

I have followed the exact steps found in the provided link which is:

[Sentiment analysis on streaming Twitter data using Spark Structured Streaming & Python](https://towardsdatascience.com/sentiment-analysis-on-streaming-twitter-data-using-spark-structured-streaming-python-fc873684bfe3)

In order to send the Tweets from the developer account, I have to set up the environment (on Linux OS) first before heading to start. I have implemented the following steps in sequence: 

- **Install Packages Required for Spark**: first I made sure that I have installed the following
    - JDK
    - Scala
    - Git

By writing the following commands: 

```jsx
sudo apt install default-jdk scala git -y
```

```jsx
java -version; javac -version; scala -version; git --version
```

- **Download and Set Up Spark on Ubuntu**

I downloaded the Spark Apache version that I want (in this case, it was 3.1.2 with hadoop 2.7)  by writing the following command:

```jsx
wget [https://downloads.apache.org/spark/spark-3.1.2/spark-3.1.2-bin-hadoop2.7.tgz](https://downloads.apache.org/spark/spark-3.0.1/spark-3.0.1-bin-hadoop2.7.tgz)
```

```jsx
tar xvf spark-*
```

```jsx
sudo mv spark-3.0.1-bin-hadoop2.7 /opt/spark
```

- **Configure Spark Environment**

This step for configuring the environmental variables. I have written the paths into .profile as follows: 

```
echo "export SPARK_HOME=/opt/spark" >> ~/.profile
echo "export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin" >> ~/.profile
echo "export PYSPARK_PYTHON=/usr/bin/python3" >> ~/.profile
```

These commands add the following line into .profile 

```
export SPARK_HOME=/opt/spark

export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin

export PYSPARK_PYTHON=/usr/bin/python3
```

after that, I sourced the .profile file as follows:

```jsx
source ~/.profile
```

- **Start Standalone Spark Master Server**

After completing the configuration of Spark environment, I can start a master server by writing:

```
start-master.sh
```

I can now access the Spark Master's web UI by three different methods: 

1. 127.0.0.1:8080
2. localhost:8080
3. *deviceName*:8080
- **Test Spark Shell**

I managed to know that everything is going fine by entering the following command in order to load the shell: 

```
spark-shell
```

### Connecting Twitter API with my [localhost](http://localhost):

I have run the two python files attached in the submission file after determining the local host and allocating a free port number to connect on. 

After that, I have connected the server master with the local host: After searching for the exact port, it connected successfully. 

After accepting the connection from the slave (local host), it start streaming the tweets from Twitter API for the keyword["Piano"].

# For part 3:

I have implemented my own sentiment analysis with the help of Google links and it is explained in details as follow: 

### The used Architecture:

The architecture of the binary classifier followed thispattern:

1)Conv1D:64filters each of size3with RELU Activation function and input shape of(N x500)and padding was applied to preserve the dimensions.

2)Conv1D:128filters each of size5with RELU Activation function and padding was applied to preserve the dimensions.

3)Conv1D:128filters each of size5with RELU Activation function and padding was applied to preserve the dimensions.

4)Max pooling 1D: with size2and padding was applied to preserve the dimensions.

5)Conv1D:128filters each of size5with RELU Activation function and padding was applied to preserve the dimensions.

6)Max pooling 1D: with size2and padding was applied to preserve the dimensions.

7)Flattening layer

8)Fully connected layer:64nodes with RELU activation function and L2 regularization =1e−29) 9)Fully connected layer:64nodes with RELU activation function and L2 regularization=1e−210)

10) Fully connected layer:2nodes with SoftMax activation function andL2regularization =1e−2

### Used Data set:

My training  and  validation  testing  set  is  originally  open-source  of 1.6M tweets from twitter  with  labelled  emotions of  two  classes:  0 for negative and 4 for positive. Due  to shortage of time, I have trained my model with only 20K tweets that is a mix of positive and negative. I have divided the 20K into training data and validation data.

