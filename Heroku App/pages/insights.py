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
            
            ## **Insights**
            
            - Accidents happen all the time around the United States. Even during the coronavirus crisis.
            - There is so many variables from a car accident. Such as, did it happened at a traffic light or at night?
            - Sadly, this app doesn't predict whether a person is attentive or not. But, we do predict the severity of car accidents on traffic.

            The distribution graph below illustrates how almost similar car accidents still are. We see a dip for 2020 when lockdown started then started 
            to surge when restrictions were eased. And, most accidents happen, you guessed it, during peak hours. But, we have a few outliers not in the
            peak hours.

            """
        ), html.Img(src='assets/SNS Displot for Hour of Day.png', className='img-fluid'),

        dcc.Markdown(
            """
            
            Let me show you another distribution graph below. This one explains the accidents by temperature. So far, 2020 is leading in car accidents 
            for this category only.

            """
        ), html.Img(src='assets/SNS Displot for Temperature.png', className='img-fluid'),
        
        dcc.Markdown(
            """
            
            The following graph is called partial dependence plot. It clearly explains the importance for the hour of day feature and by the different classes.
            Those classes are:
            - Least Impact
            - Impactful
            - More Impactful
            - Significant Impact

            By clearly explain, it means the marginal effect on my machine learning model. Which is called CatBoostClassifier. It also shows the
            effect on the score and predicted outcome. Also, the dark line in the plot represents the average of the models predicted outcome. The blue
            area range around the line shows an important effect on the relationship with the model's performance.

            """
        ), html.Img(src='assets/PDP Isolation Hour of Day from CatBoost.png', className='img-fluid'),

                dcc.Markdown(
            """
            
            Here's another partial dependence plot and it explains the relationship with my model for traffic light. This plot is not as great as
            above but it still shows strong significance to the prediction outcome. 

            """
        ), html.Img(src='assets/PDP Isolation Traffic Signal from CatBoost.png', className='img-fluid'),

            dcc.Markdown(
            """

            ### **Closing**
            - Car accidents are going to happen no matter what until full self-driving cars are a thing.
            - Most car accidents are impactful to traffic flow which then increases your time to get from point A to point B.
            - Even selecting or predicting the side of the street where the car accident happened, will predict the delay.

            Drive safe!

            """
        ),

    ],
)

layout = dbc.Row([column1])