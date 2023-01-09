CREATE TABLE IF NOT EXISTS registers (
  id SERIAL PRIMARY KEY,
  collected timestamptz,
  topic varchar(250) NOT NULL,
  command varchar(250),
  lat varchar(250),
  lng varchar(250),
  disp_id varchar(250) NOT NULL
);

