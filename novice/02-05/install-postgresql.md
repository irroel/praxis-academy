#### Install PostgreSQL 12 in Elementary OS 5.1

sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

sudo apt-get update

sudo apt-get install postgresql-12

sudo apt-get install pgadmin4

pip install psycopg2

#comment in pgdg.list, prevent postgresql upgrade,
/etc/apt/sources.list.d/pgdg.list

#check postgresql,
service postgresql status

sudo -u postgres psql -c "ALTER USER postgres PASSWORD '*****';"

#make password,
sudo passwd postgres

#restart, 
sudo service postgresql restart

#open postgresql application,

#create server,

