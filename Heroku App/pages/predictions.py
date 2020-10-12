# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load
import pandas as pd

# Imports from this application
from app import app

pipeline = load('assets/CatBoost.joblib')

@app.callback(Output('prediction-content', 'children'),
             [Input('Weekend', 'value'),
              Input('Hour_of_Day', 'value'),
              Input('Side', 'value'),
              Input('Street_Kind', 'value'),
              Input('Crossing', 'value'),
              Input('Stop', 'value'),
              Input('Traffic_Signal', 'value'),
              Input('Sunrise_Sunset', 'value'),
              Input('Distance_Feet', 'value'),
              Input('Description_Length', 'value')
              ])
def predict(Weekend, Hour_of_Day, Side, Street_Kind, Crossing, Stop, Traffic_Signal, Sunrise_Sunset, Distance_Feet, Description_Length):
    df = pd.DataFrame(
        columns=['Weekend', 'Hour_of_Day', 'Side', 'Street_Kind', 'Crossing', 'Stop', 'Traffic_Signal', 'Sunrise_Sunset', 'Distance_Feet', 'Description_Length'],
        data = [[Weekend, Hour_of_Day, Side, Street_Kind, Crossing, Stop, Traffic_Signal, Sunrise_Sunset, Distance_Feet, Description_Length]]
    )

    y_pred = pipeline.predict(df)[0]
    return f'Prediction ---> {", ".join(y_pred)} on traffic'

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        html.Img(src='assets/car crash.jpg', className='img-fluid'),

        dcc.Markdown(
            """
        
            ## **Make Predictions**

            Tune the variables on the right and find out if the given features result in a significant impact or least impactful to the traffic.
            
            If you get 'Least Impact', that's pretty lucky. Send me an email if you do.

            """
        ),
                dcc.Markdown(
            """

            Below is the prediction:

            """
        ),
        # html.H2('Predicted Car Accident Traffic Impact', className='mb-5'), 
        html.Div(id='prediction-content', className='lead')
    ],
    md=4,
)

column2 = dbc.Col(
    [
        dcc.Markdown('#### **Accident Description Length**'), 
        dcc.Slider(
            id='Description_Length', 
            min=14, 
            max=312, 
            step=12, 
            value=44, 
            marks={n: str(n) for n in range(14,312,30)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### **Accident Hour of Day**'), 
        dcc.Slider(
            id='Hour_of_Day', 
            min=0, 
            max=23, 
            step=1, 
            value=12, 
            marks={n: str(n) for n in range(0,23,1)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### **Traffic Impact Distance(F)**'), 
        dcc.Slider(
            id='Distance_Feet', 
            min=0, 
            max=1761566, 
            step=88078, 
            value=0, 
            marks={n: str(n) for n in range(0,1761566,250000)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### **Day or Night**'), 
        dcc.Dropdown(
            id='Sunrise_Sunset', 
            options = [
                {'label': 'Day', 'value': 'Day'}, 
                {'label': 'Night', 'value': 'Night'}, 
            ], 
            value = 'Day', 
            className='mb-5', 
        ),
        dcc.Markdown('#### **Traffic Light**'), 
        dcc.Dropdown(
            id='Traffic_Signal', 
            options = [
                {'label': 'No Traffic Light', 'value': '0'}, 
                {'label': 'Traffic Light', 'value': '1'}, 
            ], 
            value = '1', 
            className='mb-5', 
        ),
        dcc.Markdown('#### **Stop Sign**'), 
        dcc.Dropdown(
            id='Stop', 
            options = [
                {'label': 'No Stop Sign', 'value': '0'}, 
                {'label': 'Stop Sign Present', 'value': '1'}, 
            ], 
            value = '1', 
            className='mb-5', 
        ),
        dcc.Markdown('#### **Crossing**'), 
        dcc.Dropdown(
            id='Crossing', 
            options = [
                {'label': 'No Crossing', 'value': '0'}, 
                {'label': 'Crossing', 'value': '1'}, 
            ], 
            value = '1', 
            className='mb-5', 
        ),
        dcc.Markdown('#### **Side of Street**'), 
        dcc.Dropdown(
            id='Side', 
            options = [
                {'label': 'Right', 'value': 'R'}, 
                {'label': 'Left', 'value': 'L'}, 
            ], 
            value = 'R', 
            className='mb-5', 
        ),
        dcc.Markdown('#### **Weekend(y/n)**'), 
        dcc.Dropdown(
            id='Weekend', 
            options = [
                {'label': 'Not Weekend', 'value': '0'}, 
                {'label': 'Weekend', 'value': '1'}, 
            ], 
            value = '0', 
            className='mb-5', 
        ),
        dcc.Markdown('#### **Road Type**'), 
        dcc.Dropdown(
            id='Street_Kind', 
            options = [
                {'label': 'Interstate', 'value': 'Interstate'}, 
                {'label': 'Road', 'value': 'Road'}, 
                {'label': 'Highway', 'value': 'Highway'}, 
                {'label': 'Street', 'value': 'Street'}, 
                {'label': 'Avenue', 'value': 'Avenue'},
                {'label': 'Freeway', 'value': 'Freeway'},
                {'label': 'Boulevard', 'value': 'Boulevard'},
                {'label': 'Expressway', 'value': 'Expressway'},
                {'label': 'Lane', 'value': 'Lane'},
                {'label': 'Turnpike', 'value': 'Turnpike'}, 
                {'label': 'Pike', 'value': 'Pike'},
                {'label': 'State Highway', 'value': 'State Highway'},
                {'label': 'Toll', 'value': 'Toll'},
                {'label': 'Trail', 'value': 'Trail'},
                {'label': 'Bridge', 'value': 'Bridge'},
                {'label': 'Throughway', 'value': 'Throughway'}, 
            ], 
            value = 'Avenue', 
            className='mb-5', 
        ), 
    ],
)

layout = dbc.Row([column1, column2])