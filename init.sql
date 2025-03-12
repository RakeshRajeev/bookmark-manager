-- Create role and database
CREATE USER postgres WITH PASSWORD 'postgres' CREATEDB;
ALTER ROLE postgres WITH LOGIN;

-- Create database if not exists
CREATE DATABASE bookmark_manager;
GRANT ALL PRIVILEGES ON DATABASE bookmark_manager TO postgres;

-- Connect to the database
\c bookmark_manager

-- Create extensions if needed
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
