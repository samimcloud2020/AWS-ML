##############################What’s the difference between labeled and unlabeled data?###############

Before we dive into the question at hand, let's first start off by defining labeled data and unlabeled data.

So, labeled vs unlabeled data — what's the difference?

Labeled data contains meaningful tags and is used in supervised learning, while unlabeled data doesn’t contain additional information and 
is used in unsupervised learning.

Labeled data requires the additional process of labeling, while unlabeled data is essentially raw data before labeling.

Labeled data is harder to obtain (there are less datasets available, or you have to label it yourself), whereas unlabeled data is more abundant.
Now, let's dive into the details.

#####################################Labeled data################################################
With the help of human annotators, labeled data enhances a set of unlabeled data with meaningful tags, labels, or classes. 
Once a labeled dataset is created, a machine learning model can be fed this labeled dataset so that when it encounters new unlabeled data,
it can accurately predict and assign an appropriate label to that data.

Labeled data is used in supervised machine learning — a machine learning approach in which labeled datasets are used to train or "supervise" 
a machine learning algorithm in categorizing data or making accurate predictions (the model can measure its accuracy and learn over time by
using labeled inputs and outputs).

It’s harder to obtain and store (can be time consuming and costly).

It can be used to identify actionable insights, such as predictions.

################################Supervised learning can further be broken down into two subsets:##################################

Classification: Using algorithms to correctly assign test data to specific categories, such as separating junk mail from your inbox.

Regression: Using algorithms to understand the relationship between dependent and independent variables and forecasting numbers based
on different data points, such as sales revenue projections.

##############################################Unlabeled data#######################################################################
Unlabeled data on the other hand, doesn't have any meaningful tags or labels and usually consists of natural or human-created samples 
such as photos, audio recordings, videos, news articles, tweets, or x-rays that can be easily obtained.

Computers use labeled and unlabeled data to train machine learning models, but what's the difference?

Unlabeled data is used in unsupervised machine learning — applies ML algorithms to analyze and cluster unlabeled data sets by
uncovering patterns without the help of humans.

It’s easier to obtain and store.

It doesn't have as many uses (however, unsupervised learning methods can help uncover new data clusters for additional categories).
Unsupervised learning models are used for three main tasks:

Clustering: Grouping unlabelled data based on similarities or differences, as seen in market segmentation, image compression, etc.

Association: Using different rules to find relationships between variables in a dataset, as used in market basket analysis 
and product recommendations.

Dimensionality reduction: Applied when the number of features (or dimensions) in a dataset is too high in the preprocessing
data stage, such as improving image quality by removing noise.
###############################################################################################################################
