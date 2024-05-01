icreate table adcs_data (
    data_id integer primary key,
    timestamp timestamp not null,
    orientation real, -- in radians
    angular_velocity_x real, -- in rad/s
    angular_velocity_y real, -- in rad/s
    angular_velocity_z real, -- in rad/s
    magnetorquer_x real, -- in Tesla
    magnetorquer_y real, -- in Tesla
    magnetorquer_z real, -- in Tesla
    star_sensor_orientation real, -- in radians
    gyroscopic_sensor_data_x real, -- in rad/s
    gyroscopic_sensor_data_y real, -- in rad/s
    gyroscopic_sensor_data_z real, -- in rad/s
    solar_sensor_orientation real, -- in radians
    error_correction_data text, -- error correction data in text format
    power_consumption real -- in watts (W) or joules per second (J/s)
);

