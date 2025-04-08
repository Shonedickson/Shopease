-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 01, 2025 at 09:33 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `shoecase`
--

-- --------------------------------------------------------

--
-- Table structure for table `area`
--

CREATE TABLE `area` (
  `area_id` int(11) NOT NULL,
  `area_code` int(11) NOT NULL,
  `area_name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `area`
--

INSERT INTO `area` (`area_id`, `area_code`, `area_name`) VALUES
(9, 1, 'kottayam'),
(10, 2, 'Alappuzha'),
(11, 3, 'trivandrum'),
(12, 4, 'ernakulam'),
(14, 5, 'kasargod'),
(15, 6, 'kannur'),
(16, 7, 'malabar'),
(17, 8, 'palakkad'),
(18, 9, 'malappuiram');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add area', 7, 'add_area'),
(26, 'Can change area', 7, 'change_area'),
(27, 'Can delete area', 7, 'delete_area'),
(28, 'Can view area', 7, 'view_area'),
(29, 'Can add auth group', 8, 'add_authgroup'),
(30, 'Can change auth group', 8, 'change_authgroup'),
(31, 'Can delete auth group', 8, 'delete_authgroup'),
(32, 'Can view auth group', 8, 'view_authgroup'),
(33, 'Can add auth group permissions', 9, 'add_authgrouppermissions'),
(34, 'Can change auth group permissions', 9, 'change_authgrouppermissions'),
(35, 'Can delete auth group permissions', 9, 'delete_authgrouppermissions'),
(36, 'Can view auth group permissions', 9, 'view_authgrouppermissions'),
(37, 'Can add auth permission', 10, 'add_authpermission'),
(38, 'Can change auth permission', 10, 'change_authpermission'),
(39, 'Can delete auth permission', 10, 'delete_authpermission'),
(40, 'Can view auth permission', 10, 'view_authpermission'),
(41, 'Can add auth user', 11, 'add_authuser'),
(42, 'Can change auth user', 11, 'change_authuser'),
(43, 'Can delete auth user', 11, 'delete_authuser'),
(44, 'Can view auth user', 11, 'view_authuser'),
(45, 'Can add auth user groups', 12, 'add_authusergroups'),
(46, 'Can change auth user groups', 12, 'change_authusergroups'),
(47, 'Can delete auth user groups', 12, 'delete_authusergroups'),
(48, 'Can view auth user groups', 12, 'view_authusergroups'),
(49, 'Can add auth user user permissions', 13, 'add_authuseruserpermissions'),
(50, 'Can change auth user user permissions', 13, 'change_authuseruserpermissions'),
(51, 'Can delete auth user user permissions', 13, 'delete_authuseruserpermissions'),
(52, 'Can view auth user user permissions', 13, 'view_authuseruserpermissions'),
(53, 'Can add category', 14, 'add_category'),
(54, 'Can change category', 14, 'change_category'),
(55, 'Can delete category', 14, 'delete_category'),
(56, 'Can view category', 14, 'view_category'),
(57, 'Can add customer', 15, 'add_customer'),
(58, 'Can change customer', 15, 'change_customer'),
(59, 'Can delete customer', 15, 'delete_customer'),
(60, 'Can view customer', 15, 'view_customer'),
(61, 'Can add customer address', 16, 'add_customeraddress'),
(62, 'Can change customer address', 16, 'change_customeraddress'),
(63, 'Can delete customer address', 16, 'delete_customeraddress'),
(64, 'Can view customer address', 16, 'view_customeraddress'),
(65, 'Can add delivery charge', 17, 'add_deliverycharge'),
(66, 'Can change delivery charge', 17, 'change_deliverycharge'),
(67, 'Can delete delivery charge', 17, 'delete_deliverycharge'),
(68, 'Can view delivery charge', 17, 'view_deliverycharge'),
(69, 'Can add django admin log', 18, 'add_djangoadminlog'),
(70, 'Can change django admin log', 18, 'change_djangoadminlog'),
(71, 'Can delete django admin log', 18, 'delete_djangoadminlog'),
(72, 'Can view django admin log', 18, 'view_djangoadminlog'),
(73, 'Can add django content type', 19, 'add_djangocontenttype'),
(74, 'Can change django content type', 19, 'change_djangocontenttype'),
(75, 'Can delete django content type', 19, 'delete_djangocontenttype'),
(76, 'Can view django content type', 19, 'view_djangocontenttype'),
(77, 'Can add django migrations', 20, 'add_djangomigrations'),
(78, 'Can change django migrations', 20, 'change_djangomigrations'),
(79, 'Can delete django migrations', 20, 'delete_djangomigrations'),
(80, 'Can view django migrations', 20, 'view_djangomigrations'),
(81, 'Can add django session', 21, 'add_djangosession'),
(82, 'Can change django session', 21, 'change_djangosession'),
(83, 'Can delete django session', 21, 'delete_djangosession'),
(84, 'Can view django session', 21, 'view_djangosession'),
(85, 'Can add employee', 22, 'add_employee'),
(86, 'Can change employee', 22, 'change_employee'),
(87, 'Can delete employee', 22, 'delete_employee'),
(88, 'Can view employee', 22, 'view_employee'),
(89, 'Can add login', 23, 'add_login'),
(90, 'Can change login', 23, 'change_login'),
(91, 'Can delete login', 23, 'delete_login'),
(92, 'Can view login', 23, 'view_login'),
(93, 'Can add merchant', 24, 'add_merchant'),
(94, 'Can change merchant', 24, 'change_merchant'),
(95, 'Can delete merchant', 24, 'delete_merchant'),
(96, 'Can view merchant', 24, 'view_merchant'),
(97, 'Can add product', 25, 'add_product'),
(98, 'Can change product', 25, 'change_product'),
(99, 'Can delete product', 25, 'delete_product'),
(100, 'Can view product', 25, 'view_product'),
(101, 'Can add product details', 26, 'add_productdetails'),
(102, 'Can change product details', 26, 'change_productdetails'),
(103, 'Can delete product details', 26, 'delete_productdetails'),
(104, 'Can view product details', 26, 'view_productdetails'),
(105, 'Can add subcategory', 27, 'add_subcategory'),
(106, 'Can change subcategory', 27, 'change_subcategory'),
(107, 'Can delete subcategory', 27, 'delete_subcategory'),
(108, 'Can view subcategory', 27, 'view_subcategory');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `bank`
--

CREATE TABLE `bank` (
  `bank_id` int(11) NOT NULL,
  `card_num` varchar(50) NOT NULL,
  `cvv_num` varchar(20) NOT NULL,
  `amount` decimal(10,0) NOT NULL,
  `exp_month` varchar(20) NOT NULL,
  `exp_year` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bank`
--

INSERT INTO `bank` (`bank_id`, `card_num`, `cvv_num`, `amount`, `exp_month`, `exp_year`) VALUES
(1, '2255', '12456789', 3333, 'december', '2030');

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `category_id` int(11) NOT NULL,
  `category_name` varchar(50) NOT NULL,
  `category_image` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`category_id`, `category_name`, `category_image`) VALUES
(2, 'jjj', 'jjj');

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `cust_id` int(11) NOT NULL,
  `cust_name` varchar(50) NOT NULL,
  `phone_number` varchar(10) NOT NULL,
  `email_id` varchar(100) NOT NULL,
  `created_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`cust_id`, `cust_name`, `phone_number`, `email_id`, `created_date`) VALUES
(11, 'deepika', '6282432022', 'n@gmail.com', '2025-01-13'),
(12, 'shone dickson', '628243021', 'shonedickson@gmail.com', '2025-02-13');

-- --------------------------------------------------------

--
-- Table structure for table `customer_address`
--

CREATE TABLE `customer_address` (
  `delivery_add_id` int(11) NOT NULL,
  `fk_cust_id` int(11) NOT NULL,
  `fk_area_id` int(11) NOT NULL,
  `street` varchar(50) NOT NULL,
  `building` varchar(100) NOT NULL,
  `flat` int(11) NOT NULL,
  `landmark` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer_address`
--

INSERT INTO `customer_address` (`delivery_add_id`, `fk_cust_id`, `fk_area_id`, `street`, `building`, `flat`, `landmark`) VALUES
(1, 10, 6, 'ggg', 'jkhbhjjgh', 666, 'jkjkhjkh'),
(2, 11, 14, 'nstreet', 'mmm', 3, 'sghc'),
(3, 11, 9, 'kk', 'mm', 9, 'kkj'),
(6, 12, 9, 'tk', 'vkkkkhousw', 15, 'mbge'),
(7, 12, 9, 'newstreet', 'gkhouse', 3, 'near temple'),
(8, 13, 10, 'eeee', '22', 33, 'eeee');

-- --------------------------------------------------------

--
-- Table structure for table `delivery_charge`
--

CREATE TABLE `delivery_charge` (
  `delivery_charge_id` int(11) NOT NULL,
  `fk_area_id` int(11) NOT NULL,
  `delivery_charge` decimal(18,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `delivery_charge`
--

INSERT INTO `delivery_charge` (`delivery_charge_id`, `fk_area_id`, `delivery_charge`) VALUES
(10, 6, 33.00),
(11, 9, 7.00),
(12, 14, 23.00),
(13, 17, 45.00);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'newapp', 'area'),
(8, 'newapp', 'authgroup'),
(9, 'newapp', 'authgrouppermissions'),
(10, 'newapp', 'authpermission'),
(11, 'newapp', 'authuser'),
(12, 'newapp', 'authusergroups'),
(13, 'newapp', 'authuseruserpermissions'),
(14, 'newapp', 'category'),
(15, 'newapp', 'customer'),
(16, 'newapp', 'customeraddress'),
(17, 'newapp', 'deliverycharge'),
(18, 'newapp', 'djangoadminlog'),
(19, 'newapp', 'djangocontenttype'),
(20, 'newapp', 'djangomigrations'),
(21, 'newapp', 'djangosession'),
(22, 'newapp', 'employee'),
(23, 'newapp', 'login'),
(24, 'newapp', 'merchant'),
(25, 'newapp', 'product'),
(26, 'newapp', 'productdetails'),
(27, 'newapp', 'subcategory'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-01-02 04:53:43.535205'),
(2, 'auth', '0001_initial', '2025-01-02 04:53:44.387008'),
(3, 'admin', '0001_initial', '2025-01-02 04:53:44.590759'),
(4, 'admin', '0002_logentry_remove_auto_add', '2025-01-02 04:53:44.601217'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2025-01-02 04:53:44.616622'),
(6, 'contenttypes', '0002_remove_content_type_name', '2025-01-02 04:53:44.715268'),
(7, 'auth', '0002_alter_permission_name_max_length', '2025-01-02 04:53:44.853633'),
(8, 'auth', '0003_alter_user_email_max_length', '2025-01-02 04:53:44.882487'),
(9, 'auth', '0004_alter_user_username_opts', '2025-01-02 04:53:44.896865'),
(10, 'auth', '0005_alter_user_last_login_null', '2025-01-02 04:53:44.986401'),
(11, 'auth', '0006_require_contenttypes_0002', '2025-01-02 04:53:44.991399'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2025-01-02 04:53:45.001585'),
(13, 'auth', '0008_alter_user_username_max_length', '2025-01-02 04:53:45.022382'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2025-01-02 04:53:45.044694'),
(15, 'auth', '0010_alter_group_name_max_length', '2025-01-02 04:53:45.067874'),
(16, 'auth', '0011_update_proxy_permissions', '2025-01-02 04:53:45.078186'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2025-01-02 04:53:45.099625'),
(18, 'sessions', '0001_initial', '2025-01-02 04:53:45.146337');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('xrhbegli34nimq9e38f2kk3fa7bz9l5q', '.eJyrVipOzU3MzFGyUsrMc0gHMpV0lHJgQhCRHL3k_FygcApcOD8JSaIWAAroFsI:1trWMZ:5-EWuJGZ39KjGcV-4fMkIQ56pPathYdQEGd5O7mNa8s', '2025-03-24 06:11:43.829419');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `emp_id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `address` text NOT NULL,
  `phone_num` varchar(50) NOT NULL,
  `email` varchar(150) NOT NULL,
  `gender` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`emp_id`, `name`, `address`, `phone_num`, `email`, `gender`) VALUES
(2, 'shone', 'thrickodithanam', '9072163440', 's@gmail.com', 'male'),
(6, 'shone', 'thrickodithanam', '6282432021', 's@gmail.com', 'male'),
(7, 'dd', 'dd', '445', 'ss', 'male'),
(8, 'noble k', 'tkdm', '7896535689', 'nob@gmail.com', 'male');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `username` varchar(100) NOT NULL,
  `password` varchar(20) NOT NULL,
  `user_type` varchar(20) NOT NULL,
  `status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`username`, `password`, `user_type`, `status`) VALUES
('admin@gmail.com', 'admin', 'admin', 'active'),
('in@gmai', 'inian@123', 'merchant', 'active'),
('n@gmail.com', 'cristiano@123', 'customer', 'active'),
('nob@gmail.com', 'noble@123', 'employee', 'active'),
('s@gmail.com', 'sfgh2!jjj', 'employee', 'active'),
('shonedickson@gmail.com', 'shone@123', 'customer', 'active');

-- --------------------------------------------------------

--
-- Table structure for table `merchant`
--

CREATE TABLE `merchant` (
  `merchant_id` int(11) NOT NULL,
  `merchant_name` varchar(50) NOT NULL,
  `address` text NOT NULL,
  `phone_number` varchar(10) NOT NULL,
  `email` varchar(100) NOT NULL,
  `image` varchar(100) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `merchant`
--

INSERT INTO `merchant` (`merchant_id`, `merchant_name`, `address`, `phone_number`, `email`, `image`, `status`) VALUES
(14, 'shone ', 'cgry', '6324678876', 's@gmail.com', 'Merchant\\cv image.jpg', 'active'),
(15, 'iniesta', 'inved', '7786272727', 'in@gmai', 'Merchant\\cv image.jpg', 'active');

-- --------------------------------------------------------

--
-- Table structure for table `order_lines`
--

CREATE TABLE `order_lines` (
  `order_line_id` int(11) NOT NULL,
  `fk_product_details_id` int(11) NOT NULL,
  `fk_order_id` int(11) NOT NULL,
  `quantity` int(100) NOT NULL,
  `sales_price` decimal(10,0) NOT NULL,
  `total_price` decimal(10,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `order_lines`
--

INSERT INTO `order_lines` (`order_line_id`, `fk_product_details_id`, `fk_order_id`, `quantity`, `sales_price`, `total_price`) VALUES
(9, 25, 6, 4, 400, 1600),
(13, 24, 8, 2, 500, 1000);

-- --------------------------------------------------------

--
-- Table structure for table `order_table`
--

CREATE TABLE `order_table` (
  `order_id` int(11) NOT NULL,
  `order_date` date DEFAULT NULL,
  `fk_cust_id` int(11) DEFAULT NULL,
  `fk_delivery_address_id` int(11) DEFAULT NULL,
  `fk_merchant_id` int(11) DEFAULT NULL,
  `delivery_charge` decimal(10,0) DEFAULT NULL,
  `net_amount` decimal(10,0) DEFAULT NULL,
  `grand_total` decimal(10,0) DEFAULT NULL,
  `order_status` varchar(50) DEFAULT NULL,
  `payment_mode` varchar(50) DEFAULT NULL,
  `delivery_date` date DEFAULT NULL,
  `delivered_time` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `order_table`
--

INSERT INTO `order_table` (`order_id`, `order_date`, `fk_cust_id`, `fk_delivery_address_id`, `fk_merchant_id`, `delivery_charge`, `net_amount`, `grand_total`, `order_status`, `payment_mode`, `delivery_date`, `delivered_time`) VALUES
(6, '2025-02-18', 12, 3, 15, 15, 1400, 1415, 'completed', NULL, '2025-03-02', '07:07:00'),
(8, '2025-02-20', 11, 3, 15, 7, 1000, 1007, 'paid', NULL, '2025-03-02', '07:07:00');

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `product_id` int(11) NOT NULL,
  `fk_merchant_id` int(11) NOT NULL,
  `product_name` varchar(100) NOT NULL,
  `product_code` varchar(100) NOT NULL,
  `product_image` varchar(100) NOT NULL,
  `fk_sub_category_id` int(11) NOT NULL,
  `cost_price` decimal(10,0) NOT NULL,
  `sales_price` decimal(10,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`product_id`, `fk_merchant_id`, `product_name`, `product_code`, `product_image`, `fk_sub_category_id`, `cost_price`, `sales_price`) VALUES
(17, 15, 'nike ', 'nike123', 'products\\randomimage.jpg', 1, 250, 500),
(18, 15, 'adidas', 'a2', 'products\\randomimage.jpg', 2, 200, 400);

-- --------------------------------------------------------

--
-- Table structure for table `product_details`
--

CREATE TABLE `product_details` (
  `product_details_id` int(11) NOT NULL,
  `fk_product_id` int(11) NOT NULL,
  `product_size` varchar(50) NOT NULL,
  `product_colour` varchar(50) NOT NULL,
  `product_img` varchar(100) NOT NULL,
  `product_quantity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product_details`
--

INSERT INTO `product_details` (`product_details_id`, `fk_product_id`, `product_size`, `product_colour`, `product_img`, `product_quantity`) VALUES
(24, 17, 'xl', 'red', 'products\\randomimage.jpg', 4),
(25, 18, 'xl', 'blue', 'products\\randomimage.jpg', 10);

-- --------------------------------------------------------

--
-- Table structure for table `schedule_employee`
--

CREATE TABLE `schedule_employee` (
  `sh_emp_id` int(11) NOT NULL,
  `fk_emp_id` int(11) NOT NULL,
  `fk_order_id` int(11) NOT NULL,
  `status` varchar(100) NOT NULL,
  `delivery_date` date NOT NULL,
  `delivery_time` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `schedule_employee`
--

INSERT INTO `schedule_employee` (`sh_emp_id`, `fk_emp_id`, `fk_order_id`, `status`, `delivery_date`, `delivery_time`) VALUES
(45, 2, 6, 'scheduled', '2025-02-09', '11:11:00'),
(46, 8, 8, 'completed', '2025-03-03', '14:55:00');

-- --------------------------------------------------------

--
-- Table structure for table `subcategory`
--

CREATE TABLE `subcategory` (
  `sub_category_id` int(11) NOT NULL,
  `fk_category_id` int(11) NOT NULL,
  `category_type` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `subcategory`
--

INSERT INTO `subcategory` (`sub_category_id`, `fk_category_id`, `category_type`) VALUES
(1, 2, 'ss'),
(2, 2, 'aa');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `area`
--
ALTER TABLE `area`
  ADD PRIMARY KEY (`area_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `bank`
--
ALTER TABLE `bank`
  ADD PRIMARY KEY (`bank_id`);

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`category_id`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`cust_id`);

--
-- Indexes for table `customer_address`
--
ALTER TABLE `customer_address`
  ADD PRIMARY KEY (`delivery_add_id`);

--
-- Indexes for table `delivery_charge`
--
ALTER TABLE `delivery_charge`
  ADD PRIMARY KEY (`delivery_charge_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`emp_id`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `merchant`
--
ALTER TABLE `merchant`
  ADD PRIMARY KEY (`merchant_id`);

--
-- Indexes for table `order_lines`
--
ALTER TABLE `order_lines`
  ADD PRIMARY KEY (`order_line_id`);

--
-- Indexes for table `order_table`
--
ALTER TABLE `order_table`
  ADD PRIMARY KEY (`order_id`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `product_details`
--
ALTER TABLE `product_details`
  ADD PRIMARY KEY (`product_details_id`);

--
-- Indexes for table `schedule_employee`
--
ALTER TABLE `schedule_employee`
  ADD PRIMARY KEY (`sh_emp_id`);

--
-- Indexes for table `subcategory`
--
ALTER TABLE `subcategory`
  ADD PRIMARY KEY (`sub_category_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `area`
--
ALTER TABLE `area`
  MODIFY `area_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=109;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `bank`
--
ALTER TABLE `bank`
  MODIFY `bank_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `category_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `cust_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `customer_address`
--
ALTER TABLE `customer_address`
  MODIFY `delivery_add_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `delivery_charge`
--
ALTER TABLE `delivery_charge`
  MODIFY `delivery_charge_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `employee`
--
ALTER TABLE `employee`
  MODIFY `emp_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `merchant`
--
ALTER TABLE `merchant`
  MODIFY `merchant_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `order_lines`
--
ALTER TABLE `order_lines`
  MODIFY `order_line_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `order_table`
--
ALTER TABLE `order_table`
  MODIFY `order_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `product_details`
--
ALTER TABLE `product_details`
  MODIFY `product_details_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `schedule_employee`
--
ALTER TABLE `schedule_employee`
  MODIFY `sh_emp_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;

--
-- AUTO_INCREMENT for table `subcategory`
--
ALTER TABLE `subcategory`
  MODIFY `sub_category_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
