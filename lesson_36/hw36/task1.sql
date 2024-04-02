
ATTACH DATABASE "taskDB.db" AS taskDB;

CREATE TABLE test_table(
    new_column varchar
);

INSERT INTO test_table
VALUES ("test1");

INSERT INTO test_table
VALUES ("test2");

INSERT INTO test_table
VALUES ("test3");

UPDATE test_table
SET new_column = "test0"
WHERE new_column = "test1";

DELETE from test_table
WHERE new_column = "test3";