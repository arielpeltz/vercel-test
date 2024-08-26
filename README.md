# vercel-test

This is a very simple applicaiton that uses a redis backend to get data and display it.
You need to create on your project on Vercel a storage of type redis and pass the
connection string in env variable `REDIS_connection_string`.   The application
will look for the key `headline` and just print it.  If it is not found an message
is displayed instead.
