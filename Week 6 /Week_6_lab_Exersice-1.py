songs = []
genre_count = {}
i = 0

print("Welcome to Music Library Manager! \n ")

while 5 > i:
    s = i + 1
    print(f"Enter Song {s}:")
    user_song = input("Song name:")
    user_genre = input("Genre:")
    songs.append((user_song, user_genre))
    print("")
    i += 1

for song_name, genre in songs:
    if genre in genre_count:
        genre_count[genre] += 1
    else:
        genre_count[genre] = 1

most_popular_genre = max(genre_count, key=genre_count.get)

print("=== YOUR MUSIC LIBRARY===")
for song_name, genre in songs:
    print(f"{song_name.capitalize()}({genre.capitalize()})")

print("\n===Genre STATISTICS===")
for genre, count in genre_count.items():
    print(f"{genre.capitalize()}:{count} songs")
print(f"Most popular genre: {most_popular_genre.capitalize()}")
