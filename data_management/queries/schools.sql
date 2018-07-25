--pulls all unique schools from master course list
--fixes data issues such as inconsistent naming

WITH t1 AS (
	SELECT 
		mc.school_id_oth
	,	mc.school_name_oth
	, 	count(mc.school_name_oth) AS count
	, 	rank() OVER 
		(
			PARTITION BY mc.school_id_oth 
			ORDER BY count(mc.school_name_oth) DESC
		) AS rank
	FROM master_courses_enriched mc
	GROUP BY mc.school_id_oth, mc.school_name_oth
)

SELECT DISTINCT 
	mce.school_id_oth AS id
,	mce.school_name_oth AS name_oth
, 	mce.lat
,	mce.long
FROM master_courses_enriched mce
JOIN t1 ON 
	t1.school_name_oth::text = mce.school_name_oth::text AND 
	t1.rank = 1::bigint;