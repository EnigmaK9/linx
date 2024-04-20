-- Run all subsystem table creation scripts for MariaDB

-- Control and Orientation Systems
source 01-acds_control.sql;
source 02-acds_sense_magnetorque.sql;
source 03-acds_reaction_wheel.sql;

-- Communication Systems
source 04-comms_437_mhz_rx.sql;
source 05-comms_437_mhz_tx.sql;
source 06-comms_2408_mhz_tx.sql;

-- Imaging and Sensors
source 07-camera_mantis.sql;
source 08-sipm.sql;
source 09-sp_cam.sql;
source 10-tuna_cam.sql;

-- On-board Control and Power Systems
source 11-obc.sql;
source 12-eps.sql;
source 13-deployment_panels_antennas.sql;


