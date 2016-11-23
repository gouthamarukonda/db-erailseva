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

-- Orders

insert into orders (pnr_no, cust_id, shop_id, item_id, quantity, paymode, status, time_stamp) values ('000000000', 2, '00001', '00001', 2, '0', '9', now());
insert into orders (pnr_no, cust_id, shop_id, item_id, quantity, paymode, status, time_stamp) values ('000000000', 2, '00001', '00002', 3, '0', '5', now());
insert into orders (pnr_no, cust_id, shop_id, item_id, quantity, paymode, status, time_stamp) values ('000000000', 2, '00001', '00004', 2, '0', '8', now());
insert into orders (pnr_no, cust_id, shop_id, item_id, quantity, paymode, status, time_stamp) values ('000000000', 2, '00001', '00003', 4, '0', '5', now());
insert into orders (pnr_no, cust_id, shop_id, item_id, quantity, paymode, status, time_stamp) values ('000000000', 2, '00001', '00002', 1, '0', '5', now());
insert into orders (pnr_no, cust_id, shop_id, item_id, quantity, paymode, status, time_stamp) values ('000000000', 2, '00001', '00005', 2, '0', '3', now());
insert into orders (pnr_no, cust_id, shop_id, item_id, quantity, paymode, status, time_stamp) values ('000000000', 2, '00001', '00004', 1, '0', '1', now());
insert into orders (pnr_no, cust_id, shop_id, item_id, quantity, paymode, status, time_stamp) values ('000000000', 2, '00001', '00001', 3, '0', '0', now());

-- Reviews

insert into review (msg, time_stamp, cust_id, shop_id) values ('The food quality and taste are amazing and they have never dissapointed. I do believe the side portions are a bit small but besides that the price is worth it. I personally recommend the churrasco pasion with a side of arroz mamposteao its amazing and to close the deal order for dessert the tres leches sampler its to die for.', now(), 2, '00001');
insert into review (msg, time_stamp, cust_id, shop_id) values ('I am sure the negative reviews that this restaurant have are not true. We have eaten more than 12 time and the food us amazing. Highly recomended', now(), 2, '00001');
insert into review (msg, time_stamp, cust_id, shop_id) values ('This place is welcoming with charming service and dfood better than I have tasted since I was in India', now(), 2, '00001');
insert into review (msg, time_stamp, cust_id, shop_id) values ('Been ordering from here since it first opened and have never had any complaints. The food is fantastic. Chilly Chicken Masala to die for.', now(), 2, '00001');