create table obc (
    id integer primary key,
    start_time text not null,
    duration integer not null,
    power real not null,
    priority_t real not null,
    priority_e real not null
);

