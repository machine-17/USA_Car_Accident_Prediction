# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            ## **Will a car accident cause an impact on traffic flow?**

            Most of the accidents are impactful to the traffic flow whereas accidents with significant impact come with a long delay to your day. 
            This app will help you predict if a car accident causes delays on traffic from least impactful to significant. 
            If the prediction results in a significant impact value. Prepare to wait and be late!

            Explore the model below and see what predictions you get given the feature values. There are 10 features in this app that are the most useful
            for the prediction. The dataset comes with 49 features or in other words columns originally.

            Additional facts:

            In the United States, there have been about 3.5 million accidents from Feb 2016 through June 2020. From April through June of 2020, during
            the coronavirus crisis, there were 260,000 accidents. However, in the same period for 2019, there were 700,000 accidents.

            Citation:

            Moosavi, Sobhan, Mohammad Hossein Samavatian, Srinivasan Parthasarathy, and Rajiv Ramnath. 
            “A Countrywide Traffic Accident Dataset.”, arXiv preprint arXiv:1906.05409 (2019).

            """
        ),
        dcc.Link(dbc.Button('Get Car Accidents Prediction', color='primary'), href='/predictions')
    ],
    md=4,
)

# gapminder = px.data.gapminder()
# fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
#            hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
        html.Img(src='assets/nyc traffic.jpg', className='img-fluid')
    ]
)

layout = dbc.Row([column1, column2])