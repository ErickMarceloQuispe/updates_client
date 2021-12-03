updates_exists="pragma table_info(updates)"
get_last_update_date="select created_at from updates order by created_at desc limit 1"
