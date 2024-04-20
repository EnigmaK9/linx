create table acds_control (
    id integer primary key,
    start_time text not null,
    duration integer not null,
    power real not null,
    priority_t real not null,
    priority_e real not null
);

create table acds_sense_magnetorque (
    id integer primary key,
    start_time text not null,
    duration integer not null,
    power real not null,
    priority_t real not null,
    priority_e real not null
);

create table acds_reaction_wheel (
    id integer primary key,
    start_time text not null,
    duration integer not null,
    power real not null,
    priority_t real not null,
    priority_e real not null
);

create table obc (
    id integer primary key,
    start_time text not null,
    duration integer not null,
    power real not null,
    priority_t real not null,
    priority_e real not null
);

create table sipm (
    id integer primary key,
    start_time text not null,
    duration integer not null,
    power real not null,
    priority_t real not null,
    priority_e real not null
);

create table camera_gecko (
    id integer primary key,
    start_time text not null,
    duration integer not null,
    power real not null,
    priority_t real not null,
    priority_e real not null
);

create table camera_mantis (
    id integer primary key,
    start_time text not null,
    duration integer not null,
    power real not null,
    priority_t real not null,
    priority_e real not null
);

create table camera_chameleon (
    id integer primary key,
    start_time text not null,
    duration integer not null,
    power real not null,
    priority_t real not null,
    priority_e real not null
);

create table comms_437_mhz_rx (
    id integer primary key,
    start_time text not null,
    duration integer not null,
    power real not null,
    priority_t real not null,
    priority_e real not null
);

create table comms_437_mhz_tx (
    id integer primary key,
    start_time text not null,
    duration integer not null,
    power real not null,
    priority_t real not null,
    priority_e real not null
);

create table comms_2408_mhz_tx (
    id integer primary key,
    start_time text not null,
    duration integer not null,
    power real not null,
    priority_t real not null,
    priority_e real not null
);

create table eps (
    id integer primary key,
    start_time text not null,
    duration integer not null,
    power real not null,
    priority_t real not null,
    priority_e real not null
);

create table deployment_panels_antennas (
    id integer primary key,
    start_time text not null,
    duration integer not null,
    power real not null,
    priority_t real not null,
    priority_e real not null
);

create table camera_simi (
    id integer primary key,
    start_time text not null,
    duration integer not null,
    power real not null,
    priority_t real not null,
    priority_e real not null
);

