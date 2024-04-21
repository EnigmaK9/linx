create table camera_computer (
    id integer primary key,
    start_time integer not null,  -- almacena la marca de tiempo unix para el inicio
    end_time integer not null,    -- almacena la marca de tiempo unix para el fin
    duration integer not null,    -- duración en segundos
    power real not null,          -- potencia en Watts
    priority_d real not null,     -- prioridad de descarga
    priority_e real not null      -- prioridad de ejecución
);
