USE alx_book_store
SELECT COLUMN_NAME, COLUMN_TYPE
FROM Information.schema.columns
WHERE TABLE_SCHEMA = "alx_book_store" AND TABLE_NAME = "Books";