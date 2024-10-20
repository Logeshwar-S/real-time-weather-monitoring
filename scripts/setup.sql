-- Create the weather_db database
CREATE DATABASE IF NOT EXISTS weather_db;

-- Use the weather_db database
USE weather_db;

-- Create a table to store daily weather summaries
CREATE TABLE IF NOT EXISTS weather_summary (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(100),
    date DATE,
    avg_temp FLOAT,
    max_temp FLOAT,
    min_temp FLOAT,
    dominant_condition VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create a table to store weather alerts
CREATE TABLE IF NOT EXISTS weather_alerts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(100),
    alert_message TEXT,
    alert_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
