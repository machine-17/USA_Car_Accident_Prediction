# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## **Process**
            This is the first time I work with a dataset that has more than a million observations and about 50 features. This one, in particular, has about
            3.5 million observations for the whole country and it's kept up to date in Kaggle. Moreover, It was very challenging working on this dataset 
            and engineering new features. Some models got froze up my kernel and had to run all again before modifying hyperparameters and fine-tuning.
            I am really glad that I got to work with a dataset like this. I learned so much about python and how to handle machine learning.
            
            ### Exploratory Data Analysis
            Before I even started fitting models. I spent a few days on just feature engineering. I created the following:
            - Duration of accident
            - Distance in feet
            - Length of description
            - Kind of street
            - Calendar information

            The hardest one from above was the 'kind of street' feature or type of road. I created a for loop that lasted roughly 6 hours and 30 minutes. 
            The loop went through every row in a column named 'street' and if it finds the value then add 'interstate', 'avenue', 'bridge', and so on. 
            I tried my best to make it run fast with multiprocessing but couldn't get it to work; so, I just left it running over the weekend.

            Also, I split X, y as follows:
            - Train: Feb 2016 through Dec 2018
            - Validation: 2019
            - Test: Jan through Jun of 2020

            All the score values will be based on the test set.

            ### Machine Learning
            I chose the following models for my dataset.
            - Category = Ordinal
            - Tuning = RandomizedSearchCV
            - CatBoostClassifier
            - RandomForestClassifier
            - LogisticRegression

            ### Evaluation
            I also tried other models like Perceptron, QuadraticDiscriminantAnalysis, GaussianProcessClassifier. But these didn't work as expected.
            Anyway, below is a horizontal bar plot that shows the performances of the models. CatBoostClassifier worked well on my dataset.
            Even with multiclass classification. LogisticRegression didn't perform as expected. I had hope for this model because I kept modifying
            the hyperparameters and no luck.

            Another note for this plot below. I wish I had a computer with 128 logical cores to run high level hyperparameters with RandomizedSearchCV
            or even infinite numbers of it. It's very scary to run this model for amateurs. I am one. I had to set minimum parameters to run it well then
            work my way up. By the way, I built my PC which has 12 logical cores and it's overclocked. It's still not enough to run RandomizedSearchCV
            with multiclass classification well.

            """
        ), html.Img(src='assets/Models Scores Performances.png', className='img-fluid'),

        dcc.Markdown(
            """

            Below is a cross validation performance plot for the 3 models used in my notebook. Again, CatBoostClassifier shines in out of sample
            accuracy. It beats the rest in the competition. Also, all models were tested with 5 k folds. Doing any more than that, I wouldn't never
            finish this app. Combining catboost with cross validation is a lot of work.

            """
        ), html.Img(src='assets/Models Cross Validation Scores Performances_.png', className='img-fluid'),

        dcc.Markdown(
            """

            Now, onto the confusion matrices for the models used. And, again CatBoostClassifier performed the best here. It predicted a higher 
            true positive rate for impactful and true negative rate for significant impact. These are the two classes with more observation than the rest.
            So, I was happy to see this result with catboost. For some reason, I believe LogisticRegression doesn't work well with multi classes.
            No matter what I threw at it, it didn't get better. At least we can use it for comparison.

            """
        ), html.Img(src='assets/Confusion Matrix from Cat-Log-For.png', className='img-fluid'),

        dcc.Markdown(
            """

            Lastly, we come to the finish line and the hardest plot to code for me. This multi-class shap summary plot gives me a good visualization
            of the top 10 factors to the prediction outcome. In my opinion, it does a greater job than simply doing a feature importances plot. We can
            see how each class affects the features in great detail.

            """
        ), html.Img(src='assets/SHAP Summary Plot from CatBoost.png', className='img-fluid'),

        
        dcc.Markdown(
            """

            If you never work with CatBoostClassifier and with multi classes, I suggest you do!

            Thanks for reading!

            """
        ),
    ],
)

layout = dbc.Row([column1])