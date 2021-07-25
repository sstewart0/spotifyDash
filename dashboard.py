# DASHBOARD
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

# Data
import pandas as pd

# spotify functions
import analysis as sf

stream_data = pd.read_csv("./assets/stream_data.csv")
stream_data['endTime'] = pd.to_datetime(stream_data['endTime'])

time_data_plot = sf.plot_time_data(stream_data)
day_data_plot = sf.plot_day_data(stream_data)

top_songs = pd.read_csv("./assets/top_songs.csv")
top_artists = pd.read_csv("./assets/top_artists.csv")

# Initialize app
app = dash.Dash(
    __name__,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ],
)
server = app.server

app.layout = html.Div(
    id="root",
    children=[
        html.Div(
            id="banner",
            children=[
                html.Img(id="logo",
                         src=app.get_asset_url("spotify_logo2.png"),
                         style={
                             'width':'212px',
                             'height':'80px'
                         })
            ]
        ),
        html.Div(
            id="app-container",
            children=[
                html.Div(
                    id="column1",
                    children=[
                        html.Div(
                            id="genre-container"
                            # polar plot
                        ),
                        html.Div(
                            className="artist-container",
                            children=[
                                html.H1(children="TOP ARTISTS"),
                                html.Div(
                                    className="list-container",
                                    children=[
                                        html.Div(
                                            className="list-col1",
                                            children=[
                                                html.H2(children="#"),
                                                html.Div(
                                                    className="artist-num-container",
                                                    children=[
                                                        html.P("1")
                                                    ]
                                                ),
                                                html.Div(
                                                    className="artist-num-container",
                                                    children=[
                                                        html.P("2")
                                                    ]
                                                ),
                                                html.Div(
                                                    className="artist-num-container",
                                                    children=[
                                                        html.P("3")
                                                    ]
                                                ),
                                                html.Div(
                                                    className="artist-num-container",
                                                    children=[
                                                        html.P("4")
                                                    ]
                                                ),
                                                html.Div(
                                                    className="artist-num-container",
                                                    children=[
                                                        html.P("5")
                                                    ]
                                                )
                                            ]
                                        ),
                                        html.Div(
                                            className="list-col2",
                                            children=[
                                                html.H2(children="ART"),
                                                html.Div(
                                                    className="artist-art-container",
                                                    children=[
                                                        html.Img(
                                                            id="image1",
                                                            src = './assets/artist0.png',
                                                            style={
                                                                'max-width':'100%',
                                                                'max-height':'100%'
                                                            }
                                                        )
                                                    ]
                                                ),
                                                html.Div(
                                                    className="artist-art-container",
                                                    children=[
                                                        html.Img(
                                                            id="image2",
                                                            src='./assets/artist1.png',
                                                            style={
                                                                'max-width': '100%',
                                                                'max-height': '100%'
                                                            }
                                                        )
                                                    ]
                                                ),
                                                html.Div(
                                                    className="artist-art-container",
                                                    children=[
                                                        html.Img(
                                                            id="image3",
                                                            src='./assets/artist2.png',
                                                            style={
                                                                'max-width': '100%',
                                                                'max-height': '100%'
                                                            }
                                                        )
                                                    ]
                                                ),
                                                html.Div(
                                                    className="artist-art-container",
                                                    children=[
                                                        html.Img(
                                                            id="image4",
                                                            src='./assets/artist3.png',
                                                            style={
                                                                'max-width': '100%',
                                                                'max-height': '100%'
                                                            }
                                                        )
                                                    ]
                                                ),
                                                html.Div(
                                                    className="artist-art-container",
                                                    children=[
                                                        html.Img(
                                                            id="image5",
                                                            src='./assets/artist4.png',
                                                            style={
                                                                'max-width': '100%',
                                                                'max-height': '100%'
                                                            }
                                                        )
                                                    ]
                                                )
                                            ]
                                        ),
                                        html.Div(
                                            className="list-col3",
                                            children=[
                                                html.H2(children="NAME"),
                                                html.Div(
                                                    className="artist-name-container",
                                                    children=[
                                                        html.P(top_artists['artist'][0])
                                                    ]
                                                ),
                                                html.Div(
                                                    className="song-name-container",
                                                    children=[
                                                        html.P(top_artists['artist'][1])
                                                    ]
                                                ),
                                                html.Div(
                                                    className="song-name-container",
                                                    children=[
                                                        html.P(top_artists['artist'][2])
                                                    ]
                                                ),
                                                html.Div(
                                                    className="song-name-container",
                                                    children=[
                                                        html.P(top_artists['artist'][3])
                                                    ]
                                                ),
                                                html.Div(
                                                    className="song-name-container",
                                                    children=[
                                                        html.P(top_artists['artist'][4])
                                                    ]
                                                )
                                            ]
                                        ),
                                        html.Div(
                                            className="list-col4",
                                            children=[
                                                html.H2(children="PLAYTIME"),
                                                html.Div(
                                                    className="artist-playtime-container",
                                                    children=[
                                                        html.P(top_artists['time_played'][0])
                                                    ]
                                                ),
                                                html.Div(
                                                    className="artist-playtime-container",
                                                    children=[
                                                        html.P(top_artists['time_played'][1])
                                                    ]
                                                ),
                                                html.Div(
                                                    className="artist-playtime-container",
                                                    children=[
                                                        html.P(top_artists['time_played'][2])
                                                    ]
                                                ),
                                                html.Div(
                                                    className="artist-playtime-container",
                                                    children=[
                                                        html.P(top_artists['time_played'][3])
                                                    ]
                                                ),
                                                html.Div(
                                                    className="artist-playtime-container",
                                                    children=[
                                                        html.P(top_artists['time_played'][4])
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                html.Div(
                    id="column2",
                    children=[
                        html.H1(children="TOP SONGS"),
                        html.Div(
                            className="list-container",
                            children=[
                                html.Div(
                                    className="list-col1",
                                    children=[
                                        html.H2(children="#"),
                                        html.Div(
                                            className="song-num-container",
                                            children=[
                                                html.P("1")
                                            ]
                                        ),
                                        html.Div(
                                            className="song-num-container",
                                            children=[
                                                html.P("2")
                                            ]
                                        ),
                                        html.Div(
                                            className="song-num-container",
                                            children=[
                                                html.P("3")
                                            ]
                                        ),
                                        html.Div(
                                            className="song-num-container",
                                            children=[
                                                html.P("4")
                                            ]
                                        ),
                                        html.Div(
                                            className="song-num-container",
                                            children=[
                                                html.P("5")
                                            ]
                                        ),
                                        html.Div(
                                            className="song-num-container",
                                            children=[
                                                html.P("6")
                                            ]
                                        ),
                                        html.Div(
                                            className="song-num-container",
                                            children=[
                                                html.P("7")
                                            ]
                                        ),
                                        html.Div(
                                            className="song-num-container",
                                            children=[
                                                html.P("8")
                                            ]
                                        ),
                                        html.Div(
                                            className="song-num-container",
                                            children=[
                                                html.P("9")
                                            ]
                                        ),
                                        html.Div(
                                            className="song-num-container",
                                            children=[
                                                html.P("10")
                                            ]
                                        )
                                    ]
                                ),
                                html.Div(
                                    className="list-col2",
                                    children=[
                                        html.H2(children="ART"),
                                        html.Div(
                                            className="song-art-container",
                                            children=[
                                                html.Img(
                                                    id="image11",
                                                    src = './assets/artwork0.png',
                                                    style={
                                                        'max-width':'100%',
                                                        'max-height':'100%'
                                                    }
                                                )
                                            ]
                                        ),
                                        html.Div(
                                            className="song-art-container",
                                            children=[
                                                html.Img(
                                                    id="image12",
                                                    src='./assets/artwork1.png',
                                                    style={
                                                        'max-width': '100%',
                                                        'max-height': '100%'
                                                    }
                                                )
                                            ]
                                        ),
                                        html.Div(
                                            className="song-art-container",
                                            children=[
                                                html.Img(
                                                    id="image13",
                                                    src='./assets/artwork2.png',
                                                    style={
                                                        'max-width': '100%',
                                                        'max-height': '100%'
                                                    }
                                                )
                                            ]
                                        ),
                                        html.Div(
                                            className="song-art-container",
                                            children=[
                                                html.Img(
                                                    id="image14",
                                                    src='./assets/artwork3.png',
                                                    style={
                                                        'max-width': '100%',
                                                        'max-height': '100%'
                                                    }
                                                )
                                            ]
                                        ),
                                        html.Div(
                                            className="song-art-container",
                                            children=[
                                                html.Img(
                                                    id="image15",
                                                    src='./assets/artwork4.png',
                                                    style={
                                                        'max-width': '100%',
                                                        'max-height': '100%'
                                                    }
                                                )
                                            ]
                                        ),
                                        html.Div(
                                            className="song-art-container",
                                            children=[
                                                html.Img(
                                                    id="image6",
                                                    src='./assets/artwork5.png',
                                                    style={
                                                        'max-width': '100%',
                                                        'max-height': '100%'
                                                    }
                                                )
                                            ]
                                        ),
                                        html.Div(
                                            className="song-art-container",
                                            children=[
                                                html.Img(
                                                    id="image7",
                                                    src='./assets/artwork6.png',
                                                    style={
                                                        'max-width': '100%',
                                                        'max-height': '100%'
                                                    }
                                                )
                                            ]
                                        ),
                                        html.Div(
                                            className="song-art-container",
                                            children=[
                                                html.Img(
                                                    id="image8",
                                                    src='./assets/artwork7.png',
                                                    style={
                                                        'max-width': '100%',
                                                        'max-height': '100%'
                                                    }
                                                )
                                            ]
                                        ),
                                        html.Div(
                                            className="song-art-container",
                                            children=[
                                                html.Img(
                                                    id="image9",
                                                    src='./assets/artwork8.png',
                                                    style={
                                                        'max-width': '100%',
                                                        'max-height': '100%'
                                                    }
                                                )
                                            ]
                                        ),
                                        html.Div(
                                            className="song-art-container",
                                            children=[
                                                html.Img(
                                                    id="image10",
                                                    src='./assets/artwork9.png',
                                                    style={
                                                        'max-width': '100%',
                                                        'max-height': '100%'
                                                    }
                                                )
                                            ]
                                        )
                                    ]
                                ),
                                html.Div(
                                    className="list-col3",
                                    children=[
                                        html.H2(children="TITLE"),
                                        html.Div(
                                            className="song-name-container",
                                            children=[
                                                html.P(top_songs['trackName'][0])
                                            ]
                                        ),
                                        html.Div(
                                            className="song-name-container",
                                            children=[
                                                html.P(top_songs['trackName'][1])
                                            ]
                                        ),
                                        html.Div(
                                            className="song-name-container",
                                            children=[
                                                html.P(top_songs['trackName'][2])
                                            ]
                                        ),
                                        html.Div(
                                            className="song-name-container",
                                            children=[
                                                html.P(top_songs['trackName'][3])
                                            ]
                                        ),
                                        html.Div(
                                            className="song-name-container",
                                            children=[
                                                html.P(top_songs['trackName'][4])
                                            ]
                                        ),
                                        html.Div(
                                            className="song-name-container",
                                            children=[
                                                html.P(top_songs['trackName'][5])
                                            ]
                                        ),
                                        html.Div(
                                            className="song-name-container",
                                            children=[
                                                html.P(top_songs['trackName'][6])
                                            ]
                                        ),
                                        html.Div(
                                            className="song-name-container",
                                            children=[
                                                html.P(top_songs['trackName'][7])
                                            ]
                                        ),
                                        html.Div(
                                            className="song-name-container",
                                            children=[
                                                html.P(top_songs['trackName'][8])
                                            ]
                                        ),
                                        html.Div(
                                            className="song-name-container",
                                            children=[
                                                html.P(top_songs['trackName'][9])
                                            ]
                                        )
                                    ]
                                ),
                                html.Div(
                                    className="list-col4",
                                    children=[
                                        html.H2(children="PLAYTIME"),
                                        html.Div(
                                            className="song-playtime-container",
                                            children=[
                                                html.P(top_songs['total_ms_played'][0])
                                            ]
                                        ),
                                        html.Div(
                                            className="song-playtime-container",
                                            children=[
                                                html.P(top_songs['total_ms_played'][1])
                                            ]
                                        ),
                                        html.Div(
                                            className="song-playtime-container",
                                            children=[
                                                html.P(top_songs['total_ms_played'][2])
                                            ]
                                        ),
                                        html.Div(
                                            className="song-playtime-container",
                                            children=[
                                                html.P(top_songs['total_ms_played'][3])
                                            ]
                                        ),
                                        html.Div(
                                            className="song-playtime-container",
                                            children=[
                                                html.P(top_songs['total_ms_played'][4])
                                            ]
                                        ),
                                        html.Div(
                                            className="song-playtime-container",
                                            children=[
                                                html.P(top_songs['total_ms_played'][5])
                                            ]
                                        ),
                                        html.Div(
                                            className="song-playtime-container",
                                            children=[
                                                html.P(top_songs['total_ms_played'][6])
                                            ]
                                        ),
                                        html.Div(
                                            className="song-playtime-container",
                                            children=[
                                                html.P(top_songs['total_ms_played'][7])
                                            ]
                                        ),
                                        html.Div(
                                            className="song-playtime-container",
                                            children=[
                                                html.P(top_songs['total_ms_played'][8])
                                            ]
                                        ),
                                        html.Div(
                                            className="song-playtime-container",
                                            children=[
                                                html.P(top_songs['total_ms_played'][9])
                                            ]
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                html.Div(
                    id="column3",
                    children=[
                        html.Div(
                            id="day-container",
                            children=[
                                html.H1(children="DAY BREAKDOWN"),
                                dcc.Graph(
                                    id="day-plot",
                                    figure=day_data_plot
                                )
                            ]
                        ),
                        html.Div(
                            id="time-container",
                            children=[
                                html.H1(children="TIME BREAKDOWN"),
                                dcc.Graph(
                                    id="time-plot",
                                    figure=time_data_plot
                                )
                            ]
                        )
                    ]
                )
            ]
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
