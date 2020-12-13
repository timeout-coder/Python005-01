1、msyql数据库查看字符集：
查看字符集：
mysql> show variables like '%character%';
查看校对规则
mysql> show variables like 'collation_%';
注意： MySQL 中的utf8 不是UTF-8 字符集

2、python连接mysql的方式
MySQLdb
其他DB-API：
• shell> pip install pymysql # 流行度最高
• shell> pip install mysql-connector-python # MySQL官方
使用ORM：
• shell> pip install sqlalchemy

PyMySQL 和SQLAlchemy 连接MySQL 数据库对比:
• pymysql.connect("server1","testuser","testpass","testdb" )
• engine=create_engine("mysql+pymysql://... ...",echo=True)

3、mysql语句执行顺序
SELECT DISTINCT player_id, player_name, count(*) as num # 顺序 5
FROM player JOIN team ON player.team_id = team.team_id  # 顺序 1
WHERE height > 1.80  # 顺序 2
GROUP BY player.team_id # 顺序 3
HAVING num > 2 # 顺序 4
ORDER BY num DESC # 顺序 6
LIMIT 2 # 顺序 7
