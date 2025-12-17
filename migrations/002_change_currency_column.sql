ALTER TABLE crypto_news
ALTER COLUMN currency TYPE TEXT;

-- After close look I noticed that it shouldn't be varchar(3) because there are names more than 
-- 3 characters long  
