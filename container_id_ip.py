#!/usr/bin/python3
import dash
import dash_core_components as dcc
import dash_html_components as html
import subprocess
app = dash.Dash()
colors = {
        'background': '#111111',
        'text': '#7FDBFF'
}

# id of running container
id_con = subprocess.getoutput("sudo docker ps -q")
y = str(id_con)
z = y.split('\n')


# ip of running container
ip_con = subprocess.getoutput("sudo docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(sudo docker ps -q)")
a = str(ip_con)
b = a.split('\n')



app.layout = html.Div(children=[
    html.H1(children='running containers',
    style={
        'textAlign':'center',
        'color': colors['text']
        }
    ),
    dcc.Graph(
        id='docker',
        figure={
            'data':[
                {'x': (z), 'y': (b), 'type': 'Scatter Plot'},
               

            ],
            'layout': {
                'title': 'Dash Data Visualization',
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                    }
                
            }
         }
    )
])

if __name__ == '__main__' :
    app.run_server(debug=True)
                
                    
                    
                    
