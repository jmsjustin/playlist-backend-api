import sqlite3


def connect_to_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def initial_setup():
    conn = connect_to_db()
    conn.execute(
        """
        DROP TABLE IF EXISTS songs;
        """
    )
    conn.execute(
        """
        CREATE TABLE songs (
          id INTEGER PRIMARY KEY NOT NULL,
          title TEXT,
          artist TEXT,
          album TEXT,
          url TEXT
        );
        """
    )
    conn.commit()
    print("Table created successfully")

    songs_seed_data = [
        ("Little Lamb", "Mother Goose", "The B Side", "test.test"),
        ("Test", "The Testers", "The A Side", "example.test"),
        ("Baby Shark", "Pink Fong", "Underwater Sessions", "test.test"),
        ("Daddy Shark", "Pink Fong", "Underwater Sessions", "sharks.test")
    ]
    conn.executemany(
        """
        INSERT INTO songs (title, artist, album, url)
        VALUES (?,?,?,?)
        """,
        songs_seed_data,
    )
    conn.commit()
    print("Seed data created successfully")

    conn.close()


if __name__ == "__main__":
    initial_setup()