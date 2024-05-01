create table multispectral_camera (
    id integer primary key,
    start_time integer not null,  -- unix timestamp for the start
    end_time integer not null,    -- unix timestamp for the end
    power real not null,          -- power in watts
    voltage real not null,        -- operating voltage in volts
    orbit integer not null,       -- orbit number of the event start
    transmission_priority real not null,     -- transmission priority
    execution_priority real not null      -- execution priority
    duration real not null,  -- duration of the activity in minutes
);

