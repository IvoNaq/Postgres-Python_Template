CREATE DATABASE docker;

\c docker;	
CREATE TABLE IF NOT EXISTS info_flag (
        flag VARCHAR ( 10 ),
        msg VARCHAR ( 200 )
        );	
	
CREATE TABLE IF NOT EXISTS cropstats (
	id INT,
	area VARCHAR ( 200 ),
	item_code INT,
	item VARCHAR ( 50 ),
	magnitud_code INT,
	magnitud VARCHAR ( 50 ),
	year_code INT,
	year INT,
	unit VARCHAR ( 10 ),
	value NUMERIC (15), 
	flag VARCHAR ( 10 )
	);
CREATE TABLE IF NOT EXISTS population (
	id INT,
	area VARCHAR ( 100 ),
	esc_id INT,
	esc VARCHAR ( 100 ),
	year INT,
	year_mid DECIMAL,
	popmale DECIMAL,
	popfemale DECIMAL,
	poptotal DECIMAL,
	popdensity DECIMAL
        );

