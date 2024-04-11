create table satellite_components (
    element varchar(255),
    work_cycles int,
    power_w float,
    operating_voltage_v float,
    weight_g int,
    lifetime_consumption float
);

insert into satellite_components (element, work_cycles, power_w, operating_voltage_v, weight_g, lifetime_consumption) values
('attitude control system (computer control)', 18, 4, 3.3, 500, 0.25),
('attitude control system (magnetorque sensor)', 12, 1, 3.5, 28, 0.1),
('attitude control system (reaction wheel)', 13, 1.5, 3.3, 35, 0.15),
('onboard computer', 100, 10, 5, 50, 1),
('silicon photomultipliers', 20, 2.5, 5, 20, 0.1),
('camera (gecko, mantis, chameleon)', 15, 4.6, 10, 500, 1),
('communications 437.7125 mhz receiver', 100, 0.36, 3.6, 100, 0.2),
('communications 437.7125 mhz transmitter', 15, 7.2, 3.6, 100, 0.5),
('communications 2408 mhz transmitter', 18, 8, 5.3, 97, 0.5),
('electrical power system', 100, 0.2, 5.3, 528, 0.1),
('deployment of panels and antennas', 1, 5, 5, null, 0.01),
('camera siim', 15, 6, 5, 550, 1);

