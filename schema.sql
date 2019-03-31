drop database if exists jinyong;
create database jinyong;

-- 人物关系表 ID：主键、Names:人物名称，alias_1、alias_2、alias_3为对应别名
create table if not exists relation (
    `ID` INT UNSIGNED AUTO_INCREMENT,
    `Names` VARCHAR(100) NOT NULL,
    `alias_1` VARCHAR(100) ,
    `alias_2` VARCHAR(100) ,
    `alias_3` VARCHAR(100) ,
    primary key (`ID`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 小说表
create table if not exists novel (
    `IdNovel` INT UNSIGNED AUTO_INCREMENT,
    `NovelName` VARCHAR(100) NOT NULL,
    primary key (`IdNovel`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 词频表 wordFrequency idJieDian：主键、UserID：人物ID、Num：频次、Novel：出现文章ID。
create table if not exists wordFrequency (
    `idJieDian` INT UNSIGNED AUTO_INCREMENT,
    `UserID` INT UNSIGNED,
    `Num` INT UNSIGNED,
    `Novel` INT UNSIGNED,
    primary key (`idJieDian`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 元数据数据库，该数据用于存储文本数据分析结果，作为一级数据库
create table if not exists metadata (
    `idData` INT UNSIGNED AUTO_INCREMENT,
    `Novel` INT UNSIGNED,
    `Dtat` blob(1024),
    primary key (`idData`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;