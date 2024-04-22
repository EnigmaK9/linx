create table sipm (
    id integer primary key,
    start_time integer not null,
    end_time integer not null,
    duration integer not null,
    power real not null,
    priority_t real not null,
    priority_e real not null
);

