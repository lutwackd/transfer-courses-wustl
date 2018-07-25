--pulls transferrable courses from a master list  
	row_number() OVER () AS id
,	mce.school_id_oth
,	mce.dept_code_oth
, 	mce.course_num_oth
, 	mce.course_title_oth
,	mce.tags_oth
,	mce.dept_code_wu
, 	mce.course_num_wu
, 	mce.course_title_wu
,	mce.units_wu
,	mce.expiration_date
FROM master_courses_enriched mce;