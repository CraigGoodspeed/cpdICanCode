DROP TABLE Client;
CREATE TABLE `Client` (
	`ClientID`	INTEGER NOT NULL,
	`IDNumber`	TEXT,
	`Name`	TEXT,
	`Password`	TEXT,
	`Surname`	TEXT,
	PRIMARY KEY(`ClientID`)
);

DROP TABLE `ACCOUNT`;
CREATE TABLE `Account` (
	`AccountID`	INTEGER,
	`AccountNumber`	TEXT NOT NULL,
	`AccountType`	INTEGER DEFAULT 1,
	`ClientID`	INTEGER NOT NULL,
	`DateCreated`	INTEGER NOT NULL,
	PRIMARY KEY(`AccountID`),
	FOREIGN KEY(`ClientID`) REFERENCES `Client`(`ClientID`)
);


DROP TABLE `TRANSACTION`;
CREATE TABLE `Transaction` (
	`TransactionID`	INTEGER NOT NULL AUTOINCREMENT,
	`Date`	INTEGER NOT NULL,
	`Amount`	NUMERIC NOT NULL,
	`AccountID`	INTEGER NOT NULL,
	PRIMARY KEY(`TransactionID`),
	FOREIGN KEY (`AccountID`) references `ACCOUNT`(`ACCOUNTID`)
);


