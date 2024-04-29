-- Enable foreign key constraint
pragma foreign_keys = on;

-- OBC table definition
create table obc (
    camera_id integer primary key,
    start_time text not null,
    end_time text not null,
    power real not null,
    voltage real not null,
    orbit integer not null,
    execution_priority integer not null
    -- Comments: The OBC table stores information about the On-Board Computer's operation times and power usage.
);

-- Multispectral Camera table definition
create table multispectral_camera (
    camera_id integer primary key,
    start_time text not null,
    end_time text not null,
    power real not null,
    voltage real not null,
    orbit integer not null,
    execution_priority integer not null,
    transmission_priority integer
    -- Comments: This table holds data for the multispectral camera operations.
);

-- Comms 437 MHz TX table definition
create table comms_437_mhz_tx (
    camera_id integer primary key,
    start_time text not null,
    end_time text not null,
    power real not null,
    voltage real not null,
    orbit integer not null,
    execution_priority integer not null,
    transmission_priority integer
    -- Comments: This table logs transmission details for the 437 MHz communication system.
);

-- Comms 2408 MHz TX table definition
create table comms_2408_mhz_tx (
    camera_id integer primary key,
    start_time text not null,
    end_time text not null,
    power real not null,
    voltage real not null,
    orbit integer not null,
    execution_priority integer not null,
    transmission_priority integer
    -- Comments: This table logs transmission details for the 2408 MHz communication system.
);

-- SiPM table definition
create table sipm (
    camera_id integer primary key,
    start_time text not null,
    end_time text not null,
    power real not null,
    voltage real not null,
    orbit integer not null,
    execution_priority integer not null,
    transmission_priority integer
    -- Comments: The SiPM table contains information on the Silicon Photomultiplier's operations.
);


-- ACS Sense Magnetorque table definition
create table acds_sense_magnetorque (
    id integer primary key,
    start_time text not null,
    end_time text not null,
    power real not null,
    voltage real not null,
    orbit integer not null,
    execution_priority integer not null,
    transmission_priority integer,
    -- Additional attributes for Magnetotorque specific information
    magnetometer_data real not null,
    torque_data real not null
    -- Comments: This table stores magnetometer and torque data for the Attitude Control System.
);


-- ACS Reaction Wheel table definition
create table acds_reaction_wheel (
    id integer primary key,
    start_time text not null,
    end_time text not null,
    power real not null,
    voltage real not null,
    orbit integer not null,
    execution_priority integer not null,
    transmission_priority integer,
    -- Additional attributes for Reaction Wheel specific information
    wheel_speed real not null,
    wheel_position real not null
    -- Comments: This table holds operational data for the reaction wheels in the Attitude Control System.
);


-- Comms 437 MHz RX table definition
create table comms_437_mhz_rx (
    id integer primary key,
    start_time text not null,
    end_time text not null,
    power real not null,
    voltage real not null,
    orbit integer not null,
    execution_priority integer not null,
    transmission_priority integer,
    -- Additional attributes for 437 MHz RX specific information
    received_data blob not null,
    signal_strength real not null
    -- Comments: The table logs reception details for the 437 MHz communication system.
);


-- SP-CAM table definition
create table sp_cam (
    id integer primary key,
    start_time text not null,
    end_time text not null,
    power real not null,
    voltage real not null,
    orbit integer not null,
    execution_priority integer not null,
    transmission_priority integer,
    -- Additional attributes for SP-CAM specific information
    image_data blob not null,
    image_metadata text not null
    -- Comments: This table is for storing images and related metadata captured by the SP-CAM.
);


-- TUNA-CAM table definition
create table tuna_cam (
    id integer primary key,
    start_time text not null,
    end_time text not null,
    power real not null,
    voltage real not null,
    orbit integer not null,
    execution_priority integer not null,
    transmission_priority integer,
    -- Additional attributes for TUNA-CAM specific information
    image_data blob not null,
    image_metadata text not null
    -- Comments: This table is for storing images and related metadata captured by the TUNA-CAM.
);


-- Electrical Power System (EPS) table definition
create table electrical_power_system (
    id integer primary key,
    start_time text not null,
    end_time text not null,
    power real not null,
    voltage real not null,
    orbit integer not null,
    execution_priority integer not null,
    transmission_priority integer,
    -- Additional attributes for EPS specific information
    battery_level real not null,
    power_consumption real not null
    -- Comments: This table logs the battery levels and power consumption of the satellite's electrical power system.
);


-- Deployment Panels and Antennas table definition
create table deployment_panels_antennas (
    id integer primary key,
    start_time text not null,
    end_time text not null,
    power real not null,
    voltage real not null,
    orbit integer not null,
    execution_priority integer not null,
    transmission_priority integer,
    -- Additional attributes for Deployment Panels and Antennas specific information
    panel_status text not null,
    antenna_status text not null
    -- Comments: This table stores the deployment status of panels and antennas on the satellite.
);

-- Nanosatellite reference table definition
create table nanosatellite (
    obc_id integer,
    multispectral_camera_id integer,
    comms_437_mhz_tx_id integer,
    comms_2408_mhz_tx_id integer,
    comms_437_mhz_rx_id integer,
    acds_control_id integer,
    acds_sense_magnetorque_id integer,
    acds_reaction_wheel_id integer,
    sp_cam_id integer,
    tuna_cam_id integer,
    electrical_power_system_id integer,
    deployment_panels_antennas_id integer,
    sipm_id integer,
    -- Primary key consisting of all subsystems' IDs
    primary key (obc_id, multispectral_camera_id, comms_437_mhz_tx_id, comms_2408_mhz_tx_id, comms_437_mhz_rx_id, acds_control_id, acds_sense_magnetorque_id, acds_reaction_wheel_id, sp_cam_id, tuna_cam_id, electri_power_system_id, deployment_panels_antennas_id, sipm_id),
    -- Foreign keys that reference the primary keys in other tables
    foreign key (obc_id) references obc (camera_id),
    foreign key (multispectral_camera_id) references multispectral_camera (camera_id),
    foreign key (comms_437_mhz_tx_id) references comms_437_mhz_tx (camera_id),
    foreign key (comms_2408_mhz_tx_id) references comms_2408_mhz_tx (camera_id),
    foreign key (comms_437_mhz_rx_id) references comms_437_mhz_rx (id),
    foreign key (acds_control_id) references acds_control (id),
    foreign key (acds_sense_magnetorque_id) references acds_sense_magnetorque (id),
    foreign key (acds_reaction_wheel_id) references acds_reaction_wheel (id),
    foreign key (sp_cam_id) references sp_cam (id),
    foreign key (tuna_cam_id) references tuna_cam (id),
    foreign key (electri_power_system_id) references electri_power_system (id),
    foreign key (deployment_panels_antennas_id) references deployment_panels_antennas (id),
    foreign key (sipm_id) references sipm (camera_id)
    -- Comments: This table serves as a central reference point for linking all associated subsystems of the nanosatellite. Each row represents a snapshot of the satellite's configuration, detailing which subsystems are currently active or in use. It helps to ensure data integrity and facilitate complex queries across different subsystems.
);

