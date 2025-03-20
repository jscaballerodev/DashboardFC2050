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
    title='Fundacion2050',
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
                html.H2([
                    "¿Qué es la Meta Asamblea Ciudadana #SumemosVoces?"
                ], style={
                    'fontSize': '24px',
                    'fontWeight': 'bold',
                    'textAlign': 'center',
                    'marginTop': '20px',
                    'fontFamily': 'Museo Sans'
                }),
                width=12
            )
        ]),

        dbc.Row([
            dbc.Col(
                html.P([
                    html.Br(),
                    "En octubre de 2024, Bogotá dio un paso hacia una democracia más deliberativa. Desde la Secretaría de Planeación, en alianza con Fundación Corona y Extituto de Política Abierta, se realizó la primera Meta Asamblea Ciudadana, un espacio para debatir, reflexionar y construir las bases de los futuros Ciclos Deliberativos que se desarrollarán en la ciudad.",
                    html.Br(), html.Br(),
                    "Durante cuatro días, del 18 al 21 de octubre, en el piso 25 del Edificio Atrio, 60 ciudadanos seleccionados de manera aleatoria bajo criterios diferenciales se reunieron para responder una pregunta clave:",
                    html.Br()
                ], style={
                    'fontSize': '18px',
                    'maxWidth': '800px',
                    'marginLeft': 'auto',
                    'marginRight': 'auto',
                    'fontFamily': 'Museo Sans',
                    'textAlign': 'justify'
                }),
                width=12
            )
        ], justify='center', style={'marginTop': '20px'}),

        dbc.Row([
            dbc.Col(
                html.H2([
                    "¿Cómo deben funcionar las futuras Asambleas Ciudadanas Deliberativas?"
                ], style={
                    'fontSize': '24px',
                    'fontWeight': 'bold',
                    'textAlign': 'center',
                    'marginTop': '20px',
                    'fontFamily': 'Museo Sans'
                }),
                width=12
            )
        ]),

        dbc.Row([
            dbc.Col(
                html.P([
                    html.Br(),
                    "Los debates, propuestas y acuerdos alcanzados en la Meta Asamblea 2024 serán la base para los próximos tres (3) Ciclos Deliberativos que Bogotá implementará entre 2025 y 2027, en cumplimiento del ",
                    html.B("Plan Distrital de Desarrollo 'Bogotá Camina Segura 2024-2028'"), "."
                ], style={
                    'fontSize': '18px',
                    'maxWidth': '800px',
                    'marginLeft': 'auto',
                    'marginRight': 'auto',
                    'fontFamily': 'Museo Sans',
                    'textAlign': 'justify'
                }),
                width=12
            ),
            dbc.Col(
                html.P([
                    html.B("¿Qué sigue?", style={'fontSize': '20px'}),
                    html.Br(), html.Br(),
                    "● La reglamentación de estos ciclos.", html.Br(),
                    "● La construcción de su decreto.", html.Br(),
                    "● Nuevos espacios de participación."
                ], style={
                    'fontSize': '18px',
                    'fontFamily': 'Museo Sans',
                    'maxWidth': '800px',
                    'marginLeft': 'auto',
                    'marginRight': 'auto',
                    'textAlign': 'justify'
                }),
                width=12
            ),

            dbc.Row([
                dbc.Col(
                    html.H2([
                        "Explora los resultados en este tablero digital"
                    ], style={
                        'fontSize': '24px',
                        'fontWeight': 'bold',
                        'textAlign': 'center',
                        'marginTop': '20px',
                        'fontFamily': 'Museo Sans'
                    }),
                    width=12
                )
            ]),

            dbc.Col(
                html.P([
                    html.Br(),
                    "Las actividades, encuestas y deliberaciones de la Meta Asamblea 2024 quedaron registradas y pueden explorarse en este ",
                    html.B("tablero digital"), ", un insumo clave para seguir sumando voces y fortaleciendo la participación ciudadana.",
                    html.Br(), html.Br(),
                    html.B("El Tablero digital"), " es una herramienta en línea que te permite ver y entender la información recogida durante los cuatro (4) días de actividades y está diseñado para que los miembros de la alianza puedan consultar la información de manera más sencilla y clara de cara a los procesos a desarrollar. En este espacio encontrarás lo siguiente:",
                    html.Br(), html.Br(),
                    "● ", html.B("Resultados"), ": los principales hallazgos y conclusiones del proceso desarrollado.", html.Br(),
                    "● ", html.B("Encuestas"), ": resultados de las preguntas que se hicieron a los participantes durante las actividades.", html.Br(),
                    "● ", html.B("Observaciones"), ": comentarios y notas adicionales que hizo el equipo encargado de analizar las actividades.", html.Br(),
                    "● ", html.B("Análisis de centralidad"), ": resultados obtenidos al revisar las grabaciones de las discusiones en dos grupos de trabajo.", html.Br(),
                    "● ", html.B("Análisis de sentimientos"), ": muestra lo que sintieron los participantes durante una actividad específica y nos ayuda a entender cómo reaccionaron cuando se habló de temas públicos.", html.Br(),
                    "● ", html.B("Productos"), ": resultados de actividades especiales como la 'Casa de la Confianza' y el 'Termómetro de la Confianza'.", html.Br(),
                    "Este tablero te ayudará a encontrar y entender toda esta información de forma fácil y ordenada."
                ], style={
                    'fontSize': '18px',
                    'fontFamily': 'Museo Sans',
                    'maxWidth': '800px',
                    'marginLeft': 'auto',
                    'marginRight': 'auto',
                    'textAlign': 'justify'
                }),
                width=12
            )
        ], justify='center', style={'marginTop': '20px'}),

        # Tabs centrados en una fila
        dbc.Col(
            dcc.Tabs(id='graph-tabs', value='ALL', children=[
                dcc.Tab(label='Resultados', value='Resultados', style={**tab_style['idle'], 'color': 'white'},
                        selected_style={**tab_style['active'], 'color': 'white'}),

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

        dbc.Row([
            dbc.Col(
                html.P([
                    "Si desea obtener más detalles sobre la información presentada en este tablero digital, puede comunicarse al correo electrónico: ",
                    html.Strong("andres.pinzon@fundacioncolombia2050.org.")
                ], style={
                    'fontSize': '18px',
                    'maxWidth': '800px',
                    'marginLeft': 'auto',
                    'marginRight': 'auto',
                    'fontFamily': 'Museo Sans',
                    'textAlign': 'center'  # Centrar el texto
                }),
                width=12
            )
        ], justify='center', style={'marginTop': '20px'})
,


    ], style={'padding': '0px', 'maxWidth': '100%'})  # Asegura que el contenedor ocupe el 100% del ancho
], style={'backgroundColor': 'white', 'minHeight': '100vh'})

## Callback para el primer archivo
#@app.callback(
#     Output("download-file1", "data"),
#    Input("btn_file1", "n_clicks"),
#    prevent_initial_call=True,
#)
#def download_file1(n_clicks):
#    return dcc.send_file("./Encuestas.xlsx")
#
# Callback para el segundo archivo
#@app.callback(
#    Output("download-file3", "data"),
#    Input("btn_file3", "n_clicks"),
#    prevent_initial_call=True,
#)
#def download_file3(n_clicks):
#    return dcc.send_file("./consolidated_transcription.txt")
#
#@app.callback(
#    Output("download-file2", "data"),
#    Input("btn_file2", "n_clicks"),
#    prevent_initial_call=True,
#)
#def download_file2(n_clicks):
#    return dcc.send_file("./ResumenObserva.xlsx")
#
#@app.callback(
#    Output("download-file4", "data"),
#    Input("btn_file4", "n_clicks"),
#    prevent_initial_call=True,
#)
#def download_file4(n_clicks):
#    return dcc.send_file("./data_sts.xlsx")
#
#@app.callback(
#    Output("download-file5", "data"),
#    Input("btn_file5", "n_clicks"),
#    prevent_initial_call=True,
#)
#def download_file5(n_clicks):
#    return dcc.send_file("./Productos.xlsx")


@app.callback(
    Output('tabs-content', 'children'),
    [Input('graph-tabs', 'value')]
)

def update_tab(tab):

    if tab == "Resultados":

        return html.Div([
            html.Br(),
            dbc.Row([
                dbc.Col(html.H3("Resultados", style={'textAlign': 'center', 'fontSize': '30px', 'fontFamily': 'Kensington'}), width=12),
            ], justify='center', style={'width': '100%', 'display': 'flex', 'justifyContent': 'center'}),

            # Pestañas internas
            # Pestañas internas
            dcc.Tabs(
                id='subtabs',
                value='metodologia',  # Valor inicial
                children=[
                    dcc.Tab(label='Metodología', value='metodologia', style={**tab_style['idle'], 'color': 'white'}, selected_style={**tab_style['active'], 'color': 'white'}),
                    dcc.Tab(label='Resultados', value='resultados', style={**tab_style['idle'], 'color': 'white'}, selected_style={**tab_style['active'], 'color': 'white'}),
                    dcc.Tab(label='Recomendaciones', value='recomendaciones', style={**tab_style['idle'], 'color': 'white'}, selected_style={**tab_style['active'], 'color': 'white'})
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

    elif tab == 'Encuestas':

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
                dbc.Col(
                    html.P([ "En esta sección, se presentan algunas sistematizaciones de las actividades realizadas y de los productos derivados de las mismas. Este documento tiene como objetivo recopilar y organizar la información clave sobre el desarrollo de cada actividad, permitiendo identificar aprendizajes, buenas prácticas y aspectos a mejorar. A través de esta sistematización, se busca proporcionar una mirada estructurada al proceso, facilitando su análisis y generando insumos que contribuyan a futuras implementaciones."],
                    style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans',
                        'textAlign': 'justify'
                    }),
                    width=12
                )
            ], justify='center', style={'marginTop': '20px'}),

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

                dbc.Row([
                dbc.Col(
                    html.P([
                        "Las observaciones fueron un proceso realizado por un equipo que hizo parte del desarrollo de la Meta-Asamblea, con el propósito de identificar elementos clave del proceso deliberativo y aportar información valiosa para la mejora de futuros ciclos. Este ejercicio permitió recopilar impresiones desde una perspectiva externa y neutral, sin un rol activo en la dinámica de las discusiones, lo que garantizó un análisis independiente de los distintos aspectos del desarrollo de las sesiones.",
                        html.Br(), html.Br(),
                        "El propósito principal de este documento es brindar a los miembros de la alianza insumos detallados sobre aquellos elementos que el equipo de observadores consideró significativos en cada una de las sesiones realizadas. Se busca, así, que la alianza pueda identificar aspectos esenciales para la consolidación y optimización del modelo deliberativo implementado.",
                        html.Br(), html.Br(),
                        "El ejercicio de observación permitió capturar elementos clave de la dinámica de las actividades, evaluando factores como:",
                        html.Br(),
                        "● ", html.Span("La interacción entre participantes", style={'fontWeight': 'bold'}), ", analizando cómo se dio el diálogo, la escucha activa y la construcción colectiva dentro de los grupos.",
                        html.Br(),
                        "● ", html.Span("El nivel de compromiso y participación", style={'fontWeight': 'bold'}), ", observando la disposición de los asambleístas para intervenir, argumentar y colaborar en la deliberación.",
                        html.Br(),
                        "● ", html.Span("La claridad de los objetivos y procesos", style={'fontWeight': 'bold'}), ", evaluando si los participantes comprendieron las instrucciones, la metodología y los propósitos de cada sesión.",
                        html.Br(),
                        "● ", html.Span("Aspectos logísticos y organizativos", style={'fontWeight': 'bold'}), ", identificando aciertos y oportunidades de mejora en la gestión de tiempos, recursos y condiciones de trabajo.",
                        html.Br(), html.Br(),
                        "A continuación, se detalla cada una de estas observaciones, resaltando los logros alcanzados y las oportunidades de mejora identificadas para fortalecer el proceso en futuras deliberaciones.",
                        html.Br(),
                        "Si desea conocer el recuento condensado de observaciones, lo invitamos a consultar el siguiente enlace:",
                        html.Br(),
                        html.A("[Analisis Obervaciones de la Meta Asamblea]", href="https://drive.google.com/drive/folders/1siKj9Cxan1Ht6tQwBtyJZaI1Jm2gyVSn", target="_blank", style={'color': 'blue', 'textDecoration': 'underline'})
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans',
                        'textAlign': 'justify'
                    }),
                    width=12
                )
            ], justify='center', style={'marginTop': '20px'}),


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

                dbc.Row([
                dbc.Col(
                    html.P([
                        "Esta representación visual muestra cómo se desarrolló la discusión durante una hora en una de las comisiones de la ", html.B("Casa"), " de la Confianza. Es un piloto de un ", html.B("análisis"), " de centralidad que realizamos para entender cómo los asambleístas estaban ocupando el tiempo en una actividad determinada y qué temas recibieron mayor atención durante la deliberación.",
                        html.Br(), html.Br(),
                        "Cada elemento del flujo se define por varios aspectos clave:",
                        html.Ul([
                            html.Li(["",html.B("Color"), ": cada nodo tiene un color que indica la categoría temática o la naturaleza del contenido abordado. Por ejemplo, el rojo representa temas de ", html.B("acciones"), " y planes concretos, mientras que el amarillo y el marrón reflejan otros aspectos como Definición de temas futuros y Seguimiento y evaluación."])
                        ]),
                        html.Ul([
                            html.Li(["", html.B("Nombre"), ": cada nodo identifica el tema central y su propósito dentro del debate. Ejemplos de temas tratados son:"])
                        ]),
                        html.Ul([
                            html.Li(["", html.B("Acciones"), ": definir acciones específicas a seguir."])
                        ]),
                        html.Ul([
                            html.Li(["", html.B("Divulgación"), ": compartir los resultados de la deliberación con todos los participantes."])
                        ]),
                        html.Ul([
                            html.Li(["", html.B("Tiempo"), ": cada nodo muestra el tiempo dedicado a discutir el tema, considerando su complejidad y prioridad. Por ejemplo: Divulgación de resultados (14 min)"])
                        ]),
                        html.Ul([
                            html.Li(["", html.B("Relación"), ": las líneas conectan los nodos, mostrando cómo una discusión llevó a otra y evidenciando el flujo lógico e interdependencia entre los temas."])
                        ]),
                        html.Ul([
                            html.Li(["", html.B("Tamaño"), ": el tamaño indica la importancia relativa del tema y la cantidad de actores involucrados en su desarrollo."])
                        ]),
                        "Dentro de las principales conclusiones las puedes encontrar a continuación:"
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans',
                        'textAlign': 'justify'
                    }),
                    width=12
                )
            ], justify='center', style={'marginTop': '20px'}),

                dbc.Row([
                dbc.Col(
                    html.P([
                        html.B("1. Diferencias en los tiempos asignados"), html.Br(),
                        html.B("Comisión 1"), html.Br(),
                        "Los tiempos son más uniformes (9 a 14 minutos) y relativamente cortos. Esto favorece una discusión más dinámica, pero puede limitar la profundidad del debate en temas clave como \"divulgación\" o \"participación de autoridades\"",
                        html.Br(), html.Br(),
                        html.B("Comisión 2"), html.Br(),
                        "Los tiempos son más amplios y variados (17 a 27 minutos), lo que permite discusiones más detalladas. Sin embargo, esta extensión podría llevar a desgaste o pérdida de enfoque.",
                        html.Br(), html.Br(),
                        html.B("2. Propuestas de mejora"), html.Br(),
                        html.Ul([
                            html.Li([html.B("Diferenciar tiempos"), " según el tamaño de los nodos y la complejidad de sus relaciones"]),
                            html.Ul([
                                html.Li("En nodos grandes o con múltiples conexiones (p. Ej., \"seguimiento y evaluación\" en Comisión 1 o \"metáfora de la casa\" en Comisión 2), asignar más tiempo para garantizar que los asambleístas puedan explorar todas las aristas.")
                            ]),
                            html.Li([html.B("Incluir pausas estratégicas"), " para evitar fatiga, incorporar pausas cortas entre nodos grandes o particularmente intensivos en discusión. Esto mantiene la energía del grupo."]),
                            html.Li([html.B("Pruebas piloto"), " (como la presente): Simular una deliberación para ajustar los tiempos según las dinámicas del grupo y el contenido. Esto permitirá prever cuellos de botella."])
                        ]),
                        html.Br(),
                        html.B("3. Establecer un marco flexible"), html.Br(),
                        "Permitir redistribuir tiempos en función de la participación activa.", html.Br(),
                        "De esta forma se asignan los nodos más grandes a aquellos temas de interés, por parte de la Asamblea, abriendo el marco de la discusión en torno a los temas que consideran más prioritarios."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans',
                        'textAlign': 'justify'
                    }),
                    width=12
                )
            ], justify='center', style={'marginTop': '20px'}),

                dbc.Row([
                dbc.Col(
                    html.P([
                        "Si deseas conocer el informe completo en donde se detalla la metodología, el análisis y las principales recomendaciones. Ingresa al siguiente enlace: ",
                        html.A("[Analisis Centralidad del Debate de la Meta Asamblea]", href="https://docs.google.com/document/d/1G5AVR51U08QJz8oZ2VCw7OPjKEfFQcVR/edit?tab=t.0", target="_blank")
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans',
                        'textAlign': 'justify'
                    }),
                    width=12
                )
            ], justify='center', style={'marginTop': '20px'}),

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

                dbc.Row([
                dbc.Col(
                    html.P([
                        "Esta gráfica muestra el balance de los sentimientos percibidos por los asambleístas cuando se abordaron temas relacionados con lo público. Utilizando el método Ruler, los sentimientos se categorizaron en cuatro colores:",
                        html.Br(), html.Br(),
                        "- ", html.Span("Amarillo", style={'backgroundColor': 'yellow', 'color': 'black'}), ": Sentimientos positivos con mucha energía.",
                        html.Br(),
                        "- ", html.Span("Verde", style={'backgroundColor': 'green', 'color': 'black'}), ": Sentimientos positivos con baja energía.",
                        html.Br(),
                        "- ", html.Span("Rojo", style={'backgroundColor': 'red', 'color': 'black'}), ": Sentimientos negativos con alta energía.",
                        html.Br(),
                        "- ", html.Span("Azul", style={'backgroundColor': 'blue', 'color': 'black'}), ": Sentimientos negativos con baja energía.",
                        html.Br(), html.Br(),
                        "Esta visualización permite identificar y comprender mejor las emociones predominantes en los asambleístas durante la actividad. Las conclusiones principales del ejercicio son las siguientes:",
                        html.Br(), html.Br(),
                        "- Las personas asocian el ciclo de la participación con sentimientos que demandan importancia y energía (independientemente sean más agradables o menos agradables). No asocian la práctica a sentimientos de baja energía.",
                        html.Br(),
                        "- La mayor proporción de los comentarios que hacían los asambleístas durante la actividad iban dirigidos a extremos del plano. Es decir, o se encontraban muy optimistas o muy frustrados/molestos, sobre las experiencias relacionadas con el ciclo de la participación.",
                        html.Br(),
                        "- Hubo una alta proporción de personas que comentaron elementos que se asocian con el cuadrante de agrado y baja energía (pensativos, satisfechos, tranquilos), un elemento a resaltar que rompe con los supuestos de agrado y molestia.",
                        html.Br(),
                        "De igual manera, en relación con los otros instrumentos implementados durante los cuatro (4) días, también se permite concluir:",
                        html.Br(),
                        "- La participación activa genera alta implicación emocional: las emociones asociadas al ciclo de la participación tienden a demandar un nivel elevado de energía, ya sea en la forma de entusiasmo o frustración. Esto muestra que las personas se involucran profundamente en estos procesos, lo cual puede ser una señal de su percepción de importancia y compromiso con los temas tratados, sin embargo, es riesgo al momento de tomar decisiones.",
                        html.Br(),
                        "- Los extremos emocionales dominan el discurso: los comentarios tienden a polarizarse entre emociones positivas intensas (optimismo) o negativas intensas (frustración). Esto sugiere que los participantes experimentan una conexión fuerte con el proceso, pero que el diseño o las dinámicas del ciclo podrían influir en estas respuestas extremas. Identificar las causas de estos extremos podría ayudar a moderar las experiencias negativas.",
                        html.Br(),
                        "- La baja energía agradable como un espacio atípico pero relevante: aunque menos frecuente, una proporción significativa de participantes reportó emociones como tranquilidad, satisfacción o reflexión, que son agradables, pero de baja energía. Este hallazgo rompe con la suposición de que solo las emociones intensas caracterizan la participación, destacando que algunos individuos encuentran en estos espacios un sentido de serenidad o contemplación. Esto podría indicar que ciertos elementos del diseño de la actividad promueven una experiencia más introspectiva."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans',
                        'textAlign': 'justify'
                    }),
                    width=12
                )
            ], justify='center', style={'marginTop': '20px'}),

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
            dbc.Row([
            dbc.Col(
                html.P([
                    "Esta sección presenta una visión general de todas las habilidades evaluadas en los participantes antes y después de las actividades. Estos datos fueron recopilados a partir de tres (3) instrumentos aplicados a los asambleístas durante los días de deliberación. A través de un análisis comparativo (gráfica que verán a continuación), se puede identificar cómo cambiaron las percepciones y habilidades en distintos ámbitos. La visualización permite tener un panorama completo del progreso general logrado durante el proceso.",
                    html.Br(), html.Br(),
                    "Esta gráfica de radar compara la percepción de los asambleístas en distintos aspectos ",
                    html.B(html.U("antes (línea roja)"), style={'color': 'red'}),
                    " y ",
                    html.B(html.U("después (línea amarilla)"), style={'color': 'darkgoldenrod'}),
                    " de las actividades. Se presentan en la gráfica ocho (8) dimensiones: siete (7) de ellas medidas en un máximo de ",
                    html.B("seis (6) puntos"), ": confianza en la Alcaldía, confianza en el proceso, confianza en la participación, confianza en el público, participación en la asamblea, participación en la ciudad y participación en decisiones públicas. Y una adicional (autoevaluación), medida en un máximo de ",
                    html.B("10 puntos"), ". En cada una de las áreas, encontrarás tres (3) datos."
                ], style={
                    'fontSize': '18px',
                    'maxWidth': '800px',
                    'marginLeft': 'auto',
                    'marginRight': 'auto',
                    'fontFamily': 'Museo Sans',
                    'textAlign': 'justify'
                }),
                width=12
            ),
            dbc.Col(
                html.P([
                    "● ", html.B("Pre"), ": que hace referencia al valor promedio de respuesta frente a esa categoría obtenida en la primera medición.", html.Br(),
                    "● ", html.B("Pos"), ": que hace referencia al valor promedio de respuesta frente a esa categoría obtenida en la segunda o tercera medición según corresponda.", html.Br(),
                    "● ", html.B("Delta"), ": que hace referencia al valor del cambio porcentual, positivo o negativo según corresponda el caso, entre las mediciones."
                ], style={
                    'fontSize': '18px',
                    'fontFamily': 'Museo Sans',
                    'maxWidth': '800px',
                    'marginLeft': 'auto',
                    'marginRight': 'auto',
                    'textAlign': 'justify'
                }),
                width=12
            ),
            dbc.Col(
                html.P([
                    "Se observa una mejora general en la mayoría de las dimensiones. Recuerda que los valores máximos que fueron descritos en párrafos anteriores, son equivalentes con la métrica de calificación. Es decir, siendo 1 muy negativo, y 6 o 10, dependiendo del caso, muy positivo. Las áreas con mayores incrementos son ",
                    html.B("autoevaluación, participación en la ciudad y confianza en la Alcaldía"), "."
                ], style={
                    'fontSize': '18px',
                    'fontFamily': 'Museo Sans',
                    'maxWidth': '800px',
                    'marginLeft': 'auto',
                    'marginRight': 'auto',
                    'textAlign': 'justify'
                }),
                width=12
            )
        ], justify='center', style={'marginTop': '20px'}),

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

        dbc.Row([
            dbc.Col(
                html.P([
                    "En esta sección se muestra cómo los participantes valoraron sus propias habilidades y competencias tras el proceso deliberativo. La autoevaluación refleja el nivel de confianza que los asambleístas tienen en sí mismos en áreas clave como argumentar, reflexionar, debatir y decidir. Esto permite identificar los cambios en su percepción personal de sus capacidades."], style={
                    'fontSize': '18px',
                    'maxWidth': '800px',
                    'marginLeft': 'auto',
                    'marginRight': 'auto',
                    'fontFamily': 'Museo Sans',
                    'textAlign': 'justify'
                }),
                width=12
            )
        ], justify='center', style={'marginTop': '20px'}),


        dbc.Row([
        dbc.Col(
            html.P([
                "Esta gráfica en forma de radar compara las habilidades de los asambleístas (", html.Strong("antes"), " (", html.Span("línea roja", style={'backgroundColor': 'red', 'color': 'white'}), " y ", html.Strong("después"), " ", html.Span("línea amarilla", style={'backgroundColor': 'yellow', 'color': 'black'}), "). Se evaluaron siete habilidades: ",
                html.Strong("reflexionar"), ", ", html.Strong("argumentar"), ", ", html.Strong("contraargumentar"), ", ", html.Strong("discutir"), ", ", html.Strong("evaluar"), ", ", html.Strong("decidir"), " y ", html.Strong("cambiar de opinión"), ".",
                html.Br(),
                "En todas las habilidades se observa una mejora tras la actividad. La mayor diferencia se aprecia en ", html.Strong("reflexionar"), " y ", html.Strong("argumentar"), ", donde el puntaje aumenta notablemente en la evaluación posterior."], style={
                'fontSize': '18px',
                'maxWidth': '800px',
                'marginLeft': 'auto',
                'marginRight': 'auto',
                'fontFamily': 'Museo Sans',
                'textAlign': 'justify'
            }),
            width=12
        )
    ], justify='center', style={'marginTop': '20px'}),
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
        dbc.Row([
        dbc.Col(
            html.P([
                "Esta gráfica muestra cómo cambió la percepción de los asambleístas sobre qué tan hábiles se sienten para reflexionar detenidamente sobre diferentes aspectos de un tema. En el gráfico, cada sección representa un valor en una escala del 1 al 10 (donde 1 es poco y 10 es mucho). El número indica cuántas personas votaron por ese valor, y el porcentaje muestra qué proporción representan. La comparación entre el ",
                html.B("Pre"), " y el ", html.B("Pos"), " revela un cambio positivo.",
                html.Br(), html.Br(),
                "Antes de las actividades, ",
                html.Span("33.3%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}),
                " se sentían muy hábiles para reflexionar (valor 10). Después, esta cifra subió a ",
                html.Span("44.7%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}), ". También aumentaron las respuestas en valores intermedios, lo que indica una ",
                html.B("mejora"), " general en esta habilidad."
            ], style={
                'fontSize': '18px',
                'maxWidth': '800px',
                'marginLeft': 'auto',
                'marginRight': 'auto',
                'fontFamily': 'Museo Sans',
                'textAlign': 'justify'
            }),
            width=12
        ),
        dbc.Col(
            html.P([
                "Además, si pasas el cursor por encima de cada sección, podrás ver el valor que votaron los asambleístas dentro de la escala. Al ser una gráfica de proporciones, si te sitúas en cada uno de los bloques, te saldrán los siguientes datos:",
                html.Br(), html.Br(),
                "● ", html.B("Valor"), ": que hace referencia a la selección que los asambleístas hicieron en una escala del 1 al 10 (donde 1 es poco y 10 es mucho) en función de la pregunta.", html.Br(),
                "● ", html.B("Proporción"), ": hace referencia a, de la totalidad de asambleístas que contestaron a la pregunta, cuál fue el porcentaje que seleccionó ese valor.", html.Br(),
                "● ", html.B("Cantidad"), ": hace referencia al número de asambleístas que eligieron esa respuesta."
            ], style={
                'fontSize': '18px',
                'fontFamily': 'Museo Sans',
                'maxWidth': '800px',
                'marginLeft': 'auto',
                'marginRight': 'auto',
                'textAlign': 'justify'
            }),
            width=12
        )
    ], justify='center', style={'marginTop': '20px'}),
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
        dbc.Row([
        dbc.Col(
            html.P([
                "Esta gráfica muestra cómo cambió la percepción de los asambleístas sobre qué tan hábiles se sienten para presentar razones a favor de una opción o postura. En el gráfico, cada sección representa un valor en una escala del 1 al 10 (donde 1 es poco y 10 es mucho). El número indica cuántas personas votaron por ese valor, y el porcentaje muestra qué proporción representan. Dentro la gráfica, si te sitúas en cada uno de los rectángulos, encontrarás estos elementos:",
                html.Br(), html.Br(),
                "La comparación entre el ", html.B("Pre"), " y el ", html.B("Pos"), " revela una mejora en esta habilidad. Antes de las actividades, ",
                html.Span("21.4%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}),
                " se sentían muy hábiles para argumentar (valor 10). Después, esta cifra subió a ",
                html.Span("28.9%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}), ". También se observa un aumento en los valores intermedios, como el valor 9, que pasó de ",
                html.Span("28.6%", style={'backgroundColor': 'orange', 'color': 'white', 'fontWeight': 'bold'}), " a ",
                html.Span("39.5%", style={'backgroundColor': 'orange', 'color': 'white', 'fontWeight': 'bold'}), "."
            ], style={
                'fontSize': '18px',
                'maxWidth': '800px',
                'marginLeft': 'auto',
                'marginRight': 'auto',
                'fontFamily': 'Museo Sans',
                'textAlign': 'justify'
            }),
            width=12
        ),
        dbc.Col(
            html.P([
                "Además, si pasas el cursor por encima de cada sección, podrás ver el valor específico que votaron los asambleístas dentro de la escala. Al ser una gráfica de proporciones, si te sitúas en cada uno de los bloques, te saldrán los siguientes datos:",
                html.Br(), html.Br(),
                "● ", html.B("Valor"), ": que hace referencia a la selección que los asambleístas hicieron en una escala del 1 al 10 (donde 1 es poco y 10 es mucho) en función de la pregunta.", html.Br(),
                "● ", html.B("Proporción"), ": hace referencia a, de la totalidad de asambleístas que contestaron a la pregunta, cuál fue el porcentaje que seleccionó ese valor.", html.Br(),
                "● ", html.B("Cantidad"), ": hace referencia al número de asambleístas que eligieron esa respuesta."
            ], style={
                'fontSize': '18px',
                'fontFamily': 'Museo Sans',
                'maxWidth': '800px',
                'marginLeft': 'auto',
                'marginRight': 'auto',
                'textAlign': 'justify'
            }),
            width=12
        )
    ], justify='center', style={'marginTop': '20px'}),
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
        dbc.Row([
        dbc.Col(
            html.P([
                "Esta gráfica muestra cómo cambiaron las proporciones de asambleístas que se sienten hábiles para presentar razones en contra de una postura, incluyendo la suya. En el gráfico, cada sección representa un valor en una escala del 1 al 10 (donde 1 es poco y 10 es mucho). El número indica cuántas personas votaron por ese valor, y el porcentaje muestra qué proporción representan.",
                html.Br(), html.Br(),
                "Antes de las actividades, ",
                html.Span("11.9%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}),
                " se consideraba muy hábil para contraargumentar (valor 10). Después, esta cifra aumentó al ",
                html.Span("26.3%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}), ". También se observa una disminución en los niveles intermedios: el ",
                html.Span("38.1%", style={'backgroundColor': 'orange', 'color': 'white', 'fontWeight': 'bold'}), " que eligió el valor 9 bajó al ",
                html.Span("28.9%", style={'backgroundColor': 'orange', 'color': 'white', 'fontWeight': 'bold'}), "."
            ], style={
                'fontSize': '18px',
                'maxWidth': '800px',
                'marginLeft': 'auto',
                'marginRight': 'auto',
                'fontFamily': 'Museo Sans',
                'textAlign': 'justify'
            }),
            width=12
        ),
        dbc.Col(
            html.P([
                "En general, se ve una mejora en la habilidad para contraargumentar, con más personas sintiéndose en los niveles más altos después de las actividades. Si pasas el cursor por encima de cada sección, podrás ver el valor específico que votaron los asambleístas dentro de la escala. Al ser una gráfica de proporciones, si te sitúas en cada uno de los bloques, te saldrán los siguientes datos:",
                html.Br(), html.Br(),
                "● ", html.B("Valor"), ": que hace referencia a la selección que los asambleístas hicieron en una escala del 1 al 10 (donde 1 es poco y 10 es mucho) en función de la pregunta.", html.Br(),
                "● ", html.B("Proporción"), ": hace referencia a, de la totalidad de asambleístas que contestaron a la pregunta, cuál fue el porcentaje que seleccionó ese valor.", html.Br(),
                "● ", html.B("Cantidad"), ": hace referencia al número de asambleístas que eligieron esa respuesta."
            ], style={
                'fontSize': '18px',
                'fontFamily': 'Museo Sans',
                'maxWidth': '800px',
                'marginLeft': 'auto',
                'marginRight': 'auto',
                'textAlign': 'justify'
            }),
            width=12
        )
    ], justify='center', style={'marginTop': '20px'}),
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
        dbc.Row([
        dbc.Col(
            html.P([
                "Esta gráfica muestra cómo cambiaron las proporciones de asambleístas que se sienten hábiles para conversar con otras personas sobre un asunto, intercambiando ideas y puntos de vista. En el gráfico, cada sección representa un valor en una escala del 1 al 10 (donde 1 es poco y 10 es mucho). El número indica cuántas personas votaron por ese valor, y el porcentaje muestra qué proporción representan.",
                html.Br(), html.Br(),
                "Antes de las actividades, ",
                html.Span("28.6%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}),
                " se consideraba muy hábil para discutir (valor 10). Después, esta cifra aumentó al ",
                html.Span("42.1%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}), ". También hubo un aumento en el nivel 9, que pasó del ",
                html.Span("19.0%", style={'backgroundColor': 'orange', 'color': 'white', 'fontWeight': 'bold'}), " al ",
                html.Span("31.6%", style={'backgroundColor': 'orange', 'color': 'white', 'fontWeight': 'bold'}), "."
            ], style={
                'fontSize': '18px',
                'maxWidth': '800px',
                'marginLeft': 'auto',
                'marginRight': 'auto',
                'fontFamily': 'Museo Sans',
                'textAlign': 'justify'
            }),
            width=12
        ),
        dbc.Col(
            html.P([
                "En general, se observa una mejora significativa en la habilidad para discutir, con más asambleístas ubicándose en los niveles más altos después de las actividades. Si pasas el cursor por encima de cada sección, podrás ver el valor específico que votaron los asambleístas dentro de la escala. Al ser una gráfica de proporciones, si te sitúas en cada uno de los bloques, te saldrán los siguientes datos:",
                html.Br(), html.Br(),
                "● ", html.B("Valor"), ": que hace referencia a la selección que los asambleístas hicieron en una escala del 1 al 10 (donde 1 es poco y 10 es mucho) en función de la pregunta.", html.Br(),
                "● ", html.B("Proporción"), ": hace referencia a, de la totalidad de asambleístas que contestaron a la pregunta, cuál fue el porcentaje que seleccionó ese valor.", html.Br(),
                "● ", html.B("Cantidad"), ": hace referencia al número de asambleístas que eligieron esa respuesta."
            ], style={
                'fontSize': '18px',
                'fontFamily': 'Museo Sans',
                'maxWidth': '800px',
                'marginLeft': 'auto',
                'marginRight': 'auto',
                'textAlign': 'justify'
            }),
            width=12
        )
    ], justify='center', style={'marginTop': '20px'}),
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
        dbc.Row([
        dbc.Col(
            html.P([
                "Esta gráfica muestra cómo cambiaron las proporciones de asambleístas que se sienten hábiles para analizar diferentes opciones o consecuencias de una decisión. En el gráfico, cada sección representa un valor en una escala del 1 al 10 (donde 1 es poco y 10 es mucho). El número indica cuántas personas votaron por ese valor, y el porcentaje muestra qué proporción representan.",
                html.Br(), html.Br(),
                "Antes de las actividades, ",
                html.Span("26.2%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}),
                " se sentía muy hábil para evaluar (valor 10). Después, esta proporción bajó ligeramente al ",
                html.Span("24.3%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}), ". Sin embargo, el nivel 9 mostró una mejora, pasando del ",
                html.Span("16.7%", style={'backgroundColor': 'orange', 'color': 'white', 'fontWeight': 'bold'}), " al ",
                html.Span("37.8%", style={'backgroundColor': 'orange', 'color': 'white', 'fontWeight': 'bold'}), "."
            ], style={
                'fontSize': '18px',
                'maxWidth': '800px',
                'marginLeft': 'auto',
                'marginRight': 'auto',
                'fontFamily': 'Museo Sans',
                'textAlign': 'justify'
            }),
            width=12
        ),
        dbc.Col(
            html.P([
                "En general, se observa una mayor concentración de respuestas en los niveles altos después de las actividades. Si pasas el cursor por encima de cada sección, podrás ver el valor específico que votaron los asambleístas dentro de la escala. Al ser una gráfica de proporciones, si te sitúas en cada uno de los bloques, te saldrán los siguientes datos:",
                html.Br(), html.Br(),
                "● ", html.B("Valor"), ": que hace referencia a la selección que los asambleístas hicieron en una escala del 1 al 10 (donde 1 es poco y 10 es mucho) en función de la pregunta.", html.Br(),
                "● ", html.B("Proporción"), ": hace referencia a, de la totalidad de asambleístas que contestaron a la pregunta, cuál fue el porcentaje que seleccionó ese valor.", html.Br(),
                "● ", html.B("Cantidad"), ": hace referencia al número de asambleístas que eligieron esa respuesta."
            ], style={
                'fontSize': '18px',
                'fontFamily': 'Museo Sans',
                'maxWidth': '800px',
                'marginLeft': 'auto',
                'marginRight': 'auto',
                'textAlign': 'justify'
            }),
            width=12
        )
    ], justify='center', style={'marginTop': '20px'}),
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
        dbc.Row([
        dbc.Col(
            html.P([
                "Esta gráfica muestra cómo cambiaron las proporciones de asambleístas que se sienten hábiles para elegir o determinar un curso de acción o posición después de reflexionar. En el gráfico, cada sección representa un valor en una escala del 1 al 10 (donde 1 es poco y 10 es mucho). El número indica cuántas personas votaron por ese valor, y el porcentaje muestra qué proporción representan.",
                html.Br(), html.Br(),
                "Antes de las actividades, ",
                html.Span("28.6%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}),
                " se consideraba muy hábil para decidir (valor 10). Después, esta proporción bajó ligeramente al ",
                html.Span("26.3%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}), ". Sin embargo, en el nivel 9, hubo una mejora notable, pasando del ",
                html.Span("14.3%", style={'backgroundColor': 'orange', 'color': 'white', 'fontWeight': 'bold'}), " al ",
                html.Span("34.2%", style={'backgroundColor': 'orange', 'color': 'white', 'fontWeight': 'bold'}), "."
            ], style={
                'fontSize': '18px',
                'maxWidth': '800px',
                'marginLeft': 'auto',
                'marginRight': 'auto',
                'fontFamily': 'Museo Sans',
                'textAlign': 'justify'
            }),
            width=12
        ),
        dbc.Col(
            html.P([
                "En general, se observa una mayor distribución de respuestas en los niveles altos después de las actividades. Si pasas el cursor por encima de cada sección, podrás ver el valor específico que votaron los asambleístas dentro de la escala. Al ser una gráfica de proporciones, si te sitúas en cada uno de los bloques, te saldrán los siguientes datos:",
                html.Br(), html.Br(),
                "● ", html.B("Valor"), ": que hace referencia a la selección que los asambleístas hicieron en una escala del 1 al 10 (donde 1 es poco y 10 es mucho) en función de la pregunta.", html.Br(),
                "● ", html.B("Proporción"), ": hace referencia a, de la totalidad de asambleístas que contestaron a la pregunta, cuál fue el porcentaje que seleccionó ese valor.", html.Br(),
                "● ", html.B("Cantidad"), ": hace referencia al número de asambleístas que eligieron esa respuesta."
            ], style={
                'fontSize': '18px',
                'fontFamily': 'Museo Sans',
                'maxWidth': '800px',
                'marginLeft': 'auto',
                'marginRight': 'auto',
                'textAlign': 'justify'
            }),
            width=12
        )
    ], justify='center', style={'marginTop': '20px'}),
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
        dbc.Row([
        dbc.Col(
            html.P([
                "Esta gráfica muestra cómo cambiaron las proporciones de asambleístas que consideran probable cambiar de opinión si otra persona presenta un argumento convincente. En el gráfico, cada sección representa un valor en una escala del 1 al 10 (donde 1 es poco y 10 es mucho). El número indica cuántas personas votaron por ese valor, y el porcentaje muestra qué proporción representan.",
                html.Br(), html.Br(),
                "Antes de las actividades, ",
                html.Span("14.6%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}),
                " se sentía muy dispuesto a cambiar de opinión (valor 10). Después, esta proporción subió al ",
                html.Span("26.3%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}), ". También hubo un aumento en el nivel 9, pasando del ",
                html.Span("29.3%", style={'backgroundColor': 'orange', 'color': 'white', 'fontWeight': 'bold'}), " al ",
                html.Span("34.2%", style={'backgroundColor': 'orange', 'color': 'white', 'fontWeight': 'bold'}), "."
            ], style={
                'fontSize': '18px',
                'maxWidth': '800px',
                'marginLeft': 'auto',
                'marginRight': 'auto',
                'fontFamily': 'Museo Sans',
                'textAlign': 'justify'
            }),
            width=12
        ),
        dbc.Col(
            html.P([
                "En general, se observa una mayor apertura a cambiar de opinión tras escuchar argumentos sólidos. Si pasas el cursor por encima de cada sección, podrás ver el valor específico que votaron los asambleístas dentro de la escala. Al ser una gráfica de proporciones, si te sitúas en cada uno de los bloques, te saldrán los siguientes datos:",
                html.Br(), html.Br(),
                "● ", html.B("Valor"), ": que hace referencia a la selección que los asambleístas hicieron en una escala del 1 al 10 (donde 1 es poco y 10 es mucho) en función de la pregunta.", html.Br(),
                "● ", html.B("Proporción"), ": hace referencia a, de la totalidad de asambleístas que contestaron a la pregunta, cuál fue el porcentaje que seleccionó ese valor.", html.Br(),
                "● ", html.B("Cantidad"), ": hace referencia al número de asambleístas que eligieron esa respuesta."
            ], style={
                'fontSize': '18px',
                'fontFamily': 'Museo Sans',
                'maxWidth': '800px',
                'marginLeft': 'auto',
                'marginRight': 'auto',
                'textAlign': 'justify'
            }),
            width=12
        )
    ], justify='center', style={'marginTop': '20px'}),

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
            dbc.Row([
                dbc.Col(
                    html.P([
                        "Esta sección desglosa los resultados de la autoevaluación según el género de los participantes. Al observar las diferencias entre hombres y mujeres en sus percepciones de habilidades, se pueden identificar patrones específicos y áreas en las que puede ser necesario aplicar enfoques diferenciados para potenciar las capacidades de cada grupo."], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans',
                        'textAlign': 'justify'
                    }),
                    width=12
                )
            ], justify='center', style={'marginTop': '20px'}),



            dbc.Row([
            dbc.Col(
                html.P([
                    "Esta gráfica muestra cómo cambiaron las proporciones de hombres y mujeres que se sienten hábiles para reflexionar detenidamente sobre diferentes aspectos de un tema. En el gráfico, cada sección representa un valor en una escala del 1 al 10 (donde 1 es poco y 10 es mucho). El número indica cuántas personas votaron por ese valor, y el porcentaje muestra qué proporción representan.",
                    html.Br(), html.Br(),
                    "En el caso de los ", html.B("hombres"), ", el porcentaje más alto en el nivel 10 pasó del ",
                    html.Span("33.3%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}),
                    " en el pre al ",
                    html.Span("23.1%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}),
                    " en el pos.",
                    html.Br(), html.Br(),
                    "Para las ", html.B("mujeres"), ", el porcentaje en el nivel 10 aumentó del ",
                    html.Span("33.3%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}),
                    " en el pre al ",
                    html.Span("58.3%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}),
                    " en el pos."
                ], style={
                    'fontSize': '18px',
                    'maxWidth': '800px',
                    'marginLeft': 'auto',
                    'marginRight': 'auto',
                    'fontFamily': 'Museo Sans',
                    'textAlign': 'justify'
                }),
                width=12
            ),
            dbc.Col(
                html.P([
                    "En general, se observa una mejora en las mujeres y una ligera disminución en los hombres. Si pasas el cursor por encima de cada sección, podrás ver el valor específico que votaron los asambleístas dentro de la escala. Al ser una gráfica de proporciones, si te sitúas en cada uno de los bloques, te saldrán los siguientes datos:",
                    html.Br(), html.Br(),
                    "● ", html.B("Valor"), ": que hace referencia a la selección que los asambleístas hicieron en una escala del 1 al 10 (donde 1 es poco y 10 es mucho) en función de la pregunta.", html.Br(),
                    "● ", html.B("Proporción"), ": hace referencia a, de la totalidad de asambleístas que contestaron a la pregunta, cuál fue el porcentaje que seleccionó ese valor.", html.Br(),
                    "● ", html.B("Cantidad"), ": hace referencia al número de asambleístas que eligieron esa respuesta."
                ], style={
                    'fontSize': '18px',
                    'fontFamily': 'Museo Sans',
                    'maxWidth': '800px',
                    'marginLeft': 'auto',
                    'marginRight': 'auto',
                    'textAlign': 'justify'
                }),
                width=12
            )
        ], justify='center', style={'marginTop': '20px'}),

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
                dbc.Row([
                dbc.Col(
                    html.P([
                        "Esta gráfica muestra cómo cambiaron las proporciones de hombres y mujeres que se sienten hábiles para presentar razones a favor de una opción o postura. En el gráfico, cada sección representa un valor en una escala del 1 al 10 (donde 1 es poco y 10 es mucho). El número indica cuántas personas votaron por ese valor, y el porcentaje muestra qué proporción representan.",
                        html.Br(), html.Br(),
                        "En el caso de los ", html.B("hombres"), ", el porcentaje en el nivel más alto (valor 10) se mantuvo estable, con un ",
                        html.Span("13.3%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}),
                        " en el pre y un ",
                        html.Span("15.4%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}),
                        " en el pos.",
                        html.Br(), html.Br(),
                        "Para las ", html.B("mujeres"), ", el porcentaje en el nivel 10 pasó del ",
                        html.Span("25.9%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}),
                        " en el pre al ",
                        html.Span("37.5%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}),
                        " en el pos. También aumentó el nivel 9, que subió del ",
                        html.Span("11.1%", style={'backgroundColor': 'orange', 'color': 'white', 'fontWeight': 'bold'}),
                        " al ",
                        html.Span("41.7%", style={'backgroundColor': 'orange', 'color': 'white', 'fontWeight': 'bold'}),
                        "."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans',
                        'textAlign': 'justify'
                    }),
                    width=12
                ),
                dbc.Col(
                    html.P([
                        "En general, se observa una mejora significativa en las mujeres. Si pasas el cursor por encima de cada sección, podrás ver el valor específico que votaron los asambleístas dentro de la escala. Al ser una gráfica de proporciones, si te sitúas en cada uno de los bloques, te saldrán los siguientes datos:",
                        html.Br(), html.Br(),
                        "● ", html.B("Valor"), ": que hace referencia a la selección que los asambleístas hicieron en una escala del 1 al 10 (donde 1 es poco y 10 es mucho) en función de la pregunta.", html.Br(),
                        "● ", html.B("Proporción"), ": hace referencia a, de la totalidad de asambleístas que contestaron a la pregunta, cuál fue el porcentaje que seleccionó ese valor.", html.Br(),
                        "● ", html.B("Cantidad"), ": hace referencia al número de asambleístas que eligieron esa respuesta."
                    ], style={
                        'fontSize': '18px',
                        'fontFamily': 'Museo Sans',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'textAlign': 'justify'
                    }),
                    width=12
                )
            ], justify='center', style={'marginTop': '20px'}),

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
                dbc.Row([
                dbc.Col(
                    html.P([
                        "Esta gráfica muestra cómo cambiaron las proporciones de hombres y mujeres que se sienten hábiles para presentar razones en contra de una opción o postura, incluyendo la suya. En el gráfico, cada sección representa un valor en una escala del 1 al 10 (donde 1 es poco y 10 es mucho). El número indica cuántas personas votaron por ese valor, y el porcentaje muestra qué proporción representan.",
                        html.Br(), html.Br(),
                        "En el caso de los ", html.B("hombres"), ", el porcentaje en el nivel más alto (valor 10) aumentó ligeramente del ",
                        html.Span("13.3%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}),
                        " en el pre al ",
                        html.Span("23.1%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}),
                        " en el pos.",
                        html.Br(), html.Br(),
                        "Para las ", html.B("mujeres"), ", el porcentaje en el nivel 10 pasó del ",
                        html.Span("11.1%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}),
                        " en el pre al ",
                        html.Span("29.2%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}),
                        " en el pos. También hubo un aumento en el nivel 9, que subió del ",
                        html.Span("33.3%", style={'backgroundColor': 'orange', 'color': 'white', 'fontWeight': 'bold'}),
                        " al ",
                        html.Span("33.3%", style={'backgroundColor': 'orange', 'color': 'white', 'fontWeight': 'bold'}),
                        "."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans',
                        'textAlign': 'justify'
                    }),
                    width=12
                ),
                dbc.Col(
                    html.P([
                        "Si pasas el cursor por encima de cada sección, podrás ver el valor específico que votaron los asambleístas dentro de la escala. Al ser una gráfica de proporciones, si te sitúas en cada uno de los bloques, te saldrán los siguientes datos:",
                        html.Br(), html.Br(),
                        "● ", html.B("Valor"), ": que hace referencia a la selección que los asambleístas hicieron en una escala del 1 al 10 (donde 1 es poco y 10 es mucho) en función de la pregunta.", html.Br(),
                        "● ", html.B("Proporción"), ": hace referencia a, de la totalidad de asambleístas que contestaron a la pregunta, cuál fue el porcentaje que seleccionó ese valor.", html.Br(),
                        "● ", html.B("Cantidad"), ": hace referencia al número de asambleístas que eligieron esa respuesta."
                    ], style={
                        'fontSize': '18px',
                        'fontFamily': 'Museo Sans',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'textAlign': 'justify'
                    }),
                    width=12
                )
            ], justify='center', style={'marginTop': '20px'}),
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
                dbc.Row([
                dbc.Col(
                    html.P([
                        "Esta gráfica muestra cómo cambiaron las proporciones de hombres y mujeres que se sienten hábiles para conversar con otras personas, intercambiando ideas y puntos de vista. En el gráfico, cada sección representa un valor en una escala del 1 al 10 (donde 1 es poco y 10 es mucho). El número indica cuántas personas votaron por ese valor, y el porcentaje muestra qué proporción representan.",
                        html.Br(), html.Br(),
                        "En el caso de los ", html.B("hombres"), ", el nivel más alto (valor 10) aumentó del ",
                        html.Span("20.0%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}),
                        " en el pre al ",
                        html.Span("30.8%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}),
                        " en el pos.",
                        html.Br(), html.Br(),
                        "Para las ", html.B("mujeres"), ", el nivel 10 pasó del ",
                        html.Span("33.3%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}),
                        " en el pre al ",
                        html.Span("50.0%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}),
                        " en el pos. También se observa una disminución en los niveles intermedios, lo que indica una mayor concentración de respuestas en los niveles más altos."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans',
                        'textAlign': 'justify'
                    }),
                    width=12
                ),
                dbc.Col(
                    html.P([
                        "Si pasas el cursor por encima de cada sección, podrás ver el valor específico que votaron los asambleístas dentro de la escala. Al ser una gráfica de proporciones, si te sitúas en cada uno de los bloques, te saldrán los siguientes datos:",
                        html.Br(), html.Br(),
                        "● ", html.B("Valor"), ": que hace referencia a la selección que los asambleístas hicieron en una escala del 1 al 10 (donde 1 es poco y 10 es mucho) en función de la pregunta.", html.Br(),
                        "● ", html.B("Proporción"), ": hace referencia a, de la totalidad de asambleístas que contestaron a la pregunta, cuál fue el porcentaje que seleccionó ese valor.", html.Br(),
                        "● ", html.B("Cantidad"), ": hace referencia al número de asambleístas que eligieron esa respuesta."
                    ], style={
                        'fontSize': '18px',
                        'fontFamily': 'Museo Sans',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'textAlign': 'justify'
                    }),
                    width=12
                )
            ], justify='center', style={'marginTop': '20px'}),

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
                dbc.Row([
                dbc.Col(
                    html.P([
                        "Esta gráfica muestra cómo cambiaron las proporciones de hombres y mujeres que se sienten hábiles para analizar diferentes opciones o consecuencias de una decisión. En el gráfico, cada sección representa un valor en una escala del 1 al 10 (donde 1 es poco y 10 es mucho). El número indica cuántas personas votaron por ese valor, y el porcentaje muestra qué proporción representan.",
                        html.Br(), html.Br(),
                        "En el caso de los ", html.B("hombres"), ", el porcentaje en el nivel más alto (valor 10) bajó del ",
                        html.Span("26.7%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}),
                        " en el pre al ",
                        html.Span("23.1%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}),
                        " en el pos. También se observa un aumento en el nivel 9, que pasó del ",
                        html.Span("33.3%", style={'backgroundColor': 'orange', 'color': 'white', 'fontWeight': 'bold'}),
                        " al ",
                        html.Span("46.2%", style={'backgroundColor': 'orange', 'color': 'white', 'fontWeight': 'bold'}),
                        ".",
                        html.Br(), html.Br(),
                        "Para las ", html.B("mujeres"), ", el nivel 10 disminuyó ligeramente del ",
                        html.Span("25.9%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}),
                        " en el pre al ",
                        html.Span("26.1%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}),
                        " en el pos. Sin embargo, el nivel 9 mostró un aumento del ",
                        html.Span("14.8%", style={'backgroundColor': 'orange', 'color': 'white', 'fontWeight': 'bold'}),
                        " al ",
                        html.Span("34.8%", style={'backgroundColor': 'orange', 'color': 'white', 'fontWeight': 'bold'}),
                        ". En general, se observa una tendencia positiva hacia niveles más altos después de las actividades."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans',
                        'textAlign': 'justify'
                    }),
                    width=12
                ),
                dbc.Col(
                    html.P([
                        "Si pasas el cursor por encima de cada sección, podrás ver el valor específico que votaron los asambleístas dentro de la escala. Al ser una gráfica de proporciones, si te sitúas en cada uno de los bloques, te saldrán los siguientes datos:",
                        html.Br(), html.Br(),
                        "● ", html.B("Valor"), ": que hace referencia a la selección que los asambleístas hicieron en una escala del 1 al 10 (donde 1 es poco y 10 es mucho) en función de la pregunta.", html.Br(),
                        "● ", html.B("Proporción"), ": hace referencia a, de la totalidad de asambleístas que contestaron a la pregunta, cuál fue el porcentaje que seleccionó ese valor.", html.Br(),
                        "● ", html.B("Cantidad"), ": hace referencia al número de asambleístas que eligieron esa respuesta."
                    ], style={
                        'fontSize': '18px',
                        'fontFamily': 'Museo Sans',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'textAlign': 'justify'
                    }),
                    width=12
                )
            ], justify='center', style={'marginTop': '20px'}),

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
                dbc.Row([
                dbc.Col(
                    html.P([
                        "Esta gráfica muestra cómo cambiaron las proporciones de hombres y mujeres que se sienten hábiles para elegir o determinar un curso de acción o posición tras reflexionar. En el gráfico, cada sección representa un valor en una escala del 1 al 10 (donde 1 es poco y 10 es mucho). El número indica cuántas personas votaron por ese valor, y el porcentaje muestra qué proporción representan.",
                        html.Br(), html.Br(),
                        "En el caso de los ", html.B("hombres"), ", el porcentaje en el nivel más alto (valor 10) pasó del ",
                        html.Span("26.7%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}),
                        " en el pre al ",
                        html.Span("23.1%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}),
                        " en el pos. También hubo un aumento en el nivel 9, del ",
                        html.Span("13.3%", style={'backgroundColor': 'orange', 'color': 'white', 'fontWeight': 'bold'}),
                        " al ",
                        html.Span("23.1%", style={'backgroundColor': 'orange', 'color': 'white', 'fontWeight': 'bold'}),
                        ".",
                        html.Br(), html.Br(),
                        "Para las ", html.B("mujeres"), ", el porcentaje en el nivel 10 se mantuvo casi igual, del ",
                        html.Span("29.6%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}),
                        " en el pre al ",
                        html.Span("29.2%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}),
                        " en el pos. Sin embargo, el nivel 9 mostró un aumento significativo, pasando del ",
                        html.Span("14.8%", style={'backgroundColor': 'orange', 'color': 'white', 'fontWeight': 'bold'}),
                        " al ",
                        html.Span("37.5%", style={'backgroundColor': 'orange', 'color': 'white', 'fontWeight': 'bold'}),
                        "."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans',
                        'textAlign': 'justify'
                    }),
                    width=12
                ),
                dbc.Col(
                    html.P([
                        "Si pasas el cursor por encima de cada sección, podrás ver el valor específico que votaron los asambleístas dentro de la escala. Al ser una gráfica de proporciones, si te sitúcs en cada uno de los bloques, te saldrán los siguientes datos:",
                        html.Br(), html.Br(),
                        "● ", html.B("Valor"), ": que hace referencia a la selección que los asambleístas hicieron en una escala del 1 al 10 (donde 1 es poco y 10 es mucho) en función de la pregunta.", html.Br(),
                        "● ", html.B("Proporción"), ": hace referencia a, de la totalidad de asambleístas que contestaron a la pregunta, cuál fue el porcentaje que seleccionó ese valor.", html.Br(),
                        "● ", html.B("Cantidad"), ": hace referencia al número de asambleístas que eligieron esa respuesta."
                    ], style={
                        'fontSize': '18px',
                        'fontFamily': 'Museo Sans',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'textAlign': 'justify'
                    }),
                    width=12
                )
            ], justify='center', style={'marginTop': '20px'})
,

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
                dbc.Row([
                dbc.Col(
                    html.P([
                        "Esta gráfica muestra cómo cambiaron las proporciones de hombres y mujeres que consideran probable cambiar de opinión si otra persona presenta un argumento convincente. En el gráfico, cada sección representa un valor en una escala del 1 al 10 (donde 1 es poco y 10 es mucho). El número indica cuántas personas votaron por ese valor, y el porcentaje muestra qué proporción representan.",
                        html.Br(), html.Br(),
                        "En el caso de los ", html.B("hombres"), ", el porcentaje en el nivel más alto (valor 10) disminuyó del ",
                        html.Span("20.0%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}),
                        " en el pre al ",
                        html.Span("15.4%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}),
                        " en el pos. Para las ", html.B("mujeres"), ", el nivel 10 aumentó del ",
                        html.Span("11.5%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}),
                        " en el pre al ",
                        html.Span("29.2%", style={'backgroundColor': 'red', 'color': 'white', 'fontWeight': 'bold'}),
                        " en el pos. También hubo un aumento en el nivel 9, pasando del ",
                        html.Span("26.9%", style={'backgroundColor': 'orange', 'color': 'white', 'fontWeight': 'bold'}),
                        " al ",
                        html.Span("37.5%", style={'backgroundColor': 'orange', 'color': 'white', 'fontWeight': 'bold'}),
                        "."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans',
                        'textAlign': 'justify'
                    }),
                    width=12
                ),
                dbc.Col(
                    html.P([
                        "Si pasas el cursor por encima de cada sección, podrás ver el valor específico que votaron los asambleístas dentro de la escala. Al ser una gráfica de proporciones, si te sitúcs en cada uno de los bloques, te saldrán los siguientes datos:",
                        html.Br(), html.Br(),
                        "● ", html.B("Valor"), ": que hace referencia a la selección que los asambleístas hicieron en una escala del 1 al 10 (donde 1 es poco y 10 es mucho) en función de la pregunta.", html.Br(),
                        "● ", html.B("Proporción"), ": hace referencia a, de la totalidad de asambleístas que contestaron a la pregunta, cuál fue el porcentaje que seleccionó ese valor.", html.Br(),
                        "● ", html.B("Cantidad"), ": hace referencia al número de asambleístas que eligieron esa respuesta.", html.Br(), html.Br(),
                        html.B("Nota aclaratoria"), ": En el ", html.B("pos"), ", se presenta una variación en el modelo de graficación debido a que algunos participantes no completaron la encuesta por motivos desconocidos. Esto afectó el proceso de graficación, generando una inconsistencia en los valores más bajos y en la distribución general de las proporciones."
                    ], style={
                        'fontSize': '18px',
                        'fontFamily': 'Museo Sans',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'textAlign': 'justify'
                    }),
                    width=12
                )
            ], justify='center', style={'marginTop': '20px'})
,

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
            dbc.Row([
                dbc.Col(
                    html.P([
                        "En esta sección se analizan los niveles de confianza de los participantes en diversas áreas relacionadas con las instituciones, el proceso deliberativo y sus propios compañeros. La confianza es un indicador clave para medir el impacto del proceso en términos de credibilidad y disposición para participar en decisiones públicas."
                        ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans',
                        'textAlign': 'justify'
                    }),
                    width=12
                )
            ], justify='center', style={'marginTop': '20px'}),

            html.Div([
                html.H3("PRE: ¿Qué sientes cuando te hablan de lo público?", style={'textAlign': 'center', 'fontFamily': 'Kensington', 'fontSize': '30px'}),
                dbc.Row([
                dbc.Col(
                    html.P([
                        "Esta nube de palabras representa las percepciones iniciales de los participantes sobre la confianza en las instituciones antes del proceso deliberativo. El tamaño de cada palabra indica la frecuencia con la que fue mencionada: cuanto más grande aparece, más veces fue repetida en las respuestas.",
                        html.Br(),
                        "● ", html.Strong("Las palabras más destacadas"), ", como ", html.Strong("público"), ", ", html.Strong("persona"), ", ", html.Strong("confianza"), " e ", html.Strong("interés"), ", reflejan un enfoque en el individuo y la idea de lo público, junto con una preocupación por el interés y el papel de las personas en la participación ciudadana.",
                        html.Br(),
                        "● También aparecen términos como ", html.Strong("frustración"), ", ", html.Strong("desconfianza"), " y ", html.Strong("temor"), ", lo que sugiere una percepción de escepticismo o desconfianza hacia las instituciones.",
                        html.Br(),
                        "● En general, la nube muestra una combinación de expectativas, preocupaciones y desconfianza, junto con un llamado a la mejora y a un mayor involucramiento ciudadano. Los colores de las palabras no tienen un significado específico, ya que no es posible categorizar todas las expresiones ni ubicarlas en un espectro de percepciones positivas o negativas."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans',
                        'textAlign': 'justify'
                    }),
                    width=12
                )
            ], justify='center', style={'marginTop': '20px'}),

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
                dbc.Row([
                dbc.Col(
                    html.P([
                        "Esta nube de palabras representa las percepciones de los participantes sobre la confianza en las instituciones después del proceso deliberativo. El tamaño de cada palabra indica la frecuencia con la que fue mencionada: cuanto más grande aparece, más veces fue repetida en las respuestas.",
                        html.Br(),
                        "● ", html.Strong("Las palabras más destacadas"), ", como ", html.Strong("confianza"), ", ", html.Strong("responsabilidad"), ", ", html.Strong("público"), " y ", html.Strong("ciudadanía"), ", reflejan un cambio hacia una percepción más centrada en el compromiso colectivo y en la responsabilidad hacia lo público.",
                        html.Br(),
                        "● También surgen términos como ", html.Strong("esperanza"), ", ", html.Strong("participación"), " y ", html.Strong("decisiones"), ", lo que sugiere una mayor confianza en los procesos y en la capacidad de tomar decisiones colectivas.",
                        html.Br(),
                        "● En general, la nube muestra una transformación hacia una percepción más positiva, con un énfasis creciente en la confianza, el compromiso y la responsabilidad ciudadana. Los colores de las palabras no tienen un significado específico, ya que no es posible categorizar todas las expresiones ni ubicarlas en un espectro de percepciones positivas o negativas."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans',
                        'textAlign': 'justify'
                    }),
                    width=12
                )
            ], justify='center', style={'marginTop': '20px'}),

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
                dbc.Row([
                dbc.Col(
                    html.P([
                        "Esta gráfica muestra cómo cambiaron las proporciones de asambleístas que confían en la capacidad de la Alcaldía Mayor de Bogotá para resolver los problemas de su comunidad. El valor máximo en esta escala es ", html.B("6"), ", representado por la sección amarilla en la parte superior.",
                        html.Br(), html.Br(),
                        "Antes de las actividades (", html.B("Pre"), "), el ", html.Span("11.9%", style={'textDecoration': 'underline', 'color': 'black', 'backgroundColor': 'yellow'}), " mostró un nivel máximo de confianza (valor 6). Después de las actividades (", html.B("Pos"), "), este porcentaje aumentó al ", html.Span("34.1%", style={'textDecoration': 'underline', 'color': 'black', 'backgroundColor': 'yellow'}), ".", html.Br(),
                        "También se observa una reducción en los niveles más bajos de confianza. El porcentaje en el nivel más bajo (valor 1) disminuyó del ", html.Span("16.7%", style={'textDecoration': 'underline', 'color': 'white', 'backgroundColor': 'red'}), " al ", html.Span("9.8%", style={'textDecoration': 'underline', 'color': 'white', 'backgroundColor': 'red'}), ".", html.Br(),
                        "En general, se nota un aumento en la confianza después de las actividades, con más participantes ubicándose en los niveles más altos. Si pasas el cursor por encima de cada sección, podrás ver el valor específico que votaron los asambleístas dentro de la escala. Al ser una gráfica de proporciones, si te situas en cada uno de los bloques, te saldrán los siguientes datos:",
                        html.Br(), html.Br(),
                        "● ", html.B("Valor"), ": que hace referencia a la selección que los asambleistas en escala del 1 al 10 (donde 1 es poco y 10 es mucho) en función de la pregunta.", html.Br(),
                        "● ", html.B("Proporción"), ": hace referencia a, de la totalidad de asambleistas que contestaron a la pregunta, cuál fue el porcentaje seleccionaron ese valor.", html.Br(),
                        "● ", html.B("Cantidad"), ": hace referencia al número de asambleistas que eligieron esa respuesta."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans',
                        'textAlign': 'justify'
                    }),
                    width=12
                )
            ], justify='center', style={'marginTop': '20px'}),
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
                dbc.Row([
                dbc.Col(
                    html.P([
                        "Esta gráfica muestra cómo cambiaron las proporciones de asambleístas respecto al grado de confianza en que sus recomendaciones sobre los temas tratados en la Asamblea Deliberativa se implementarán. El valor máximo en esta escala está representado por la sección amarilla más clara en la parte superior de cada barra.",
                        html.Br(), html.Br(),
                        "Antes de las actividades, el ", html.Span("31.0%", style={'textDecoration': 'underline', 'color': 'black', 'backgroundColor': 'yellow'}), " mostró un nivel máximo de confianza. Después de las actividades, esta proporción aumentó al ", html.Span("39.0%", style={'textDecoration': 'underline', 'color': 'black', 'backgroundColor': 'yellow'}), ".",
                        html.Br(),
                        "En los niveles intermedios de confianza, se nota un cambio leve: el 45.2% en el nivel previo (", html.B("Pre"), ") pasó a un 43.9% en el nivel posterior (", html.B("Pos"), "), mostrando una ligera disminución.", html.Br(),
                        "En los niveles más bajos de confianza, la proporción en el nivel más bajo disminuyó. Antes de las actividades, el ", html.Span("4.8%", style={'textDecoration': 'underline', 'color': 'white', 'backgroundColor': 'red'}), " mostró este nivel mínimo de confianza, mientras que después de las actividades este porcentaje se redujo al 0%.", html.Br(),
                        "Si pasas el cursor por encima de cada sección, podrás ver el valor específico que votaron los asambleístas dentro de la escala. Al ser una gráfica de proporciones, si te situas en cada uno de los bloques, te saldrán los siguientes datos:",
                        html.Br(), html.Br(),
                        "● ", html.B("Valor"), ": que hace referencia a la selección que los asambleistas en escala del 1 al 10 (donde 1 es poco y 10 es mucho) en función de la pregunta.", html.Br(),
                        "● ", html.B("Proporción"), ": hace referencia a, de la totalidad de asambleistas que contestaron a la pregunta, cuál fue el porcentaje seleccionaron ese valor.", html.Br(),
                        "● ", html.B("Cantidad"), ": hace referencia al número de asambleistas que eligieron esa respuesta."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans',
                        'textAlign': 'justify'
                    }),
                    width=12
                )
            ], justify='center', style={'marginTop': '20px'}),

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
                dbc.Row([
                dbc.Col(
                    html.P([
                        "Esta gráfica muestra por qué las personas tienden a no involucrarse en los espacios de participación promovidos por la Alcaldía Mayor de Bogotá.",
                        html.Br(), html.Br(),
                        "● ", html.Span("38.1%", style={'textDecoration': 'underline', 'color': 'white', 'backgroundColor': 'red'}), " indicó que la razón principal es el ", html.B("desconocimiento"), ".", html.Br(),
                        "● ", html.Span("28.6%", style={'textDecoration': 'underline', 'color': 'white', 'backgroundColor': 'orange'}), " mencionó que ", html.B("no"), " creen que estos espacios resuelvan las problemáticas de su comunidad.", html.Br(),
                        "● ", html.Span("21.4%", style={'textDecoration': 'underline', 'color': 'black', 'backgroundColor': 'yellow'}), " expresó que no participan debido al ", html.B("desinterés"), ".", html.Br(),
                        "● ", html.Span("11.9%", style={'textDecoration': 'underline', 'color': 'white', 'backgroundColor': 'brown'}), " afirmó que ", html.B("no"), " cuentan con el tiempo ni recursos para movilizarse."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans',
                        'textAlign': 'justify'
                    }),
                    width=12
                )
            ], justify='center', style={'marginTop': '20px'}),

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
                dbc.Row([
                dbc.Col(
                    html.P([
                        "Esta gráfica muestra la disposición de los participantes para implementar las recomendaciones generadas en el proceso deliberativo.",
                        html.Br(), html.Br(),
                        "● El ", html.Span("65%", style={'textDecoration': 'underline', 'color': 'black', 'backgroundColor': 'yellow'}), " de los participantes indicó que implementaría ", html.B("todas"), " las recomendaciones.", html.Br(),
                        "● El ", html.Span("35%", style={'textDecoration': 'underline', 'color': 'white', 'backgroundColor': 'red'}), " señaló que implementaría las recomendaciones ", html.B("parcialmente"), "."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans',
                        'textAlign': 'justify'
                    }),
                    width=12
                )
            ], justify='center', style={'marginTop': '20px'}),

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

                dbc.Row([
                    dbc.Col(
                        html.P([
                            "Aquí se presentan las percepciones de los participantes sobre los aspectos organizativos y operativos del evento. Se analizan áreas como el tiempo disponible, los recursos utilizados, la comunicación y otros factores que influyeron en el desarrollo de las actividades. Esta sección identifica qué aspectos de la logística funcionaron bien y cuáles pueden mejorar en el futuro."], style={
                            'fontSize': '18px',
                            'maxWidth': '800px',
                            'marginLeft': 'auto',
                            'marginRight': 'auto',
                            'fontFamily': 'Museo Sans',
                            'textAlign': 'justify'
                        }),
                        width=12
                    )
                ], justify='center', style={'marginTop': '20px'}),


                dbc.Row([
                dbc.Col(
                    html.P([
                        "Esta gráfica muestra las opiniones de los asambleístas sobre si consideraron suficiente el tiempo disponible para las sesiones.",
                        html.Br(),
                        "Las respuestas se distribuyeron de la siguiente manera: ",
                        html.Span("19.5%", style={'textDecoration': 'underline', 'color': 'black', 'backgroundColor': 'yellow'}), " consideró que el tiempo fue ", html.Strong("totalmente"), "; ",
                        html.Span("26.8%", style={'textDecoration': 'underline', 'color': 'white', 'backgroundColor': 'darkgoldenrod'}), " opinó que el tiempo fue ", html.Strong("suficiente"), "; ",
                        html.Span("17.1%", style={'textDecoration': 'underline', 'color': 'white', 'backgroundColor': 'orange'}), " sintió que el tiempo fue ", html.Strong("parcialmente"), "; ",
                        html.Span("19.5%", style={'textDecoration': 'underline', 'color': 'white', 'backgroundColor': 'red'}), " consideró que el tiempo fue ", html.Strong("insuficiente"), "; ",
                        html.Span("12.2%", style={'textDecoration': 'underline', 'color': 'white', 'backgroundColor': 'brown'}), " afirmó que el tiempo fue ", html.Strong("muy insuficiente"), "; ",
                        html.Span("4.9%", style={'textDecoration': 'underline', 'color': 'white', 'backgroundColor': 'darkbrown'}), " expresó que el tiempo fue ", html.Strong("totalmente insuficiente"), ".",
                        html.Br(),
                        "En general, aunque una mayoría consideró el tiempo adecuado o suficiente, una parte significativa sintió que el tiempo asignado no fue suficiente para cubrir las necesidades de las sesiones."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans',
                        'textAlign': 'justify'
                    }),
                    width=12
                )
            ], justify='center', style={'marginTop': '20px'}),

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
                dbc.Row([
                dbc.Col(
                    html.P([
                        "Esta gráfica muestra cuánto tiempo adicional los asambleístas consideraron que habría sido útil para las sesiones:",
                        html.Br(),
                        "● ", html.Span("46.5%", style={'textDecoration': 'underline', 'color': 'white', 'backgroundColor': 'red'}), " indicó que se necesitaban al menos ", html.Strong("dos"), " o tres días más.",
                        html.Br(),
                        "● ", html.Span("20.9%", style={'textDecoration': 'underline', 'color': 'black', 'backgroundColor': 'yellow'}), " consideró necesario al menos ", html.Strong("un"), " día completo más.",
                        html.Br(),
                        "● ", html.Span("18.6%", style={'textDecoration': 'underline', 'color': 'white', 'backgroundColor': 'darkorange'}), " opinó que ", html.Strong("medio"), " día o menos habría sido suficiente.",
                        html.Br(),
                        "● ", html.Span("14%", style={'textDecoration': 'underline', 'color': 'white', 'backgroundColor': 'orange'}), " señaló que ", html.Strong("no"), " era necesario más tiempo.",
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans',
                        'textAlign': 'justify'
                    }),
                    width=12
                )
            ], justify='center', style={'marginTop': '20px'}),

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
                dbc.Row([
                dbc.Col(
                    html.P([
                        "Esta gráfica muestra cómo los participantes aprovecharían el tiempo adicional si el proceso lo permitiera:",
                        html.Br(),
                        "● ", html.Span("35.3%", style={'textDecoration': 'underline', 'color': 'black', 'backgroundColor': 'yellow'}), " lo utilizaría para ", html.Strong("deliberar"), " y discutir más los diferentes argumentos.",
                        html.Br(),
                        "● ", html.Span("19.1%", style={'textDecoration': 'underline', 'color': 'white', 'backgroundColor': 'red'}), " consideró necesario ", html.Strong("desarrollar"), " más nuestras recomendaciones.",
                        html.Br(),
                        "● ", html.Span("20.6%", style={'textDecoration': 'underline', 'color': 'white', 'backgroundColor': 'orange'}), " lo dedicaría a ", html.Strong("acordar"), " la redacción final de las recomendaciones.",
                        html.Br(),
                        "● ", html.Span("16.2%", style={'textDecoration': 'underline', 'color': 'white', 'backgroundColor': 'darkorange'}), " preferiría ", html.Strong("escuchar"), " a más expertos.",
                        html.Br(),
                        "● ", html.Span("8.82%", style={'textDecoration': 'underline', 'color': 'white', 'backgroundColor': 'brown'}), " afirmó que ", html.Strong("no"), " era necesario más tiempo.",
                        html.Br(), html.Br(),
                        html.Strong("Relación"), " con respuestas anteriores:",
                        html.Br(),
                        "Esta gráfica es consistente con los resultados previos sobre la insuficiencia del tiempo en las sesiones. La mayoría de los participantes expresó la necesidad de tiempo adicional para deliberar más y desarrollar mejor las recomendaciones. Esto coincide con la percepción de que el tiempo asignado no fue suficiente y con el 46.5% que pidió dos o tres días más en la gráfica anterior."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans',
                        'textAlign': 'justify'
                    }),
                    width=12
                )
            ], justify='center', style={'marginTop': '20px'})
,

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
                dbc.Row([
                dbc.Col(
                    html.P([
                        "Esta gráfica muestra si los participantes sintieron que tuvieron suficientes oportunidades para expresarse durante las sesiones:",
                        html.Br(),
                        "● ", html.Span("64.9%", style={'textDecoration': 'underline', 'color': 'black', 'backgroundColor': 'yellow'}), " respondió ", html.Strong("sí"), ", indicando que tuvieron el espacio necesario para hablar.",
                        html.Br(),
                        "● ", html.Span("35.1%", style={'textDecoration': 'underline', 'color': 'white', 'backgroundColor': 'red'}), " respondió ", html.Strong("no"), ", sintiendo que no tuvieron suficientes oportunidades para expresarse."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans',
                        'textAlign': 'justify'
                    }),
                    width=12
                )
            ], justify='center', style={'marginTop': '20px'}),
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
                dbc.Row([
                dbc.Col(
                    html.P([
                        "Esta gráfica muestra cómo les fue a los participantes utilizando WhatsApp para recibir las comunicaciones de la Asamblea Deliberativa:",
                        html.Br(),
                        "● ", html.Span("80.0%", style={'textDecoration': 'underline', 'color': 'black', 'backgroundColor': 'yellow'}), " consideró que el uso de WhatsApp fue ", html.Strong("bueno"), " o muy bueno para recibir la información.",
                        html.Br(),
                        "● ", html.Span("12.5%", style={'textDecoration': 'underline', 'color': 'white', 'backgroundColor': 'orange'}), " indicó que el uso fue ", html.Strong("regular"), ".",
                        html.Br(),
                        "● Un pequeño porcentaje tuvo experiencias negativas, con una proporción muy baja que consideró el uso ", html.Strong("malo"), " o muy malo.",
                        html.Br(),
                        "En general, WhatsApp fue una herramienta efectiva para la mayoría de los participantes en la comunicación durante el proceso deliberativo."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans',
                        'textAlign': 'justify'
                    }),
                    width=12
                )
            ], justify='center', style={'marginTop': '20px'})
,

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
                dbc.Row([
                dbc.Col(
                    html.P([
                        "Esta gráfica muestra qué aspectos de la logística del evento mejorarían los participantes:",
                        html.Br(),
                        "● ", html.Span("39.5%", style={'textDecoration': 'underline', 'color': 'white', 'backgroundColor': 'orange'}), " consideró necesario mejorar la ", html.Strong("asistencia"), ".",
                        html.Br(),
                        "● ", html.Span("25.6%", style={'textDecoration': 'underline', 'color': 'black', 'backgroundColor': 'yellow'}), " sugirió mejoras en la ", html.Strong("seguridad"), ".",
                        html.Br(),
                        "● ", html.Span("23.3%", style={'textDecoration': 'underline', 'color': 'white', 'backgroundColor': 'brown'}), " opinó que ", html.Strong("no"), " era necesario hacer mejoras.",
                        html.Br(),
                        "● ", html.Span("6.98%", style={'textDecoration': 'underline', 'color': 'white', 'backgroundColor': 'red'}), " mencionó mejoras en el ", html.Strong("transporte"), ".",
                        html.Br(),
                        "● ", html.Span("4.65%", style={'textDecoration': 'underline', 'color': 'white', 'backgroundColor': 'darkorange'}), " señaló la ", html.Strong("alimentación"), " como área de mejora.",
                        html.Br(),
                        "En general, la mayoría de los participantes cree que se deben realizar mejoras en la asistencia y la seguridad para futuros eventos."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans',
                        'textAlign': 'justify'
                    }),
                    width=12
                )
            ], justify='center', style={'marginTop': '20px'})
,

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

                dbc.Row([
                    dbc.Col(
                        html.P([
                            "Esta sección evalúa cómo fue la participación de los asambleístas durante las actividades. Se consideran aspectos como el respeto por los turnos de palabra, la disposición para escuchar, la claridad en las intervenciones y el nivel de implicación en el proceso. Los resultados permiten identificar buenas prácticas y áreas donde se puede fomentar una participación más efectiva y equitativa."
                        ], style={
                            'fontSize': '18px',
                            'maxWidth': '800px',
                            'marginLeft': 'auto',
                            'marginRight': 'auto',
                            'fontFamily': 'Museo Sans',
                            'textAlign': 'justify'
                        }),
                        width=12
                    )
                ], justify='center', style={'marginTop': '20px'}),


                dbc.Row([
                dbc.Col(
                    html.P([
                        "Esta gráfica muestra en qué medida los participantes se involucran actualmente en las decisiones gubernamentales que los afectan cuando se les preguntó previo al inicio de la actividad:",
                        html.Br(),
                        "● ", html.Span("14.3%", style={'backgroundColor': 'yellow', 'color': 'black'}), " siente que participa ", html.Strong("mucho"), ".",
                        html.Br(),
                        "● ", html.Span("14.3%", style={'backgroundColor': 'orange', 'color': 'white'}), " considera que su participación es ", html.Strong("moderada"), ".",
                        html.Br(),
                        "● ", html.Span("14.3%", style={'backgroundColor': 'darkorange', 'color': 'white'}), " cree que participa ", html.Strong("poco"), ".",
                        html.Br(),
                        "● ", html.Span("21.4%", style={'backgroundColor': 'red', 'color': 'white'}), " siente que su participación es ", html.Strong("muy"), " baja.",
                        html.Br(),
                        "● ", html.Span("23.8%", style={'backgroundColor': 'darkorange', 'color': 'white'}), " indica que participa ", html.Strong("mínimamente"), ".",
                        html.Br(),
                        "● ", html.Span("11.9%", style={'backgroundColor': 'brown', 'color': 'white'}), " afirma que ", html.Strong("no"), " participa en absoluto.",
                        html.Br(),
                        "En general, la mayoría de los participantes reporta niveles bajos o mínimos de participación en las decisiones gubernamentales que los afectan."], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans',
                        'textAlign': 'justify'
                    }),
                    width=12
                )
            ], justify='center', style={'marginTop': '20px'})
,
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
                dbc.Row([
                dbc.Col(
                    html.P([
                        "Esta gráfica muestra las opiniones sobre si las asambleas deliberativas pueden ayudar a que la ciudadanía tenga mayor influencia en las decisiones gubernamentales antes de iniciar la actividad.",
                        html.Br(),
                        "● ", html.Span("57.1%", style={'backgroundColor': 'yellow', 'color': 'black'}), " considera que estas asambleas sí pueden ", html.Strong("aumentar"), " la influencia ciudadana.",
                        html.Br(),
                        "● ", html.Span("35.7%", style={'backgroundColor': 'orange', 'color': 'white'}), " opina que pueden ", html.Strong("contribuir"), " en cierta medida.",
                        html.Br(),
                        "● ", html.Span("4.8%", style={'backgroundColor': 'red', 'color': 'white'}), " cree que las asambleas ", html.Strong("no"), " aumentan la influencia.",
                        html.Br(),
                        "En general, la mayoría confía en que las asambleas deliberativas pueden ser una herramienta efectiva para fortalecer la participación ciudadana en decisiones gubernamentales."], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans',
                        'textAlign': 'justify'
                    }),
                    width=12
                )
            ], justify='center', style={'marginTop': '20px'})

,

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
                dbc.Row([
                dbc.Col(
                    html.P([
                        "Esta nube de palabras muestra las expectativas expresadas por los participantes cuando se les preguntó qué esperaban del proceso deliberativo.",
                        html.Br(), html.Br(),
                        "Las palabras más destacadas, como ", html.B("participación"), ", ", html.B("poder"), ", ", html.B("confianza"), " y ", html.B("expectativa"), ", reflejan un fuerte deseo de involucrarse, sentirse escuchados y tener incidencia en las decisiones.", html.Br(),
                        "Otras palabras como ", html.B("ciudad"), ", ", html.B("mejorar"), ", ", html.B("escuchada"), " y ", html.B("comunidad"), " sugieren que los participantes esperan cambios positivos en su entorno, mayor inclusión y procesos transparentes.", html.Br(),
                        "El tamaño de cada palabra indica la frecuencia con la que fue mencionada: cuanto más grande aparece, más veces fue repetida en las respuestas. Los colores, en cambio, no representan categorías específicas, ya que no es posible clasificar la totalidad de las expresiones ni encasillarlas en un espectro de percepciones positivas o negativas.", html.Br(),
                        "Esta nube captura de manera visual las expectativas de los participantes, mostrando sus principales inquietudes y deseos relacionados con el proceso deliberativo."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans',
                        'textAlign': 'justify'
                    }),
                    width=12
                )
            ], justify='center', style={'marginTop': '20px'})
,
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
                dbc.Row([
                dbc.Col(
                    html.P([
                        "Esta nube de palabras muestra las respuestas de los participantes después del proceso deliberativo, reflejando cómo evolucionaron sus expectativas y percepciones. El tamaño de cada palabra indica la frecuencia con la que fue mencionada: cuanto más grande aparece, más veces fue repetida en las respuestas.",
                        html.Br(), html.Br(),
                        "Las palabras más destacadas incluyen ", html.B("aportar"), ", ", html.B("ciudad"), ", ", html.B("poder"), " y ", html.B("participar"), ". Estas palabras reflejan un énfasis en la ", html.B("acción"), ", la ", html.B("contribución"), " y el deseo de tener una ", html.B("ciudad"), " más participativa y colaborativa.", html.Br(),
                        "También aparecen términos como ", html.B("conocer"), ", ", html.B("decisiones"), ", ", html.B("confianza"), " y ", html.B("Bogotá"), ", evidenciando una mayor disposición a involucrarse y una visión más clara del rol de los participantes en los procesos ciudadanos.", html.Br(),
                        "Los colores de las palabras no tienen un significado específico, ya que no es posible clasificar todas las expresiones dentro de categorías fijas ni ubicarlas en un espectro de percepciones positivas o negativas. Esta nube de palabras permite identificar visualmente los temas más recurrentes en las respuestas, destacando las principales inquietudes y percepciones de los participantes."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans',
                        'textAlign': 'justify'
                    }),
                    width=12
                )
            ], justify='center', style={'marginTop': '20px'}),

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
                dbc.Row([
                dbc.Col(
                    html.P([
                        "Esta gráfica muestra cómo los participantes esperan involucrarse en el futuro en decisiones gubernamentales que los afectan.",
                        html.Br(),
                        "● ", html.Span("55.0%", style={'backgroundColor': 'darkgoldenrod', 'color': 'black'}), " cree que tendrá un ", html.Strong("alto"), " grado de participación.",
                        html.Br(),
                        "● ", html.Span("37.5%", style={'backgroundColor': 'orange', 'color': 'white'}), " espera participar ", html.Strong("moderadamente"), ".",
                        html.Br(),
                        "● ", html.Span("5.0%", style={'backgroundColor': 'red', 'color': 'white'}), " anticipa una ", html.Strong("baja"), " participación.",
                        html.Br(),
                        "Comparación con la participación actual",
                        html.Br(),
                        "En la gráfica del pre test sobre la participación actual, solo un ", html.Span("14.3%", style={'backgroundColor': 'yellow', 'color': 'black'}), " mencionaba participar mucho en decisiones gubernamentales, mientras que un ", html.Span("21.4%", style={'backgroundColor': 'red', 'color': 'white'}), " sentía que su participación era muy baja.",
                        html.Br(),
                        "Este gráfico refleja una mejora en las expectativas: más de la mitad espera un alto grado de participación en el futuro. Esto indica que las actividades y discusiones en la asamblea deliberativa generaron una mayor confianza y motivación para involucrarse en procesos de toma de decisiones."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans',
                        'textAlign': 'justify'
                    }),
                    width=12
                )
            ], justify='center', style={'marginTop': '20px'}),

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
                dbc.Row([
                dbc.Col(
                    html.P([
                        "Antes de la asamblea, el ", html.Span("16.7%", style={'backgroundColor': 'red', 'color': 'white'}), " no confiaba en la Alcaldía y solo el ", html.Span("11.9%", style={'backgroundColor': 'darkgoldenrod', 'color': 'white'}), " tenía mucha confianza. Después, la desconfianza bajó al ", html.Span("9.8%", style={'backgroundColor': 'red', 'color': 'white'}), " y la confianza aumentó al ", html.Span("34.1%", style={'backgroundColor': 'yellow', 'color': 'black'}), ".",
                        html.Br(),
                        "Si pasas el cursor por encima de cada sección, podrás ver el valor específico que votaron los asambleístas dentro de la escala."], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans',
                        'textAlign': 'justify'
                    }),
                    width=12
                )
            ], justify='center', style={'marginTop': '20px'}),
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
                dbc.Row([
                dbc.Col(
                    html.P([
                        "La mayoría de los asambleístas, el ", html.Span("39.0%", style={'backgroundColor': 'brown', 'color': 'white'}), " no sintió ninguna presión para estar de acuerdo con los demás. Un ", html.Span("9.8%", style={'backgroundColor': 'orange', 'color': 'white'}), " sintió algo de presión, mientras que solo el ", html.Span("4.9%", style={'backgroundColor': 'darkgoldenrod', 'color': 'white'}), " sintió presión moderada y el ", html.Span("2.4%", style={'backgroundColor': 'red', 'color': 'white'}), " sintió presión alta.",
                        html.Br(),
                        "Esto sugiere que en general, el ambiente fue libre y respetuoso para expresar opiniones. Si pasas el cursor por encima de cada sección, podrás ver el valor específico que votaron los asambleístas dentro de la escala."], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans',
                        'textAlign': 'justify'
                    }),
                    width=12
                )
            ], justify='center', style={'marginTop': '20px'}),
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
                dbc.Row([
                dbc.Col(
                    html.P([
                        "En esta gráfica, todas las respuestas se concentraron en los valores más altos de una escala del 1 al 6. El ", html.Span("61.9%", style={'backgroundColor': 'darkgoldenrod', 'color': 'white'}), " sintió una representación alta por parte de los participantes (valor 6). El ", html.Span("31.0%", style={'backgroundColor': 'orange', 'color': 'white'}), " se ubicó en un nivel de representación moderado (valor 5), mientras que solo el ", html.Span("7.1%", style={'backgroundColor': 'red', 'color': 'white'}), " se sintió menos representado (valor 4).",
                        html.Br(),
                        "Esto indica que, en general, los asambleístas se sintieron bien representados durante las deliberaciones."
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans',
                        'textAlign': 'justify'
                    }),
                    width=12
                )
            ], justify='center', style={'marginTop': '20px'}),

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
                dbc.Row([
                    dbc.Col(
                        html.P([
                            "Esta nube de palabras representa los grupos que, según los participantes, no tuvieron suficiente representación durante el proceso deliberativo. El tamaño de cada palabra indica la frecuencia con la que fue mencionada: cuanto más grande aparece, más veces fue repetida en las respuestas.",
                            html.Br(),
                            "● ", html.Strong("Las palabras más destacadas"), ", como ", html.Strong("discapacidad"), ", ", html.Strong("madres"), ", ", html.Strong("pueblos étnicos"), " y ", html.Strong("jóvenes"), ", reflejan una preocupación por la inclusión de comunidades que pueden enfrentar barreras adicionales para participar.",
                            html.Br(),
                            "● ", html.Strong("estudiantes"), " y ", html.Strong("colegios"), ", resaltando la necesidad de mayor representación en espacios educativos.",
                            html.Br(),
                            "● ", html.Strong("recicladores"), " y ", html.Strong("migrantes"), ", lo que evidencia inquietudes sobre la participación de trabajadores informales y personas en situación de movilidad.",
                            html.Br(),
                            "● Los colores de las palabras no tienen un significado específico, ya que no es posible categorizar todas las expresiones dentro de un solo marco interpretativo."
                        ], style={
                            'fontSize': '18px',
                            'maxWidth': '800px',
                            'marginLeft': 'auto',
                            'marginRight': 'auto',
                            'fontFamily': 'Museo Sans',
                            'textAlign': 'justify'
                        }),
                        width=12
                    )
                ], justify='center', style={'marginTop': '20px'}),
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
            dbc.Row([
            dbc.Col(
                html.P([
                    html.B("Casa de la Confianza"), " tuvo como objetivo identificar lo que podría ocurrir en futuras asambleas a través de la discusión y deliberación. Se utilizaron ", html.B("nueve (9) fichas"), ", cada una relacionada con diferentes espacios de un hogar. Los asambleístas ubicaron estas fichas según lo que esperaban de las siguientes asambleas, definiendo los actores involucrados en cada proceso y sus funciones. Algunos de los espacios clave fueron:",
                    html.Br(), html.Br(),
                    "● ", html.B("Comedor"), ": representó el espacio de toma de decisiones. Los asambleístas definieron quiénes debían participar en las decisiones y con qué frecuencia deberían tomarse. Además, señalaron las funciones específicas de cada actor en este proceso.", html.Br(),
                    "● ", html.B("Estudio"), ": simbolizó el seguimiento y la evaluación. Se establecieron las entidades responsables de dar seguimiento a los acuerdos y evaluar su cumplimiento, detallando las tareas que cada actor debía realizar para garantizar el avance adecuado.", html.Br(),
                    "● ", html.B("Televisor"), ": reflejó la divulgación. En este espacio, los asambleístas identificaron a los actores encargados de asegurar la transparencia y rendición de cuentas, explicando qué funciones debían cumplir para garantizar que toda la información fuera clara y accesible.", html.Br(),
                    "● ", html.B("Sala"), ": representó el ejercicio de consulta. Aquí, se señalaron los procesos de participación y se identificaron a los actores encargados de promover el diálogo y asegurar que se escucharan todas las voces durante las asambleas."
                ], style={
                    'fontSize': '18px',
                    'maxWidth': '800px',
                    'marginLeft': 'auto',
                    'marginRight': 'auto',
                    'fontFamily': 'Museo Sans',
                    'textAlign': 'justify'
                }),
                width=12
            )
        ], justify='center', style={'marginTop': '20px'}),

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

                    dbc.Row([
                    dbc.Col(
                        html.P([
                            "Esta gráfica muestra la primera pregunta del termómetro de la deliberación sobre si los participantes estuvieron escuchando con atención las ideas de sus compañeros. La escala utilizada fue del 1 al 5, y las respuestas se concentraron únicamente en los niveles más altos:",
                            html.Br(),
                            "- ", html.Span("El 73.7%", style={'textDecoration': 'underline', 'backgroundColor': 'yellow', 'color': 'black'}), " eligió el nivel 5, indicando un alto nivel de atención.",
                            html.Br(),
                            "- ", html.Span("El 15.8%", style={'textDecoration': 'underline', 'backgroundColor': 'orange', 'color': 'black'}), " seleccionó el nivel 4.",
                            html.Br(),
                            "- ", html.Span("El 10.5%", style={'textDecoration': 'underline', 'backgroundColor': 'red', 'color': 'white'}), " optó por el nivel 3.",
                            html.Br(),
                            "Esto refleja una percepción general positiva respecto a la atención prestada durante la deliberación."
                        ], style={
                            'fontSize': '18px',
                            'maxWidth': '800px',
                            'marginLeft': 'auto',
                            'marginRight': 'auto',
                            'fontFamily': 'Museo Sans',
                            'textAlign': 'justify'
                        }),
                        width=12
                    )
                ], justify='center', style={'marginTop': '20px'}),

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

                    dbc.Row([
                    dbc.Col(
                        html.P([
                            "Esta gráfica muestra las respuestas a la pregunta sobre si la participación de los asambleístas tuvo en cuenta la información recibida durante la semana de formación. La escala fue del 1 al 5, y los resultados se distribuyeron en los niveles más altos:",
                            html.Br(),
                            "- ", html.Span("El 47.4%", style={'textDecoration': 'underline', 'backgroundColor': 'yellow', 'color': 'black'}), " eligió el nivel 5, reflejando un uso alto de la información recibida.",
                            html.Br(),
                            "- ", html.Span("El 31.6%", style={'textDecoration': 'underline', 'backgroundColor': 'orange', 'color': 'black'}), " seleccionó el nivel 4.",
                            html.Br(),
                            "- ", html.Span("El 21.1%", style={'textDecoration': 'underline', 'backgroundColor': 'red', 'color': 'white'}), " indicó el nivel 3.",
                            html.Br(),
                            "Esto sugiere que, en general, la mayoría de los participantes integraron la información recibida en su participación."
                        ], style={
                            'fontSize': '18px',
                            'maxWidth': '800px',
                            'marginLeft': 'auto',
                            'marginRight': 'auto',
                            'fontFamily': 'Museo Sans',
                            'textAlign': 'justify'
                        }),
                        width=12
                    )
                ], justify='center', style={'marginTop': '20px'}),

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
                    dbc.Row([
                    dbc.Col(
                        html.P([
                            "Esta gráfica muestra las respuestas a la pregunta sobre si los asambleístas permitieron que sus compañeros expusieran su punto de vista. La escala fue del 1 al 5, y los resultados se distribuyeron en los niveles más altos:",
                            html.Br(),
                            "- ", html.Span("El 84.2%", style={'textDecoration': 'underline', 'backgroundColor': 'yellow', 'color': 'black'}), " eligió el nivel 5, indicando una alta disposición para escuchar puntos de vista ajenos.",
                            html.Br(),
                            "- ", html.Span("El 15.8%", style={'textDecoration': 'underline', 'backgroundColor': 'orange', 'color': 'black'}), " seleccionó el nivel 4.",
                            html.Br(),
                            "Esto refleja que una amplia mayoría de los participantes permitió que sus compañeros expresaran sus ideas durante la deliberación.",
                        ], style={
                            'fontSize': '18px',
                            'maxWidth': '800px',
                            'marginLeft': 'auto',
                            'marginRight': 'auto',
                            'fontFamily': 'Museo Sans',
                            'textAlign': 'justify'
                        }),
                        width=12
                    )
                ], justify='center', style={'marginTop': '20px'}),

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
                    dbc.Row([
                    dbc.Col(
                        html.P([

                            "Esta gráfica muestra las respuestas a la pregunta sobre si los asambleístas realizaron intervenciones cortas y claras para permitir que otros también pudieran hablar. La escala fue del 1 al 5, y los resultados se distribuyeron en los niveles más altos:",
                            html.Br(),
                            "- ", html.Span("El 63.2%", style={'textDecoration': 'underline', 'backgroundColor': 'yellow', 'color': 'black'}), " seleccionó el nivel 5.",
                            html.Br(),
                            "- ", html.Span("El 26.3%", style={'textDecoration': 'underline', 'backgroundColor': 'orange', 'color': 'black'}), " eligió el nivel 4.",
                            html.Br(),
                            "- ", html.Span("El 10.5%", style={'textDecoration': 'underline', 'backgroundColor': 'red', 'color': 'white'}), " escogió el nivel 3.",
                            html.Br(),
                            "Esto indica que una mayoría de los participantes considera que sus intervenciones permitieron el diálogo fluido de sus compañeros."
                        ], style={
                            'fontSize': '18px',
                            'maxWidth': '800px',
                            'marginLeft': 'auto',
                            'marginRight': 'auto',
                            'fontFamily': 'Museo Sans',
                            'textAlign': 'justify'
                        }),
                        width=12
                    )
                ], justify='center', style={'marginTop': '20px'}),

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
                    dbc.Row([
                    dbc.Col(
                        html.P([
                            "Esta gráfica muestra las respuestas a la pregunta sobre si los asambleístas se pronunciaron de manera respetuosa sobre las ideas, opiniones y argumentos de sus compañeros. La escala utilizada fue del 1 al 5, y los resultados se distribuyeron principalmente en los niveles más altos:",
                            html.Br(),
                            "- ", html.Span("El 63.2%", style={'textDecoration': 'underline', 'backgroundColor': 'yellow', 'color': 'black'}), " seleccionó el nivel 5.",
                            html.Br(),
                            "- ", html.Span("El 21.1%", style={'textDecoration': 'underline', 'backgroundColor': 'orange', 'color': 'black'}), " eligió el nivel 4.",
                            html.Br(),
                            "- ", html.Span("El 10.5%", style={'textDecoration': 'underline', 'backgroundColor': 'red', 'color': 'white'}), " escogió el nivel 3.",
                            html.Br(),
                            "- ", html.Span("El 5.3%", style={'textDecoration': 'underline', 'backgroundColor': 'brown', 'color': 'black'}), " seleccionó el nivel 2.",
                            html.Br(),
                            "Esto sugiere que una gran mayoría percibió que sus intervenciones fueron respetuosas durante el proceso deliberativo."], style={
                            'fontSize': '18px',
                            'maxWidth': '800px',
                            'marginLeft': 'auto',
                            'marginRight': 'auto',
                            'fontFamily': 'Museo Sans',
                            'textAlign': 'justify'
                        }),
                        width=12
                    )
                ], justify='center', style={'marginTop': '20px'}),
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
                    dbc.Row([
                    dbc.Col(
                        html.P([
                            "Esta gráfica muestra las respuestas a la pregunta sobre si los asambleístas al intervenir hablaban de las ideas de sus compañeros o solo de sus propias ideas. La escala utilizada fue del 1 al 5, y las respuestas se concentraron en los niveles más altos:",
                            html.Br(),
                            "- ", html.Span("El 42.1%", style={'textDecoration': 'underline', 'backgroundColor': 'yellow', 'color': 'black'}), " seleccionó el nivel 5.",
                            html.Br(),
                            "- ", html.Span("El 36.8%", style={'textDecoration': 'underline', 'backgroundColor': 'orange', 'color': 'black'}), " eligió el nivel 4.",
                            html.Br(),
                            "- ", html.Span("El 10.5%", style={'textDecoration': 'underline', 'backgroundColor': 'red', 'color': 'white'}), " escogió el nivel 3.",
                            html.Br(),
                            "- ", html.Span("El 5.3%", style={'textDecoration': 'underline', 'backgroundColor': 'brown', 'color': 'black'}), " seleccionó el nivel 2.",
                            html.Br(),
                            "- Otro ", html.Span("5.3%", style={'textDecoration': 'underline', 'backgroundColor': 'brown', 'color': 'black'}), " seleccionó el nivel 1.",
                            html.Br(),
                            "Esto sugiere que una mayoría de los participantes mencionaba tanto sus propias ideas como las de sus compañeros al intervenir."
                        ], style={
                            'fontSize': '18px',
                            'maxWidth': '800px',
                            'marginLeft': 'auto',
                            'marginRight': 'auto',
                            'fontFamily': 'Museo Sans',
                            'textAlign': 'justify'
                        }),
                        width=12
                    )
                ], justify='center', style={'marginTop': '20px'}),

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
                    dbc.Row([
                    dbc.Col(
                        html.P([
                            "Esta gráfica muestra la disposición de los participantes para cambiar de posición durante el diálogo. La escala utilizada fue del 1 al 5, y las respuestas se distribuyeron en los niveles más altos:",
                            html.Br(),
                            "- ", html.Span("El 52.6%", style={'textDecoration': 'underline', 'backgroundColor': 'yellow', 'color': 'black'}), " seleccionó el nivel 5.",
                            html.Br(),
                            "- ", html.Span("El 15.8%", style={'textDecoration': 'underline', 'backgroundColor': 'orange', 'color': 'black'}), " eligió el nivel 4.",
                            html.Br(),
                            "- ", html.Span("El 26.3%", style={'textDecoration': 'underline', 'backgroundColor': 'red', 'color': 'white'}), " escogió el nivel 3.",
                            html.Br(),
                            "- ", html.Span("El 5.3%", style={'textDecoration': 'underline', 'backgroundColor': 'brown', 'color': 'black'}), " seleccionó el nivel 2.",
                            html.Br(),
                            "Estos resultados indican que una mayoría de los participantes estaba abierta a cambiar su posición durante el diálogo."
                        ], style={
                            'fontSize': '18px',
                            'maxWidth': '800px',
                            'marginLeft': 'auto',
                            'marginRight': 'auto',
                            'fontFamily': 'Museo Sans',
                            'textAlign': 'justify'
                        }),
                        width=12
                    )
                ], justify='center', style={'marginTop': '20px'}),


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
                    dbc.Row([
                    dbc.Col(
                        html.P([
                            "Esta gráfica muestra la distribución de los puntajes totales obtenidos por cada participante al sumar sus respuestas en todas las gráficas anteriores.",
                            html.Br(),
                            "- La puntuación final de los participantes oscila entre ", html.Span("23 y 35", style={'fontWeight': 'bold'}), " puntos.",
                            html.Br(),
                            "- Se observa que la mayor concentración de puntajes está entre ", html.Span("31 y 34", style={'fontWeight': 'bold'}), ", con una frecuencia máxima de 3 participantes en esos valores.",
                            html.Br(),
                            "- Valores más bajos como ", html.Span("23 y 25", style={'fontWeight': 'bold'}), " son menos frecuentes.",
                            html.Br(),
                            "- Esto refleja que la mayoría de los participantes puntuaron en rangos medios y altos, indicando una participación consistente y positiva en las actividades evaluadas."
                        ], style={
                            'fontSize': '18px',
                            'maxWidth': '800px',
                            'marginLeft': 'auto',
                            'marginRight': 'auto',
                            'fontFamily': 'Museo Sans',
                            'textAlign': 'justify'
                        }),
                        width=12
                    )
                ], justify='center', style={'marginTop': '20px'}),
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

    elif selected_subtab == "metodologia":

        return html.Div([

                html.Br(), html.Br(),
                html.H3("Metodología", style={'textAlign': 'center', 'fontSize': '30px', 'fontFamily': 'Kensington'}),  # Título centrado
                dbc.Row([
                    dbc.Col(
                        html.P([
                            "Para comprender a fondo los resultados de la Meta Asamblea, es fundamental partir de ",
                            html.Span("la metodología utilizada para su sistematización", style={'fontWeight': 'bold'}), ". En primer lugar, se estableció un enfoque estructurado basado en cinco (5) etapas clave: ",
                            html.Span("determinar, captar, organizar, categorizar y analizar", style={'fontWeight': 'bold'}), ". Este proceso permitió identificar las áreas prioritarias de sistematización, recopilar la información esencial, organizar los datos en formatos adecuados, clasificar la información obtenida y, finalmente, extraer conclusiones que sirvieran como base para recomendaciones futuras. A través de esta metodología, se logró transformar las experiencias y percepciones de los participantes en insumos valiosos para fortalecer la deliberación ciudadana y la toma de decisiones informadas."
                        ], style={
                            'fontSize': '18px',
                            'maxWidth': '800px',
                            'marginLeft': 'auto',
                            'marginRight': 'auto',
                            'fontFamily': 'Museo Sans',
                            'textAlign': 'justify'
                        }),
                        width=12
                    )
                ], justify='center', style={'marginTop': '20px'}),

                html.Div(
                    html.Img(
                        src='/assets/Metodo1.png',
                        style={'width': 'auto', 'height': 'auto', 'display': 'block'}
                    ),
                    style={
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center',
                        'margin': '12px 0',
                        'width': '100%',
                    }
                ),

                dbc.Row([
                    dbc.Col(
                        html.P([
                            html.Br(),
                            "De manera complementaria, además de seguir una metodología estructurada, la sistematización respondió a áreas de interés clave definidas por la alianza de actores involucrados en la Meta Asamblea. Estas áreas incluyeron las conclusiones y propuestas formuladas por los participantes, los sentimientos y percepciones expresados a lo largo del proceso deliberativo, y la centralidad del debate, es decir, los temas que concentraron mayor atención y discusión dentro de la Asamblea. La identificación y análisis de estas dimensiones permitieron no solo capturar el contenido explícito de la deliberación, sino también comprender el impacto emocional del proceso y reconocer qué temas fueron considerados más relevantes por los asambleístas. De esta manera, se logró una visión más integral de la experiencia colectiva, facilitando la generación de aprendizajes y líneas de acción para futuras iniciativas de participación ciudadana.",
                            html.Br()
                        ], style={
                            'fontSize': '18px',
                            'maxWidth': '800px',
                            'marginLeft': 'auto',
                            'marginRight': 'auto',
                            'fontFamily': 'Museo Sans',
                            'textAlign': 'justify'
                        }),
                        width=12
                    )
                ], justify='center', style={'marginTop': '20px'}),

                html.Div(
                    html.Img(
                        src='/assets/Metodo2.png',
                        style={'width': 'auto', 'height': 'auto', 'display': 'block'}
                    ),
                    style={
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center',
                        'margin': '12px 0',
                        'width': '100%',
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


    elif selected_subtab == "resultados":

        return html.Div([
            html.Br(), html.Br(),
            html.H3("Resultados", style={'textAlign': 'center', 'fontSize': '30px', 'fontFamily': 'Kensington'}),  # Título centrado
            dbc.Row([
                dbc.Col(
                    html.P([
                        "En esta sección presentamos los resultados obtenidos tras un exhaustivo proceso de análisis de la Meta Asamblea, un ejercicio deliberativo que ha permitido capturar la riqueza de la participación ciudadana en toda su complejidad. El análisis que compartimos a continuación representa un esfuerzo por comprender y estructurar las diversas dimensiones que emergieron durante este proceso participativo.",
                        html.Br(), html.Br(),
                        "La sistematización ha sido meticulosamente desarrollada siguiendo una metodología multidimensional que documenta desde las observaciones realizadas por los facilitadores hasta las expresiones emocionales y propuestas surgidas en los espacios colectivos. Hemos procesado una cantidad significativa de información proveniente de relatorías, registros de la Casa de la Confianza, Lienzos de trabajo y mediciones del Termómetro de la Deliberación, lo que nos ha permitido construir una visión integral de los hallazgos.",
                        html.Br(), html.Br(),
                        "Un aspecto fundamental de nuestro análisis ha sido la distinción entre conclusiones —que representan los aprendizajes colectivos y consensos alcanzados— y propuestas —que reflejan las acciones concretas sugeridas para transformar la realidad. Esta separación nos permite apreciar tanto el proceso reflexivo como su potencial impacto práctico.",
                        html.Br(), html.Br(),
                        "Entre los temas más relevantes que emergieron destacan el fortalecimiento de la participación ciudadana, la necesidad de establecer reglas claras con metodologías adaptables, y la importancia de garantizar la transparencia y rendición de cuentas en todos los procesos participativos.",
                        html.Br(), html.Br(),
                        "Para acceder al documento completo de análisis de resultados, con todos los detalles metodológicos y hallazgos específicos, le invitamos a consultar el siguiente enlace: ",
                        html.A("[Resultados de la Meta Asamblea]", href="https://docs.google.com/document/d/1-Q0NuKKYs1yY4w5HPme6Q0-sXYkEIMc8/edit?usp=sharing&ouid=102616880601579909657&rtpof=true&sd=true", target="_blank")
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans',
                        'textAlign': 'justify'
                    }),
                    width=12
                )
            ], justify='center', style={'marginTop': '20px'})
        ], style={
            'display': 'flex',
            'flexDirection': 'column',
            'alignItems': 'center',  # Alineación centrada
            #'textAlign': 'center',
            'maxWidth': '2100px',  # Ancho máximo para evitar que se expandan demasiado en pantallas grandes
            'margin': '0 auto'  # Centra el contenido horizontalmente
        })

    elif selected_subtab == "recomendaciones":

        return html.Div([
            html.Br(), html.Br(),
            html.H3("Recomendaciones", style={'textAlign': 'center', 'fontSize': '30px', 'fontFamily': 'Kensington'}),  # Título centrado
            dbc.Row([
                dbc.Col(
                    html.P([
                        "A partir del análisis de la deliberación y la sistematización del proceso, se formularon una serie de recomendaciones orientadas a fortalecer futuras experiencias de participación ciudadana. Estas recomendaciones surgen de la evaluación de los diferentes momentos del proceso y buscan optimizar tanto la estructura como la experiencia de la deliberación.",
                        html.Br(), html.Br(),
                        html.Strong("Para una mejor comprensión, las recomendaciones se agruparon en cinco (5) categorías clave:"),
                        html.Br(), html.Br(),
                        html.Strong("Estructura y diseño:"), " enfocada en la configuración general del proceso, su planificación y los elementos organizativos esenciales.",
                        html.Br(),
                        html.Strong("Experiencia de la deliberación:"), " centrada en los aspectos que influyeron en la participación, el ambiente y la dinámica de discusión.",
                        html.Br(),
                        html.Strong("Aspectos posteriores a la deliberación:"), " considera las acciones necesarias para garantizar la continuidad del proceso y el impacto de los resultados.",
                        html.Br(),
                        html.Strong("Metodología:"), " evalúa las herramientas y enfoques utilizados para facilitar la deliberación y su efectividad.",
                        html.Br(),
                        html.Strong("Criterios de selección:"), " analiza los mecanismos empleados para seleccionar los temas de las deliberaciones.",
                        html.Br(), html.Br(),
                        "Para acceder al documento completo de presentación de recomendaciones, le invitamos a consultar el siguiente enlace: ",
                        html.A("[Recomenadaciones de la Meta Asamblea]", href="https://docs.google.com/document/d/10BahMFG092WeWLrHc_k0IR1PYST0zZ4c/edit?usp=sharing&ouid=102616880601579909657&rtpof=true&sd=true", target="_blank")
                    ], style={
                        'fontSize': '18px',
                        'maxWidth': '800px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                        'fontFamily': 'Museo Sans',
                        'textAlign': 'justify'
                    }),
                    width=12
                )
            ], justify='center', style={'marginTop': '20px'})

        ], style={
            'display': 'flex',
            'flexDirection': 'column',
            'alignItems': 'center',  # Alineación centrada
            #'textAlign': 'center',
            'maxWidth': '2100px',  # Ancho máximo para evitar que se expandan demasiado en pantallas grandes
            'margin': '0 auto'  # Centra el contenido horizontalmente
        })

    else:
        return html.Div("Contenido no encontrado")


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8050))  # Render provee el puerto en la variable PORT
    app.run_server(host="0.0.0.0", port=port, debug=False)
