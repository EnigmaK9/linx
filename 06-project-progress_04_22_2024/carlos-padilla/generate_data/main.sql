-- Run all subsystem table creation scripts for MariaDB

-- Control and Orientation Systems
source acds_control.sql;
source acds_sense_magnetorque.sql;
source acds_reaction_wheel.sql;

-- Communication Systems
source comms_437_mhz_rx.sql;
source comms_437_mhz_tx.sql;
source comms_2408_mhz_tx.sql;

-- Imaging and Sensors
source camera_mantis.sql;
source sipm.sql;
source sp_cam.sql;
source tuna_cam.sql;

-- On-board Control and Power Systems
source obc.sql;
source eps.sql;
source deployment_panels_antennas.sql;

