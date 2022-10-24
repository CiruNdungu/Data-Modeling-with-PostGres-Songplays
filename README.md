
**PURPOSE**

The purpose of the project is to write an ETL pipeline that transfers data from log files in JSON format and real data from the 'million song dataset', into Postgres database tables to allow effective data analysis by a music startup, Sparkify. This will allow Sparkify to gain insights into their user behaviors to improve their service to them.

**SCHEMA**
A fact table (songplays) is used together with dimension tables (users, songs, artists and time) to create a star schema optimized for queries for data analysis.

![image](https://user-images.githubusercontent.com/116004104/197465221-4a14d0d6-bb2c-4aa0-9004-1db8d3d71363.png)



**Fact Table**
**songplays** - records in log data associated with song plays i.e. records with page NextSong

 •	songplay_id (SERIAL CONSTRAINT songplay_pk) PRIMARY KEY: ID of each song play
 •	start_time (TIMESTAMP) REFERENCES time (start_time) NOT NULL: beginning of user activity
 •	user_id (INT) RFERENCES users (user_id) NOT NULL: ID of user
 •	level (VARCHAR): User level either free or paid
 •	song_id (VARCHAR) NOT NULL: ID of song played

•	artist_id (VARCHAR) NOT NULL: ID of the artist of the song played
•	session_id (INT): ID of the user session
•	location (VARCHAR): Location of the user
•	user_agent (VARCHAR): Agent used by user to access the Sparkify platform

![songplay](https://user-images.githubusercontent.com/116004104/197466106-40891804-4c14-40d1-87f0-80cdbd96c588.png)

 
**Dimension Tables**
**songs** - songs in music database
•	song_id (VARCHAR CONSTRAINT songs_pk) PRIMARY KEY: ID of Song
•	title (VARCHAR) NOT NULL: Title of Song
•	artist_id (VARCHAR) NOT NULL: ID of song Artist
•	year (INT): Year of song release
•	duration (FLOAT) NOT NULL: Duration of song in milliseconds
 
![songs](https://user-images.githubusercontent.com/116004104/197466129-a95aa62d-7568-4d90-805b-2cf0ccd0c219.png)



**artists** - artists in music database
•	artist_id (VARCHAR CONSTRAINT artists_pk) PRIMARY KEY: ID of the artist
•	name (VARCHAR) NOT NULL: Artist’s name
•	location (VARCHAR): Name of Artists city
•	latitude (FLOAT): Latitude location of artist
•	longitude (FLOAT): Longitude location of artist
 
![artists](https://user-images.githubusercontent.com/116004104/197466159-dbd2d61c-482b-48a9-b84d-c3c84d89e33a.png)

**time** - timestamps of records in songplays 
•	start_time (TIMESTAMP) PRIMARY KEY: Timestamp
•	hour (SMALLINT) NOT NULL: Hour of start_time
•	day (SMALLINT) NOT NULL: Day of start_time
•	week (SMALLINT) NOT NULL: Week of year for start_time
•	month (SMALLINT) NOT NULL: Month of start_time
•	year (SMALLINT) NOT NULL: Year of start_time
•	weekday (SMALLINT) NOT NULL: Name of weekday of start_time

 ![time](https://user-images.githubusercontent.com/116004104/197466190-c7dd5084-cef2-4beb-b580-6986cb02c029.png)

**users** - users in the app
•	user_id (INT) CONSTRIANT users_pk PRIMARY KEY: ID of user
•	first_name (VARCHAR): First name of user
•	last_name (VARCHAR): Last Name of user
•	gender (VARCHAR): users gender (M | F)
•	level (VARCHAR): User level (free | paid)

 ![users](https://user-images.githubusercontent.com/116004104/197466204-b593d7c2-3425-4a6b-a649-ad7b292f4706.png)


**ETL PIPELINE**
ETL is performed on the files on the songs_data directory to create two dimension tables (songs and artists).
We extracted data for the songs and artists table, using the columns as guided by the star schema.
The data was then inserted into the respective tables using the queries on the sql_queries.py file.
ETL was also performed on the log data directory to create the other dimension tables (time and users)
The timestamp column was extracted from the 'time' table and was used to create the additional column as per the schema guide.
The appropriate columns were also extracted from the log files as per the star schema guide.
The data was then loaded into the respective tables.

**ETL procedure**
1. Run the create_tables.py to create the database and the tables from the terminal
2. Run test.ipynb to confirm creation of the tables with the correct columns.
3. Run etl.ipynb to process a single file from song_data and log_data then load data onto the tables. Run etl.py to read and process the files from the song_data and log_data files and load the rest of the rows onto the tables.
4. Run test.ipynb to confirm the records were successfully inserted into each table


**END**
A postgres database with fact tables and dimension tables was created to perform song play anaysis and the data loaded successfully.









