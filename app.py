from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import dash
import pandas as pd
import os

# Estilo de la tarjeta
tab_style = {
    'idle':{
        'borderRadius': '10px',
        'padding': '10px 20px',
        'marginInline': '15px',
        'display':'flex',
        'alignItems':'center',
        'justifyContent':'center',
        'fontWeight': 'white',
        'backgroundColor': '#E52421',
        'border':'none',
        "fontSize": "18px",
        "borderRadius": "5px",
        'fontFamily': 'Museo Sans'
    },
    'active':{
        'borderRadius': '12px',
        'padding': '10px 20px',
        'marginInline': '15px',
        'display':'flex',
        'alignItems':'center',
        'justifyContent':'center',
        'fontWeight': 'bold',
        'border':'none',
        "fontSize": "18px",
        "borderRadius": "5px",
        'textDecoration': 'underline',
        'backgroundColor': '#E52421',
        'fontFamily': 'Museo Sans'
    }
}
# Ruta para la carpeta de imágenes
static_folder = os.path.join(os.path.dirname(__file__), "assets")

# Configurar la aplicación Dash con la carpeta de assets personalizada
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
    title='Asamblea Deliberativa 2024',
    assets_folder=static_folder  # Configurar carpeta de assets
)

server = app.server

app.layout = html.Div([
    dbc.Container([

        # Título y texto entre las Tabs y los gráficos
        dbc.Row([
            dbc.Col(html.H1("META ASAMBLEA CIUDADANA DELIBERATIVA",
                            style={'textAlign': 'center',
                                   'fontSize': '40px',
                                   'fontWeight': 'bold',
                                   'fontFamily': 'Kensington'}),
                    width=12),
        ], justify='center', style={'marginTop': '30px'}),

        dbc.Row([
            dbc.Col(html.H3("Bogotá 2024",
                            style={'textAlign': 'center',
                                   'fontSize': '30px',
                                   'fontFamily': 'Kensington'}),
                    width=12),
        ], justify='center', style={'marginTop': '10px'}),

        dbc.Col(
            html.P([
                "Con el apoyo de:"], style={
                'fontSize': '18px',
                'maxWidth': '800px',
                'marginLeft': 'auto',
                'marginRight': 'auto',
                'textAlign': 'center',
                'fontFamily': 'Museo Sans'
            }),
            width=12
        ),

        # Fila para el logo y las Tabs
        dbc.Row([
            # Logo centrado en una fila
            dbc.Col(html.Img(src="/assets/Logo_mtp.png", width=1050, height=100), width=12, style={'display': 'flex', 'justifyContent': 'center', 'marginBottom': '30px'}),


        dbc.Row([
            dbc.Col(
                html.P([
                    "Desde la Secretaría de Planeación de la ciudad de Bogotá, en alianza con la Fundación Corona y el Extituto de Política Abierta, este 2024 se lanzó la Meta Asamblea ",
                    html.B("#SumemosVoces"), ".",
                    html.Br(), html.Br(),
                    "Se realizó del 18 al 21 de octubre en el Edificio Atrio en el centro de Bogotá. Allí, y a 25 pisos de altura, ",
                    html.B("60 asambleístas elegidos por sorteo"), " siguiendo criterios diferenciales y poblacionales, se dieron cita para aprender, deliberar y construir consensos sobre las reglas que guiarán las futuras Asambleas Ciudadanas Deliberativas.",
                    html.Br(), html.Br(),
                    "Los resultados de las diferentes actividades y encuestas realizadas durante la Meta Asamblea, que se pueden explorar en este ",
                    html.B("tablero digital"), ", son un insumo para seguir sumando voces en este proceso innovador.",
                    html.Br(), html.Br(),
                    html.B("El Tablero digital"), " es una herramienta en línea que te permite ver y entender la información recogida durante los 4 días de actividades. En este espacio encontrarás lo siguiente:"
                ], style={
                    'fontSize': '18px',
                    'maxWidth': '800px',
                    'marginLeft': 'auto',
                    'marginRight': 'auto',
                    'fontFamily': 'Museo Sans'
                }),
                width=12
            ),
            dbc.Col(
                html.P([
                    "- ", html.B("Encuestas"), ": resultados de las preguntas que se hicieron a los participantes durante las actividades.",
                    html.Br(),
                    "- ", html.B("Análisis de sentimientos"), ": muestra lo que sintieron los participantes durante una actividad específica y nos ayuda a entender cómo reaccionaron cuando se habló de temas públicos.",
                    html.Br(),
                    "- ", html.B("Análisis de centralidad"), ": resultados obtenidos al revisar las grabaciones de las discusiones en dos grupos de trabajo.",
                    html.Br(),
                    "- ", html.B("Observaciones"), ": comentarios y notas adicionales que hizo el equipo encargado de analizar las actividades.",
                    html.Br(),
                    "- ", html.B("Productos"), ": resultados de actividades especiales como la \"Casa de la Confianza\" y el \"Termómetro de la Deliberación\"."
                ], style={
                    'fontSize': '18px',
                    'fontFamily': 'Museo Sans',
                    'maxWidth': '800px',
                    'marginLeft': 'auto',
                    'marginRight': 'auto'
                }),
                width=12
            ),
            dbc.Col(
                html.P(
                    "Este tablero te ayudará a encontrar y entender toda esta información de forma fácil y ordenada.",
                    style={
                        'fontSize': '18px',
                        'fontFamily': 'Museo Sans',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto'
                    }
                ),
                width=12
            )
        ], justify='center', style={'marginTop': '20px'}),

        # Tabs centrados en una fila
        dbc.Col(
            dcc.Tabs(id='graph-tabs', value='ALL', children=[
                dcc.Tab(label='Encuestas', value='Encuestas', style={**tab_style['idle'], 'color': 'white'},
                        selected_style={**tab_style['active'], 'color': 'white'}),

                dcc.Tab(label='Observaciones', value='Observaciones', style={**tab_style['idle'], 'color': 'white'},
                        selected_style={**tab_style['active'], 'color': 'white'}),

                dcc.Tab(label='Análisis de centralidad', value='Debate', style={**tab_style['idle'], 'color': 'white'},
                        selected_style={**tab_style['active'], 'color': 'white'}),

                dcc.Tab(label='Sentimientos', value='Sentimientos', style={**tab_style['idle'], 'color': 'white'},
                        selected_style={**tab_style['active'], 'color': 'white'}),

                dcc.Tab(label='Productos de las actividades', value='Productos', style={**tab_style['idle'], 'color': 'white'},
                        selected_style={**tab_style['active'], 'color': 'white'}),

            ], style={'marginTop': '15px', 'height': '50px', 'width': '100%'})
            , width=68, style={'display': 'flex', 'justifyContent': 'center'}),  # Centrado de los tabs
    ]),

        html.Br(),

        # Fila para el contenido de los gráficos
        dbc.Row([
            dcc.Loading([
                html.Div(id='tabs-content')
            ], type='default', color='#2956A4', style={'width': '100%'})  # El ancho ahora es 100%
        ], justify='center'),  # Asegura que los gráficos se centren en la fila

        html.Br(),

        dbc.Row([
            dbc.Col(
                html.P(
                    "Acá unos recuerdos para que siempre acompañen tu recorrido:",
                    style={
                        'fontSize': '18px',
                        'fontFamily': 'Museo Sans',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto'
                    }
                ),
                width=12
            ),
        ], justify='center', style={'marginTop': '10px'}),

        # Carrusel de imágenes
        dbc.Row([
            dbc.Col(
                dbc.Carousel(
                    items=[
                        {"key": str(i), "src": f"/assets/Image_{i}.JPG"} for i in range(1, 13)
                    ],
                    controls=True,
                    indicators=True,
                    interval=3000,
                    ride="carousel",
                ), width=12, style={"width": "60%", "margin": "0 auto"}
            )
        ], justify='center'),

        html.Br(),
        html.Br(),

        # Div contenedor para centrar los botones
        html.Div(
            children=[
                html.Button(
                    "Descargar Encuestas",
                    id="btn_file1",
                    style={
                        "backgroundColor": "#e9202e",
                        "color": "white",
                        "padding": "10px 20px",
                        "fontSize": "18px",
                        "border": "none",
                        "borderRadius": "5px",
                        "cursor": "pointer",
                        "boxShadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
                        'fontFamily': 'Museo Sans'
                    },
                ),
                html.Button(
                    "Descargar Observaciones",
                    id="btn_file2",
                    style={
                        "backgroundColor": "#f8cd03",
                        "color": "white",
                        "padding": "10px 20px",
                        "fontSize": "18px",
                        "border": "none",
                        "borderRadius": "5px",
                        "cursor": "pointer",
                        "boxShadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
                        'fontFamily': 'Museo Sans'
                    },
                ),
                html.Button(
                    "Descargar Transcripciones",
                    id="btn_file3",
                    style={
                        "backgroundColor": "#ff6709",
                        "color": "white",
                        "padding": "10px 20px",
                        "fontSize": "18px",
                        "border": "none",
                        "borderRadius": "5px",
                        "cursor": "pointer",
                        "boxShadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
                        'fontFamily': 'Museo Sans'
                    },
                ),
                html.Button(
                    "Descargar Analisis Sentimientos",
                    id="btn_file4",
                    style={
                        "backgroundColor": "#c08217",
                        "color": "white",
                        "padding": "10px 20px",
                        "fontSize": "18px",
                        "border": "none",
                        "borderRadius": "5px",
                        "cursor": "pointer",
                        "boxShadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
                        'fontFamily': 'Museo Sans'
                    },
                ),
                html.Button(
                    "Descargar Productos Actividades",
                    id="btn_file5",
                    style={
                        "backgroundColor": "#ff746c",
                        "color": "white",
                        "padding": "10px 20px",
                        "fontSize": "18px",
                        "border": "none",
                        "borderRadius": "5px",
                        "cursor": "pointer",
                        "boxShadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
                        'fontFamily': 'Museo Sans'
                    },
                ),
                dcc.Download(id="download-file1"),
                dcc.Download(id="download-file2"),
                dcc.Download(id="download-file3"),
                dcc.Download(id="download-file4"),
                dcc.Download(id="download-file5"),
            ],
            style={
                "display": "flex",         # Utiliza flexbox
                #"flexDirection": "column", # Alineación vertical
                "alignItems": "center",    # Centra los botones horizontalmente
                "justifyContent": "center", # Centra los botones verticalmente si es necesario
                #"height": "100vh",         # Establece altura completa de la ventana
                "textAlign": "center",     # Alinea el texto
            }
        ),


    ], style={'padding': '0px', 'maxWidth': '100%'})  # Asegura que el contenedor ocupe el 100% del ancho
], style={'backgroundColor': 'white', 'minHeight': '100vh'})

# Callback para el primer archivo
@app.callback(
    Output("download-file1", "data"),
    Input("btn_file1", "n_clicks"),
    prevent_initial_call=True,
)
def download_file1(n_clicks):
    return dcc.send_file("./Encuestas.xlsx")

# Callback para el segundo archivo
@app.callback(
    Output("download-file3", "data"),
    Input("btn_file3", "n_clicks"),
    prevent_initial_call=True,
)
def download_file3(n_clicks):
    return dcc.send_file("./consolidated_transcription.txt")

@app.callback(
    Output("download-file2", "data"),
    Input("btn_file2", "n_clicks"),
    prevent_initial_call=True,
)
def download_file2(n_clicks):
    return dcc.send_file("./ResumenObserva.xlsx")

@app.callback(
    Output("download-file4", "data"),
    Input("btn_file4", "n_clicks"),
    prevent_initial_call=True,
)
def download_file4(n_clicks):
    return dcc.send_file("./data_sts.xlsx")

@app.callback(
    Output("download-file5", "data"),
    Input("btn_file5", "n_clicks"),
    prevent_initial_call=True,
)
def download_file5(n_clicks):
    return dcc.send_file("./Productos.xlsx")


@app.callback(
    Output('tabs-content', 'children'),
    [Input('graph-tabs', 'value')]
)

def update_tab(tab):

    if tab == 'Encuestas':

        # Retornar el layout con pestañas internas
        return html.Div([
            html.Br(),
            dbc.Row([
                dbc.Col(html.H3("Encuestas", style={'textAlign': 'center', 'fontSize': '30px', 'fontFamily': 'Kensington'}), width=12),
            ], justify='center', style={'width': '100%', 'display': 'flex', 'justifyContent': 'center'}),

            dbc.Row([
                dbc.Col(
                    html.P([
                        html.B("Les damos la bienvenida a la sección de encuestas"), ". Acá encontrarás los principales resultados que surgieron de las tres encuestas que les realizamos a los asambleístas durante los días de deliberación.",
                        html.Br(), html.Br(),
                        "En estas encuestas les preguntamos sobre temas de ",
                        html.B("confianza"), ", ",
                        html.B("participación"), ", ",
                        html.B("logística"), " y ",
                        html.B("habilidades básicas de la deliberación"), ".",
                        html.Br(), html.Br(),
                        "Buscamos que este apartado logre darte un panorama general de los resultados."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans'
                    }),
                    width=12
                ),
            ], justify='center', style={'width': '100%', 'display': 'flex', 'justifyContent': 'center','marginTop': '20px'}),

            # Pestañas internas
            # Pestañas internas
            dcc.Tabs(
                id='subtabs',
                value='general',  # Valor inicial
                children=[
                    dcc.Tab(label='General', value='general', style={**tab_style['idle'], 'color': 'white'}, selected_style={**tab_style['active'], 'color': 'white'}),
                    dcc.Tab(label='Auto Evaluación', value='autoeval', style={**tab_style['idle'], 'color': 'white'}, selected_style={**tab_style['active'], 'color': 'white'}),
                    dcc.Tab(label='Auto Evaluación por Género', value='autoevalgenero', style={**tab_style['idle'], 'color': 'white'}, selected_style={**tab_style['active'], 'color': 'white'}),
                    dcc.Tab(label='Confianza', value='confianza', style={**tab_style['idle'], 'color': 'white'}, selected_style={**tab_style['active'], 'color': 'white'}),
                    dcc.Tab(label='Logística', value='logistica', style={**tab_style['idle'], 'color': 'white'}, selected_style={**tab_style['active'], 'color': 'white'}),
                    dcc.Tab(label='Participación', value='participacion', style={**tab_style['idle'], 'color': 'white'}, selected_style={**tab_style['active'], 'color': 'white'}),
                ],
                style={
                    'marginTop': '15px',
                    'height': '50px',  # Aumenté la altura para dar espacio a dos líneas
                    'width': '100%'
                }
            ),

        # Contenido de las subpestañas
        html.Div(id='subtabs-content')  # Será actualizado dinámicamente
    ])

    elif tab == 'Productos':

        # Retornar el layout con pestañas internas
        return html.Div([
            html.Br(),
            dbc.Row([
                dbc.Col(html.H3("Productos de las Actividades", style={'textAlign': 'center', 'fontSize': '30px', 'fontFamily': 'Kensington'}), width=12),
            ], justify='center', style={'width': '100%', 'display': 'flex', 'justifyContent': 'center'}),

            dbc.Row([
                dbc.Col(html.P("""
                    Parlita Productos
                """, style={'textAlign': 'center', 'fontSize': '18px', 'maxWidth': '800px', 'marginLeft': 'auto', 'marginRight': 'auto'}), width=12),
            ], justify='center', style={'width': '100%', 'display': 'flex', 'justifyContent': 'center'}),

            # Pestañas internas
            dcc.Tabs(
                id='subtabs',
                value='casa',  # Valor inicial
                children=[
                    dcc.Tab(label='La Casa de la Confianza', value='casa', style={**tab_style['idle'], 'color': 'white'},
                            selected_style={**tab_style['active'], 'color': 'white'}),
                    dcc.Tab(label='Termómetro de la Deliberación', value='termometro', style={**tab_style['idle'], 'color': 'white'},
                            selected_style={**tab_style['active'], 'color': 'white'}),
                ], style={'marginTop': '15px', 'height': '50px', 'width': '100%'}),

        # Contenido de las subpestañas
        html.Div(id='subtabs-content')  # Será actualizado dinámicamente
    ])

    elif tab == 'Observaciones':

        return html.Div([
                html.Br(),

                dbc.Row([
                    dbc.Col(html.H3("Observaciones", style={'textAlign': 'center', 'fontSize': '30px', 'fontFamily': 'Kensington'}), width=12),
                ], justify='center', style={'width': '100%', 'display': 'flex', 'justifyContent': 'center'}),

                dbc.Col(
                    html.P([
                        "Estas fueron ", html.B("observaciones"), " registradas por el equipo de sistematización durante las actividades desarrolladas. El propósito de estas observaciones fue ",
                        html.B("identificar"), " buenas prácticas y áreas de mejora desde un punto de vista externo y neutral, sin un rol activo de participación. ",
                        "Las observaciones permitieron capturar elementos clave de la dinámica de las actividades, evaluando factores como: ",
                        html.Br(),
                        "- ", html.B("La interacción entre participantes"),
                        html.Br(),
                        "- ", html.B("El nivel de compromiso y participación"),
                        html.Br(),
                        "- ", html.B("La claridad de los objetivos y procesos"),
                        html.Br(),
                        "- ", html.B("Aspectos logísticos y organizativos"), ". ",
                        html.Br(),
                        "A continuación, se detalla cada una de estas observaciones, resaltando los logros identificados y las oportunidades de mejora para futuras deliberaciones."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans'
                    }),
                    width=12
                ),


                html.Div([
                    html.H4("", style={'textAlign': 'center'}),  # Título centrado
                    html.Div(
                        html.Iframe(
                            src='/assets/TreemapObservaciones.html',  # Enlace al archivo HTML
                            style={'width': '80%', 'height': '900px', 'border': 'none'}
                        ),
                        style={
                            'display': 'flex',  # Usamos flexbox
                            'justifyContent': 'center',  # Centra el iframe horizontalmente
                            'alignItems': 'center',  # Centra el iframe verticalmente
                            'margin': '20px 0',  # Añadir margen para separación entre elementos
                            'width': '100%',  # Asegura que el contenedor ocupe todo el ancho disponible
                        }
                    ),
                ], style={
                    'display': 'flex',
                    'flexDirection': 'column',
                    'alignItems': 'center',  # Alineación centrada
                    'textAlign': 'center',
                    'maxWidth': '2100px',  # Ancho máximo para evitar que se expandan demasiado en pantallas grandes
                    'margin': '0 auto'  # Centra el contenido horizontalmente
                })
            ])

    elif tab == 'Debate':

        return html.Div([
                html.Br(),
                html.Br(),

                dbc.Col(
                    html.P([
                        "Esta representación visual muestra cómo se desarrolló la discusión durante una hora en una de las comisiones de la ",
                        html.B("Casa"), ". Es un piloto de un ", html.B("análisis"), " de centralidad que realizamos para entender cómo los asambleístas estaban ocupando el tiempo en una actividad determinada y qué temas recibieron mayor atención durante la deliberación.",
                        html.Br(), html.Br(),
                        "Cada elemento del flujo se define por varios aspectos clave:",
                        html.Br(), html.Br(),
                        "- ", html.B("Color"), " del nodo: cada nodo tiene un color que indica la categoría temática o la naturaleza del contenido abordado. Por ejemplo, el rojo representa temas de ", html.B("acciones"), " y planes concretos, mientras que el amarillo y el marrón reflejan otros aspectos como Definición de temas futuro y Seguimiento y evaluación.",
                        html.Br(), html.Br(),
                        "- ", html.B("Nombre"), " y descripción: cada nodo identifica el tema central y su propósito dentro del debate. Ejemplos de temas tratados son: ", html.B("Acciones"), ": definir acciones específicas a seguir.",
                        html.Br(), html.Br(),
                        "- ", html.B("Divulgación"), " de resultados: compartir los resultados de la deliberación con todos los participantes.",
                        html.Br(), html.Br(),
                        "- ", html.B("Tiempo"), " asignado: cada nodo muestra el tiempo dedicado a discutir el tema, considerando su complejidad y prioridad. Por ejemplo: Divulgación de resultados (14 min).",
                        html.Br(), html.Br(),
                        "- ", html.B("Relación"), " entre nodos: las líneas conectan los nodos, mostrando cómo una discusión llevó a otra y evidenciando el flujo lógico e interdependencia entre los temas.",
                        html.Br(), html.Br(),
                        "- ", html.B("Tamaño"), " del nodo y de la red: el tamaño indica la importancia relativa del tema y la cantidad de actores involucrados en su desarrollo."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans'
                    }),
                    width=12
                ),

                dbc.Row([
                    dbc.Col(html.H3("Centralidad del Debate 1", style={'textAlign': 'center', 'fontSize': '30px', 'fontFamily': 'Kensington'}), width=12),
                ], justify='center', style={'width': '100%', 'display': 'flex', 'justifyContent': 'center'}),

                html.Div([
                    html.H4("", style={'textAlign': 'center'}),  # Título centrado
                    html.Div(
                        html.Iframe(
                            src='/assets/flujo_de_temas.html',  # Enlace al archivo HTML
                            style={'width': '80%', 'height': '900px', 'border': 'none'}
                        ),
                        style={
                            'display': 'flex',  # Usamos flexbox
                            'justifyContent': 'center',  # Centra el iframe horizontalmente
                            'alignItems': 'center',  # Centra el iframe verticalmente
                            'margin': '20px 0',  # Añadir margen para separación entre elementos
                            'width': '100%',  # Asegura que el contenedor ocupe todo el ancho disponible
                        }
                    ),
                ], style={
                    'display': 'flex',
                    'flexDirection': 'column',
                    'alignItems': 'center',  # Alineación centrada
                    #'textAlign': 'center',
                    'maxWidth': '2100px',  # Ancho máximo para evitar que se expandan demasiado en pantallas grandes
                    'margin': '0 auto'  # Centra el contenido horizontalmente
                }),

                html.Br(),

                dbc.Row([
                    dbc.Col(html.H3("Centralidad del Debate 2", style={'textAlign': 'center', 'fontSize': '30px', 'fontFamily': 'Kensington'}), width=12),
                ], justify='center', style={'width': '100%', 'display': 'flex', 'justifyContent': 'center'}),

                html.Div([
                    html.H4("", style={'textAlign': 'center'}),  # Título centrado
                    html.Div(
                        html.Iframe(
                            src='/assets/flujo_de_temas2.html',  # Enlace al archivo HTML
                            style={'width': '80%', 'height': '900px', 'border': 'none'}
                        ),
                        style={
                            'display': 'flex',  # Usamos flexbox
                            'justifyContent': 'center',  # Centra el iframe horizontalmente
                            'alignItems': 'center',  # Centra el iframe verticalmente
                            'margin': '30px 0',  # Añadir margen para separación entre elementos
                            'width': '100%',  # Asegura que el contenedor ocupe todo el ancho disponible
                        }
                    ),
                ], style={
                    'display': 'flex',
                    'flexDirection': 'column',
                    'alignItems': 'center',  # Alineación centrada
                    'textAlign': 'center',
                    'maxWidth': '2100px',  # Ancho máximo para evitar que se expandan demasiado en pantallas grandes
                    'margin': '0 auto'  # Centra el contenido horizontalmente
                })
            ])

    elif tab == 'Sentimientos':

        return html.Div([
                html.Br(),

                dbc.Row([
                    dbc.Col(html.H3("Sentimientos", style={'textAlign': 'center', 'fontSize': '30px', 'fontFamily': 'Kensington'}), width=12),
                ], justify='center', style={'width': '100%', 'display': 'flex', 'justifyContent': 'center'}),

                dbc.Col(
                    html.P([
                        "Esta gráfica muestra el balance de los sentimientos percibidos por los asambleístas cuando se abordaron temas relacionados con lo público. Utilizando el método Ruler, los sentimientos se categorizaron en cuatro colores: ",
                        html.Span("Amarillo", style={"backgroundColor": "yellow", "color": "black", "fontWeight": "bold"}), ": Sentimientos positivos con mucha energía. ",
                        html.Span("Verde", style={"backgroundColor": "green", "color": "white", "fontWeight": "bold"}), ": Sentimientos positivos con baja energía. ",
                        html.Span("Rojo", style={"backgroundColor": "red", "color": "white", "fontWeight": "bold"}), ": Sentimientos negativos con alta energía. ",
                        html.Span("Azul", style={"backgroundColor": "blue", "color": "white", "fontWeight": "bold"}), ": Sentimientos negativos con baja energía.",
                        " Esta visualización permite identificar y comprender mejor las emociones predominantes en los asambleístas durante la actividad."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans'
                    }),
                    width=12
                ),

                html.Div([
                    html.H4("", style={'textAlign': 'center'}),  # Título centrado
                    html.Div(
                        html.Iframe(
                            src='/assets/sentimientos.html',  # Enlace al archivo HTML
                            style={'width': '80%', 'height': '900px', 'border': 'none'}
                        ),
                        style={
                            'display': 'flex',  # Usamos flexbox
                            'justifyContent': 'center',  # Centra el iframe horizontalmente
                            'alignItems': 'center',  # Centra el iframe verticalmente
                            'margin': '20px 0',  # Añadir margen para separación entre elementos
                            'width': '100%',  # Asegura que el contenedor ocupe todo el ancho disponible
                        }
                    ),
                ], style={
                    'display': 'flex',
                    'flexDirection': 'column',
                    'alignItems': 'center',  # Alineación centrada
                    #'textAlign': 'center',
                    'maxWidth': '2100px',  # Ancho máximo para evitar que se expandan demasiado en pantallas grandes
                    'margin': '0 auto'  # Centra el contenido horizontalmente
                })
            ])

@app.callback(
    Output('subtabs-content', 'children'),
    Input('subtabs', 'value')
)
def update_subtabs(selected_subtab):

    if selected_subtab == "general":

        return html.Div([
            dbc.Col(
                html.P([
                    html.Br(), html.Br(),
                    "Esta sección presenta una visión general de todas las habilidades evaluadas en los participantes antes y después de las actividades. A través de un análisis comparativo, se puede identificar cómo cambiaron las percepciones y habilidades en distintos ámbitos. La visualización permite tener un panorama completo del progreso general logrado durante el proceso.",
                    html.Br(), html.Br(),
                    "Esta gráfica de radar compara la percepción de los asambleístas en distintos aspectos antes ",
                    html.Span("línea roja", style={"backgroundColor": "red", "color": "black", "fontWeight": "bold"}),
                    " y después ", html.Span("línea amarilla", style={"backgroundColor": "yellow", "color": "black", "fontWeight": "bold"}),
                    " de las actividades. Se midieron ocho dimensiones: (",
                    html.Span("autoevaluación, ", style={"fontWeight": "bold"}),
                    html.Span("confianza en la Alcaldía, ", style={"fontWeight": "bold"}),
                    html.Span("confianza en el proceso, ", style={"fontWeight": "bold"}),
                    html.Span("confianza en la participación, ", style={"fontWeight": "bold"}),
                    html.Span("confianza en el público, ", style={"fontWeight": "bold"}),
                    html.Span("participación en la asamblea, ", style={"fontWeight": "bold"}),
                    html.Span("participación en la ciudad, ", style={"fontWeight": "bold"}),
                    " y ", html.Span("participación en decisiones", style={"fontWeight": "bold"}), ".",
                    html.Br(), html.Br(),
                    "Se observa una mejora general en la mayoría de las dimensiones. Las áreas con mayores incrementos son ",
                    html.Span("autoevaluación", style={"fontWeight": "bold"}),
                    ", ", html.Span("participación en la ciudad", style={"fontWeight": "bold"}),
                    " y ", html.Span("confianza en la Alcaldía", style={"fontWeight": "bold"}), "."
                ], style={
                    'fontSize': '18px',
                    'maxWidth': '800px',
                    'marginLeft': 'auto',
                    'marginRight': 'auto',
                    'fontFamily': 'Museo Sans'
                }),
                width=12
            ),

            html.Div(
                html.Iframe(
                    src='/assets/Radar_total.html',  # Enlace al archivo HTML
                    style={'width': '80%', 'height': '500px', 'border': 'none'}
                ),
                style={
                    'display': 'flex',  # Usamos flexbox
                    'justifyContent': 'center',  # Centra el iframe horizontalmente
                    'alignItems': 'center',  # Centra el iframe verticalmente
                    'margin': '20px 0',  # Añadir margen para separación entre elementos
                    'width': '100%',  # Asegura que el contenedor ocupe todo el ancho disponible
                }
            ),
        ], style={
            'display': 'flex',
            'flexDirection': 'column',
            'alignItems': 'center',  # Alineación centrada
            #'textAlign': 'center',
            'maxWidth': '1200px',  # Ancho máximo para evitar que se expandan demasiado en pantallas grandes
            'margin': '0 auto'  # Centra el contenido horizontalmente
        })

    elif selected_subtab == "autoeval":

        return html.Div([
    # Contenedor para la Visualización 1
    html.Div([
        html.Br(),
        dbc.Col(
            html.P([
                html.Br(),
                "En esta sección se muestra cómo los participantes valoraron sus propias habilidades y competencias tras el proceso deliberativo. La autoevaluación refleja el nivel de confianza que los asambleístas tienen en sí mismos en áreas clave como argumentar, reflexionar, debatir y decidir. Esto permite identificar los cambios en su percepción personal de sus capacidades.",
                html.Br(), html.Br(),
                "Esta gráfica en forma de radar compara las habilidades de los asambleístas ",
                html.Span("antes", style={"fontWeight": "bold"}),
                " ", html.Span("línea roja", style={"backgroundColor": "red", "color": "black", "fontWeight": "bold"}),
                ", y ", html.Span("después", style={"fontWeight": "bold"}),
                " ", html.Span("línea amarilla", style={"backgroundColor": "yellow", "color": "black", "fontWeight": "bold"}),
                ". Se evaluaron siete habilidades: ",
                html.Span("reflexionar", style={"fontWeight": "bold"}),
                ", ", html.Span("argumentar", style={"fontWeight": "bold"}),
                ", ", html.Span("contraargumentar", style={"fontWeight": "bold"}),
                ", ", html.Span("discutir", style={"fontWeight": "bold"}),
                ", ", html.Span("evaluar", style={"fontWeight": "bold"}),
                ", ", html.Span("decidir", style={"fontWeight": "bold"}),
                " y ", html.Span("cambiar de opinión", style={"fontWeight": "bold"}), ".",
                html.Br(), html.Br(),
                "En todas las habilidades se observa una mejora tras la actividad. La mayor diferencia se aprecia en ",
                html.Span("reflexionar", style={"fontWeight": "bold"}),
                " y ", html.Span("argumentar", style={"fontWeight": "bold"}),
                ", donde el puntaje aumenta notablemente en la evaluación posterior."
            ], style={
                'fontSize': '18px',
                'maxWidth': '800px',
                'marginLeft': 'auto',
                'marginRight': 'auto',
                'fontFamily': 'Museo Sans'
            }),
            width=12
        ),
        html.Div(
            html.Iframe(
                src='/assets/Radar_Autoeval.html',  # Enlace al archivo HTML
                style={'width': '80%', 'height': '800px', 'border': 'none'}
            ),
            style={
                'display': 'flex',  # Usamos flexbox
                'justifyContent': 'center',  # Centra el iframe horizontalmente
                'alignItems': 'center',  # Centra el iframe verticalmente
                'margin': '20px 0',  # Añadir margen para separación entre elementos
                'width': '100%',  # Asegura que el contenedor ocupe todo el ancho disponible
            }
        ),
    ], style={
        'display': 'flex',
        'flexDirection': 'column',
        'alignItems': 'center',  # Alineación centrada
        'maxWidth': '1200px',  # Ancho máximo para evitar que se expandan demasiado en pantallas grandes
        'margin': '0 auto'  # Centra el contenido horizontalmente
    }),

    # Repetimos la estructura para cada visualización
    html.Div([
        dbc.Col(
            html.P([
                html.Br(),
                "Esta gráfica muestra cómo cambió la percepción de los asambleístas sobre qué tan hábiles se sienten para reflexionar detenidamente sobre diferentes aspectos de un tema. En el gráfico, cada sección representa un valor en una escala del 1 al 10 (donde 1 es poco y 10 es mucho). El número indica cuántas personas votaron por ese valor, y el porcentaje muestra qué proporción representan. La comparación entre el ",
                html.B("Pre"), " y el ", html.B("Pos"), " revela un cambio positivo.",
                html.Br(), html.Br(),
                "Antes de las actividades, ", html.Span("33.3%", style={'color': 'white', 'backgroundColor': 'red'}), " se sentían muy hábiles para reflexionar (valor 10). Después, esta cifra subió a ",
                html.Span("44.7%", style={'color': 'white', 'backgroundColor': 'red'}), ". También aumentaron las respuestas en valores intermedios, lo que indica una ",
                html.B("mejora"), " general en esta habilidad.",
                html.Br(), html.Br(),
                "Además, si pasas el cursor por encima de cada sección, podrás ver el valor que votaron los asambleístas dentro de la escala."
            ], style={
                'fontSize': '18px',
                'maxWidth': '800px',
                'marginLeft': 'auto',
                'marginRight': 'auto',
                'fontFamily': 'Museo Sans'
            }),
            width=12
        ),
        html.Div(
            html.Iframe(
                src='/assets/AutoEval_0.html',
                style={'width': '80%', 'height': '500px', 'border': 'none'}
            ),
            style={
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center',
                'margin': '20px 0',
                'width': '100%',
            }
        ),
    ], style={
        'display': 'flex',
        'flexDirection': 'column',
        'alignItems': 'center',
        'maxWidth': '1200px',  # Ancho máximo
        'margin': '0 auto'  # Centrado horizontal
    }),

    html.Div([
        dbc.Col(
            html.P([
                "Esta gráfica muestra cómo cambió la percepción de los asambleístas sobre qué tan hábiles se sienten para presentar razones a favor de una opción o postura. En el gráfico, cada sección representa un valor en una escala del 1 al 10 (donde 1 es poco y 10 es mucho). El número indica cuántas personas votaron por ese valor, y el porcentaje muestra qué proporción representan.",
                html.Br(), html.Br(),
                "La comparación entre el ", html.B("Pre"), " y el ", html.B("Pos"), " revela una mejora en esta habilidad. Antes de las actividades, ",
                html.Span("21.4%", style={'color': 'white', 'backgroundColor': 'red'}), " se sentían muy hábiles para argumentar (valor 10). Después, esta cifra subió a ",
                html.Span("28.9%", style={'color': 'white', 'backgroundColor': 'red'}), ". También se observa un aumento en los valores intermedios, como el valor 9, que pasó de ",
                html.Span("28.6%", style={'color': 'white', 'backgroundColor': 'orange'}), " a ",
                html.Span("39.5%", style={'color': 'white', 'backgroundColor': 'orange'}), ".",
                html.Br(), html.Br(),
                "Además, si pasas el cursor por encima de cada sección, podrás ver el valor específico que votaron los asambleístas dentro de la escala."
            ], style={
                'fontSize': '18px',
                'maxWidth': '800px',
                'marginLeft': 'auto',
                'marginRight': 'auto',
                'fontFamily': 'Museo Sans'
            }),
            width=12
        ),
        html.Div(
            html.Iframe(
                src='/assets/AutoEval_1.html',
                style={'width': '80%', 'height': '500px', 'border': 'none'}
            ),
            style={
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center',
                'margin': '20px 0',
                'width': '100%',
            }
        ),
    ], style={
        'display': 'flex',
        'flexDirection': 'column',
        'alignItems': 'center',
        'maxWidth': '1200px',  # Ancho máximo
        'margin': '0 auto'  # Centrado horizontal
    }),

    html.Div([
        dbc.Col(
            #html.Br(),
            html.P([
                "Esta gráfica muestra cómo cambiaron las proporciones de asambleístas que se sienten hábiles para presentar razones en contra de una postura, incluyendo la suya. En el gráfico, cada sección representa un valor en una escala del 1 al 10 (donde 1 es poco y 10 es mucho). El número indica cuántas personas votaron por ese valor, y el porcentaje muestra qué proporción representan.",
                html.Br(), html.Br(),
                "Antes de las actividades, el ", html.Span("11.9%", style={'color': 'white', 'backgroundColor': 'red'}), " se consideraba muy hábil para contraargumentar (valor 10). Después, esta cifra aumentó al ",
                html.Span("26.3%", style={'color': 'white', 'backgroundColor': 'red'}), ". También se observa una disminución en los niveles intermedios: el ",
                html.Span("38.1%", style={'color': 'white', 'backgroundColor': 'orange'}), " que eligió el valor 9 bajó al ",
                html.Span("28.9%", style={'color': 'white', 'backgroundColor': 'orange'}), ".",
                html.Br(), html.Br(),
                "En general, se ve una mejora en la habilidad para contraargumentar, con más personas sintiéndose en los niveles más altos después de las actividades. Si pasas el cursor por encima de cada sección, podrás ver el valor específico que votaron los asambleístas dentro de la escala."
            ], style={
                'fontSize': '18px',
                'maxWidth': '800px',
                'marginLeft': 'auto',
                'marginRight': 'auto',
                'fontFamily': 'Museo Sans'
            }),
            width=12
        ),
        html.Div(
            html.Iframe(
                src='/assets/AutoEval_2.html',
                style={'width': '80%', 'height': '500px', 'border': 'none'}
            ),
            style={
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center',
                'margin': '20px 0',
                'width': '100%',
            }
        ),
    ], style={
        'display': 'flex',
        'flexDirection': 'column',
        'alignItems': 'center',
        'maxWidth': '1200px',  # Ancho máximo
        'margin': '0 auto'  # Centrado horizontal
    }),

    html.Div([
        dbc.Col(
            #html.Br(),
            html.P([
                "Esta gráfica muestra cómo cambiaron las proporciones de asambleístas que se sienten hábiles para conversar con otras personas sobre un asunto, intercambiando ideas y puntos de vista. En el gráfico, cada sección representa un valor en una escala del 1 al 10 (donde 1 es poco y 10 es mucho). El número indica cuántas personas votaron por ese valor, y el porcentaje muestra qué proporción representan.",
                html.Br(), html.Br(),
                "Antes de las actividades, el ", html.Span("28.6%", style={'color': 'white', 'backgroundColor': 'red'}), " se consideraba muy hábil para discutir (valor 10). Después, esta cifra aumentó al ",
                html.Span("42.1%", style={'color': 'white', 'backgroundColor': 'red'}), ". También hubo un aumento en el nivel 9, que pasó del ",
                html.Span("19.0%", style={'color': 'white', 'backgroundColor': 'orange'}), " al ",
                html.Span("31.6%", style={'color': 'white', 'backgroundColor': 'orange'}), ".",
                html.Br(), html.Br(),
                "En general, se observa una mejora significativa en la habilidad para discutir, con más asambleístas ubicándose en los niveles más altos después de las actividades. Si pasas el cursor por encima de cada sección, podrás ver el valor específico que votaron los asambleístas dentro de la escala."
            ], style={
                'fontSize': '18px',
                'maxWidth': '800px',
                'marginLeft': 'auto',
                'marginRight': 'auto',
                'fontFamily': 'Museo Sans'
            }),
            width=12
        ),
        html.Div(
            html.Iframe(
                src='/assets/AutoEval_3.html',
                style={'width': '80%', 'height': '500px', 'border': 'none'}
            ),
            style={
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center',
                'margin': '20px 0',
                'width': '100%',
            }
        ),
    ], style={
        'display': 'flex',
        'flexDirection': 'column',
        'alignItems': 'center',
        #'textAlign': 'center',
        'maxWidth': '1200px',  # Ancho máximo
        'margin': '0 auto'  # Centrado horizontal
    }),

    html.Div([
        dbc.Col(
            #html.Br(),
            html.P([
                "Esta gráfica muestra cómo cambiaron las proporciones de asambleístas que se sienten hábiles para analizar diferentes opciones o consecuencias de una decisión. En el gráfico, cada sección representa un valor en una escala del 1 al 10 (donde 1 es poco y 10 es mucho). El número indica cuántas personas votaron por ese valor, y el porcentaje muestra qué proporción representan.",
                html.Br(), html.Br(),
                "Antes de las actividades, el ", html.Span("26.2%", style={'color': 'white', 'backgroundColor': 'red'}), " se sentía muy hábil para evaluar (valor 10). Después, esta proporción bajó ligeramente al ",
                html.Span("24.3%", style={'color': 'white', 'backgroundColor': 'red'}), ". Sin embargo, el nivel 9 mostró una mejora, pasando del ",
                html.Span("16.7%", style={'color': 'white', 'backgroundColor': 'orange'}), " al ",
                html.Span("37.8%", style={'color': 'white', 'backgroundColor': 'orange'}), ".",
                html.Br(), html.Br(),
                "En general, se observa una mayor concentración de respuestas en los niveles altos después de las actividades. Si pasas el cursor por encima de cada sección, podrás ver el valor específico que votaron los asambleístas dentro de la escala."
            ], style={
                'fontSize': '18px',
                'maxWidth': '800px',
                'marginLeft': 'auto',
                'marginRight': 'auto',
                'fontFamily': 'Museo Sans'
            }),
            width=12
        ),
        html.Div(
            html.Iframe(
                src='/assets/AutoEval_4.html',
                style={'width': '80%', 'height': '500px', 'border': 'none'}
            ),
            style={
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center',
                'margin': '20px 0',
                'width': '100%',
            }
        ),
    ], style={
        'display': 'flex',
        'flexDirection': 'column',
        'alignItems': 'center',
        #'textAlign': 'center',
        'maxWidth': '1200px',  # Ancho máximo
        'margin': '0 auto'  # Centrado horizontal
    }),

    html.Div([
        dbc.Col(
            #html.Br(),
            html.P([
                "Esta gráfica muestra cómo cambiaron las proporciones de asambleístas que se sienten hábiles para elegir o determinar un curso de acción o posición después de reflexionar. En el gráfico, cada sección representa un valor en una escala del 1 al 10 (donde 1 es poco y 10 es mucho). El número indica cuántas personas votaron por ese valor, y el porcentaje muestra qué proporción representan.",
                html.Br(), html.Br(),
                "Antes de las actividades, el ", html.Span("28.6%", style={'color': 'white', 'backgroundColor': 'red'}), " se consideraba muy hábil para decidir (valor 10). Después, esta proporción bajó ligeramente al ",
                html.Span("26.3%", style={'color': 'white', 'backgroundColor': 'red'}), ". Sin embargo, en el nivel 9, hubo una mejora notable, pasando del ",
                html.Span("14.3%", style={'color': 'white', 'backgroundColor': 'orange'}), " al ",
                html.Span("34.2%", style={'color': 'white', 'backgroundColor': 'orange'}), ".",
                html.Br(), html.Br(),
                "En general, se observa una mayor distribución de respuestas en los niveles altos después de las actividades. Si pasas el cursor por encima de cada sección, podrás ver el valor específico que votaron los asambleístas dentro de la escala."
            ], style={
                'fontSize': '18px',
                'maxWidth': '800px',
                'marginLeft': 'auto',
                'marginRight': 'auto',
                'fontFamily': 'Museo Sans'
            }),
            width=12
        ),
        html.Div(
            html.Iframe(
                src='/assets/AutoEval_5.html',
                style={'width': '80%', 'height': '500px', 'border': 'none'}
            ),
            style={
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center',
                'margin': '20px 0',
                'width': '100%',
            }
        ),
    ], style={
        'display': 'flex',
        'flexDirection': 'column',
        'alignItems': 'center',
        #'textAlign': 'center',
        'maxWidth': '1200px',  # Ancho máximo
        'margin': '0 auto'  # Centrado horizontal
    }),

    html.Div([
        dbc.Col(
            #html.Br(),
            html.P([
                "Esta gráfica muestra cómo cambiaron las proporciones de asambleístas que consideran probable cambiar de opinión si otra persona presenta un argumento convincente. En el gráfico, cada sección representa un valor en una escala del 1 al 10 (donde 1 es poco y 10 es mucho). El número indica cuántas personas votaron por ese valor, y el porcentaje muestra qué proporción representan.",
                html.Br(), html.Br(),
                "Antes de las actividades, el ", html.Span("14.6%", style={'color': 'white', 'backgroundColor': 'red'}), " se sentía muy dispuesto a cambiar de opinión (valor 10). Después, esta proporción subió al ",
                html.Span("26.3%", style={'color': 'white', 'backgroundColor': 'red'}), ". También hubo un aumento en el nivel 9, pasando del ",
                html.Span("29.3%", style={'color': 'white', 'backgroundColor': 'orange'}), " al ",
                html.Span("34.2%", style={'color': 'white', 'backgroundColor': 'orange'}), ".",
                html.Br(), html.Br(),
                "En general, se observa una mayor apertura a cambiar de opinión tras escuchar argumentos sólidos. Si pasas el cursor por encima de cada sección, podrás ver el valor específico que votaron los asambleístas dentro de la escala."
            ], style={
                'fontSize': '18px',
                'maxWidth': '800px',
                'marginLeft': 'auto',
                'marginRight': 'auto',
                'fontFamily': 'Museo Sans'
            }),
            width=12
        ),

        html.Div(
            html.Iframe(
                src='/assets/AutoEval_6.html',
                style={'width': '80%', 'height': '500px', 'border': 'none'}
            ),
            style={
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center',
                'margin': '20px 0',
                'width': '100%',
            }
        ),
    ], style={
        'display': 'flex',
        'flexDirection': 'column',
        'alignItems': 'center',
        #'textAlign': 'center',
        'maxWidth': '1200px',  # Ancho máximo
        'margin': '0 auto'  # Centrado horizontal
    }),
])


    elif selected_subtab == "autoevalgenero":

        return html.Div([
            #html.Br(),
            dbc.Col(
                #html.Br(),
                html.P([
                    html.Br(), html.Br(),
                    "Esta sección desglosa los resultados de la autoevaluación según el género de los participantes. Al observar las diferencias entre hombres y mujeres en sus percepciones de habilidades, se pueden identificar patrones específicos y áreas en las que puede ser necesario aplicar enfoques diferenciados para potenciar las capacidades de cada grupo.",
                    html.Br(), html.Br(),
                    "Esta gráfica muestra cómo cambiaron las proporciones de hombres y mujeres que se sienten hábiles para reflexionar detenidamente sobre diferentes aspectos de un tema. En el gráfico, cada sección representa un valor en una escala del 1 al 10 (donde 1 es poco y 10 es mucho). El número indica cuántas personas votaron por ese valor, y el porcentaje muestra qué proporción representan.",
                    html.Br(), html.Br(),
                    "En el caso de los ", html.B("hombres"), ", el porcentaje más alto en el nivel 10 pasó del ",
                    html.Span("33.3%", style={'color': 'white', 'backgroundColor': 'red'}), " en el pre al ",
                    html.Span("23.1%", style={'color': 'white', 'backgroundColor': 'red'}), " en el pos.",
                    html.Br(), html.Br(),
                    "Para las ", html.B("mujeres"), ", el porcentaje en el nivel 10 aumentó del ",
                    html.Span("33.3%", style={'color': 'white', 'backgroundColor': 'red'}), " en el pre al ",
                    html.Span("58.3%", style={'color': 'white', 'backgroundColor': 'red'}), " en el pos.",
                    html.Br(), html.Br(),
                    "En general, se observa una mejora en las mujeres y una ligera disminución en los hombres. Si pasas el cursor por encima de cada sección, podrás ver el valor específico que votaron los asambleístas dentro de la escala."
                ], style={
                    'fontSize': '18px',
                    'maxWidth': '800px',
                    'marginLeft': 'auto',
                    'marginRight': 'auto',
                    'fontFamily': 'Museo Sans'
                }),
                width=12
            ),

            html.Div([
                html.H4("", style={'textAlign': 'center'}),
                html.Div(
                    html.Iframe(
                        src='/assets/AutoEval_Genero_0.html',
                        style={'width': '80%', 'height': '500px', 'border': 'none'}
                    ),
                    style={
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center',
                        'margin': '20px 0',
                        'width': '100%',
                    }
                ),
            ], style={
                'display': 'flex',
                'flexDirection': 'column',
                'alignItems': 'center',
                #'textAlign': 'center',
                'maxWidth': '1200px',
                'margin': '0 auto'
            }),

            html.Div([
                dbc.Col(
                    #html.Br(),
                    html.P([
                        "Esta gráfica muestra cómo cambiaron las proporciones de hombres y mujeres que se sienten hábiles para presentar razones a favor de una opción o postura. En el gráfico, cada sección representa un valor en una escala del 1 al 10 (donde 1 es poco y 10 es mucho). El número indica cuántas personas votaron por ese valor, y el porcentaje muestra qué proporción representan.",
                        html.Br(), html.Br(),
                        "En el caso de los ", html.B("hombres"), ", el porcentaje en el nivel más alto (valor 10) se mantuvo estable, con un ",
                        html.Span("13.3%", style={'color': 'white', 'backgroundColor': 'red'}), " en el pre y un ",
                        html.Span("15.4%", style={'color': 'white', 'backgroundColor': 'red'}), " en el pos.",
                        html.Br(), html.Br(),
                        "Para las ", html.B("mujeres"), ", el porcentaje en el nivel 10 pasó del ",
                        html.Span("25.9%", style={'color': 'white', 'backgroundColor': 'red'}), " en el pre al ",
                        html.Span("37.5%", style={'color': 'white', 'backgroundColor': 'red'}), " en el pos. También aumentó el nivel 9, que subió del ",
                        html.Span("11.1%", style={'color': 'white', 'backgroundColor': 'orange'}), " al ",
                        html.Span("41.7%", style={'color': 'white', 'backgroundColor': 'orange'}), ".",
                        html.Br(), html.Br(),
                        "En general, se observa una mejora significativa en las mujeres. Si pasas el cursor por encima de cada sección, podrás ver el valor específico que votaron los asambleístas dentro de la escala."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans'
                    }),
                    width=12
                ),
                html.Div(
                    html.Iframe(
                        src='/assets/AutoEval_Genero_1.html',
                        style={'width': '80%', 'height': '500px', 'border': 'none'}
                    ),
                    style={
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center',
                        'margin': '20px 0',
                        'width': '100%',
                    }
                ),
            ], style={
                'display': 'flex',
                'flexDirection': 'column',
                'alignItems': 'center',
                #'textAlign': 'center',
                'maxWidth': '1200px',
                'margin': '0 auto'
            }),

            html.Div([
                dbc.Col(
                    #html.Br(),
                    html.P([
                        "Esta gráfica muestra cómo cambiaron las proporciones de hombres y mujeres que se sienten hábiles para presentar razones en contra de una opción o postura, incluyendo la suya. En el gráfico, cada sección representa un valor en una escala del 1 al 10 (donde 1 es poco y 10 es mucho). El número indica cuántas personas votaron por ese valor, y el porcentaje muestra qué proporción representan.",
                        html.Br(), html.Br(),
                        "En el caso de los ", html.B("hombres"), ", el porcentaje en el nivel más alto (valor 10) aumentó ligeramente del ",
                        html.Span("13.3%", style={'color': 'white', 'backgroundColor': 'red'}), " en el pre al ",
                        html.Span("23.1%", style={'color': 'white', 'backgroundColor': 'red'}), " en el pos.",
                        html.Br(), html.Br(),
                        "Para las ", html.B("mujeres"), ", el porcentaje en el nivel 10 pasó del ",
                        html.Span("11.1%", style={'color': 'white', 'backgroundColor': 'red'}), " en el pre al ",
                        html.Span("29.2%", style={'color': 'white', 'backgroundColor': 'red'}), " en el pos. También hubo un aumento en el nivel 9, que subió del ",
                        html.Span("14.8%", style={'color': 'white', 'backgroundColor': 'orange'}), " al ",
                        html.Span("33.3%", style={'color': 'white', 'backgroundColor': 'orange'}), ".",
                        html.Br(), html.Br(),
                        "Si pasas el cursor por encima de cada sección, podrás ver el valor específico que votaron los asambleístas dentro de la escala."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans'
                    }),
                    width=12
                ),
                html.Div(
                    html.Iframe(
                        src='/assets/AutoEval_Genero_2.html',
                        style={'width': '80%', 'height': '500px', 'border': 'none'}
                    ),
                    style={
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center',
                        'margin': '20px 0',
                        'width': '100%',
                    }
                ),
            ], style={
                'display': 'flex',
                'flexDirection': 'column',
                'alignItems': 'center',
                #'textAlign': 'center',
                'maxWidth': '1200px',
                'margin': '0 auto'
            }),

            html.Div([
                dbc.Col(
                    html.P([
                        "Esta gráfica muestra cómo cambiaron las proporciones de hombres y mujeres que se sienten hábiles para conversar con otras personas, intercambiando ideas y puntos de vista. En el gráfico, cada sección representa un valor en una escala del 1 al 10 (donde 1 es poco y 10 es mucho). El número indica cuántas personas votaron por ese valor, y el porcentaje muestra qué proporción representan.",
                        html.Br(), html.Br(),
                        "En el caso de los ", html.B("hombres"), ", el nivel más alto (valor 10) aumentó del ",
                        html.Span("20.0%", style={'color': 'white', 'backgroundColor': 'red'}), " en el pre al ",
                        html.Span("30.8%", style={'color': 'white', 'backgroundColor': 'red'}), " en el pos.",
                        html.Br(), html.Br(),
                        "Para las ", html.B("mujeres"), ", el nivel 10 pasó del ",
                        html.Span("33.3%", style={'color': 'white', 'backgroundColor': 'red'}), " en el pre al ",
                        html.Span("50.0%", style={'color': 'white', 'backgroundColor': 'red'}), " en el pos. También se observa una disminución en los niveles intermedios, lo que indica una mayor concentración de respuestas en los niveles más altos.",
                        html.Br(), html.Br(),
                        "Si pasas el cursor por encima de cada sección, podrás ver el valor específico que votaron los asambleístas dentro de la escala."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans'
                    }),
                    width=12
                ),

                html.Div(
                    html.Iframe(
                        src='/assets/AutoEval_Genero_3.html',
                        style={'width': '80%', 'height': '500px', 'border': 'none'}
                    ),
                    style={
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center',
                        'margin': '20px 0',
                        'width': '100%',
                    }
                ),
            ], style={
                'display': 'flex',
                'flexDirection': 'column',
                'alignItems': 'center',
                #'textAlign': 'center',
                'maxWidth': '1200px',
                'margin': '0 auto'
            }),

            html.Div([
                dbc.Col(
                    html.P([
                        "Esta gráfica muestra cómo cambiaron las proporciones de hombres y mujeres que se sienten hábiles para analizar diferentes opciones o consecuencias de una decisión. En el gráfico, cada sección representa un valor en una escala del 1 al 10 (donde 1 es poco y 10 es mucho). El número indica cuántas personas votaron por ese valor, y el porcentaje muestra qué proporción representan.",
                        html.Br(), html.Br(),
                        "En el caso de los ", html.B("hombres"), ", el porcentaje en el nivel más alto (valor 10) bajó del ",
                        html.Span("26.7%", style={'color': 'white', 'backgroundColor': 'red'}), " en el pre al ",
                        html.Span("23.1%", style={'color': 'white', 'backgroundColor': 'red'}), " en el pos. También se observa un aumento en el nivel 9, que pasó del ",
                        html.Span("33.3%", style={'color': 'white', 'backgroundColor': 'orange'}), " al ",
                        html.Span("46.2%", style={'color': 'white', 'backgroundColor': 'orange'}), ".",
                        html.Br(), html.Br(),
                        "Para las ", html.B("mujeres"), ", el nivel 10 disminuyó ligeramente del ",
                        html.Span("25.9%", style={'color': 'white', 'backgroundColor': 'red'}), " en el pre al ",
                        html.Span("26.1%", style={'color': 'white', 'backgroundColor': 'red'}), " en el pos. Sin embargo, el nivel 9 mostró un aumento del ",
                        html.Span("14.8%", style={'color': 'white', 'backgroundColor': 'orange'}), " al ",
                        html.Span("34.8%", style={'color': 'white', 'backgroundColor': 'orange'}), ".",
                        html.Br(), html.Br(),
                        "En general, se observa una tendencia positiva hacia niveles más altos después de las actividades. Si pasas el cursor por encima de cada sección, podrás ver el valor específico que votaron los asambleístas dentro de la escala."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans'
                    }),
                    width=12
                ),

                html.Div(
                    html.Iframe(
                        src='/assets/AutoEval_Genero_4.html',
                        style={'width': '80%', 'height': '500px', 'border': 'none'}
                    ),
                    style={
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center',
                        'margin': '20px 0',
                        'width': '100%',
                    }
                ),
            ], style={
                'display': 'flex',
                'flexDirection': 'column',
                'alignItems': 'center',
                #'textAlign': 'center',
                'maxWidth': '1200px',
                'margin': '0 auto'
            }),

            html.Div([
                dbc.Col(
                    html.P([
                        "Esta gráfica muestra cómo cambiaron las proporciones de hombres y mujeres que se sienten hábiles para elegir o determinar un curso de acción o posición tras reflexionar. En el gráfico, cada sección representa un valor en una escala del 1 al 10 (donde 1 es poco y 10 es mucho). El número indica cuántas personas votaron por ese valor, y el porcentaje muestra qué proporción representan.",
                        html.Br(), html.Br(),
                        "En el caso de los ", html.B("hombres"), ", el porcentaje en el nivel más alto (valor 10) pasó del ",
                        html.Span("26.7%", style={'color': 'white', 'backgroundColor': 'red'}), " en el pre al ",
                        html.Span("23.1%", style={'color': 'white', 'backgroundColor': 'red'}), " en el pos. También hubo un aumento en el nivel 9, del ",
                        html.Span("13.3%", style={'color': 'white', 'backgroundColor': 'orange'}), " al ",
                        html.Span("23.1%", style={'color': 'white', 'backgroundColor': 'orange'}), ".",
                        html.Br(), html.Br(),
                        "Para las ", html.B("mujeres"), ", el porcentaje en el nivel 10 se mantuvo casi igual, del ",
                        html.Span("29.6%", style={'color': 'white', 'backgroundColor': 'red'}), " en el pre al ",
                        html.Span("29.2%", style={'color': 'white', 'backgroundColor': 'red'}), " en el pos. Sin embargo, el nivel 9 mostró un aumento significativo, pasando del ",
                        html.Span("14.8%", style={'color': 'white', 'backgroundColor': 'orange'}), " al ",
                        html.Span("37.5%", style={'color': 'white', 'backgroundColor': 'orange'}), ".",
                        html.Br(), html.Br(),
                        "Si pasas el cursor por encima de cada sección, podrás ver el valor específico que votaron los asambleístas dentro de la escala."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans'
                    }),
                    width=12
                ),

                html.Div(
                    html.Iframe(
                        src='/assets/AutoEval_Genero_5.html',
                        style={'width': '80%', 'height': '500px', 'border': 'none'}
                    ),
                    style={
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center',
                        'margin': '20px 0',
                        'width': '100%',
                    }
                ),
            ], style={
                'display': 'flex',
                'flexDirection': 'column',
                'alignItems': 'center',
                #'textAlign': 'center',
                'maxWidth': '1200px',
                'margin': '0 auto'
            }),

            html.Div([
                dbc.Col(
                    html.P([
                        "Esta gráfica muestra cómo cambiaron las proporciones de hombres y mujeres que consideran probable cambiar de opinión si otra persona presenta un argumento convincente. En el gráfico, cada sección representa un valor en una escala del 1 al 10 (donde 1 es poco y 10 es mucho). El número indica cuántas personas votaron por ese valor, y el porcentaje muestra qué proporción representan.",
                        html.Br(), html.Br(),
                        "En el caso de los ", html.B("hombres"), ", el porcentaje en el nivel más alto (valor 10) disminuyó del ",
                        html.Span("20.0%", style={'color': 'white', 'backgroundColor': 'red'}), " en el pre al ",
                        html.Span("15.4%", style={'color': 'white', 'backgroundColor': 'red'}), " en el pos. Para las ",
                        html.B("mujeres"), ", el nivel 10 aumentó del ",
                        html.Span("11.5%", style={'color': 'white', 'backgroundColor': 'red'}), " en el pre al ",
                        html.Span("29.2%", style={'color': 'white', 'backgroundColor': 'red'}), " en el pos. También hubo un aumento en el nivel 9, pasando del ",
                        html.Span("26.9%", style={'color': 'white', 'backgroundColor': 'orange'}), " al ",
                        html.Span("37.5%", style={'color': 'white', 'backgroundColor': 'orange'}), ".",
                        html.Br(), html.Br(),
                        html.B("Nota aclaratoria:"), " En el pos de los ",
                        html.B("hombres"), ", se presenta una variación en el modelo de graficación debido a que algunos participantes no completaron la encuesta por motivos desconocidos. Esto afectó el proceso de graficación, generando una inconsistencia en los valores más bajos y en la distribución general de las proporciones."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans'
                    }),
                    width=12
                ),

                html.Div(
                    html.Iframe(
                        src='/assets/AutoEval_Genero_6.html',
                        style={'width': '80%', 'height': '500px', 'border': 'none'}
                    ),
                    style={
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center',
                        'margin': '20px 0',
                        'width': '100%',
                    }
                ),
            ], style={
                'display': 'flex',
                'flexDirection': 'column',
                'alignItems': 'center',
                #'textAlign': 'center',
                'maxWidth': '1200px',
                'margin': '0 auto'
            }),
        ])

    elif selected_subtab == "confianza":

        return html.Div([
            html.Br(),
            html.P([
                html.Br(), html.Br(),
                "En esta sección se analizan los niveles de confianza de los participantes en diversas áreas relacionadas con las instituciones, el proceso deliberativo y sus propios compañeros. La confianza es un indicador clave para medir el impacto del proceso en términos de credibilidad y disposición para participar en decisiones públicas.",
            ], style={
                'fontSize': '18px',
                'maxWidth': '800px',
                'marginLeft': 'auto',
                'marginRight': 'auto',
                'fontFamily': 'Museo Sans'
            }),
            html.Div([
                html.H3("PRE: ¿Qué sientes cuando te hablan de lo público?", style={'textAlign': 'center', 'fontFamily': 'Kensington', 'fontSize': '30px'}),
                dbc.Col(
                    html.P([
                        "Esta nube refleja las percepciones iniciales de los participantes sobre la confianza en las instituciones antes del proceso deliberativo.",
                        html.Br(), html.Br(),
                        "Las palabras más destacadas son ", html.B("público"), ", ", html.B("persona"), ", ",
                        html.B("confianza"), " e ", html.B("interés"), ". Estas palabras muestran un enfoque en el individuo y la idea de lo público, con cierta inquietud por el interés y el papel de las personas en la participación ciudadana.",
                        html.Br(), html.Br(),
                        "También se resaltan palabras como ", html.B("frustración"), ", ", html.B("desconfianza"),
                        " y ", html.B("temor"), ", lo que indica una percepción negativa o de escepticismo hacia las instituciones.",
                        html.Br(), html.Br(),
                        "En general, se percibe una combinación de expectativas, desconfianza y frustración, junto con un llamado a la mejora y a un mayor involucramiento ciudadano."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans'
                    }),
                    width=12
                ),

                html.Div(
                    html.Img(
                        src='/assets/nube_pre.png',
                        style={'width': '80%', 'height': 'auto', 'display': 'block'}
                    ),
                    style={
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center',
                        'margin': '20px 0',
                        'width': '100%',
                    }
                ),
            ], style={
                'display': 'flex',
                'flexDirection': 'column',
                'alignItems': 'center',
                #'textAlign': 'center',
                'maxWidth': '1200px',
                'margin': '0 auto'
            }),

            html.Br(),

            html.Div([
                html.H3("POS: Después de ser parte de este proceso ¿Qué sientes cuando te hablan de lo público?", style={'textAlign': 'center', 'fontSize': '30px', 'fontFamily': 'Kensington'}),
                dbc.Col(
                    html.P([
                        "Esta nube refleja las percepciones después del proceso deliberativo sobre confianza en las instituciones.",
                        html.Br(), html.Br(),
                        "Las palabras más destacadas son ", html.B("confianza"), ", ", html.B("responsabilidad"), ", ",
                        html.B("público"), " y ", html.B("ciudadanía"), ". Esto indica un cambio hacia una percepción más centrada en el compromiso colectivo y en el sentido de responsabilidad hacia lo público.",
                        html.Br(), html.Br(),
                        "También surgen palabras como ", html.B("esperanza"), ", ", html.B("participación"), " y ",
                        html.B("decisiones"), ", lo que sugiere una mayor confianza en los procesos y en la capacidad de tomar decisiones colectivas.",
                        html.Br(), html.Br(),
                        "En general, se observa una transformación hacia una percepción más positiva, con mayor énfasis en la confianza, el compromiso y la responsabilidad ciudadana."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans'
                    }),
                    width=12
                ),
                html.Div(
                    html.Img(
                        src='/assets/nube_pos.png',
                        style={'width': '80%', 'height': 'auto', 'display': 'block'}
                    ),
                    style={
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center',
                        'margin': '20px 0',
                        'width': '100%',
                    }
                ),
            ], style={
                'display': 'flex',
                'flexDirection': 'column',
                'alignItems': 'center',
                #'textAlign': 'center',
                'maxWidth': '1200px',
                'margin': '0 auto'
            }),

            html.Br(),

            html.Div([
                dbc.Col(
                    html.P([
                        "Esta gráfica muestra cómo cambiaron las proporciones de asambleístas que confían en la capacidad de la Alcaldía Mayor de Bogotá para resolver los problemas de su comunidad.",
                        html.Br(), html.Br(),
                        "El valor máximo en esta escala es ", html.B("6"), ", representado por la sección amarilla en la parte superior.",
                        html.Br(), html.Br(),
                        "Antes de las actividades (", html.B("Pre"), "), el ",
                        html.Span("11.9%", style={"backgroundColor": "#FFD700", "color": "black"}),
                        " mostró un nivel máximo de confianza (valor ", html.B("6"), "). Después de las actividades (",
                        html.B("Pos"), "), este porcentaje aumentó al ",
                        html.Span("34.1%", style={"backgroundColor": "#FFD700", "color": "black"}), ".",
                        html.Br(), html.Br(),
                        "También se observa una reducción en los niveles más bajos de confianza. El porcentaje en el nivel más bajo (valor ",
                        html.B("1"), ") disminuyó del ",
                        html.Span("16.7%", style={"backgroundColor": "#FF0000", "color": "white"}),
                        " al ", html.Span("9.8%", style={"backgroundColor": "#FF0000", "color": "white"}), ".",
                        html.Br(), html.Br(),
                        "En general, se nota un aumento en la confianza después de las actividades, con más participantes ubicándose en los niveles más altos. Si pasas el cursor por encima de cada sección, podrás ver el valor específico que votaron los asambleístas dentro de la escala."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans'
                    }),
                    width=12
                ),
                html.Div(
                    html.Iframe(
                        src='/assets/ComparacionConfianza_0.html',
                        style={'width': '80%', 'height': '500px', 'border': 'none'}
                    ),
                    style={
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center',
                        'margin': '20px 0',
                        'width': '100%',
                    }
                ),
            ], style={
                'display': 'flex',
                'flexDirection': 'column',
                'alignItems': 'center',
                #'textAlign': 'center',
                'maxWidth': '1200px',
                'margin': '0 auto'
            }),

            html.Div([
                dbc.Col(
                    html.P([
                        "Esta gráfica muestra cómo cambiaron las proporciones de asambleístas respecto al grado de confianza en que sus recomendaciones sobre los temas tratados en la Asamblea Deliberativa se implementarán.",
                        html.Br(), html.Br(),
                        "El valor máximo en esta escala está representado por la sección amarilla más clara en la parte superior de cada barra.",
                        html.Br(), html.Br(),
                        "Antes de las actividades, el ",
                        html.Span("31.0%", style={"backgroundColor": "#FFD700", "color": "black"}),
                        " mostró un nivel máximo de confianza. Después de las actividades, esta proporción aumentó al ",
                        html.Span("39.0%", style={"backgroundColor": "#FFD700", "color": "black"}), ".",
                        html.Br(), html.Br(),
                        "En los niveles intermedios de confianza, se nota un cambio leve: el ",
                        html.Span("45.2%", style={"backgroundColor": "#FFD700", "color": "black"}),
                        " en el nivel previo (", html.B("Pre"), ") pasó a un ",
                        html.Span("43.9%", style={"backgroundColor": "#FFD700", "color": "black"}),
                        " en el nivel posterior (", html.B("Pos"), "), mostrando una ligera disminución.",
                        html.Br(), html.Br(),
                        "En los niveles más bajos de confianza, la proporción en el nivel más bajo disminuyó. Antes de las actividades, el ",
                        html.Span("4.8%", style={"backgroundColor": "#FF0000", "color": "white"}),
                        " mostró este nivel mínimo de confianza, mientras que después de las actividades este porcentaje se redujo al ",
                        html.Span("0%", style={"backgroundColor": "#FF0000", "color": "white"}), ".",
                        html.Br(), html.Br(),
                        "Si pasas el cursor por encima de cada sección, podrás ver el valor específico que votaron los asambleístas dentro de la escala."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans'
                    }),
                    width=12
                ),

                html.Div(
                    html.Iframe(
                        src='/assets/ComparacionConfianza_1.html',
                        style={'width': '80%', 'height': '500px', 'border': 'none'}
                    ),
                    style={
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center',
                        'margin': '20px 0',
                        'width': '100%',
                    }
                ),
            ], style={
                'display': 'flex',
                'flexDirection': 'column',
                'alignItems': 'center',
                #'textAlign': 'center',
                'maxWidth': '1200px',
                'margin': '0 auto'
            }),

            html.Div([
                dbc.Col(
                    html.P([
                        "Esta gráfica muestra por qué las personas tienden a no involucrarse en los espacios de participación promovidos por la Alcaldía Mayor de Bogotá.",
                        html.Br(), html.Br(),
                        "- El 38.1% (subrayado en rojo y texto en blanco desde 3) indicó que la razón principal es el ",
                        html.B("desconocimiento"), ".",
                        html.Br(), html.Br(),
                        "- El 28.6% (subrayado en naranja y texto en blanco desde 2) mencionó que no creen que estos espacios resuelvan las problemáticas de su comunidad (",
                        html.B("no"), ").",
                        html.Br(), html.Br(),
                        "- El 21.4% (subrayado en amarillo y texto en negro desde 2) expresó que no participan debido al ",
                        html.B("desinterés"), ".",
                        html.Br(), html.Br(),
                        "- El 11.9% (subrayado en marrón y texto en blanco desde 1) afirmó que no cuentan con el tiempo ni recursos para movilizarse (",
                        html.B("no"), ")."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans'
                    }),
                    width=12
                ),

                html.Div(
                    html.Iframe(
                        src='/assets/Confianza4_pre.html',
                        style={'width': '80%', 'height': '500px', 'border': 'none'}
                    ),
                    style={
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center',
                        'margin': '20px 0',
                        'width': '100%',
                    }
                ),
            ], style={
                'display': 'flex',
                'flexDirection': 'column',
                'alignItems': 'center',
                #'textAlign': 'center',
                'maxWidth': '1200px',
                'margin': '0 auto'
            }),

            html.Div([
                dbc.Col(
                    html.P([
                        "Esta gráfica muestra la disposición de los participantes para implementar las recomendaciones generadas en el proceso deliberativo.",
                        html.Br(), html.Br(),
                        "- El 65% (subrayado en amarillo y texto en negro desde 6) de los participantes indicó que implementaría ",
                        html.B("todas"), " las recomendaciones.",
                        html.Br(), html.Br(),
                        "- El 35% (subrayado en rojo y texto en blanco desde 3) señaló que implementaría las recomendaciones ",
                        html.B("parcialmente"), "."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans'
                    }),
                    width=12
                ),

                html.Div(
                    html.Iframe(
                        src='/assets/Confianza4_pos.html',
                        style={'width': '80%', 'height': '500px', 'border': 'none'}
                    ),
                    style={
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center',
                        'margin': '20px 0',
                        'width': '100%',
                    }
                ),
            ], style={
                'display': 'flex',
                'flexDirection': 'column',
                'alignItems': 'center',
                #'textAlign': 'center',
                'maxWidth': '1200px',
                'margin': '0 auto'
            }),

        ])


    elif selected_subtab == "logistica":

        return html.Div([
            html.Div([
                dbc.Col(
                    html.P([
                        html.Br(), html.Br(),
                        "Aquí se presentan las percepciones de los participantes sobre los aspectos organizativos y operativos del evento. Se analizan áreas como el tiempo disponible, los recursos utilizados, la comunicación y otros factores que influyeron en el desarrollo de las actividades. Esta sección identifica qué aspectos de la logística funcionaron bien y cuáles pueden mejorar en el futuro.",
                        html.Br(), html.Br(),
                        "Esta gráfica muestra las opiniones de los asambleístas sobre si consideraron suficiente el tiempo disponible para las sesiones.",
                        html.Br(), html.Br(),
                        "Las respuestas se distribuyeron de la siguiente manera: ",
                        html.Span("19.5%", style={'backgroundColor': 'yellow', 'color': 'black'}),
                        " consideró que el tiempo fue ", html.B("totalmente"), " suficiente; ",
                        html.Span("26.8%", style={'backgroundColor': '#ffcc66', 'color': 'white'}),
                        " opinó que el tiempo fue ", html.B("suficiente"), "; ",
                        html.Span("17.1%", style={'backgroundColor': 'orange', 'color': 'white'}),
                        " sintió que el tiempo fue ", html.B("parcialmente"), " suficiente; ",
                        html.Span("19.5%", style={'backgroundColor': 'red', 'color': 'white'}),
                        " consideró que el tiempo fue ", html.B("insuficiente"), "; ",
                        html.Span("12.2%", style={'backgroundColor': 'brown', 'color': 'white'}),
                        " afirmó que el tiempo fue ", html.B("muy"), " insuficiente; ",
                        html.Span("4.9%", style={'backgroundColor': '#5c4033', 'color': 'white'}),
                        " expresó que el tiempo fue ", html.B("totalmente"), " insuficiente.",
                        html.Br(), html.Br(),
                        "En general, aunque una mayoría consideró el tiempo adecuado o ", html.B("suficiente"), ", una parte significativa sintió que el tiempo asignado no fue ", html.B("suficiente"), " para cubrir las necesidades de las sesiones."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans'
                    }),
                    width=12
                ),
                html.Div(
                    html.Iframe(
                        src='/assets/Logistica1.html',
                        style={'width': '80%', 'height': '500px', 'border': 'none'}
                    ),
                    style={
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center',
                        'margin': '20px 0',
                        'width': '100%',
                    }
                ),
            ], style={
                'display': 'flex',
                'flexDirection': 'column',
                'alignItems': 'center',
                #'textAlign': 'center',
                'maxWidth': '1200px',
                'margin': '0 auto'
            }),

            html.Div([
                dbc.Col(
                    html.P([
                        "Esta gráfica muestra cuánto tiempo adicional los asambleístas consideraron que habría sido útil para las sesiones:",
                        html.Br(), html.Br(),
                        html.Span("46.5%", style={'backgroundColor': 'red', 'color': 'white'}),
                        " indicó que se necesitaban al menos ", html.B("dos"), " o tres días más; ",
                        html.Span("20.9%", style={'backgroundColor': 'yellow', 'color': 'black'}),
                        " consideró necesario al menos ", html.B("un"), " día completo más; ",
                        html.Span("18.6%", style={'backgroundColor': '#8B4513', 'color': 'white'}),
                        " opinó que ", html.B("medio"), " día o menos habría sido suficiente; ",
                        html.Span("14%", style={'backgroundColor': 'orange', 'color': 'white'}),
                        " señaló que ", html.B("no"), " era necesario más tiempo.",
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans'
                    }),
                    width=12
                ),

                html.Div(
                    html.Iframe(
                        src='/assets/Logistica2.html',
                        style={'width': '80%', 'height': '500px', 'border': 'none'}
                    ),
                    style={
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center',
                        'margin': '20px 0',
                        'width': '100%',
                    }
                ),
            ], style={
                'display': 'flex',
                'flexDirection': 'column',
                'alignItems': 'center',
                #'textAlign': 'center',
                'maxWidth': '1200px',
                'margin': '0 auto'
            }),

            html.Div([
                dbc.Col(
                    html.P([
                        "Esta gráfica muestra cómo los participantes aprovecharían el tiempo adicional si el proceso lo permitiera:",
                        html.Br(), html.Br(),
                        html.Span("35.3%", style={'backgroundColor': 'yellow', 'color': 'black'}),
                        " lo utilizaría para ", html.B("deliberar"), " y discutir más los diferentes argumentos; ",
                        html.Span("19.1%", style={'backgroundColor': 'red', 'color': 'white'}),
                        " consideró necesario ", html.B("desarrollar"), " más nuestras recomendaciones; ",
                        html.Span("20.6%", style={'backgroundColor': 'orange', 'color': 'white'}),
                        " lo dedicaría a ", html.B("acordar"), " la redacción final de las recomendaciones; ",
                        html.Span("16.2%", style={'backgroundColor': '#8B4513', 'color': 'white'}),
                        " preferiría ", html.B("escuchar"), " a más expertos; ",
                        html.Span("8.82%", style={'backgroundColor': 'brown', 'color': 'white'}),
                        " afirmó que ", html.B("no"), " era necesario más tiempo.",
                        html.Br(), html.Br(),
                        html.B("Relación"), ": Esta gráfica es consistente con los resultados previos sobre la insuficiencia del tiempo en las sesiones. ",
                        "La mayoría de los participantes expresó la necesidad de tiempo adicional para deliberar más y desarrollar mejor las recomendaciones. ",
                        "Esto coincide con la percepción de que el tiempo asignado no fue suficiente y con el ",
                        html.Span("46.5%", style={'backgroundColor': 'red', 'color': 'white'}),
                        " que pidió dos o tres días más en la gráfica anterior."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans'
                    }),
                    width=12
                ),
                html.Div(
                    html.Iframe(
                        src='/assets/Logistica3.html',
                        style={'width': '80%', 'height': '500px', 'border': 'none'}
                    ),
                    style={
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center',
                        'margin': '20px 0',
                        'width': '100%',
                    }
                ),
            ], style={
                'display': 'flex',
                'flexDirection': 'column',
                'alignItems': 'center',
                #'textAlign': 'center',
                'maxWidth': '1200px',
                'margin': '0 auto'
            }),

            html.Div([
                dbc.Col(
                    html.P([
                        "Esta gráfica muestra si los participantes sintieron que tuvieron suficientes oportunidades para expresarse durante las sesiones:",
                        html.Br(), html.Br(),
                        html.Span("64.9%", style={'backgroundColor': 'yellow', 'color': 'black'}),
                        " respondió ", html.B("sí"), ", indicando que tuvieron el espacio necesario para hablar. ",
                        html.Span("35.1%", style={'backgroundColor': 'red', 'color': 'white'}),
                        " respondió ", html.B("no"), ", sintiendo que no tuvieron suficientes oportunidades para expresarse."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans'
                    }),
                    width=12
                ),
                html.Div(
                    html.Iframe(
                        src='/assets/Logistica4.html',
                        style={'width': '80%', 'height': '500px', 'border': 'none'}
                    ),
                    style={
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center',
                        'margin': '20px 0',
                        'width': '100%',
                    }
                ),
            ], style={
                'display': 'flex',
                'flexDirection': 'column',
                'alignItems': 'center',
                #'textAlign': 'center',
                'maxWidth': '1200px',
                'margin': '0 auto'
            }),

            html.Div([
                dbc.Col(
                    html.P([
                        "Esta gráfica muestra cómo les fue a los participantes utilizando WhatsApp para recibir las comunicaciones de la Asamblea Deliberativa:",
                        html.Br(), html.Br(),
                        html.Span("80.0%", style={'backgroundColor': 'yellow', 'color': 'black'}),
                        " consideró que el uso de WhatsApp fue ", html.B("bueno o muy bueno"), " para recibir la información.",
                        html.Br(),
                        html.Span("12.5%", style={'backgroundColor': 'orange', 'color': 'white'}),
                        " indicó que el uso fue ", html.B("regular"), ".",
                        html.Br(),
                        "Un pequeño porcentaje tuvo experiencias negativas, con una proporción muy baja que consideró el uso ", html.B("malo o muy malo"), ".",
                        html.Br(), html.Br(),
                        "Podemos concluir que WhatsApp fue una herramienta efectiva para la mayoría de los participantes en la comunicación durante el proceso deliberativo."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans'
                    }),
                    width=12
                ),

                html.Div(
                    html.Iframe(
                        src='/assets/Logistica5.html',
                        style={'width': '80%', 'height': '500px', 'border': 'none'}
                    ),
                    style={
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center',
                        'margin': '20px 0',
                        'width': '100%',
                    }
                ),
            ], style={
                'display': 'flex',
                'flexDirection': 'column',
                'alignItems': 'center',
                #'textAlign': 'center',
                'maxWidth': '1200px',
                'margin': '0 auto'
            }),

            html.Div([
                dbc.Col(
                    html.P([
                        "Esta gráfica muestra qué aspectos de la logística del evento mejorarían los participantes:",
                        html.Br(), html.Br(),
                        html.Span("39.5%", style={'backgroundColor': 'orange', 'color': 'white'}),
                        " consideró necesario mejorar la ", html.B("asistencia"), ".",
                        html.Br(),
                        html.Span("25.6%", style={'backgroundColor': 'yellow', 'color': 'black'}),
                        " sugirió mejoras en la ", html.B("seguridad"), ".",
                        html.Br(),
                        html.Span("23.3%", style={'backgroundColor': 'brown', 'color': 'white'}),
                        " opinó que no era necesario hacer mejoras ", html.B("no"), ".",
                        html.Br(),
                        html.Span("6.98%", style={'backgroundColor': 'red', 'color': 'white'}),
                        " mencionó mejoras en el ", html.B("transporte"), ".",
                        html.Br(),
                        html.Span("4.65%", style={'backgroundColor': 'darkorange', 'color': 'white'}),
                        " señaló la ", html.B("alimentación"), " como área de mejora.",
                        html.Br(), html.Br(),
                        "En general, la mayoría de los participantes cree que se deben realizar mejoras en la ",
                        html.B("asistencia"), " y la ", html.B("seguridad"), " para futuros eventos."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans'
                    }),
                    width=12
                ),

                html.Div(
                    html.Iframe(
                        src='/assets/Logistica6.html',
                        style={'width': '80%', 'height': '500px', 'border': 'none'}
                    ),
                    style={
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center',
                        'margin': '20px 0',
                        'width': '100%',
                    }
                ),
            ], style={
                'display': 'flex',
                'flexDirection': 'column',
                'alignItems': 'center',
                #'textAlign': 'center',
                'maxWidth': '1200px',
                'margin': '0 auto'
            }),
        ])

    elif selected_subtab == "participacion":

        return html.Div([
            html.Div([
                dbc.Col(
                    html.P([
                        html.Br(), html.Br(),
                        "Esta sección evalúa cómo fue la participación de los asambleístas durante las actividades. Se consideran aspectos como el respeto por los turnos de palabra, la disposición para escuchar, la claridad en las intervenciones y el nivel de implicación en el proceso. Los resultados permiten identificar buenas prácticas y áreas donde se puede fomentar una participación más efectiva y equitativa.",
                        html.Br(), html.Br(),
                        "Esta gráfica muestra en qué medida los participantes se involucran actualmente en las decisiones gubernamentales que los afectan cuando se les preguntó previo al inicio de la actividad:",
                        html.Br(), html.Br(),
                        "– ",
                        #html.Span("80.0%", style={'backgroundColor': 'yellow', 'color': 'black'}),
                        html.Span("14.3%", style={"textDecoration": "underline", "backgroundColor": "yellow", "fontWeight": "bold"}), " siente que participa mucho (",
                        html.Span("mucho", style={"fontWeight": "bold"}), ").",
                        html.Br(),
                        "– ",
                        html.Span("14.3%", style={"textDecoration": "underline", "backgroundColor": "orange", "fontWeight": "bold"}), " considera que su participación es moderada (",
                        html.Span("moderada", style={"fontWeight": "bold"}), ").",
                        html.Br(),
                        "– ",
                        html.Span("14.3%", style={"textDecoration": "underline", "backgroundColor": "darkorange", "fontWeight": "bold"}), " cree que participa poco (",
                        html.Span("poco", style={"fontWeight": "bold"}), ").",
                        html.Br(),
                        "– ",
                        html.Span("21.4%", style={"textDecoration": "underline", "backgroundColor": "red", "fontWeight": "bold"}), " siente que su participación es muy baja (",
                        html.Span("muy", style={"fontWeight": "bold"}), ").",
                        html.Br(),
                        "– ",
                        html.Span("23.8%", style={"textDecoration": "underline", "backgroundColor": "darkorange", "fontWeight": "bold"}), " indica que participa mínimamente (",
                        html.Span("mínimamente", style={"fontWeight": "bold"}), ").",
                        html.Br(),
                        "– ",
                        html.Span("11.9%", style={"textDecoration": "underline", "backgroundColor": "brown", "fontWeight": "bold"}), " afirma que no participa (",
                        html.Span("no", style={"fontWeight": "bold"}), ") en absoluto.",
                        html.Br(), html.Br(),
                        "En general, la mayoría de los participantes reporta niveles bajos o mínimos de participación en las decisiones gubernamentales que los afectan."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans'
                    }),
                    width=12
                ),
                html.Div(
                    html.Iframe(
                        src='/assets/Participacion1.html',
                        style={'width': '80%', 'height': '500px', 'border': 'none'}
                    ),
                    style={
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center',
                        'margin': '20px 0',
                        'width': '100%',
                    }
                ),
            ], style={
                'display': 'flex',
                'flexDirection': 'column',
                'alignItems': 'center',
                #'textAlign': 'center',
                'maxWidth': '1200px',
                'margin': '0 auto'
            }),

            html.Div([
                dbc.Col(
                    html.P([
                        "Esta gráfica muestra las opiniones sobre si las asambleas deliberativas pueden ayudar a que la ciudadanía tenga mayor influencia en las decisiones gubernamentales antes de iniciar la actividad.",
                        html.Br(), html.Br(),
                        "– ",
                        html.Span("57.1%", style={"textDecoration": "underline", "backgroundColor": "yellow", "fontWeight": "bold"}), " considera que estas asambleas sí pueden aumentar la influencia ciudadana (",
                        html.Span("aumentar", style={"fontWeight": "bold"}), ").",
                        html.Br(),
                        "– ",
                        html.Span("35.7%", style={"textDecoration": "underline", "backgroundColor": "orange", "fontWeight": "bold"}), " opina que pueden contribuir en cierta medida (",
                        html.Span("contribuir", style={"fontWeight": "bold"}), ").",
                        html.Br(),
                        "– ",
                        html.Span("4.8%", style={"textDecoration": "underline", "backgroundColor": "red", "fontWeight": "bold"}), " cree que las asambleas no aumentan la influencia (",
                        html.Span("no", style={"fontWeight": "bold"}), ").",
                        html.Br(), html.Br(),
                        "En general, la mayoría confía en que las asambleas deliberativas pueden ser una herramienta efectiva para fortalecer la participación ciudadana en decisiones gubernamentales."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans'
                    }),
                    width=12
                ),

                html.Div(
                    html.Iframe(
                        src='/assets/Participacion2.html',
                        style={'width': '80%', 'height': '500px', 'border': 'none'}
                    ),
                    style={
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center',
                        'margin': '20px 0',
                        'width': '100%',
                    }
                ),
            ], style={
                'display': 'flex',
                'flexDirection': 'column',
                'alignItems': 'center',
                #'textAlign': 'center',
                'maxWidth': '1200px',
                'margin': '0 auto'
            }),

            html.Div([
                html.H3("¿Qué expectativas te generó ser invitado/a por la Alcaldía Mayor de Bogotá a la Asamblea Deliberativa con el objetivo de contribuir a la toma de decisiones públicas?", style={'textAlign': 'center', 'fontFamily': 'Kensington', 'fontSize': '30px'}),
                dbc.Col(
                    html.P([
                        html.Br(),
                        "Esta nube de palabras muestra las expectativas expresadas por los participantes cuando se les preguntó qué esperaban del proceso deliberativo.",
                        html.Br(), html.Br(),
                        "Las palabras más destacadas, como “",
                        html.B("participación"), "”, “",
                        html.B("poder"), "”, “",
                        html.B("confianza"), "”, y “",
                        html.B("expectativa"), "”, reflejan un fuerte deseo de involucrarse, sentirse escuchados y tener incidencia en las decisiones.",
                        html.Br(), html.Br(),
                        "Otras palabras como “",
                        html.B("ciudad"), "”, “",
                        html.B("mejorar"), "”, “",
                        html.B("escuchada"), "”, y “",
                        html.B("comunidad"), "” sugieren que los participantes esperan cambios positivos en su entorno, mayor inclusión y procesos transparentes.",
                        html.Br(), html.Br(),
                        "Esta nube captura de manera visual las expectativas de los participantes, mostrando sus principales inquietudes y deseos relacionados con el proceso deliberativo."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans'
                    }),
                    width=12
                ),
                html.Div(
                    html.Img(
                        src='/assets/Expect1.png',
                        style={'width': '80%', 'height': 'auto', 'display': 'block'}
                    ),
                    style={
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center',
                        'margin': '20px 0',
                        'width': '100%',
                    }
                ),
            ], style={
                'display': 'flex',
                'flexDirection': 'column',
                'alignItems': 'center',
                #'textAlign': 'center',
                'maxWidth': '1200px',
                'margin': '0 auto'
            }),

            html.Br(),

            html.Div([
                html.H3("¿Qué te motivó a aceptar la invitación de la Alcaldía Mayor para ser parte de la Meta Asamblea?", style={'textAlign': 'center', 'fontFamily': 'Kensington', 'fontSize': '30px'}),
                dbc.Col(
                    html.P([
                        html.Br(),
                        "Esta nube de palabras muestra las respuestas de los participantes después del proceso deliberativo, reflejando cómo evolucionaron sus expectativas y percepciones.",
                        html.Br(), html.Br(),
                        "Las palabras más destacadas incluyen “",
                        html.B("aportar"), "”, “",
                        html.B("ciudad"), "”, “",
                        html.B("poder"), "”, y “",
                        html.B("participar"), "”. Estas palabras indican un énfasis en la ",
                        html.B("acción"), ", la ",
                        html.B("contribución"), ", y el deseo de tener una ",
                        html.B("ciudad"), " más participativa y colaborativa.",
                        html.Br(), html.Br(),
                        "También aparecen términos como “",
                        html.B("conocer"), "”, “",
                        html.B("decisiones"), "”, “",
                        html.B("confianza"), "” y “",
                        html.B("Bogotá"), "”, mostrando una mayor disposición a involucrarse y una visión más clara de su rol en los procesos ciudadanos."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans'
                    }),
                    width=12
                ),

                html.Div(
                    html.Img(
                        src='/assets/Expect2.png',
                        style={'width': '80%', 'height': 'auto', 'display': 'block'}
                    ),
                    style={
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center',
                        'margin': '20px 0',
                        'width': '100%',
                    }
                ),
            ], style={
                'display': 'flex',
                'flexDirection': 'column',
                'alignItems': 'center',
                #'textAlign': 'center',
                'maxWidth': '1200px',
                'margin': '0 auto'
            }),

            html.Br(),

            html.Div([
                dbc.Col(
                    html.P([
                        "Esta gráfica muestra cómo los participantes esperan involucrarse en el futuro en decisiones gubernamentales que los afectan.",
                        html.Br(), html.Br(),
                        "– ",
                        html.Span("55.0%", style={"textDecoration": "underline", "backgroundColor": "yellow", "fontWeight": "bold"}), " cree que tendrá un ",
                        html.Span("alto", style={"fontWeight": "bold"}), " grado de participación.",
                        html.Br(),
                        "– ",
                        html.Span("37.5%", style={"textDecoration": "underline", "backgroundColor": "orange", "fontWeight": "bold"}), " espera participar ",
                        html.Span("moderadamente", style={"fontWeight": "bold"}), ".",
                        html.Br(),
                        "– ",
                        html.Span("5.0%", style={"textDecoration": "underline", "backgroundColor": "red", "fontWeight": "bold"}), " anticipa una ",
                        html.Span("baja", style={"fontWeight": "bold"}), " participación.",
                        html.Br(), html.Br(),
                        "Comparación con la participación actual",
                        html.Br(),
                        "En la gráfica del pre test sobre la participación actual, solo un ",
                        html.Span("14.3%", style={"textDecoration": "underline", "backgroundColor": "yellow"}), " mencionaba participar mucho en decisiones gubernamentales, mientras que un ",
                        html.Span("21.4%", style={"textDecoration": "underline", "backgroundColor": "red"}), " sentía que su participación era muy baja.",
                        html.Br(), html.Br(),
                        "Este gráfico refleja una mejora en las expectativas: más de la mitad espera un alto grado de participación en el futuro. Esto indica que las actividades y discusiones en la asamblea deliberativa generaron una mayor confianza y motivación para involucrarse en procesos de toma de decisiones."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans'
                    }),
                    width=12
                ),

                html.Div(
                    html.Iframe(
                        src='/assets/ParticipacionPos_0.html',
                        style={'width': '80%', 'height': '500px', 'border': 'none'}
                    ),
                    style={
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center',
                        'margin': '20px 0',
                        'width': '100%',
                    }
                ),
            ], style={
                'display': 'flex',
                'flexDirection': 'column',
                'alignItems': 'center',
                #'textAlign': 'center',
                'maxWidth': '1200px',
                'margin': '0 auto'
            }),

            html.Div([
                dbc.Col(
                    html.P([
                        "Antes de la asamblea, el ",
                        html.Span("16.7%", style={"textDecoration": "underline", "backgroundColor": "red", "fontWeight": "bold"}), " no confiaba en la Alcaldía y solo el ",
                        html.Span("11.9%", style={"textDecoration": "underline", "backgroundColor": "yellow", "fontWeight": "bold"}), " tenía mucha confianza.",
                        html.Br(),
                        "Después, la desconfianza bajó al ",
                        html.Span("9.8%", style={"textDecoration": "underline", "backgroundColor": "red", "fontWeight": "bold"}), " y la confianza aumentó al ",
                        html.Span("34.1%", style={"textDecoration": "underline", "backgroundColor": "yellow", "fontWeight": "bold"}), ".",
                        html.Br(), html.Br(),
                        "Si pasas el cursor por encima de cada sección, podrás ver el valor específico que votaron los asambleístas dentro de la escala."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans'
                    }),
                    width=12
                ),
                html.Div(
                    html.Iframe(
                        src='/assets/ParticipacionPos_1.html',
                        style={'width': '80%', 'height': '500px', 'border': 'none'}
                    ),
                    style={
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center',
                        'margin': '20px 0',
                        'width': '100%',
                    }
                ),
            ], style={
                'display': 'flex',
                'flexDirection': 'column',
                'alignItems': 'center',
                #'textAlign': 'center',
                'maxWidth': '1200px',
                'margin': '0 auto'
            }),

            html.Div([
                dbc.Col(
                    html.P([
                        "La mayoría de los asambleístas, el ",
                        html.Span("39.0%", style={"textDecoration": "underline", "backgroundColor": "brown", "fontWeight": "bold"}), " no sintió ninguna presión para estar de acuerdo con los demás. Un ",
                        html.Span("9.8%", style={"textDecoration": "underline", "backgroundColor": "orange", "fontWeight": "bold"}), " sintió algo de presión, mientras que solo el ",
                        html.Span("4.9%", style={"textDecoration": "underline", "backgroundColor": "yellow", "fontWeight": "bold"}), " sintió presión moderada y el ",
                        html.Span("2.4%", style={"textDecoration": "underline", "backgroundColor": "red", "fontWeight": "bold"}), " sintió presión alta.",
                        html.Br(), html.Br(),
                        "Esto sugiere que en general, el ambiente fue libre y respetuoso para expresar opiniones.",
                        html.Br(), html.Br(),
                        "Si pasas el cursor por encima de cada sección, podrás ver el valor específico que votaron los asambleístas dentro de la escala."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans'
                    }),
                    width=12
                ),
                html.Div(
                    html.Iframe(
                        src='/assets/ParticipacionPos_2.html',
                        style={'width': '80%', 'height': '500px', 'border': 'none'}
                    ),
                    style={
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center',
                        'margin': '20px 0',
                        'width': '100%',
                    }
                ),
            ], style={
                'display': 'flex',
                'flexDirection': 'column',
                'alignItems': 'center',
                #'textAlign': 'center',
                'maxWidth': '1200px',
                'margin': '0 auto'
            }),

            html.Div([
                dbc.Col(
                    html.P([
                        "En esta gráfica, todas las respuestas se concentraron en los valores más altos de una escala del 1 al 6. El ",
                        html.Span("61.9%", style={"textDecoration": "underline", "backgroundColor": "yellow", "fontWeight": "bold"}), " sintió una representación alta por parte de los participantes (valor ",
                        html.Span("6", style={"fontWeight": "bold"}), "). El ",
                        html.Span("31.0%", style={"textDecoration": "underline", "backgroundColor": "orange", "fontWeight": "bold"}), " se ubicó en un nivel de representación moderado (valor ",
                        html.Span("5", style={"fontWeight": "bold"}), "), mientras que solo el ",
                        html.Span("7.1%", style={"textDecoration": "underline", "backgroundColor": "red", "fontWeight": "bold"}), " se sintió menos representado (valor ",
                        html.Span("4", style={"fontWeight": "bold"}), ").",
                        html.Br(), html.Br(),
                        "Esto indica que, en general, los asambleístas se sintieron bien representados durante las deliberaciones."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans'
                    }),
                    width=12
                ),

                html.Div(
                    html.Iframe(
                        src='/assets/ParticipacionPos_4.html',
                        style={'width': '80%', 'height': '500px', 'border': 'none'}
                    ),
                    style={
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center',
                        'margin': '20px 0',
                        'width': '100%',
                    }
                ),
            ], style={
                'display': 'flex',
                'flexDirection': 'column',
                'alignItems': 'center',
                #'textAlign': 'center',
                'maxWidth': '1200px',
                'margin': '0 auto'
            }),

            html.Br(),

            html.Div([
                html.H3("Si sientes que algún grupo o sector de la sociedad no estuvo representado, ¿Qué grupo o grupos crees que faltaron?", style={'textAlign': 'center', 'fontFamily': 'Kensington', 'fontSize': '30px'}),
                dbc.Col(
                    html.P([
                        "Esta nube muestra los grupos que, según los participantes, no tuvieron suficiente representación durante el proceso deliberativo.",
                        html.Br(), html.Br(),
                        "Las palabras más destacadas son “",
                        html.Span("discapacidad", style={"fontWeight": "bold"}), "”, “",
                        html.Span("madres", style={"fontWeight": "bold"}), "”, “",
                        html.Span("pueblos étnicos", style={"fontWeight": "bold"}), "” y “",
                        html.Span("jóvenes", style={"fontWeight": "bold"}), "”. Esto refleja una preocupación por incluir a comunidades que pueden enfrentar barreras adicionales para participar.",
                        html.Br(), html.Br(),
                        "También se mencionan grupos como: ",
                        html.Br(), html.Br(),
                        "– “", html.Span("estudiantes", style={"fontWeight": "bold"}), "” y “",
                        html.Span("colegios", style={"fontWeight": "bold"}), "”.",
                        html.Br(),
                        "– “", html.Span("recicladores", style={"fontWeight": "bold"}), "” y “",
                        html.Span("migrantes", style={"fontWeight": "bold"}), "”, que evidencian la preocupación por trabajadores informales y personas en situación de movilidad."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans'
                    }),
                    width=12
                ),
                html.Div(
                    html.Img(
                        src='/assets/Parti6.png',
                        style={'width': '80%', 'height': 'auto', 'display': 'block'}
                    ),
                    style={
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center',
                        'margin': '20px 0',
                        'width': '100%',
                    }
                ),
            ], style={
                'display': 'flex',
                'flexDirection': 'column',
                'alignItems': 'center',
                #'textAlign': 'center',
                'maxWidth': '1200px',
                'margin': '0 auto'
            }),

            # Similar blocks for remaining visualizations...
        ])

    elif selected_subtab == "casa":

        return html.Div([
            html.Br(), html.Br(),
            html.H3("La Casa de la Confianza", style={'textAlign': 'center', 'fontSize': '30px', 'fontFamily': 'Kensington'}),  # Título centrado
            dbc.Col(
                html.P([
                    html.B("Casa de la Confianza"), " tuvo como objetivo identificar lo que podría ocurrir en futuras asambleas a través de la discusión y deliberación. Se utilizaron ",
                    html.B("9"), " fichas, cada una relacionada con diferentes espacios de un hogar. Los asambleístas ubicaron estas fichas según lo que esperaban de las siguientes asambleas, definiendo los actores involucrados en cada proceso y sus funciones. Algunos de los espacios clave fueron:",
                    html.Br(), html.Br(),
                    html.B("Comedor"), ": representó el espacio de toma de decisiones. Los asambleístas definieron quiénes debían participar en las decisiones y con qué frecuencia deberían tomarse. Además, señalaron las funciones específicas de cada actor en este proceso.",
                    html.Br(), html.Br(),
                    html.B("Estudio"), ": simbolizó el seguimiento y la evaluación. Se establecieron las entidades responsables de dar seguimiento a los acuerdos y evaluar su cumplimiento, detallando las tareas que cada actor debía realizar para garantizar el avance adecuado.",
                    html.Br(), html.Br(),
                    html.B("Televisor"), ": reflejó la divulgación. En este espacio, los asambleístas identificaron a los actores encargados de asegurar la transparencia y rendición de cuentas, explicando qué funciones debían cumplir para garantizar que toda la información fuera clara y accesible.",
                    html.Br(), html.Br(),
                    html.B("Sala"), ": representó el ejercicio de consulta. Aquí, se señalaron los procesos de participación y se identificaron a los actores encargados de promover el diálogo y asegurar que se escucharan todas las voces durante las asambleas."
                ], style={
                    'fontSize': '18px',
                    'maxWidth': '800px',
                    'marginLeft': 'auto',
                    'marginRight': 'auto',
                    'fontFamily': 'Museo Sans'
                }),
                width=12
            ),

            html.Div(
                html.Iframe(
                    src='/assets/CasitaXD.html',  # Enlace al archivo HTML
                    style={'width': '80%', 'height': '900px', 'border': 'none'}
                ),
                style={
                    'display': 'flex',  # Usamos flexbox
                    'justifyContent': 'center',  # Centra el iframe horizontalmente
                    'alignItems': 'center',  # Centra el iframe verticalmente
                    'margin': '20px 0',  # Añadir margen para separación entre elementos
                    'width': '100%',  # Asegura que el contenedor ocupe todo el ancho disponible
                }
            ),
        ], style={
            'display': 'flex',
            'flexDirection': 'column',
            'alignItems': 'center',  # Alineación centrada
            #'textAlign': 'center',
            'maxWidth': '2100px',  # Ancho máximo para evitar que se expandan demasiado en pantallas grandes
            'margin': '0 auto'  # Centra el contenido horizontalmente
        })

    elif selected_subtab == "termometro":

        return html.Div([
                # Contenedor para la Visualización 1
                html.Div([
                    html.Br(), html.Br(),
                    html.H3("Termómetro de la Deliberación", style={'textAlign': 'center', 'fontSize': '30px', 'fontFamily': 'Kensington'}),  # Título centrado
                    html.Br(),
                    dbc.Col(
                        html.P([
                            "Esta gráfica muestra la primera pregunta del termómetro de la deliberación sobre si los participantes estuvieron escuchando con atención las ideas de sus compañeros. La escala utilizada fue del 1 al 5, y las respuestas se concentraron únicamente en los niveles más altos: ",
                            html.Span("El 73.7%", style={"backgroundColor": "yellow", "color": "black", "fontWeight": "bold"}), " eligió el nivel 5, indicando un alto nivel de atención. ",
                            html.Span("El 15.8%", style={"backgroundColor": "orange", "color": "black", "fontWeight": "bold"}), " seleccionó el nivel 4. ",
                            html.Span("El 10.5%", style={"backgroundColor": "red", "color": "white", "fontWeight": "bold"}), " optó por el nivel 3.",
                            " Esto refleja una percepción general positiva respecto a la atención prestada durante la deliberación."
                        ], style={
                            'fontSize': '18px',
                            'maxWidth': '800px',
                            'marginLeft': 'auto',
                            'marginRight': 'auto',
                            'fontFamily': 'Museo Sans'
                        }),
                        width=12
                    ),
                    html.Div(
                        html.Iframe(
                            src='/assets/Termometro_0.html',  # Enlace al archivo HTML
                            style={'width': '80%', 'height': '500px', 'border': 'none'}
                        ),
                        style={
                            'display': 'flex',  # Usamos flexbox
                            'justifyContent': 'center',  # Centra el iframe horizontalmente
                            'alignItems': 'center',  # Centra el iframe verticalmente
                            'margin': '20px 0',  # Añadir margen para separación entre elementos
                            'width': '100%',  # Asegura que el contenedor ocupe todo el ancho disponible
                        }
                    ),
                ], style={
                    'display': 'flex',
                    'flexDirection': 'column',
                    'alignItems': 'center',  # Alineación centrada
                    #'textAlign': 'center',
                    'maxWidth': '1200px',  # Ancho máximo para evitar que se expandan demasiado en pantallas grandes
                    'margin': '0 auto'  # Centra el contenido horizontalmente
                }),

                # Repetimos la estructura para cada visualización
                html.Div([
                    dbc.Col(
                        html.P([
                            "Esta gráfica muestra las respuestas a la pregunta sobre si la participación de los asambleístas tuvo en cuenta la información recibida durante la semana de formación. La escala fue del 1 al 5, y los resultados se distribuyeron en los niveles más altos: ",
                            html.Span("El 47.4%", style={"backgroundColor": "yellow", "color": "black", "fontWeight": "bold"}), " eligió el nivel 5, reflejando un uso alto de la información recibida. ",
                            html.Span("El 31.6%", style={"backgroundColor": "orange", "color": "black", "fontWeight": "bold"}), " seleccionó el nivel 4. ",
                            html.Span("El 21.1%", style={"backgroundColor": "red", "color": "white", "fontWeight": "bold"}), " indicó el nivel 3.",
                            " Esto sugiere que, en general, la mayoría de los participantes integraron la información recibida en su participación."
                        ], style={
                            'fontSize': '18px',
                            'maxWidth': '800px',
                            'marginLeft': 'auto',
                            'marginRight': 'auto',
                            'fontFamily': 'Museo Sans'
                        }),
                        width=12
                    ),
                    html.Div(
                        html.Iframe(
                            src='/assets/Termometro_1.html',
                            style={'width': '80%', 'height': '500px', 'border': 'none'}
                        ),
                        style={
                            'display': 'flex',
                            'justifyContent': 'center',
                            'alignItems': 'center',
                            'margin': '20px 0',
                            'width': '100%',
                        }
                    ),
                ], style={
                    'display': 'flex',
                    'flexDirection': 'column',
                    'alignItems': 'center',
                    #'textAlign': 'center',
                    'maxWidth': '1200px',  # Ancho máximo
                    'margin': '0 auto'  # Centrado horizontal
                }),

                html.Div([
                    dbc.Col(
                        html.P([
                            "Esta gráfica muestra las respuestas a la pregunta sobre si los asambleístas permitieron que sus compañeros expusieran su punto de vista. La escala fue del 1 al 5, y los resultados se distribuyeron en los niveles más altos: ",
                            html.Span("El 84.2%", style={"backgroundColor": "yellow", "color": "black", "fontWeight": "bold"}), " eligió el nivel 5, indicando una alta disposición para escuchar puntos de vista ajenos. ",
                            html.Span("El 15.8%", style={"backgroundColor": "orange", "color": "black", "fontWeight": "bold"}), " seleccionó el nivel 4.",
                            " Esto refleja que una amplia mayoría de los participantes permitió que sus compañeros expresaran sus ideas durante la deliberación."
                        ], style={
                            'fontSize': '18px',
                            'maxWidth': '800px',
                            'marginLeft': 'auto',
                            'marginRight': 'auto',
                            'fontFamily': 'Museo Sans'
                        }),
                        width=12
                    ),

                    html.Div(
                        html.Iframe(
                            src='/assets/Termometro_2.html',
                            style={'width': '80%', 'height': '500px', 'border': 'none'}
                        ),
                        style={
                            'display': 'flex',
                            'justifyContent': 'center',
                            'alignItems': 'center',
                            'margin': '20px 0',
                            'width': '100%',
                        }
                    ),
                ], style={
                    'display': 'flex',
                    'flexDirection': 'column',
                    'alignItems': 'center',
                    #'textAlign': 'center',
                    'maxWidth': '1200px',  # Ancho máximo
                    'margin': '0 auto'  # Centrado horizontal
                }),

                html.Div([
                    dbc.Col(
                        html.P([
                            "Esta gráfica muestra las respuestas a la pregunta sobre si los asambleístas realizaron intervenciones cortas y claras para permitir que otros también pudieran hablar. La escala fue del 1 al 5, y los resultados se distribuyeron en los niveles más altos: ",
                            html.Span("El 63.2%", style={"backgroundColor": "yellow", "color": "black", "fontWeight": "bold"}), " seleccionó el nivel 5. ",
                            html.Span("El 26.3%", style={"backgroundColor": "orange", "color": "black", "fontWeight": "bold"}), " eligió el nivel 4. ",
                            html.Span("El 10.5%", style={"backgroundColor": "red", "color": "white", "fontWeight": "bold"}), " escogió el nivel 3.",
                            " Esto indica que una mayoría de los participantes considera que sus intervenciones permitieron el diálogo fluido de sus compañeros."
                        ], style={
                            'fontSize': '18px',
                            'maxWidth': '800px',
                            'marginLeft': 'auto',
                            'marginRight': 'auto',
                            'fontFamily': 'Museo Sans'
                        }),
                        width=12
                    ),

                    html.Div(
                        html.Iframe(
                            src='/assets/Termometro_3.html',
                            style={'width': '80%', 'height': '500px', 'border': 'none'}
                        ),
                        style={
                            'display': 'flex',
                            'justifyContent': 'center',
                            'alignItems': 'center',
                            'margin': '20px 0',
                            'width': '100%',
                        }
                    ),
                ], style={
                    'display': 'flex',
                    'flexDirection': 'column',
                    'alignItems': 'center',
                    #'textAlign': 'center',
                    'maxWidth': '1200px',  # Ancho máximo
                    'margin': '0 auto'  # Centrado horizontal
                }),

                html.Div([
                    dbc.Col(
                        html.P([
                            "Esta gráfica muestra las respuestas a la pregunta sobre si los asambleístas se pronunciaron de manera respetuosa sobre las ideas, opiniones y argumentos de sus compañeros. La escala utilizada fue del 1 al 5, y los resultados se distribuyeron principalmente en los niveles más altos: ",
                            html.Span("El 63.2%", style={"backgroundColor": "yellow", "color": "black", "fontWeight": "bold"}), " seleccionó el nivel 5. ",
                            html.Span("El 21.1%", style={"backgroundColor": "orange", "color": "black", "fontWeight": "bold"}), " eligió el nivel 4. ",
                            html.Span("El 10.5%", style={"backgroundColor": "red", "color": "white", "fontWeight": "bold"}), " escogió el nivel 3. ",
                            html.Span("El 5.3%", style={"backgroundColor": "brown", "color": "black", "fontWeight": "bold"}), " seleccionó el nivel 2.",
                            " Esto sugiere que una gran mayoría percibió que sus intervenciones fueron respetuosas durante el proceso deliberativo."
                        ], style={
                            'fontSize': '18px',
                            'maxWidth': '800px',
                            'marginLeft': 'auto',
                            'marginRight': 'auto',
                            'fontFamily': 'Museo Sans'
                        }),
                        width=12
                    ),
                    html.Div(
                        html.Iframe(
                            src='/assets/Termometro_4.html',
                            style={'width': '80%', 'height': '500px', 'border': 'none'}
                        ),
                        style={
                            'display': 'flex',
                            'justifyContent': 'center',
                            'alignItems': 'center',
                            'margin': '20px 0',
                            'width': '100%',
                        }
                    ),
                ], style={
                    'display': 'flex',
                    'flexDirection': 'column',
                    'alignItems': 'center',
                    #'textAlign': 'center',
                    'maxWidth': '1200px',  # Ancho máximo
                    'margin': '0 auto'  # Centrado horizontal
                }),

                html.Div([
                    dbc.Col(
                        html.P([
                            "Esta gráfica muestra las respuestas a la pregunta sobre si los asambleístas al intervenir hablaban de las ideas de sus compañeros o solo de sus propias ideas. La escala utilizada fue del 1 al 5, y las respuestas se concentraron en los niveles más altos: ",
                            html.Span("El 42.1%", style={"backgroundColor": "yellow", "color": "black", "fontWeight": "bold"}), " seleccionó el nivel 5. ",
                            html.Span("El 36.8%", style={"backgroundColor": "orange", "color": "black", "fontWeight": "bold"}), " eligió el nivel 4. ",
                            html.Span("El 10.5%", style={"backgroundColor": "red", "color": "white", "fontWeight": "bold"}), " escogió el nivel 3. ",
                            html.Span("El 5.3%", style={"backgroundColor": "brown", "color": "black", "fontWeight": "bold"}), " seleccionó el nivel 2. ",
                            "Otro ", html.Span("5.3%", style={"backgroundColor": "brown", "color": "black", "fontWeight": "bold"}), " seleccionó el nivel 1.",
                            " Esto sugiere que una mayoría de los participantes mencionaba tanto sus propias ideas como las de sus compañeros al intervenir."
                        ], style={
                            'fontSize': '18px',
                            'maxWidth': '800px',
                            'marginLeft': 'auto',
                            'marginRight': 'auto',
                            'fontFamily': 'Museo Sans'
                        }),
                        width=12
                    ),

                    html.Div(
                        html.Iframe(
                            src='/assets/Termometro_5.html',
                            style={'width': '80%', 'height': '500px', 'border': 'none'}
                        ),
                        style={
                            'display': 'flex',
                            'justifyContent': 'center',
                            'alignItems': 'center',
                            'margin': '20px 0',
                            'width': '100%',
                        }
                    ),
                ], style={
                    'display': 'flex',
                    'flexDirection': 'column',
                    'alignItems': 'center',
                    #'textAlign': 'center',
                    'maxWidth': '1200px',  # Ancho máximo
                    'margin': '0 auto'  # Centrado horizontal
                }),

                html.Div([
                    dbc.Col(
                        html.P([
                            "Esta gráfica muestra la disposición de los participantes para cambiar de posición durante el diálogo. La escala utilizada fue del 1 al 5, y las respuestas se distribuyeron en los niveles más altos: ",
                            html.Span("El 52.6%", style={"backgroundColor": "yellow", "color": "black", "fontWeight": "bold"}), " seleccionó el nivel 5. ",
                            html.Span("El 15.8%", style={"backgroundColor": "orange", "color": "black", "fontWeight": "bold"}), " eligió el nivel 4. ",
                            html.Span("El 26.3%", style={"backgroundColor": "red", "color": "white", "fontWeight": "bold"}), " escogió el nivel 3. ",
                            html.Span("El 5.3%", style={"backgroundColor": "brown", "color": "black", "fontWeight": "bold"}), " seleccionó el nivel 2.",
                            " Estos resultados indican que una mayoría de los participantes estaba abierta a cambiar su posición durante el diálogo."
                        ], style={
                            'fontSize': '18px',
                            'maxWidth': '800px',
                            'marginLeft': 'auto',
                            'marginRight': 'auto',
                            'fontFamily': 'Museo Sans'
                        }),
                        width=12
                    ),


                    html.Div(
                        html.Iframe(
                            src='/assets/Termometro_6.html',
                            style={'width': '80%', 'height': '500px', 'border': 'none'}
                        ),
                        style={
                            'display': 'flex',
                            'justifyContent': 'center',
                            'alignItems': 'center',
                            'margin': '20px 0',
                            'width': '100%',
                        }
                    ),
                ], style={
                    'display': 'flex',
                    'flexDirection': 'column',
                    'alignItems': 'center',
                    #'textAlign': 'center',
                    'maxWidth': '1200px',  # Ancho máximo
                    'margin': '0 auto'  # Centrado horizontal
                }),

                html.Div([
                    dbc.Col(
                        html.P([
                            "Esta gráfica muestra la distribución de los puntajes totales obtenidos por cada participante al sumar sus respuestas en todas las gráficas anteriores. ",
                            "La puntuación final de los participantes oscila entre 23 y 35 puntos. ",
                            "Se observa que la mayor concentración de puntajes está entre 31 y 34, con una frecuencia máxima de 3 participantes en esos valores. ",
                            "Valores más bajos como 23 y 25 son menos frecuentes. ",
                            "Esto refleja que la mayoría de los participantes puntuaron en rangos medios y altos, indicando una participación consistente y positiva en las actividades evaluadas."
                        ], style={
                            'fontSize': '18px',
                            'maxWidth': '800px',
                            'marginLeft': 'auto',
                            'marginRight': 'auto',
                            'fontFamily': 'Museo Sans'
                        }),
                        width=12
                    ),
                    html.Div(
                        html.Iframe(
                            src='/assets/TermometroTotal.html',
                            style={'width': '80%', 'height': '500px', 'border': 'none'}
                        ),
                        style={
                            'display': 'flex',
                            'justifyContent': 'center',
                            'alignItems': 'center',
                            'margin': '20px 0',
                            'width': '100%',
                        }
                    ),
                ], style={
                    'display': 'flex',
                    'flexDirection': 'column',
                    'alignItems': 'center',
                    #'textAlign': 'center',
                    'maxWidth': '1200px',  # Ancho máximo
                    'margin': '0 auto'  # Centrado horizontal
                }),
            ])

    else:
        return html.Div("Contenido no encontrado")


if __name__ == '__main__':
    #port = int(os.environ.get("PORT", 8050))  # Render provee el puerto en la variable PORT
    app.run_server(host="0.0.0.0", port=8080, debug=False)
