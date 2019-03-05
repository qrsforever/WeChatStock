-- Table: stock profile

DROP TABLE IF EXISTS `profile`;

CREATE TABLE `profile` (
    `code` varchar(16) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
    `name` varchar(256) CHARACTER SET utf8 COLLATE utf8_bin,
    `issue_price` int(11),
    `time_market` date,
    PRIMARY KEY (`code`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- Table: histroy info per day

DROP TABLE IF EXISTS `histroy_day`;

CREATE TABLE `histroy_day` (
    `day` date NOT NULL,
    `code` varchar(16) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
    `tclose` float(12, 2),
    `high` float(12, 2),
    `low` float(12, 2),
    `topen` float(12, 2),
    `lclose` float(12, 2),
    `chg` float(12, 2),
    `pchg`  float(12, 2),
    `turnover` float(12, 2),
    `voturnover` float(12, 2),
    `vaturnover` float(12, 2),
    `tcap` float(12, 2),
    `mcap` float(12, 2),
    PRIMARY KEY (`day`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

