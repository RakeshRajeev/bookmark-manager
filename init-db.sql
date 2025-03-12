CREATE DATABASE bookmarks;

\c bookmarks;

-- Enable required extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Create users table indices
CREATE INDEX idx_users_email ON users(email);

-- Create bookmarks table indices
CREATE INDEX idx_bookmarks_slug ON bookmarks(slug);
CREATE INDEX idx_bookmarks_user_id ON bookmarks(user_id);
