CREATE TABLE embeds (
  url varchar(48) not null,
  color varchar(6) not null,
  title varchar(64) not null,
  description varchar(256) not null,
  image varchar(128),
  small varchar(32),
  expiry timestamp DEFAULT now() + interval '7' day
);