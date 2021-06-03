-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 03, 2021 at 11:36 AM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `fundanalyst`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts`
--

CREATE TABLE `accounts` (
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `surname` varchar(255) NOT NULL,
  `owner` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `accounts`
--

INSERT INTO `accounts` (`username`, `password`, `name`, `surname`, `owner`) VALUES
('GiannisT', 'test123', 'Giannis', 'Terlegkas', 1);

-- --------------------------------------------------------

--
-- Table structure for table `employees`
--

CREATE TABLE `employees` (
  `name` varchar(255) NOT NULL,
  `lastname` varchar(255) NOT NULL,
  `id` int(11) NOT NULL,
  `salary` float NOT NULL,
  `month` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `employees`
--

INSERT INTO `employees` (`name`, `lastname`, `id`, `salary`, `month`) VALUES
('Elias', 'Dimitriou', 1, 1000, ''),
('Iraklis', 'Ioannidis', 2, 1600, ''),
('Prokopis', 'Iordanou', 3, 1200, ''),
('Paraskevi', 'Dimitriou', 4, 1200, ''),
('Vasilis', 'Papageorgiou', 5, 1800, '');

-- --------------------------------------------------------

--
-- Table structure for table `operatingcosts`
--

CREATE TABLE `operatingcosts` (
  `power` float NOT NULL,
  `water` float NOT NULL,
  `phone` float NOT NULL,
  `rent` float NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `operatingcosts`
--

INSERT INTO `operatingcosts` (`power`, `water`, `phone`, `rent`, `date`) VALUES
(143.32, 115.22, 9469450000, 350, '2021-06-14'),
(69.96, 61.13, 6988210000, 300, '2021-06-18'),
(93.61, 173.57, 6858840000, 320, '2021-06-10'),
(161.3, 93.15, 6939720000, 400, '2021-06-24'),
(134.55, 76.91, 6854770000, 350, '2021-06-12');

-- --------------------------------------------------------

--
-- Table structure for table `sales`
--

CREATE TABLE `sales` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL,
  `date` date NOT NULL,
  `price` float NOT NULL,
  `amount` int(255) NOT NULL,
  `purchase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `sales`
--

INSERT INTO `sales` (`id`, `name`, `type`, `date`, `price`, `amount`, `purchase`) VALUES
(234, 'Dell mousepad', 'Peripheral', '2021-05-12', 20.5, 2, 'e-shop'),
(235, 'Asus Nvidia RTX 2070', 'Hardware', '2021-05-13', 460, 1, 'Physical Shop'),
(236, 'WD 2TB HDD', 'Hardware', '2021-05-10', 49.9, 10, 'e-shop'),
(237, 'PSU EVGA 400W', 'Hardware', '2021-05-11', 29.9, 4, 'Physical Shop'),
(238, 'Logitech MX Ergo Mouse', 'Peripheral', '2021-05-17', 90, 6, 'Physical Shop'),
(239, 'Microsoft Office 2019 Pro', 'Software', '2021-05-17', 49.99, 10, 'e-shop');

-- --------------------------------------------------------

--
-- Table structure for table `supplies`
--

CREATE TABLE `supplies` (
  `cost` varchar(255) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `supplies`
--

INSERT INTO `supplies` (`cost`, `date`) VALUES
('267.29', '2021-06-08'),
('462.28', '2021-06-03'),
('483.89', '2021-06-29'),
('532.53', '2021-06-16'),
('527.80', '2021-06-20');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accounts`
--
ALTER TABLE `accounts`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `employees`
--
ALTER TABLE `employees`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sales`
--
ALTER TABLE `sales`
  ADD PRIMARY KEY (`id`,`date`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `employees`
--
ALTER TABLE `employees`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `sales`
--
ALTER TABLE `sales`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=240;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
