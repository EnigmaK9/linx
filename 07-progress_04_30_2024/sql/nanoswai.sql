-- Enable foreign key constraint
pragma foreign_keys = on;

-- Operation Periods table to hold common fields across multiple subsystems
create table operation_periods (
    period_id integer primary key,
    start_time text not null,
    end_time text not null,
    power real check (power >= 0) not null,
    voltage real check (voltage >= 0) not null,
    orbit integer not null,
    execution_priority integer not null,
    transmission_priority integer
);

-- Multispectral Camera table with reference to Operation Periods
create table multispectral_camera (
    multispectral_cam_id integer primary key,
    period_id integer not null,
    operational_status text check (operational_status in ('active', 'inactive', 'maintenance')),
    last_updated timestamp default current_timestamp,
    foreign key (period_id) references operation_periods (period_id)
);

-- Comms 437 MHz RX with reference to Operation Periods
create table comms_437_mhz_rx (
    comms_437_rx_id integer primary key,
    period_id integer not null,
    received_data blob not null,
    signal_strength real check (signal_strength >= 0) not null,
    reception_status text default 'pending' check (reception_status in ('success', 'failure', 'pending')),
    error_code integer,
    last_updated timestamp default current_timestamp,
    foreign key (period_id) references operation_periods (period_id)
);

-- Comms 437 MHz TX with reference to Operation Periods
create table comms_437_mhz_tx (
    comms_437_tx_id integer primary key,
    period_id integer not null,
    transmission_status text check (transmission_status in ('success', 'failure', 'pending')),
    last_error_code integer,
    last_updated timestamp default current_timestamp,
    foreign key (period_id) references operation_periods (period_id)
);

-- Comms 2408 MHz TX with reference to Operation Periods
create table comms_2408_mhz_tx (
    comms_2408_tx_id integer primary key,
    period_id integer not null,
    transmission_status text default 'pending' check (transmission_status in ('active', 'completed', 'error')),
    error_code integer,
    last_updated timestamp default current_timestamp,
    foreign key (period_id) references operation_periods (period_id)
);

-- ACS Sense Magnetorque with reference to Operation Periods
create table acds_sense_magnetorque (
    magnetorque_id integer primary key,
    period_id integer not null,
    magnetometer_data real not null,
    torque_data real not null,
    foreign key (period_id) references operation_periods (period_id)
);

-- ACS Reaction Wheel with reference to Operation Periods
create table acds_reaction_wheel (
    reaction_wheel_id integer primary key,
    period_id integer not null,
    wheel_speed real not null,
    wheel_position real not null,
    foreign key (period_id) references operation_periods (period_id)
);

-- Electrical Power System (EPS) with reference to Operation Periods
create table electrical_power_system (
    eps_id integer primary key,
    period_id integer not null,
    battery_level real not null,
    power_consumption real not null,
    foreign key (period_id) references operation_periods (period_id)
);

-- SP-CAM table with reference to Operation Periods
create table sp_cam (
    sp_cam_id integer primary key,
    period_id integer not null,
    image_data blob not null,
    image_metadata text not null,
    foreign key (period_id) references operation_periods (period_id)
);

-- TUNA-CAM table with reference to Operation Periods
create table tuna_cam (
    tuna_cam_id integer primary key,
    period_id integer not null,
    image_data blob not null,
    image_metadata text not null,
    foreign key (period_id) references operation_periods (period_id)
);

-- Deployment Panels and Antennas with reference to Operation Periods
create table deployment_panels_antennas (
    panel_id integer primary key,
    period_id integer not null,
    panel_status text not null,
    antenna_status text not null,
    foreign key (period_id) references operation_periods (period_id)
);

-- SiPM table with reference to Operation Periods
create table sipm (
    sipm_id integer primary key,
    period_id integer not null,
    foreign key (period_id) references operation_periods (period_id)
);

-- ACS Control table with reference to Operation Periods
create table acds_control (
    control_id integer primary key,
    period_id integer not null,
    control_data blob not null,
    control_status text not null,
    foreign key (period_id) references operation_periods (period_id)
);

-- Nanosatellite reference table definition
create table nanosatellite (
    obc_id integer,
    multispectral_cam_id integer,
    comms_437_mhz_tx_id integer,
    comms_2408_mhz_tx_id integer,
    comms_437_mhz_rx_id integer,
    acds_control_id integer,
    acds_sense_magnetorque_id integer,
    acds_reaction_wheel_id integer,
    sp_cam_id integer,
    tuna_cam_id integer,
    eps_id integer,
    deployment_panels_antennas_id integer,
    sipm_id integer,
    -- Primary key consisting of all subsystems' IDs
    primary key (obc_id, multispectral_cam_id, comms_437_mhz_tx_id, comms_2408_mhz_tx_id, comms_437_mhz_rx_id, acds_control_id, acds_sense_magnetorque_id, acds_reaction_wheel_id, sp_cam_id, tuna_cam_id, eps_id, deployment_panels_antennas_id, sipm_id),
    -- Foreign keys that reference the primary keys in other tables
    foreign key (obc_id) references multispectral_camera (multispectral_cam_id),
    foreign key (multispectral_cam_id) references multispectral_camera (multispectral_cam_id),
    foreign key (comms_437_mhz_tx_id) references comms_437_mhz_tx (tx_id),
    foreign key (comms_2408_mhz_tx_id) references comms_2408_mhz_tx (tx_id),
    foreign key (comms_437_mhz_rx_id) references comms_437_mhz_rx (rx_id),
    foreign key (acds_control_id) references acds_control (control_id),
    foreign key (acds_sense_magnetorque_id) references acds_sense_magnetorque (magnetorque_id),
    foreign key (acds_reaction_wheel_id) references acds_reaction_wheel (reaction_wheel_id),
    foreign key (sp_cam_id) references sp_cam (sp_cam_id),
    foreign key (tuna_cam_id) references tuna_cam (tuna_cam_id),
    foreign key (eps_id) references electrical_power_system (eps_id),
    foreign key (deployment_panels_antennas_id) references deployment_panels_antennas (panel_id),
    foreign key (sipm_id) references sipm (sipm_id)
);
