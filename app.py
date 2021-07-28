# Gui functions
from tkinter import *
from tkinter import filedialog
# Spotify functions
import analysis as sf

# Gui to get path to spotify data directory
def get_directory():
    root = Tk()
    root.withdraw()
    path = filedialog.askdirectory(title="Choose path to spotify data folder")
    return path

def main():
    path = get_directory()+"/"
    stream_data = sf.get_data(path_to_json=path)

    if stream_data is not None:
        sf.save_data(stream_data, "./assets/stream_data.csv")

        top_songs = sf.get_top_songs(stream_data)
        sf.save_data(top_songs, "./assets/top_songs.csv")

        # save top song artwork
        num = 0
        for index, row in top_songs.head(10).iterrows():
            img = sf.get_genius_image(row)
            fp = './assets/artwork{i}.png'.format(i=num)
            sf.save_image(img, fp)
            num += 1

        top_artists = sf.get_top_artists(stream_data)
        sf.save_data(top_artists, "./assets/top_artists.csv")

        # Save artist artwork
        num = 0
        for index, row in top_artists.iterrows():
            img = sf.get_artist_picture(row[0])
            fp = './assets/artist{i}.png'.format(i=num)
            sf.save_image(img, fp)
            num += 1
    else:
        return None

if __name__ == "__main__":
    main()
    exec(open('dashboard.py').read())
