
# DROP TABLES
songplay_table_drop = ("DROP TABLE IF EXISTS songplays")
user_table_drop = ("DROP TABLE IF EXISTS users")
song_table_drop = ("DROP TABLE IF EXISTS songs")
artist_table_drop = ("DROP TABLE IF EXISTS artists")
time_table_drop = ("DROP TABLE IF EXISTS time")

   
    
# CREATE TABLES
##Fact table = songplays

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS Songplays(
        songplay_id SERIAL CONSTRAINT songplay_pk PRIMARY KEY,
        start_time TIMESTAMP REFERENCES time (start_time), 
        user_id INT REFERENCES users (user_id), 
        level VARCHAR(24), 
        song_id VARCHAR(50) REFERENCES songs (song_id) NOT NULL, 
        artist_id VARCHAR(50) REFERENCES artists (artist_id) NOT NULL, 
        session_id INT NOT NULL, 
        location VARCHAR(50), 
        user_agent VARCHAR);""")


##Dimension table = 'users'
user_table_create = ("""CREATE TABLE IF NOT EXISTS users(
        user_id INT CONSTRAINT users_pk PRIMARY KEY,
        first_name VARCHAR(256) NOT NULL,
        last_name VARCHAR(256) NOT NULL,
        gender VARCHAR,
        level VARCHAR(24))""")



##Dimension table = 'songs'
song_table_create = ("""CREATE TABLE IF NOT EXISTS songs(
        song_id VARCHAR CONSTRAINT songs_pk PRIMARY KEY,
        title VARCHAR NOT NULL,
        artist_id VARCHAR NOT NULL,
        year INT,
        duration DECIMAL NOT NULL)""")

    
##Dimension table = 'artists'
artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists(
        artist_id VARCHAR(24) CONSTRAINT artists_pk PRIMARY KEY,
        name VARCHAR(256) NOT NULL,
        location VARCHAR(256),
        latitude FLOAT,
        longitude FLOAT)""")
    
    
##Dimension table = 'time'
time_table_create =  ("""CREATE TABLE IF NOT EXISTS time(
        start_time timestamp PRIMARY KEY,
        hour SMALLINT NOT NULL,
        day SMALLINT NOT NULL,
        week SMALLINT NOT NULL,
        month SMALLINT NOT NULL,
        year SMALLINT NOT NULL,
        weekday SMALLINT NOT NULL)""")


# INSERT RECORDS
songplay_table_insert = ("""INSERT INTO songplays(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (songplay_id) DO NOTHING"""
    )
   
    
user_table_insert = ("""INSERT INTO users(
    user_id, first_name, last_name, gender, level)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id)
    DO UPDATE SET level = EXCLUDED.level"""
    )
    
    
    
song_table_insert = ("""INSERT INTO songs(
    song_id, title, artist_id, year, duration)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (song_id) DO NOTHING """
    )

artist_table_insert = ("""INSERT INTO artists(
    artist_id, name, location, latitude, longitude)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id) DO NOTHING"""
    )


time_table_insert = ("""INSERT INTO time(
    start_time, hour, day, week, month, year, weekday)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time) DO NOTHING"""
    )

          

# FIND SONGS
song_select = ("""SELECT songs.song_id, artists.artist_id
    FROM songs JOIN artists ON songs.artist_id=artists.artist_id
    WHERE songs.title=%s 
    AND artists.name=%s 
    AND songs.duration=%s;
    ;""")
                

# QUERY LISTS
create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]