CREATE DATABASE emp_data;
use emp_data;
CREATE TABLE `employee_table` (
  `ID` varchar(200) NOT NULL,
  `NAME` varchar(200) NOT NULL,
  `AGE` varchar(200) NOT NULL,
  `DEPARTMENT` varchar(200) NOT NULL,
   PRIMARY KEY (`STUDID`)
);

INSERT INTO `empployee_table` (`ID`, `NAME`, `AGE`, `DEPARTMENT`) VALUES
('1','Eurekha','21','Mechanical'),
('2','Thanuja','21','CSE'),
('3', 'Meghala', '20','Mechanical);