-- Trains

insert into train values ('T1001', 'Shatabdi Express', '01:00:00', '23:00:00', now(), '00001', '00004');
insert into train values ('T1002', 'LTT', '02:00:00', '18:00:00', now(), '00008', '00003');

-- Stops

insert into stop (arr_time, dept_time, stop_num, day_of_journey, time_stamp, station_id, train_no) values (null, '01:00:00', 0, 0, now(), '00001', 'T1001');
insert into stop (arr_time, dept_time, stop_num, day_of_journey, time_stamp, station_id, train_no) values ('08:00:00', '09:00:00', 1, 0, now(), '00002', 'T1001');
insert into stop (arr_time, dept_time, stop_num, day_of_journey, time_stamp, station_id, train_no) values ('15:00:00', '16:00:00', 2, 0, now(), '00003','T1001');
insert into stop (arr_time, dept_time, stop_num, day_of_journey, time_stamp, station_id, train_no) values ('23:00:00', null, 3, 0, now(), '00004', 'T1001');
insert into stop (arr_time, dept_time, stop_num, day_of_journey, time_stamp, station_id, train_no) values (null, '02:00:00', 0, 0, now(), '00008', 'T1002');
insert into stop (arr_time, dept_time, stop_num, day_of_journey, time_stamp, station_id, train_no) values ('11:00:00', '12:00:00', 1, 0, now(), '00007', 'T1002');
insert into stop (arr_time, dept_time, stop_num, day_of_journey, time_stamp, station_id, train_no) values ('19:00:00', '20:00:00', 2, 0, now(), '00006', 'T1002');
insert into stop (arr_time, dept_time, stop_num, day_of_journey, time_stamp, station_id, train_no) values ('05:00:00', '06:00:00', 3, 1, now(), '00005', 'T1002');
insert into stop (arr_time, dept_time, stop_num, day_of_journey, time_stamp, station_id, train_no) values ('12:00:00', '13:00:00', 4, 1, now(), '00004', 'T1002');
insert into stop (arr_time, dept_time, stop_num, day_of_journey, time_stamp, station_id, train_no) values ('18:00:00', null, 5, 1, now(), '00003', 'T1002');

-- PNR

insert into pnr values ('000000001', 1, 20, '01/01/2017 01:00:00', '01/12/2016 00:00:00', now(), 'T1001');
insert into pnr values ('000000000', 2, 40, '01/01/2017 02:00:00', '01/12/2016 00:00:00', now(), 'T1002');
