\c docker
COPY info_flag(flag,msg)
FROM '/var/lib/postgresql/Crops_flags.csv'
DELIMITER ','
CSV HEADER;


COPY cropstats(id, area, item_code,item,magnitud_code,magnitud,year_code,year,unit,value,flag)
FROM '/var/lib/postgresql/Crops_AllData_Normalized.csv'
DELIMITER ','
CSV HEADER
ENCODING 'LATIN1';

COPY population(id, area,esc_id,esc,year,year_mid,popmale,popfemale,poptotal,popdensity)
FROM '/var/lib/postgresql/Total_Population_All_Countries.csv'
DELIMITER ','
CSV HEADER;
