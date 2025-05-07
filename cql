Connected as hossai24@students.rowan.edu.
Connected to cndb at cassandra.ingress:9042.
[cqlsh 6.8.0 | Cassandra 4.0.11-3a52ecb0d31d | CQL spec 3.4.5 | Native protocol v4 | TLS]
Use HELP for help.
token@cqlsh> USE netflix_keyspace ;
token@cqlsh:netflix_keyspace> 
token@cqlsh:netflix_keyspace> DESCRIBE TABLE developer_survey;

CREATE TABLE netflix_keyspace.developer_survey (
    id uuid PRIMARY KEY,
    companysize text,
    country text,
    employment text,
    formaleducation text,
    hobby text,
    opensource text,
    student text,
    undergradmajor text
) WITH additional_write_policy = '99p'
    AND bloom_filter_fp_chance = 0.01
    AND caching = {'keys': 'ALL', 'rows_per_partition': 'NONE'}
    AND comment = ''
    AND compaction = {'class': 'org.apache.cassandra.db.compaction.UnifiedCompactionStrategy'}
    AND compression = {'chunk_length_in_kb': '16', 'class': 'org.apache.cassandra.io.compress.LZ4Compressor'}
    AND crc_check_chance = 1.0
    AND default_time_to_live = 0
    AND gc_grace_seconds = 864000
    AND max_index_interval = 2048
    AND memtable_flush_period_in_ms = 0
    AND min_index_interval = 128
    AND read_repair = 'BLOCKING'
    AND speculative_retry = '99p';

token@cqlsh:netflix_keyspace> SELECT COUNT(*) FROM developer_survey;

 count
--------
 100000

(1 rows)

Warnings :
Aggregation query used without partition key

token@cqlsh:netflix_keyspace> SELECT * FROM developer_survey LIMIT 5;

 id                                   | companysize          | country            | employment                         | formaleducation                                                                    | hobby | opensource | student        | undergradmajor
--------------------------------------+----------------------+--------------------+------------------------------------+------------------------------------------------------------------------------------+-------+------------+----------------+-----------------------------------------------------------------------
 ad97de00-2f3e-4296-8965-fc30cb4631bc |                   NA |      United States | Not employed, but looking for work | Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.) |   Yes |        Yes | Yes, full-time |                                                                    NA
 fc14ec4d-3aed-47f0-9f11-b33d8eae3535 | 100 to 499 employees |              India |                 Employed full-time |                                           Bachelor’s degree (BA, BS, B.Eng., etc.) |   Yes |        Yes |             No | Information systems, information technology, or system administration
 7e55c759-3940-41c5-91f0-5c10a282e976 |   20 to 99 employees |       South Africa |                 Employed full-time |                                           Bachelor’s degree (BA, BS, B.Eng., etc.) |   Yes |         No |             No |       Computer science, computer engineering, or software engineering
 1818b5b8-d5d7-4dbc-ba6f-29bd16d9b7be |                   NA | Russian Federation | Not employed, but looking for work |                                           Bachelor’s degree (BA, BS, B.Eng., etc.) |   Yes |         No |             No |                                                                    NA
 899fdfc6-6149-48ee-81d2-df8091fe60e9 |   20 to 99 employees |             Norway |                 Employed full-time |                                        Master’s degree (MA, MS, M.Eng., MBA, etc.) |    No |         No | Yes, full-time |       Computer science, computer engineering, or software engineering

(5 rows)
token@cqlsh:netflix_keyspace> SELECT * FROM top_countries LIMIT 10;

 country            | count
--------------------+-------
      United States | 20553
             Canada |  3431
             Brazil |  2536
     United Kingdom |  6269
              India | 13881
             France |  2596
 Russian Federation |  2897
            Germany |  6560
             Poland |  2147
          Australia |  2041

(10 rows)
token@cqlsh:netflix_keyspace> SELECT * FROM top_countries WHERE country = 'India';

 country | count
---------+-------
   India | 13881

(1 rows)
token@cqlsh:netflix_keyspace> SELECT country, converted_salary 
                    ... FROM developer_survey 
                    ... WHERE converted_salary > 100000 
                    ... LIMIT 10;
InvalidRequest: Error from server: code=2200 [Invalid query] message="Undefined column name converted_salary in table "netflix_keyspace".developer_survey"
token@cqlsh:netflix_keyspace> SELECT * FROM top_countries LIMIT 10;

 country            | count
--------------------+-------
      United States | 20553
             Canada |  3431
             Brazil |  2536
     United Kingdom |  6269
              India | 13881
             France |  2596
 Russian Federation |  2897
            Germany |  6560
             Poland |  2147
          Australia |  2041

(10 rows)
token@cqlsh:netflix_keyspace> SELECT * FROM top_countries  LIMIT 10;

 country            | count
--------------------+-------
      United States | 20553
             Canada |  3431
             Brazil |  2536
     United Kingdom |  6269
              India | 13881
             France |  2596
 Russian Federation |  2897
            Germany |  6560
             Poland |  2147
          Australia |  2041

(10 rows)
token@cqlsh:netflix_keyspace> SELECT * FROM education_distribution   LIMIT 10;

 education                                                                          | count
------------------------------------------------------------------------------------+-------
                                                                                 NA |  4190
                                          Other doctoral degree (Ph.D, Ed.D., etc.) |  2231
                                             I never completed any formal education |   714
                             Some college/university study without earning a degree | 11836
                                                 Professional degree (JD, MD, etc.) |  1469
 Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.) |  9058
                                           Bachelor’s degree (BA, BS, B.Eng., etc.) | 44180
                                                          Primary/elementary school |  1672
                                        Master’s degree (MA, MS, M.Eng., MBA, etc.) | 21646
                                                                   Associate degree |  3004

(10 rows)
token@cqlsh:netflix_keyspace> SELECT * FROM opensource_by_company  LIMIT 10;

 companysize              | count
--------------------------+-------
                       NA | 12462
     500 to 999 employees |  1977
       20 to 99 employees |  7589
 1,000 to 4,999 employees |  3108
       10 to 19 employees |  3725
     100 to 499 employees |  6065
 5,000 to 9,999 employees |  1203
 10,000 or more employees |  3965
  Fewer than 10 employees |  3507

(9 rows)
token@cqlsh:netflix_keyspace> 
