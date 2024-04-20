-- drop all subsystem tables and the database for mariadb

-- drop tables if they exist
drop table if exists acds_control;
drop table if exists acds_sense_magnetorque;
drop table if exists acds_reaction_wheel;
drop table if exists comms_437_mhz_rx;
drop table if exists comms_437_mhz_tx;
drop table if exists comms_2408_mhz_tx;
drop table if exists camera_mantis;
drop table if exists sipm;
drop table if exists sp_cam;
drop table if exists tuna_cam;
drop table if exists obc;
drop table if exists eps;
drop table if exists deployment_panels_antennas;

-- drop the database
-- warning: this will remove the entire database, ensure this is the desired action!
drop database if exists your_database_name;

