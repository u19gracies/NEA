import sqlite3

conn = sqlite3.connect('clientData.db')
curs = conn.cursor()

curs.execute('''
    CREATE TABLE IF NOT EXISTS tblSession (
        sessionID INTEGER PRIMARY KEY AUTOINCREMENT,
        playerCount INTEGER NOT NULL,
        region TEXT NOT NULL
    )
''')

curs.execute('''
    CREATE TABLE IF NOT EXISTS tblUsers (
        userID INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

curs.execute('''
    CREATE TABLE IF NOT EXISTS tblPlayerData (
        playerID INTEGER PRIMARY KEY AUTOINCREMENT,
        userID INTEGER NOT NULL,
        coordinates TUPLE NOT NULL,
        health INT NOT NULL,
        food INT NOT NULL,
        strength INT NOT NULL,
        velocity FLOAT NOT NULL,
        FOREIGN KEY (userID) REFERENCES tblUsers(userID)
    )
''')

curs.execute('''
    CREATE TABLE IF NOT EXISTS tblPlayerInventory (
        invID INTEGER PRIMARY KEY AUTOINCREMENT,
        gridNo INTEGER NOT NULL,
        itemID INTEGER NOT NULL,
        itemQuantity INTEGER NOT NULL,
        playerID INTEGER NOT NULL,
        FOREIGN KEY(playerID) REFERENCES tblPlayerData(playerID),
        FOREIGN KEY(itemID) REFERENCES tblItems(itemID)
    )
''')

curs.execute('''
    CREATE TABLE IF NOT EXISTS tblItems(
        itemID INTEGER PRIMARY KEY AUTOINCREMENT,
        itemName TEXT NOT NULL,
        itemType TEXT NOT NULL,
        qualities TEXT NOT NULL,
        desc TEXT NOT NULL,
        imgPath TEXT NOT NULL
    )
''')

conn.commit()