create table sipm (
    id integer primary key,
    start_time integer not null,  -- stores unix timestamp for the start
    end_time integer not null,    -- stores unix timestamp for the end
    duration integer not null,    -- duration in seconds
    power real not null,          -- power in watts
    voltage real not null,        -- operating voltage in volts
    priority_t real not null,     -- transmission priority
    priority_e real not null      -- execution priority
);
