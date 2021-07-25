# Images
from __future__ import print_function
from PIL import Image
from io import BytesIO

# Web-scraping
from bs4 import BeautifulSoup
import requests

# OS
import os

# Data
import pandas as pd
import datetime
import json

# Strings
import re

# Numpy
import numpy as np

# Plotting
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

# Saving data
import pickle

# Read streaming history(sh) json files into a pandas dataframe
def get_data(path_to_json = './MyData/'):
    json_files = [sh for sh in os.listdir(path_to_json) if sh.startswith('StreamingHistory')]

    streaming_history = pd.DataFrame(columns=['endTime', 'artistName', 'trackName', 'msPlayed'])

    for js in json_files:
        with open(os.path.join(path_to_json, js)) as json_file:
            json_text = pd.read_json(json_file)
            streaming_history = pd.concat([streaming_history, json_text])

    streaming_history['endTime'] = pd.to_datetime(streaming_history['endTime'])

    return streaming_history

def ms_to_time(data):
    return data.apply(lambda x: datetime.timedelta(milliseconds=x))

def time_to_string(data):
    return data.apply(lambda x: str(x)[7:9]+" hours "+str(x)[10:12]+" mins")


def get_top_songs(data):
    grouped_df = data[['trackName', 'msPlayed', 'artistName']].groupby(['trackName', 'artistName'])
    df = pd.DataFrame({'count': grouped_df.size(),
                       'total_ms_played': grouped_df.agg({'msPlayed': 'sum'})['msPlayed']}
                      ).reset_index()
    df = df.sort_values('total_ms_played', ascending=False)
    df['total_ms_played'] = ms_to_time(df['total_ms_played'])
    df['total_ms_played'] = time_to_string(df['total_ms_played'])
    return df


"""# Test get top songs
print(get_top_songs(streaming_history).head(5))"""


def get_top_artists(data):
    grouped_df = data.groupby(['artistName'])
    df = pd.DataFrame(
        dict(
            total_ms_played=grouped_df.agg({'msPlayed': 'sum'})['msPlayed']
        )
    ).reset_index()
    df.columns = ['artist', 'time_played']
    df = df.sort_values('time_played', ascending=False).head(5)
    df['time_played'] = ms_to_time(df['time_played'])
    df['time_played'] = time_to_string(df['time_played'])
    return df


"""# Test top artists
print(get_top_artists(streaming_history).head(20))"""


def get_genius_url_format(track_name, artist_name):
    if ' (' in track_name:
        if len(track_name.split(' (')) == 2:
            song, feature = track_name.split(' (')
        if len(track_name.split(' (')) != 2:
            song, feature = "",""
        words = ('feat.', 'with')
        if not feature.startswith(words):
            collabs = re.sub('[^A-Za-z0-9]+', ' ', feature)
            a = '-'.join(c for c in collabs.split(' '))
            a = a[:-1]
            index = a.rfind('-')
            artists = a[:index] + '-And' + a[index:]
        else:
            artists = artist_name.replace(' ', '-')
    else:
        song = track_name
        artists = artist_name.replace(' ', '-')

    song = re.sub('[^A-Za-z0-9]+', '-', song)
    return artists + '-' + song


"""# Test get_genius_url_format
print(streaming_history[['trackName','artistName']].head(40))
print(streaming_history[['trackName','artistName']].head(40).
      apply(lambda x: get_genius_url_format(x[0],x[1]), axis=1))"""

# Get song artwork
def get_genius_image(entry):
    trackName, artistName = entry[0], entry[1]
    url = 'https://genius.com/' + get_genius_url_format(trackName, artistName) + '-lyrics'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, features="html.parser")
    images = soup.findAll('img')
    image_src = images[0]['src']
    response = requests.get(image_src)
    return Image.open(BytesIO(response.content))


"""# Test get image
x = 0
for index, row in streaming_history.iterrows():
    get_genius_image(row).show()
    x += 1
    if x == 5:
        break"""


def get_song_genre(entry):
    artistName, trackName = entry[1], entry[0]
    song = get_genius_url_format(trackName, artistName)
    google_search = 'https://www.google.com/search?q=' + song + '-genre'
    page = requests.get(google_search)
    soup = BeautifulSoup(page.text, features='html.parser')
    text = soup.find_all(text=True)
    if 'Genre' in text:
        indx = text.index('Genre')
        genre = text[indx + 1]
        return genre
    else:
        return None


"""
# Test get song genre:
x = 0
for index, row in streaming_history.iterrows():
    print(get_song_genre(row))
    x += 1
    if x == 10:
        break"""


def get_day_data(data):
    dates = data['endTime'].apply(lambda x: datetime.datetime.date(x))
    unique_dates = dates.unique()
    dates_as_weekdays = np.array([datetime.datetime.weekday(x) for x in unique_dates])
    day_count = {}
    for day in dates_as_weekdays:
        if day in day_count.keys():
            day_count[day] += 1
        else:
            day_count[day] = 1
    count = np.array([c for c in day_count.values()])
    data['weekday'] = data['endTime'].apply(lambda x: datetime.datetime.weekday(x))
    grouped_by_day = data.groupby(['weekday'])
    day_data = pd.DataFrame(dict(
        total_ms_played=grouped_by_day.agg({'msPlayed': 'sum'})['msPlayed']
    )).reset_index()
    day_data['count'] = count
    day_data['avg_minutes_played'] = round(day_data['total_ms_played'] / (60000 * day_data['count']), 2)
    return day_data


def get_hour(time):
    return int(str(time).split(':')[0])


def get_time_data(data):
    data['time'] = data['endTime'].apply(lambda x: datetime.datetime.time(x))
    data['time'] = data['time'].apply(lambda x: get_hour(x))
    data['msPlayed'] = pd.to_numeric(data['msPlayed'])
    grouped_by_time = data.groupby(['time'])
    time_data = pd.DataFrame(
        dict(
            total_time_played=grouped_by_time.agg({'msPlayed':'sum'})['msPlayed']
        )
    ).reset_index()
    time_data['total_time_played'] = time_data['total_time_played'].apply(lambda x: round(x/60000,0))
    return time_data

"""# Test get time data
print(get_time_data(streaming_history))"""

def get_artist_picture(artist):
    artist = artist.replace(' ','-')
    genius_search = 'https://www.genius.com/artists/' + artist
    page = requests.get(genius_search)
    soup = BeautifulSoup(page.text, features='html.parser')
    images = soup.findAll('img')
    image_src = images[0]['src']
    response = requests.get(image_src)
    return Image.open(BytesIO(response.content))

def save_image(image, fp):
    image.save(fp=fp,format='png')

def save_data(data, fp):
    data.to_csv(fp)


times = np.array([
    "00:00-01:00","01:00-02:00","02:00-03:00","03:00-04:00","04:00-05:00","05:00-06:00",
    "06:00-07:00","07:00-08:00","08:00-09:00","09:00-10:00","10:00-11:00","11:00-12:00",
    "12:00-13:00","13:00-14:00","14:00-15:00","15:00-16:00","16:00-17:00","17:00-18:00",
    "18:00-19:00","19:00-20:00","20:00-21:00","21:00-22:00","22:00-23:00","23:00-00:00"
])

def plot_time_data(data):
    hour_data = get_time_data(data)
    fig = px.bar(hour_data,
                 x=times,
                 y="total_time_played",
                 labels=dict(
                     total_time_played = "Total Time Played (mins)",
                     time = "Time of day"
                 ))
    fig.update_layout(xaxis_title = "Time of Day",
                      hoverlabel=dict(
                          bgcolor="white",
                          font_size=12
                      ),
                      plot_bgcolor = "rgba(0, 0, 0, 0)",
                      paper_bgcolor = "rgba(0, 0, 0, 0)"
                      )
    fig.update_traces(marker_color='#1DB954')
    return fig

days = np.array(["Mon","Tues","Wed","Thurs","Fri","Sat","Sun"])
def plot_day_data(data):
    day_data = get_day_data(data)
    fig = px.bar(day_data,
                 x=days,
                 y="avg_minutes_played",
                 labels=dict(
                     avg_minutes_played="Avg Time Played (mins)",
                     weekday="Day"
                 ))
    fig.update_layout(xaxis_title="Day of the Week",
                      hoverlabel=dict(
                          bgcolor="white",
                          font_size=12
                      ),
                      plot_bgcolor="rgba(0, 0, 0, 0)",
                      paper_bgcolor="rgba(0, 0, 0, 0)"
                      )
    fig.update_traces(marker_color='#1DB954')
    return fig

def main():

    stream_data = get_data()
    save_data(stream_data, "./assets/stream_data.csv")
    top_songs = get_top_songs(stream_data)
    """
    save_data(top_songs, "./assets/top_songs.csv")
    # save top song artwork
    num = 0
    for index, row in top_songs.head(10).iterrows():
        img = get_genius_image(row)
        fp = './assets/artwork{i}.png'.format(i=num)
        save_image(img, fp)
        num += 1"""
    top_artists = get_top_artists(stream_data)
    """num = 0
    for index, row in top_artists.iterrows():
        img = get_artist_picture(row[0])
        fp = './assets/artist{i}.png'.format(i=num)
        save_image(img, fp)
        num += 1"""
    genres = {}
    for index, row in top_songs.head(1000).iterrows():
        genre = get_song_genre(row)
        print(genre)
        if genre is not None:
            if genre in genres:
                genres[genre] += 1
            else:
                genres[genre] = 1

    genre_data = pd.DataFrame.from_dict(genres)
    save_data(genre_data, "./assets/genre_data.csv")
    #save_data(top_artists, "./assets/top_artists.csv")



if __name__ == "__main__":
    main()
