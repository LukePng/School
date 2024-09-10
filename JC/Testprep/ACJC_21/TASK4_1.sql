CREATE TABLE Kiosk (
    KioskID INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
    Location TEXT,
    Rating REAL
);

CREATE TABLE BentoBox (
    BentoName TEXT UNIQUE PRIMARY KEY,
    ProductionCost REAL,
    ContainEgg INTEGER,
    ContainNut INTEGER,
    ContainSeafood INTEGER
);

CREATE TABLE KioskBento (
    KioskID INTEGER REFERENCES Kiosk(KioskID),
    BentoName TEXT REFERENCES BentoBox(BentoName),
    SellPrice REAL,
    PRIMARY KEY(KioskID, BentoName)
